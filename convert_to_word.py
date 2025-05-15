# convert_to_word.py
#
# This script converts academic papers and essays from markdown to Word (.docx) using Pandoc.
#
# Features:
# - Supports both single-file (paper.md) and multi-file (section-per-chapter) workflows.
# - Automatically detects and uses a single paper.md file if present, or assembles from section files per outline.
# - Ensures all required sections are present (if using section files) before conversion.
# - Preprocesses custom page break tags (\\pagebreak) to Pandoc-compatible page breaks (\\newpage).
# - Uses a reference .docx template for consistent APA/academic formatting.
# - Enables advanced markdown features and citation processing.
#
# Usage:
#   python convert_to_word.py <paper_folder>
#
# See LEARNINGS.md for best practices and troubleshooting.

import os
import sys
from pathlib import Path
import markdown
import pypandoc
import re

# APA/Word formatting files
REFERENCE_DOCX = Path(__file__).parent / 'apa_pandoc_reference.docx'  # Must contain running head, page numbers, font, margins, etc.

def get_short_title(paper_dir):
    """
    Extract a short, title-cased version of the paper title for the running head and output filename.
    Tries input_requirements.md, then introduction.md.
    """
    import string
    candidates = [paper_dir / 'input_requirements.md', paper_dir / 'introduction.md']
    for file in candidates:
        if file.exists():
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
    return 'Paper'


def update_reference_docx_running_head(reference_docx_path, running_head):
    """
    Update the running head in the Word template header to the provided value.
    Requires python-docx.
    """
    try:
        from docx import Document
        doc = Document(reference_docx_path)
        for section in doc.sections:
            header = section.header
            for paragraph in header.paragraphs:
                if paragraph.text.strip():
                    paragraph.text = running_head
        doc.save(reference_docx_path)
    except Exception as e:
        print(f"Warning: Could not update running head in template: {e}")


def detect_outline_file(paper_dir):
    """
    Determine which outline to use (research paper or essay) based on input_requirements.md.
    Returns the Path to the outline file.
    """
    req_file = paper_dir / 'input_requirements.md'
    if not req_file.exists():
        return Path('outlines/researchpaper_general.md')
    with open(req_file, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    if 'essay' in text:
        return Path('outlines/essay_general.md')
    return Path('outlines/researchpaper_general.md')


def parse_outline(outline_path):
    """
    Parse the outline file to extract the canonical section order and optional sections.
    Returns (ordered_sections, optional_sections)
    """
    ordered = []
    optional = []
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
    return ordered, optional


def section_to_filename(section):
    """
    Map a section name from the outline to a filename in the paper folder.
    """
    # Lowercase, replace spaces and slashes with underscores, remove punctuation
    name = section.lower().replace('/', ' ').replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
    # Essay sections use essay_ prefix
    if name in ['introduction', 'body', 'conclusion', 'references']:
        if (Path('outlines/essay_general.md').exists()):
            return f'essay_{name}.md'
    return f'{name}.md'


def find_single_file(paper_dir):
    """
    If a single file (paper.md) exists in the paper directory, return its path. Otherwise, return None.
    """
    single_file = paper_dir / 'paper.md'
    if single_file.exists():
        return single_file
    return None


def get_pandoc_template_for_style(style):
    """
    Map a writing style to a Pandoc template filename (assumed to be in ./templates/).
    Returns the template path or None for default.
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
        tpath = Path(__file__).parent / 'templates' / fname
        if tpath.exists():
            return str(tpath)
    return None


def convert_to_word(paper_dir):
    """
    Convert a paper folder to a Word (.docx) document.
    - If paper.md exists, uses it directly (single-file workflow).
    - Otherwise, assembles section files in outline order.
    - Preprocesses custom page break tags (\\pagebreak) to Pandoc-compatible page breaks (\\newpage).
    - Uses a reference .docx for formatting and enables advanced markdown features.
    - Halts and prints errors if required sections are missing (multi-file mode).
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    output_md = paper_dir / 'assembled_paper.md'
    output_docx = paper_dir / f'{short_title}.docx'
    reference_docx = REFERENCE_DOCX

    # Update the running head in the template
    update_reference_docx_running_head(reference_docx, short_title)

    # Select outline and parse for section order
    outline_path = detect_outline_file(paper_dir)
    ordered_sections, optional_sections = parse_outline(outline_path)
    section_files = [section_to_filename(s) for s in ordered_sections]
    optional_files = [section_to_filename(s) for s in optional_sections]

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
            print(f"\nERROR: The following required sections are missing and must be created before conversion: {', '.join(missing)}\n")
            print("Conversion halted. Please create the missing sections and re-run the script.")
            sys.exit(2)

    # Preprocess: Replace '\\pagebreak' and '\pagebreak' with Pandoc's page break syntax
    if single_file:
        with open(single_file, 'r', encoding='utf-8') as f:
            content = f.read()
        # Pandoc recognizes '\newpage' or '<div style="page-break-after: always;"></div>' as page breaks
        content = re.sub(r'\\+pagebreak', '\\newpage', content)
        # Write to a temp file for conversion
        temp_md = paper_dir / 'temp_paper_for_conversion.md'
        with open(temp_md, 'w', encoding='utf-8') as f:
            f.write(content)
        output_md = temp_md

    if single_file:
        # Use the single file directly for conversion
        output_md = single_file
        print(f"Detected single-file paper: {single_file.name}. Proceeding with direct conversion.")
    else:
        # Concatenate sections dynamically in outline order
        with open(output_md, 'w', encoding='utf-8') as outfile:
            for fname in section_files:
                fpath = paper_dir / fname
                with open(fpath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')
            # Optionally include present optional sections
            for fname in optional_files:
                fpath = paper_dir / fname
                if fpath.exists():
                    with open(fpath, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n\n')

    # Use only the reference .docx for all formatting and enable advanced markdown features
    extra_args = [
        '--standalone',
        '--wrap=auto',
        # '--toc',  # Removed: Table of Contents causes conversion issues with some templates
        '--extract-media=.',
        '--markdown-headings=atx',
        '--columns=80',
        '--shift-heading-level-by=0',
        '--highlight-style=pygments',
        '--citeproc',
        '--resource-path=.',
        '--from=markdown+fenced_code_blocks+raw_html+table_captions+yaml_metadata_block+footnotes+definition_lists+pipe_tables+grid_tables+auto_identifiers+smart',
    ]

    # Convert to docx using Pandoc
    try:
        pypandoc.convert_file(
            str(output_md),
            'docx',
            outputfile=str(output_docx),
            extra_args=extra_args
        )
        print(f"Successfully created {output_docx}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_to_word.py <paper_folder>")
        sys.exit(1)
    convert_to_word(sys.argv[1])
