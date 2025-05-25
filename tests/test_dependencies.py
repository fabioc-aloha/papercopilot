"""
Tests for the dependency checker module.
"""

import unittest
from unittest import mock
import sys
import importlib
from pathlib import Path

# Add parent directory to path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from dependencies import DependencyChecker


class TestDependencyChecker(unittest.TestCase):
    """Test the dependency checker functionality."""
    
    def test_check_python_version(self):
        """Test Python version checking."""
        checker = DependencyChecker()
        
        # Should pass with lower version
        self.assertTrue(checker.check_python_version((1, 0)))
        
        # Should fail with future version
        self.assertFalse(checker.check_python_version((99, 0)))
    
    def test_compare_versions(self):
        """Test version comparison logic."""
        checker = DependencyChecker()
        
        self.assertEqual(checker._compare_versions("1.0", "1.0"), 0)
        self.assertEqual(checker._compare_versions("1.1", "1.0"), 1)
        self.assertEqual(checker._compare_versions("1.0", "1.1"), -1)
        self.assertEqual(checker._compare_versions("1.0.1", "1.0"), 1)
        self.assertEqual(checker._compare_versions("1.0", "1.0.1"), -1)
        self.assertEqual(checker._compare_versions("1.0.0", "1.0"), 0)
        self.assertEqual(checker._compare_versions("1.10", "1.9"), 1)
        self.assertEqual(checker._compare_versions("1.9", "1.10"), -1)
    
    @mock.patch('importlib.import_module')
    def test_check_module(self, mock_import):
        """Test module checking with mocked imports."""
        checker = DependencyChecker()
        
        # Mock a module with version
        mock_module = mock.MagicMock()
        mock_module.__version__ = "1.0.0"
        mock_import.return_value = mock_module
        
        # Should pass with exact version
        self.assertTrue(checker.check_module("testmodule", "1.0.0"))
        
        # Should pass with lower required version
        self.assertTrue(checker.check_module("testmodule", "0.9.0"))
        
        # Should fail with higher required version
        self.assertFalse(checker.check_module("testmodule", "1.1.0"))
        
        # Should pass with no version requirement
        self.assertTrue(checker.check_module("testmodule"))
        
        # Test import error
        mock_import.side_effect = ImportError("Module not found")
        self.assertFalse(checker.check_module("missing_module"))
    
    @mock.patch('shutil.which')
    @mock.patch('subprocess.run')
    def test_check_external_tool(self, mock_run, mock_which):
        """Test external tool checking with mocked subprocess."""
        checker = DependencyChecker()
        
        # Mock tool not in PATH
        mock_which.return_value = None
        self.assertFalse(checker.check_external_tool("tool"))
        
        # Mock tool in PATH
        mock_which.return_value = "/usr/bin/tool"
        
        # Mock subprocess result with version
        mock_process = mock.MagicMock()
        mock_process.returncode = 0
        mock_process.stdout = "tool version 1.0.0"
        mock_run.return_value = mock_process
        
        # Should pass with exact version pattern
        self.assertTrue(checker.check_external_tool(
            "tool", "1.0.0", version_pattern=r'version\s+([0-9.]+)'
        ))
        
        # Should pass with lower required version
        self.assertTrue(checker.check_external_tool(
            "tool", "0.9.0", version_pattern=r'version\s+([0-9.]+)'
        ))
        
        # Should fail with higher required version
        self.assertFalse(checker.check_external_tool(
            "tool", "1.1.0", version_pattern=r'version\s+([0-9.]+)'
        ))
        
        # Should pass with no version requirement
        self.assertTrue(checker.check_external_tool("tool"))
    
    @mock.patch('dependencies.DependencyChecker.check_python_version')
    @mock.patch('dependencies.DependencyChecker.check_module')
    @mock.patch('dependencies.DependencyChecker.check_pandoc')
    def test_check_all_dependencies(self, mock_pandoc, mock_module, mock_python):
        """Test comprehensive dependency checking with mocked methods."""
        checker = DependencyChecker()
        
        # All checks pass
        mock_python.return_value = True
        mock_module.return_value = True
        mock_pandoc.return_value = True
        self.assertTrue(checker.check_all_dependencies())
        
        # Python check fails
        mock_python.return_value = False
        mock_module.return_value = True
        mock_pandoc.return_value = True
        self.assertFalse(checker.check_all_dependencies())
        
        # Module check fails
        mock_python.return_value = True
        mock_module.return_value = False
        mock_pandoc.return_value = True
        self.assertFalse(checker.check_all_dependencies())
        
        # Pandoc check fails
        mock_python.return_value = True
        mock_module.return_value = True
        mock_pandoc.return_value = False
        self.assertFalse(checker.check_all_dependencies())


if __name__ == '__main__':
    unittest.main()