#!/usr/bin/env python3
"""
Convert academic papers and essays from Markdown to Word (.docx) and LaTeX formats using Pandoc.

Features:
- Supports both single-file (paper.md) and multi-file (section-per-chapter) workflows.
- Automatically detects and uses a single paper.md file if present, or assembles from section files per outline.
- Ensures all required sections are present (if using section files) before conversion.
- Preprocesses custom page break tags (\\pagebreak) to Pandoc-compatible page breaks (\\newpage).
- Uses a reference .docx template for consistent APA/academic formatting.
- Enables advanced markdown features and citation processing.
- Supports LaTeX output for preserving complex formulas with paper.latex generation.

Usage:
  python convert_to_word.py <paper_folder>

See LEARNINGS.md for best practices and troubleshooting.
"""

import os
import sys
import re
from pathlib import Path
import markdown
import pypandoc

# Import our custom modules for robustness
from logger import log
from config import config, get_path
from dependencies import dependency_checker

# Set up configuration paths
if not Path('papercopilot_config.json').exists():
    # Use default paths if no config file exists
    REFERENCE_DOCX = Path(__file__).parent / 'apa_pandoc_reference.docx'
else:
    # Otherwise, use paths from config
    REFERENCE_DOCX = Path(get_path('reference_docx'))


def get_short_title(paper_dir):
    """
    Extract a short, title-cased version of the paper title for the running head and output filename.
    
    Args:
        paper_dir (Path): Path to paper directory
        
    Returns:
        str: Short title for filename and running head
    """
    import string
    candidates = [paper_dir / 'input_requirements.md', paper_dir / 'introduction.md']
    
    for file in candidates:
        if file.exists():
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    text = f.read()
                    match = re.search(r'Title\s*[:\n]+(.+)', text, re.IGNORECASE)
                    if match:
                        title = match.group(1).strip()
                    else:
                        lines = [l.strip() for l in text.splitlines() if l.strip()]
                        title = lines[0] if lines else 'Paper'
                    short = re.sub(r'[^A-Za-z0-9 ]', '', title).split()
                    short = short[:5]  # Use first 5 words max
                    # Title case for filename, join with spaces
                    return ' '.join([w.capitalize() for w in short])
            except Exception as e:
                log.error(f"Error extracting title from {file}: {e}")
                # Continue to next candidate file
    
    log.warning("Could not extract paper title, using default")
    return 'Paper'


def update_reference_docx_running_head(reference_docx_path, running_head):
    """
    Update the running head in the Word template header to the provided value.
    
    Args:
        reference_docx_path (Path): Path to reference .docx template
        running_head (str): Running head text
        
    Returns:
        bool: True if successful, False if failed
    """
    try:
        from docx import Document
        
        log.debug(f"Updating running head in {reference_docx_path} to '{running_head}'")
        doc = Document(reference_docx_path)
        for section in doc.sections:
            header = section.header
            for paragraph in header.paragraphs:
                if paragraph.text.strip():
                    paragraph.text = running_head
        doc.save(reference_docx_path)
        return True
    except ImportError:
        log.warning("python-docx module not installed; running head not updated")
        return False
    except Exception as e:
        log.warning(f"Could not update running head in template: {e}")
        return False


def detect_outline_file(paper_dir):
    """
    Determine which outline to use (research paper or essay) based on input_requirements.md.
    
    Args:
        paper_dir (Path): Path to paper directory
        
    Returns:
        Path: Path to the appropriate outline file
    """
    req_file = paper_dir / 'input_requirements.md'
    try:
        if not req_file.exists():
            log.debug("No input_requirements.md found, using default research paper outline")
            return Path(get_path('outlines')) / 'researchpaper_general.md'
            
        with open(req_file, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            
        if 'essay' in text:
            log.debug("Essay document type detected")
            return Path(get_path('outlines')) / 'essay_general.md'
            
        log.debug("Research paper document type detected")
        return Path(get_path('outlines')) / 'researchpaper_general.md'
    
    except Exception as e:
        log.warning(f"Error detecting outline file: {e}. Using default research paper outline.")
        return Path(get_path('outlines')) / 'researchpaper_general.md'


def parse_outline(outline_path):
    """
    Parse the outline file to extract the canonical section order and optional sections.
    
    Args:
        outline_path (Path): Path to outline file
        
    Returns:
        tuple: (ordered_sections, optional_sections)
    """
    ordered = []
    optional = []
    
    try:
        with open(outline_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or line.startswith('---'):
                    continue
                if re.match(r'\d+\.\s', line):
                    section = re.sub(r'\d+\.\s*', '', line)
                    # Remove parenthetical (optional)
                    if '(optional)' in section.lower():
                        section = section.replace('(optional)', '').strip()
                        optional.append(section)
                    ordered.append(section)
    except Exception as e:
        log.error(f"Error parsing outline file {outline_path}: {e}")
        # Return empty lists if we can't parse the outline
        return [], []
        
    return ordered, optional


def section_to_filename(section):
    """
    Map a section name from the outline to a filename in the paper folder.
    
    Args:
        section (str): Section name from outline
        
    Returns:
        str: Corresponding filename
    """
    # Lowercase, replace spaces and slashes with underscores, remove punctuation
    name = section.lower().replace('/', ' ').replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
    
    # Essay sections use essay_ prefix
    if name in ['introduction', 'body', 'conclusion', 'references']:
        if (Path(get_path('outlines')) / 'essay_general.md').exists():
            return f'essay_{name}.md'
    
    return f'{name}.md'


def find_single_file(paper_dir):
    """
    If a single file (paper.md) exists in the paper directory, return its path.
    
    Args:
        paper_dir (Path): Path to paper directory
        
    Returns:
        Path or None: Path to single file if it exists, otherwise None
    """
    single_file = paper_dir / 'paper.md'
    if single_file.exists():
        return single_file
    return None


def get_pandoc_template_for_style(style):
    """
    Map a writing style to a Pandoc template filename (assumed to be in ./templates/).
    
    Args:
        style (str): Writing style name (apa7, mla, etc.)
        
    Returns:
        str or None: Path to template file or None for default
    """
    if not style:
        return None
        
    style_map = {
        'apa7': 'apa7.latex',
        'mla': 'mla.latex',
        'chicago': 'chicago.latex',
        'abnt': 'abnt.latex',
        'harvard': 'harvard.latex',
        'ieee': 'ieee.latex',
        'vancouver': 'vancouver.latex',
        'turabian': 'turabian.latex',
    }
    
    fname = style_map.get(style)
    if fname:
        try:
            templates_dir = Path(get_path('templates'))
            tpath = templates_dir / fname
            if tpath.exists():
                return str(tpath)
            else:
                log.warning(f"Template file {tpath} not found")
        except Exception as e:
            log.error(f"Error locating template for style {style}: {e}")
    
    return None


def convert_to_latex(paper_dir):
    """
    Convert a paper folder to a LaTeX (.latex) document.
    
    - If paper.md exists, uses it directly (single-file workflow).
    - Otherwise, assembles section files in outline order.
    - Preserves LaTeX math formulas and complex equations.
    - Outputs file as paper.latex in the paper directory.
    - Halts and prints errors if required sections are missing (multi-file mode).
    
    Args:
        paper_dir (Path): Path to paper directory
        
    Returns:
        bool: True if conversion successful, False otherwise
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    output_md = paper_dir / 'assembled_paper.md'
    output_latex = paper_dir / 'paper.latex'
    
    log.info(f"Converting {paper_dir} to LaTeX...")
    
    # Select outline and parse for section order
    try:
        outline_path = detect_outline_file(paper_dir)
        ordered_sections, optional_sections = parse_outline(outline_path)
        section_files = [section_to_filename(s) for s in ordered_sections]
        optional_files = [section_to_filename(s) for s in optional_sections]
    except Exception as e:
        log.error(f"Error determining document structure: {e}")
        return False

    # --- Single-file support ---
    single_file = find_single_file(paper_dir)
    
    # If using single-file, skip section presence check
    if not single_file:
        # Check for missing required sections before conversion
        missing = []
        for fname in section_files:
            fpath = paper_dir / fname
            if not fpath.exists():
                missing.append(fname)
                
        if missing:
            log.error(f"Missing required sections: {', '.join(missing)}")
            log.error("Conversion halted. Please create the missing sections and re-run the script.")
            return False

    # Preprocess: Create a working copy of the file
    try:
        if single_file:
            with open(single_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Write to a temp file for conversion
            temp_md = paper_dir / 'temp_paper_for_conversion.md'
            with open(temp_md, 'w', encoding='utf-8') as f:
                f.write(content)
                
            output_md = temp_md  # <-- Ensure we use the preprocessed file for conversion
            log.info(f"Using single file: {single_file.name}")
        else:
            # Concatenate sections dynamically in outline order
            with open(output_md, 'w', encoding='utf-8') as outfile:
                for fname in section_files:
                    fpath = paper_dir / fname
                    try:
                        with open(fpath, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                            outfile.write('\n\n')
                    except Exception as e:
                        log.error(f"Error reading section file {fpath}: {e}")
                        return False
                
                # Optionally include present optional sections
                for fname in optional_files:
                    fpath = paper_dir / fname
                    if fpath.exists():
                        try:
                            with open(fpath, 'r', encoding='utf-8') as infile:
                                outfile.write(infile.read())
                                outfile.write('\n\n')
                        except Exception as e:
                            log.warning(f"Error including optional section {fpath}: {e}")
            
            log.info("Assembled multiple section files into a single document")
    except Exception as e:
        log.error(f"Error preparing document for conversion: {e}")
        return False

    # Configure LaTeX-specific arguments for Pandoc
    extra_args = [
        '--standalone',
        '--wrap=auto',
        '--extract-media=.',
        '--markdown-headings=atx',
        f'--columns={config.get("conversion", "wrap_text_columns", 80)}',
        '--shift-heading-level-by=0',
        '--highlight-style=pygments',
        '--citeproc',
        '--resource-path=.',
        # Enable all advanced markdown features, including LaTeX math support
        '--from=markdown+fenced_code_blocks+raw_html+table_captions+yaml_metadata_block+footnotes+definition_lists+pipe_tables+grid_tables+auto_identifiers+smart+tex_math_dollars+tex_math_single_backslash+tex_math_double_backslash',
    ]

    # Convert to LaTeX using Pandoc
    try:
        pypandoc.convert_file(
            str(output_md),
            'latex',
            outputfile=str(output_latex),
            extra_args=extra_args
        )
        log.info(f"Successfully created {output_latex}")
        return True
    except Exception as e:
        log.error(f"Error during LaTeX conversion: {e}")
        return False


def convert_to_word(paper_dir):
    """
    Convert a paper folder to a Word (.docx) document from Markdown.
    
    - If paper.md exists, uses it directly (single-file workflow).
    - Otherwise, assembles section files in outline order.
    - Preprocesses custom page break tags (\\pagebreak) to Pandoc-compatible page breaks (\\newpage).
    - Uses a reference .docx for formatting and enables advanced markdown features.
    - Halts and prints errors if required sections are missing (multi-file mode).
    
    Args:
        paper_dir (Path): Path to paper directory
        
    Returns:
        bool: True if conversion successful, False otherwise
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    output_md = paper_dir / 'assembled_paper.md'
    output_docx = paper_dir / f'{short_title}.docx'
    reference_docx = REFERENCE_DOCX
    
    log.info(f"Converting {paper_dir} to Word...")
    
    # Update the running head in the template
    update_reference_docx_running_head(reference_docx, short_title)
    
    # Select outline and parse for section order
    try:
        outline_path = detect_outline_file(paper_dir)
        ordered_sections, optional_sections = parse_outline(outline_path)
        section_files = [section_to_filename(s) for s in ordered_sections]
        optional_files = [section_to_filename(s) for s in optional_sections]
    except Exception as e:
        log.error(f"Error determining document structure: {e}")
        return False
    
    # --- Single-file support ---
    single_file = find_single_file(paper_dir)
    
    # If using single-file, skip section presence check
    if not single_file:
        # Check for missing required sections before conversion
        missing = []
        for fname in section_files:
            fpath = paper_dir / fname
            if not fpath.exists():
                missing.append(fname)
                
        if missing:
            log.error(f"Missing required sections: {', '.join(missing)}")
            log.error("Conversion halted. Please create the missing sections and re-run the script.")
            return False
    
    # Preprocess: Replace '\\pagebreak' and '\\newpage' with DOCX raw XML page break for best compatibility
    try:
        if single_file:
            with open(single_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Try DOCX raw XML page break for Pandoc
            content = re.sub(r'\\+pagebreak|\\+newpage', '\n<w:br w:type="page"/>\n', content)
            
            # Write to a temp file for conversion
            temp_md = paper_dir / 'temp_paper_for_conversion.md'
            with open(temp_md, 'w', encoding='utf-8') as f:
                f.write(content)
                
            output_md = temp_md  # <-- Ensure we use the preprocessed file for conversion
            log.info(f"Using single file: {single_file.name}")
        else:
            # Concatenate sections dynamically in outline order
            with open(output_md, 'w', encoding='utf-8') as outfile:
                for fname in section_files:
                    fpath = paper_dir / fname
                    try:
                        with open(fpath, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            # Process page breaks
                            content = re.sub(r'\\+pagebreak|\\+newpage', '\n<w:br w:type="page"/>\n', content)
                            outfile.write(content)
                            outfile.write('\n\n')
                    except Exception as e:
                        log.error(f"Error reading section file {fpath}: {e}")
                        return False
                
                # Optionally include present optional sections
                for fname in optional_files:
                    fpath = paper_dir / fname
                    if fpath.exists():
                        try:
                            with open(fpath, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                content = re.sub(r'\\+pagebreak|\\+newpage', '\n<w:br w:type="page"/>\n', content)
                                outfile.write(content)
                                outfile.write('\n\n')
                        except Exception as e:
                            log.warning(f"Error including optional section {fpath}: {e}")
            
            log.info("Assembled multiple section files into a single document")
    except Exception as e:
        log.error(f"Error preparing document for conversion: {e}")
        return False
    
    # Use only the reference .docx for all formatting and enable advanced markdown features
    extra_args = [
        '--standalone',
        '--wrap=auto',
        # '--toc',  # Removed: Table of Contents causes conversion issues with some templates
        '--extract-media=.',
        '--markdown-headings=atx',
        f'--columns={config.get("conversion", "wrap_text_columns", 80)}',
        '--shift-heading-level-by=0',
        '--highlight-style=pygments',
        '--citeproc',
        '--resource-path=.',
        # Reference docx for formatting
        f'--reference-doc={reference_docx}',
        # Enable all advanced markdown features, including LaTeX math support
        '--from=markdown+fenced_code_blocks+raw_html+table_captions+yaml_metadata_block+footnotes+definition_lists+pipe_tables+grid_tables+auto_identifiers+smart+tex_math_dollars+tex_math_single_backslash+tex_math_double_backslash',
    ]
    
    # Convert to docx using Pandoc
    try:
        pypandoc.convert_file(
            str(output_md),
            'docx',
            outputfile=str(output_docx),
            extra_args=extra_args
        )
        log.info(f"Successfully created {output_docx}")
        return True
    except Exception as e:
        log.error(f"Error during Word conversion: {e}")
        return False


def convert_latex_to_word(paper_dir):
    """
    Convert a LaTeX (.latex) file to a Word (.docx) document.
    
    - Uses the paper.latex file in the paper directory.
    - Outputs a distinct file as paper_latex.docx to differentiate from the Markdown-derived .docx.
    - Preserves formatting from LaTeX as accurately as possible.
    
    Args:
        paper_dir (Path): Path to paper directory
        
    Returns:
        bool: True if conversion successful, False otherwise
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    input_latex = paper_dir / 'paper.latex'
    output_docx = paper_dir / f'{short_title}_latex.docx'
    reference_docx = REFERENCE_DOCX
    
    log.info(f"Converting LaTeX to Word...")
    
    # Check if LaTeX file exists
    if not input_latex.exists():
        log.error(f"LaTeX file {input_latex} not found. Please run convert_to_latex first.")
        return False
    
    # Update the running head in the template
    update_reference_docx_running_head(reference_docx, short_title)
    
    # Configure arguments for Pandoc
    extra_args = [
        '--standalone',
        '--wrap=auto',
        '--extract-media=.',
        f'--columns={config.get("conversion", "wrap_text_columns", 80)}',
        '--shift-heading-level-by=0',
        '--highlight-style=pygments',
        '--citeproc',
        '--resource-path=.',
        # Reference docx for formatting
        f'--reference-doc={reference_docx}',
    ]
    
    # Convert LaTeX to docx using Pandoc
    try:
        pypandoc.convert_file(
            str(input_latex),
            'docx',
            outputfile=str(output_docx),
            extra_args=extra_args
        )
        log.info(f"Successfully created {output_docx} from LaTeX source")
        return True
    except Exception as e:
        log.error(f"Error during LaTeX to Word conversion: {e}")
        return False


def verify_requirements():
    """
    Verify that all required dependencies are installed.
    
    Returns:
        bool: True if all requirements are met, False otherwise
    """
    log.info("Verifying system requirements...")
    
    # Check Python packages and external tools
    if not dependency_checker.check_all_dependencies():
        log.error("Required dependencies are missing. Please install them before continuing.")
        log.info("\nDependency Report:\n" + dependency_checker.get_dependency_report())
        return False
    
    # Check configuration
    if not config.validate():
        log.warning("Configuration validation failed. Some features may not work correctly.")
    
    # Verification successful
    log.info("All requirements verified successfully.")
    return True


def main():
    """Main entry point for the script."""
    # Configure logging
    log.set_level(config.get('logging', 'level', 'INFO'))
    if config.get('logging', 'enable_file_logging', False):
        log_dir = config.get('logging', 'log_directory', './logs')
        log.setup_file_handler(log_dir)
    
    log.info("PaperCopilot Document Conversion Tool")
    
    if len(sys.argv) != 2:
        log.error("Usage: python convert_to_word.py <paper_folder>")
        return 1
    
    # Verify requirements before running
    if not verify_requirements():
        log.error("System requirements check failed. Please fix the issues and try again.")
        return 1
    
    paper_dir = sys.argv[1]
    paper_path = Path(paper_dir)
    
    if not paper_path.exists() or not paper_path.is_dir():
        log.error(f"Paper folder '{paper_dir}' does not exist or is not a directory")
        return 1
    
    try:
        # Convert to Word from Markdown
        if not convert_to_word(paper_dir):
            log.error("Word conversion failed. See error messages above.")
            return 1
        
        # Convert to LaTeX if enabled
        if config.get('conversion', 'enable_latex', True):
            if not convert_to_latex(paper_dir):
                log.warning("LaTeX conversion failed, but Word conversion was successful.")
                
            # Generate Word document from LaTeX for comparison
            if not convert_latex_to_word(paper_dir):
                log.warning("LaTeX to Word conversion failed, but direct Word conversion was successful.")
        
        log.info("All enabled conversions completed successfully!")
        return 0
    except Exception as e:
        log.critical(f"Unhandled error during conversion: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
