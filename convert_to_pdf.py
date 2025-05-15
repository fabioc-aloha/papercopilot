# convert_to_pdf.py
#
# This script converts academic papers and essays from markdown to PDF using Pandoc.
#
# Features:
# - Supports both single-file (paper.md) and multi-file (section-per-chapter) workflows.
# - Automatically detects and uses a single paper.md file if present, or assembles from section files per outline.
# - Ensures all required sections are present (if using section files) before conversion.
# - Preprocesses custom page break tags (\\pagebreak) to Pandoc-compatible page breaks (\\newpage).
# - Uses a Pandoc native template for refined formatting (no custom reference DOCX by default).
# - Enables advanced markdown features and citation processing.
#
# Usage:
#   python convert_to_pdf.py <paper_folder>
#
# See LEARNINGS.md for best practices and troubleshooting.

import os
import sys
from pathlib import Path
import markdown
import pypandoc
import re

REFERENCE_DOCX = None  # Deprecated: No longer used, using Pandoc native template

# ...reuse get_short_title, update_reference_docx_running_head, detect_outline_file, parse_outline, section_to_filename from convert_to_word.py...

def get_short_title(paper_dir):
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
                short = short[:5]
                return ' '.join([w.capitalize() for w in short])
    return 'Paper'

def detect_outline_file(paper_dir):
    req_file = paper_dir / 'input_requirements.md'
    if not req_file.exists():
        return Path('outlines/researchpaper_general.md')
    with open(req_file, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    if 'essay' in text:
        return Path('outlines/essay_general.md')
    return Path('outlines/researchpaper_general.md')

def parse_outline(outline_path):
    ordered = []
    optional = []
    with open(outline_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('---'):
                continue
            if re.match(r'\d+\.\s', line):
                section = re.sub(r'\d+\.\s*', '', line)
                if '(optional)' in section.lower():
                    section = section.replace('(optional)', '').strip()
                    optional.append(section)
                ordered.append(section)
    return ordered, optional

def section_to_filename(section):
    name = section.lower().replace('/', ' ').replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
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

def get_writing_style(paper_dir):
    """
    Parse input_requirements.md to extract the required writing style (e.g., apa7, mla, chicago).
    Returns the style as a lowercase string, or None if not found.
    """
    req_file = paper_dir / 'input_requirements.md'
    if not req_file.exists():
        return None
    with open(req_file, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    # Look for a line like 'Writing style: APA 7' or 'Style: MLA'
    match = re.search(r'(writing style|style)\s*[:\-]+\s*([a-z0-9 .\-]+)', text)
    if match:
        style = match.group(2).strip().replace(' ', '').replace('-', '').replace('.', '')
        return style
    # Fallback: look for style keywords
    for style in ['apa7', 'mla', 'chicago', 'abnt', 'harvard', 'ieee', 'vancouver', 'turabian']:
        if style in text:
            return style
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

def convert_to_pdf(paper_dir):
    """
    Convert a paper folder to a PDF document.
    - If paper.md exists, uses it directly (single-file workflow).
    - Otherwise, assembles section files in outline order.
    - Preprocesses custom page break tags (\\pagebreak) to Pandoc-compatible page breaks (\\newpage).
    - Uses Pandoc's native PDF template for refined formatting (no reference DOCX).
    - Halts and prints errors if required sections are missing (multi-file mode).
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    output_md = paper_dir / 'assembled_paper.md'
    output_pdf = paper_dir / f'{short_title}.pdf'

    outline_path = detect_outline_file(paper_dir)
    ordered_sections, optional_sections = parse_outline(outline_path)
    section_files = [section_to_filename(s) for s in ordered_sections]
    optional_files = [section_to_filename(s) for s in optional_sections]

    # --- Single-file support ---
    single_file = find_single_file(paper_dir)
    # If using single-file, skip section presence check
    if not single_file:
        missing = []
        for fname in section_files:
            fpath = paper_dir / fname
            if not fpath.exists():
                missing.append(fname)
        if missing:
            print(f"\nERROR: The following required sections are missing and must be created before conversion: {', '.join(missing)}\n")
            print("Conversion halted. Please create the missing sections and re-run the script.")
            sys.exit(2)

        with open(output_md, 'w', encoding='utf-8') as outfile:
            for fname in section_files:
                fpath = paper_dir / fname
                with open(fpath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')
            for fname in optional_files:
                fpath = paper_dir / fname
                if fpath.exists():
                    with open(fpath, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n\n')

    # Preprocess: Replace any '\pagebreak' (one or more backslashes) with a raw LaTeX page break on its own line
    if single_file:
        with open(single_file, 'r', encoding='utf-8') as f:
            content = f.read()
        # Replace any number of backslashes before 'pagebreak' with a single LaTeX page break on its own line
        content = re.sub(r'^[ 	]*\\+pagebreak[ 	]*$', r'\\newpage', content, flags=re.MULTILINE)
        # Also replace inline (not on its own line) for robustness
        content = re.sub(r'\\+pagebreak', r'\\newpage', content)
        temp_md = paper_dir / 'temp_paper_for_conversion.md'
        with open(temp_md, 'w', encoding='utf-8') as f:
            f.write(content)
        output_md = temp_md

    # Detect writing style and select template
    style = get_writing_style(paper_dir)
    template_path = get_pandoc_template_for_style(style)

    extra_args = [
        '--standalone',
        '--wrap=auto',
        # '--toc',  # Removed: Table of Contents causes conversion issues with some templates
        '--extract-media=.',
        '--markdown-headings=atx',
        '--columns=80',
        '--shift-heading-level-by=0',
        '--highlight-style=pygments',
        '--citeproc',  # Use built-in citeproc instead of deprecated filter
        '--resource-path=.',
        '--from=markdown+fenced_code_blocks+raw_html+table_captions+yaml_metadata_block+footnotes+definition_lists+pipe_tables+grid_tables+auto_identifiers+smart',
    ]
    if template_path:
        extra_args.append(f'--template={template_path}')

    try:
        pypandoc.convert_file(
            str(output_md),
            'pdf',
            outputfile=str(output_pdf),
            extra_args=extra_args
        )
        print(f"Successfully created {output_pdf} using style: {style if style else 'default'}")
    except Exception as e:
        print(f"Error during PDF conversion: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_to_pdf.py <paper_folder>")
        sys.exit(1)
    convert_to_pdf(sys.argv[1])
