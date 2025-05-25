"""
Configuration module for PaperCopilot.

This module provides centralized configuration management for the application,
including paths, settings, and default values.
"""

import os
import json
from pathlib import Path
import sys

# Import our logger
from logger import log


class Config:
    """
    Configuration manager for PaperCopilot.
    
    Handles loading, validation, and access to application configurations.
    """
    
    # Default configuration values
    DEFAULTS = {
        "paths": {
            "templates": "./templates",
            "outlines": "./outlines",
            "guidelines": "./guidelines",
            "reference_docx": "./apa_pandoc_reference.docx"
        },
        "conversion": {
            "pandoc_path": "pandoc",  # Will search in PATH by default
            "enable_latex": True,
            "enable_html": False,
            "enable_syntax_highlighting": True,
            "wrap_text_columns": 80
        },
        "logging": {
            "level": "INFO",
            "enable_file_logging": False,
            "log_directory": "./logs"
        }
    }
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern to ensure only one configuration instance."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize with default configuration if not already initialized."""
        if not hasattr(self, '_initialized') or not self._initialized:
            self._config = self.DEFAULTS.copy()
            self._config_file = Path(os.environ.get('PAPERCOPILOT_CONFIG', 'papercopilot_config.json'))
            self._initialized = True
            
            # Try to load configuration from file
            self.load_config()
    
    def load_config(self, config_path=None):
        """
        Load configuration from a file.
        
        Args:
            config_path (str, optional): Path to configuration file. If None, uses default path.
            
        Returns:
            bool: True if configuration was loaded successfully, False otherwise.
        """
        if config_path:
            self._config_file = Path(config_path)
        
        try:
            if self._config_file.exists():
                with open(self._config_file, 'r') as f:
                    user_config = json.load(f)
                
                # Update default config with user config (deep merge)
                self._deep_update(self._config, user_config)
                log.info(f"Configuration loaded from {self._config_file}")
                
                # Update logging level if specified
                log_level = self._config.get('logging', {}).get('level', 'INFO')
                log.set_level(log_level)
                
                # Setup file logging if enabled
                if self._config.get('logging', {}).get('enable_file_logging', False):
                    log_dir = self._config.get('logging', {}).get('log_directory', './logs')
                    log.setup_file_handler(log_dir)
                
                return True
            else:
                log.debug(f"No configuration file found at {self._config_file}, using defaults")
                return False
        except Exception as e:
            log.error(f"Error loading configuration: {e}")
            return False
    
    def _deep_update(self, target, source):
        """
        Recursively update nested dictionaries.
        
        Args:
            target (dict): Dict to update
            source (dict): Dict with updates
        """
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._deep_update(target[key], value)
            else:
                target[key] = value
    
    def validate(self):
        """
        Validate configuration values.
        
        Returns:
            bool: True if configuration is valid, False otherwise.
        """
        try:
            # Check paths exist
            templates_path = Path(self.get_path('templates'))
            outlines_path = Path(self.get_path('outlines'))
            guidelines_path = Path(self.get_path('guidelines'))
            reference_docx = Path(self.get_path('reference_docx'))
            
            issues = []
            
            if not templates_path.exists():
                issues.append(f"Templates directory not found: {templates_path}")
            
            if not outlines_path.exists():
                issues.append(f"Outlines directory not found: {outlines_path}")
            
            if not guidelines_path.exists():
                issues.append(f"Guidelines directory not found: {guidelines_path}")
            
            if not reference_docx.exists():
                issues.append(f"Reference DOCX template not found: {reference_docx}")
            
            # Validate Pandoc installation
            pandoc_path = self._config['conversion']['pandoc_path']
            if pandoc_path == 'pandoc':
                # Check if pandoc is in PATH
                if not self._check_command_exists('pandoc'):
                    issues.append("Pandoc not found in PATH. Please install Pandoc or set correct path in configuration.")
            else:
                # Check if custom pandoc path exists
                pandoc_full_path = Path(pandoc_path)
                if not pandoc_full_path.exists():
                    issues.append(f"Pandoc not found at specified path: {pandoc_path}")
            
            # Report issues
            if issues:
                for issue in issues:
                    log.warning(issue)
                return False
            
            return True
        
        except Exception as e:
            log.error(f"Error validating configuration: {e}")
            return False
    
    def _check_command_exists(self, command):
        """
        Check if a command exists in PATH.
        
        Args:
            command (str): Command to check
            
        Returns:
            bool: True if command exists, False otherwise
        """
        if sys.platform == 'win32':
            check_cmd = f'where {command}'
        else:
            check_cmd = f'which {command}'
        
        return os.system(check_cmd + ' > /dev/null 2>&1') == 0
    
    def get_path(self, key):
        """
        Get path from configuration with resolved absolute path.
        
        Args:
            key (str): Path key in configuration
            
        Returns:
            str: Absolute path for the configuration value
        """
        path_str = self._config['paths'].get(key, '')
        
        # If the path is relative, make it absolute from the application root
        path = Path(path_str)
        if not path.is_absolute():
            app_root = Path(__file__).parent
            path = (app_root / path).resolve()
        
        return str(path)
    
    def get(self, section, key=None, default=None):
        """
        Get a configuration value.
        
        Args:
            section (str): Configuration section
            key (str, optional): Configuration key within section. If None, returns entire section.
            default: Default value if key is not found
            
        Returns:
            Configuration value or default if not found
        """
        if section not in self._config:
            return default
            
        if key is None:
            return self._config[section]
            
        return self._config[section].get(key, default)
    
    def set(self, section, key, value):
        """
        Set a configuration value.
        
        Args:
            section (str): Configuration section
            key (str): Configuration key within section
            value: Value to set
        """
        if section not in self._config:
            self._config[section] = {}
            
        self._config[section][key] = value
    
    def save(self, config_path=None):
        """
        Save configuration to a file.
        
        Args:
            config_path (str, optional): Path to save configuration file. If None, uses default path.
            
        Returns:
            bool: True if configuration was saved successfully, False otherwise.
        """
        if config_path:
            save_path = Path(config_path)
        else:
            save_path = self._config_file
            
        try:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, 'w') as f:
                json.dump(self._config, f, indent=2)
            
            log.info(f"Configuration saved to {save_path}")
            return True
        except Exception as e:
            log.error(f"Error saving configuration: {e}")
            return False


# Create a singleton instance for easy import
config = Config()

# For direct access to common configuration methods
get_path = config.get_path
validate = config.validate
get = config.get
set_value = config.set