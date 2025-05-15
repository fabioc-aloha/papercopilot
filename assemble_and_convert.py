# assemble_and_convert.py
#
# This script assembles academic papers and essays from markdown section files and exports them to Word (.docx) using Pandoc.
#
# Best practices for reliable Markdown to Word conversion are documented in LEARNINGS.md (see section 'Best Practices for Markdown to Word Conversion').
# Key points reflected in this script:
# - Explicit support for advanced markdown features (fenced code blocks, tables, raw HTML, footnotes, definition lists, smart punctuation, etc.)
# - Use of a reference .docx template for consistent formatting
# - Table of contents, code highlighting, and smart punctuation enabled for professional output
# - Pandoc filters and arguments are documented and maintained for transparency and reproducibility
# - Contributors are encouraged to use only supported markdown features and to preview exports regularly
#
# If you update the Pandoc arguments or add new markdown features, update LEARNINGS.md accordingly.

import os
import sys
from pathlib import Path
import markdown
import pypandoc
import re

# Configuration
# Canonical order for research papers (see README for logic)
CHAPTER_ORDER = [
    'title_page.md',
    'abstract.md',
    'introduction.md',
    'literature_review.md',
    'methods.md',
    'results.md',
    'discussion.md',
    'conclusion.md',
    'references.md'
]
# Canonical order for essays
ESSAY_ORDER = [
    'essay_introduction.md',
    'essay_body.md',
    'essay_conclusion.md',
    'essay_references.md'
]

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


def detect_paper_type_and_style(paper_dir):
    """
    Detect if the project is a research paper or essay and determine the required style and chapters/sections.
    Returns: (type, style, required_chapters, optional_chapters)
    """
    req_file = paper_dir / 'input_requirements.md'
    if not req_file.exists():
        return 'paper', 'APA 7', CHAPTER_ORDER, []
    with open(req_file, 'r', encoding='utf-8') as f:
        text = f.read()
    # Detect essay or paper
    is_essay = 'essay format' in text.lower() or 'essay' in text.lower()
    # Detect style
    style_match = re.search(r'(APA 7|IEEE|Chicago|Harvard|MLA|Turabian|Vancouver|ABNT)', text, re.IGNORECASE)
    style = style_match.group(1).upper() if style_match else 'APA 7'
    # Parse for additional required/optional chapters
    required = []
    optional = []
    # Look for explicit chapter/section mentions in requirements
    for line in text.splitlines():
        if re.match(r'-?\s*(include|add)\s+([\w /]+)', line, re.IGNORECASE):
            chapter = re.sub(r'[^a-z_\-/ ]', '', line.split()[-1].lower().replace(' ', '_'))
            if chapter and chapter + '.md' not in required:
                required.append(chapter + '.md')
        if re.match(r'-?\s*(optional|may include)\s+([\w /]+)', line, re.IGNORECASE):
            chapter = re.sub(r'[^a-z_\-/ ]', '', line.split()[-1].lower().replace(' ', '_'))
            if chapter and chapter + '.md' not in optional:
                optional.append(chapter + '.md')
    # Use canonical order for type/style
    if is_essay:
        canonical = ESSAY_ORDER.copy()
    else:
        style_map = {
            'APA 7': CHAPTER_ORDER,
            'IEEE': CHAPTER_ORDER,
            'MLA': ['introduction.md', 'literature_review.md', 'methods.md', 'results.md', 'discussion.md', 'conclusion.md', 'references.md'],
            'CHICAGO': ['title_page.md', 'abstract.md', 'introduction.md', 'literature_review.md', 'methods.md', 'results.md', 'discussion.md', 'conclusion.md', 'bibliography.md'],
            'HARVARD': CHAPTER_ORDER,
            'TURABIAN': CHAPTER_ORDER,
            'VANCOUVER': CHAPTER_ORDER,
            'ABNT': ['title_page.md', 'resumo.md', 'sumario.md', 'introduction.md', 'literature_review.md', 'methods.md', 'results.md', 'discussion.md', 'conclusion.md', 'references.md'],
        }
        canonical = style_map.get(style, CHAPTER_ORDER)
    # Merge required chapters from requirements, preserving canonical order
    final_required = [c for c in canonical if c not in required] + required
    return ('essay' if is_essay else 'paper', style, final_required, optional)


def assemble_and_convert(paper_dir):
    """
    Assemble chapter files in canonical order and convert to a Word (.docx) document.
    Uses the root-level apa_pandoc_reference.docx as the only style source to preserve all formatting (font, line spacing, etc).
    Enforces that all required chapters are present before export; halts and prints error if any are missing.
    Dynamically includes all present optional chapters in canonical order after required ones.
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    output_md = paper_dir / 'assembled_paper.md'
    output_docx = paper_dir / f'{short_title}.docx'
    reference_docx = REFERENCE_DOCX

    # Update the running head in the template
    update_reference_docx_running_head(reference_docx, short_title)

    # Detect type, style, and chapters
    paper_type, style, required_chapters, optional_chapters = detect_paper_type_and_style(paper_dir)

    # Check for missing required chapters before assembly
    missing = []
    for chapter in required_chapters:
        chapter_path = paper_dir / chapter
        if not chapter_path.exists():
            missing.append(chapter)
    if missing:
        print(f"\nERROR: The following required chapters are missing and must be created before export: {', '.join(missing)}\n")
        print("Assembly halted. Please create the missing chapters and re-run the script.")
        sys.exit(2)

    # Assemble chapters dynamically in canonical order
    with open(output_md, 'w', encoding='utf-8') as outfile:
        for chapter in required_chapters:
            chapter_path = paper_dir / chapter
            with open(chapter_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')
        # Optionally include present optional chapters in canonical order
        for chapter in optional_chapters:
            chapter_path = paper_dir / chapter
            if chapter_path.exists():
                with open(chapter_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')

    # Use only the reference .docx for all formatting and enable advanced markdown features
    extra_args = [
        f'--reference-doc={reference_docx}',  # Consistent formatting (font, margins, etc.)
        '--standalone',  # Output a standalone document
        '--wrap=auto',  # Preserve line wrapping
        '--toc',  # Table of contents if headings present
        '--extract-media=.',  # Extract images if any
        '--markdown-headings=atx',  # Use ATX-style headings
        '--columns=80',  # Set column width for text wrapping
        '--shift-heading-level-by=0',  # No heading level shift
        '--highlight-style=pygments',  # Code block syntax highlighting
        '--smart',  # Smart punctuation (quotes, dashes, etc.)
        '--filter=pandoc-citeproc',  # For references/citations (if present)
        '--resource-path=.',  # Look for resources in current dir
        # '--lua-filter=filters/fix-references.lua',  # (Optional) Custom filter for references formatting
        # Enable all advanced markdown features used in academic writing:
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
        print("Usage: python assemble_and_convert.py <paper_folder>")
        sys.exit(1)
    assemble_and_convert(sys.argv[1])
