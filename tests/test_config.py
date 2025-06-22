"""
Tests for the configuration module.
"""

import unittest
from unittest import mock
import sys
import json
import os
import tempfile
from pathlib import Path

# Add parent directory to path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# We need to mock the logger before importing config
with mock.patch('logger.log'):
    from config import Config


class TestConfig(unittest.TestCase):
    """Test the configuration functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory for test files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        
        # Create a fresh Config instance for each test
        Config._instance = None
    
    def test_singleton_pattern(self):
        """Test that Config uses the singleton pattern."""
        config1 = Config()
        config2 = Config()
        self.assertIs(config1, config2)
    
    def test_default_config(self):
        """Test that default configuration is loaded."""
        config = Config()
        
        # Check a few default values
        self.assertEqual(config.get('conversion', 'pandoc_path'), 'pandoc')
        self.assertEqual(config.get('logging', 'level'), 'INFO')
        self.assertTrue('templates' in config.get('paths'))
    
    @mock.patch('logger.log')
    def test_load_config(self, mock_log):
        """Test loading configuration from file."""
        config = Config()
        
        # Create a test config file
        config_path = Path(self.temp_dir.name) / 'test_config.json'
        test_config = {
            'paths': {
                'templates': './custom_templates',
            },
            'conversion': {
                'pandoc_path': '/custom/path/to/pandoc',
            }
        }
        
        with open(config_path, 'w') as f:
            json.dump(test_config, f)
        
        # Load the test config
        config.load_config(config_path)
        
        # Check that values were updated
        self.assertEqual(config.get('paths', 'templates'), './custom_templates')
        self.assertEqual(config.get('conversion', 'pandoc_path'), '/custom/path/to/pandoc')
        
        # Check that other values remain default
        self.assertEqual(config.get('logging', 'level'), 'INFO')
    
    def test_deep_update(self):
        """Test deep updating of nested dictionaries."""
        config = Config()
        
        target = {
            'a': 1,
            'b': {
                'c': 2,
                'd': 3
            }
        }
        
        source = {
            'b': {
                'c': 4,
                'e': 5
            },
            'f': 6
        }
        
        config._deep_update(target, source)
        
        # Check that values were updated correctly
        self.assertEqual(target['a'], 1)  # Unchanged
        self.assertEqual(target['b']['c'], 4)  # Updated
        self.assertEqual(target['b']['d'], 3)  # Unchanged
        self.assertEqual(target['b']['e'], 5)  # Added
        self.assertEqual(target['f'], 6)  # Added
    
    @mock.patch('logger.log')
    def test_get_path(self, mock_log):
        """Test path resolution logic."""
        config = Config()
        
        # Set a test path
        config.set('paths', 'test_path', './test_directory')
        
        # Get the resolved path
        path = config.get_path('test_path')
        
        # Check that the path was resolved to an absolute path
        self.assertTrue(Path(path).is_absolute())
        self.assertTrue(path.endswith('test_directory'))
    
    def test_get_method(self):
        """Test the get method for retrieving configuration values."""
        config = Config()
        
        # Set a test value
        config.set('test_section', 'test_key', 'test_value')
        
        # Test getting the value
        self.assertEqual(config.get('test_section', 'test_key'), 'test_value')
        
        # Test getting a non-existent value
        self.assertIsNone(config.get('test_section', 'non_existent'))
        
        # Test getting with a default value
        self.assertEqual(config.get('test_section', 'non_existent', 'default'), 'default')
        
        # Test getting an entire section
        self.assertEqual(config.get('test_section'), {'test_key': 'test_value'})
        
        # Test getting a non-existent section
        self.assertIsNone(config.get('non_existent_section'))
    
    def test_set_method(self):
        """Test the set method for setting configuration values."""
        config = Config()
        
        # Set a value in an existing section
        config.set('paths', 'new_path', 'new_value')
        self.assertEqual(config.get('paths', 'new_path'), 'new_value')
        
        # Set a value in a new section
        config.set('new_section', 'new_key', 'new_value')
        self.assertEqual(config.get('new_section', 'new_key'), 'new_value')
    
    @mock.patch('logger.log')
    def test_save_config(self, mock_log):
        """Test saving configuration to a file."""
        config = Config()
        
        # Set a test value
        config.set('test_section', 'test_key', 'test_value')
        
        # Save to a temporary file
        config_path = Path(self.temp_dir.name) / 'saved_config.json'
        config.save(config_path)
        
        # Check that the file was created
        self.assertTrue(config_path.exists())
        
        # Load the saved config into a new instance
        new_config = Config()
        new_config.load_config(config_path)
        
        # Check that the value was saved and loaded correctly
        self.assertEqual(new_config.get('test_section', 'test_key'), 'test_value')


if __name__ == '__main__':
    unittest.main()