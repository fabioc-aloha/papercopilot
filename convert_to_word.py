#!/usr/bin/env python3
"""
PaperCopilot Document Converter
Clean, simple Word document conversion from Markdown
"""

import sys
import logging
from pathlib import Path
import re
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

try:
    import pypandoc
except ImportError:
    logger.error("pypandoc is required. Install with: pip install pypandoc")
    sys.exit(1)

class DocumentConverter:
    """Simple, reliable document converter."""
    
    def __init__(self, paper_folder: str):
        self.paper_dir = Path(paper_folder).resolve()
        self.templates_dir = Path(__file__).parent / 'templates'
        
        if not self.paper_dir.exists():
            raise FileNotFoundError(f"Paper folder not found: {self.paper_dir}")
        
        # Check Pandoc is available
        try:
            version = pypandoc.get_pandoc_version()
            logger.info(f"Pandoc version: {version}")
        except OSError:
            raise RuntimeError("Pandoc is not installed. Please install Pandoc.")
    
    def get_paper_metadata(self) -> Dict[str, str]:
        """Extract basic metadata from input_requirements.md."""
        metadata = {
            'title': 'Academic Paper',
            'style': 'apa7',
            'type': 'research paper'
        }
        
        req_file = self.paper_dir / 'input_requirements.md'
        if req_file.exists():
            try:
                content = req_file.read_text(encoding='utf-8').lower()
                
                # Extract title
                if '## topic' in content:
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if '## topic' in line and i + 1 < len(lines):
                            metadata['title'] = lines[i + 1].strip()
                            break
                
                # Extract style
                if 'ieee' in content:
                    metadata['style'] = 'ieee'
                elif 'mla' in content:
                    metadata['style'] = 'mla'
                elif 'chicago' in content:
                    metadata['style'] = 'chicago'
                elif 'harvard' in content:
                    metadata['style'] = 'harvard'
                elif 'vancouver' in content:
                    metadata['style'] = 'vancouver'
                elif 'abnt' in content:
                    metadata['style'] = 'abnt'
                elif 'turabian' in content:
                    metadata['style'] = 'turabian'
                # Default to APA7
                
            except Exception as e:
                logger.warning(f"Could not parse requirements: {e}")
        
        return metadata
    
    def get_safe_filename(self, title: str) -> str:
        """Create a safe filename from title."""
        # Remove unsafe characters and limit length
        safe = re.sub(r'[^\w\s-]', '', title)
        safe = re.sub(r'[-\s]+', '_', safe).strip('_')
        return safe[:50] if safe else 'Academic_Paper'
    
    def convert_to_word(self) -> str:
        """Convert paper to Word document."""
        metadata = self.get_paper_metadata()
        safe_title = self.get_safe_filename(metadata['title'])
        
        # Find the paper source
        paper_file = self.paper_dir / 'paper.md'
        if not paper_file.exists():
            raise FileNotFoundError(f"No paper.md found in {self.paper_dir}")
        
        # Output file
        output_file = self.paper_dir / f"{safe_title}.docx"
        
        # Prepare Pandoc arguments
        pandoc_args = [
            '--standalone',
            '--wrap=auto',
            '--from=markdown',
            '--to=docx'
        ]
        
        try:
            logger.info(f"Converting {paper_file} to {output_file}")
            
            pypandoc.convert_file(
                str(paper_file),
                'docx',
                outputfile=str(output_file),
                extra_args=pandoc_args
            )
            
            logger.info(f"Successfully created: {output_file}")
            return str(output_file)
            
        except Exception as e:
            logger.error(f"Conversion failed: {e}")
            raise

def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("PaperCopilot Document Converter")
        print("===============================")
        print("Usage: python convert_to_word.py <paper_folder>")
        print("\nFeatures:")
        print("  • Simple, reliable Markdown to Word conversion")
        print("  • Automatic filename generation from paper title")
        print("  • Comprehensive error handling and validation")
        print("\nExamples:")
        print("  python convert_to_word.py test_paper_1")
        print("  python convert_to_word.py my_research_paper")
        print("\nRequirements:")
        print("  • Pandoc must be installed on your system")
        print("  • Python package: pypandoc (see requirements.txt)")
        sys.exit(1)
    
    paper_folder = sys.argv[1]
    
    try:
        converter = DocumentConverter(paper_folder)
        output_file = converter.convert_to_word()
        print(f"✅ Successfully created: {output_file}")
        
    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()