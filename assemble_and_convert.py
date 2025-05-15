import os
import sys
from pathlib import Path
import markdown
import pypandoc
import re

# Configuration
CHAPTER_ORDER = [
    'introduction.md',
    'literature_review.md',
    'methods.md',
    'results.md',
    'discussion.md',
    'conclusion.md',
    'references.md'
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


def assemble_and_convert(paper_dir):
    """
    Assemble chapter files in canonical order and convert to a Word (.docx) document.
    Uses the root-level apa_pandoc_reference.docx as the only style source to preserve all formatting (font, line spacing, etc).
    """
    paper_dir = Path(paper_dir)
    short_title = get_short_title(paper_dir)
    output_md = paper_dir / 'assembled_paper.md'
    output_docx = paper_dir / f'{short_title}.docx'
    reference_docx = REFERENCE_DOCX

    # Update the running head in the template
    update_reference_docx_running_head(reference_docx, short_title)

    # Assemble chapters
    with open(output_md, 'w', encoding='utf-8') as outfile:
        for chapter in CHAPTER_ORDER:
            chapter_path = paper_dir / chapter
            if chapter_path.exists():
                with open(chapter_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')
            else:
                print(f"Warning: {chapter} not found in {paper_dir}")

    # Use only the reference .docx for all formatting
    extra_args = [
        f'--reference-doc={reference_docx}'
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
