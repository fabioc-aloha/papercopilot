"""
Tests for the convert_to_word module.
"""

import unittest
from unittest import mock
import os
import sys
import tempfile
from pathlib import Path

# Add parent directory to path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Mock the logger before importing the module
with mock.patch('logger.log'):
    import convert_to_word


class TestConversionUtilities(unittest.TestCase):
    """Test utility functions in the convert_to_word module."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory for test files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)
        self.addCleanup(self.temp_dir.cleanup)
    
    def test_get_short_title(self):
        """Test extracting a short title from paper files."""
        # Create a test input_requirements.md file
        req_file = self.test_dir / 'input_requirements.md'
        with open(req_file, 'w') as f:
            f.write("Title: Test Paper Title For Conversion\n")
            f.write("Type: Research Paper\n")
        
        # Test title extraction
        short_title = convert_to_word.get_short_title(self.test_dir)
        self.assertEqual(short_title, "Test Paper Title For Conversion")
        
        # Test title extraction with no explicit title
        intro_file = self.test_dir / 'introduction.md'
        with open(intro_file, 'w') as f:
            f.write("# Introduction to the Research\n")
        
        # Rename the requirements file to test fallback
        req_file.rename(self.test_dir / 'input_requirements.md.bak')
        
        short_title = convert_to_word.get_short_title(self.test_dir)
        self.assertEqual(short_title, "Introduction To The Research")
        
        # Test with no valid files
        intro_file.unlink()
        short_title = convert_to_word.get_short_title(self.test_dir)
        self.assertEqual(short_title, "Paper")  # Default value
    
    def test_section_to_filename(self):
        """Test conversion of section names to filenames."""
        # First, mock Path.exists to return False for essay outline
        with mock.patch('pathlib.Path.exists', return_value=False):
            self.assertEqual(convert_to_word.section_to_filename("Introduction"), "introduction.md")
            self.assertEqual(convert_to_word.section_to_filename("Results and Discussion"), "results_and_discussion.md")
            self.assertEqual(convert_to_word.section_to_filename("Literature Review/Background"), "literature_review_background.md")
        
        # Now mock Path.exists to return True for essay outline
        with mock.patch('pathlib.Path.exists', return_value=True):
            self.assertEqual(convert_to_word.section_to_filename("Introduction"), "essay_introduction.md")
            self.assertEqual(convert_to_word.section_to_filename("Conclusion"), "essay_conclusion.md")
    
    def test_parse_outline(self):
        """Test parsing outline files for section order."""
        # Create a test outline file
        outline_file = self.test_dir / 'test_outline.md'
        with open(outline_file, 'w') as f:
            f.write("# Research Paper Outline\n\n")
            f.write("1. Introduction\n")
            f.write("2. Literature Review\n")
            f.write("3. Methodology\n")
            f.write("4. Results\n")
            f.write("5. Discussion\n")
            f.write("6. Conclusion\n")
            f.write("7. Appendix (optional)\n")
            f.write("8. References\n")
        
        # Test outline parsing
        ordered, optional = convert_to_word.parse_outline(outline_file)
        
        # Check the ordered sections
        self.assertEqual(len(ordered), 8)
        self.assertEqual(ordered[0], "Introduction")
        self.assertEqual(ordered[6], "Appendix")
        
        # Check the optional sections
        self.assertEqual(len(optional), 1)
        self.assertEqual(optional[0], "Appendix")
    
    def test_find_single_file(self):
        """Test detection of single paper.md file."""
        # Create a test paper.md file
        paper_file = self.test_dir / 'paper.md'
        with open(paper_file, 'w') as f:
            f.write("# Test Paper\n\nThis is a test paper content.")
        
        # Test finding the file
        found_file = convert_to_word.find_single_file(self.test_dir)
        self.assertEqual(found_file, paper_file)
        
        # Test when file doesn't exist
        paper_file.unlink()
        found_file = convert_to_word.find_single_file(self.test_dir)
        self.assertIsNone(found_file)
    
    @mock.patch('convert_to_word.get_pandoc_template_for_style')
    def test_get_pandoc_template_for_style(self, mock_get_template):
        """Test mapping styles to template files."""
        # Mock template paths
        mock_get_template.return_value = "/path/to/template.latex"
        
        # Test with valid style
        template = convert_to_word.get_pandoc_template_for_style("apa7")
        self.assertEqual(template, "/path/to/template.latex")
        
        # Test with None style
        mock_get_template.return_value = None
        template = convert_to_word.get_pandoc_template_for_style(None)
        self.assertIsNone(template)
    
    def test_detect_outline_file(self):
        """Test detection of appropriate outline file."""
        # Create a test input_requirements.md file for essay
        req_file = self.test_dir / 'input_requirements.md'
        with open(req_file, 'w') as f:
            f.write("Title: Test Essay\n")
            f.write("Type: Essay\n")
        
        # Mock the outline path existence
        with mock.patch('pathlib.Path.exists', return_value=True):
            # Test detection for essay
            outline = convert_to_word.detect_outline_file(self.test_dir)
            self.assertEqual(outline.name, "essay_general.md")
            
            # Update to research paper type
            with open(req_file, 'w') as f:
                f.write("Title: Test Research Paper\n")
                f.write("Type: Research Paper\n")
            
            # Test detection for research paper
            outline = convert_to_word.detect_outline_file(self.test_dir)
            self.assertEqual(outline.name, "researchpaper_general.md")
            
            # Test with no requirements file
            req_file.unlink()
            outline = convert_to_word.detect_outline_file(self.test_dir)
            self.assertEqual(outline.name, "researchpaper_general.md")  # Default


if __name__ == '__main__':
    unittest.main()