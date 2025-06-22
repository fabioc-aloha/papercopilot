"""
Logger module for PaperCopilot.

This module provides a centralized logging system for the PaperCopilot application
with configurable log levels, formatting, and handlers.
"""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path


class Logger:
    """
    Centralized logger for PaperCopilot.
    
    Features:
    - Configurable log levels
    - Colored terminal output
    - Log file output
    - Standardized formatting
    """
    
    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[36m',  # Cyan
        'INFO': '\033[32m',   # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',   # Red
        'CRITICAL': '\033[41m\033[37m',  # White on Red background
        'RESET': '\033[0m'    # Reset to default
    }
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern to ensure only one logger instance."""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Initialize the logger with default settings if not already initialized."""
        if not hasattr(self, '_initialized') or not self._initialized:
            self.logger = logging.getLogger('papercopilot')
            self.logger.setLevel(logging.INFO)
            self.logger.propagate = False
            
            # Clear any existing handlers
            if self.logger.handlers:
                self.logger.handlers.clear()
            
            # Create console handler with custom formatter
            self._setup_console_handler()
            
            self._initialized = True
    
    def _setup_console_handler(self):
        """Set up the console handler with colored output."""
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        
        # Use a custom formatter for colored output
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                                     datefmt='%Y-%m-%d %H:%M:%S')
        console.setFormatter(formatter)
        self.logger.addHandler(console)
    
    def setup_file_handler(self, log_dir=None):
        """
        Set up a file handler for logging to a file.
        
        Args:
            log_dir (str, optional): Directory to store log files. Defaults to current directory.
        """
        if log_dir:
            log_path = Path(log_dir)
        else:
            log_path = Path.cwd()
        
        # Create log directory if it doesn't exist
        log_path.mkdir(exist_ok=True)
        
        # Use timestamp in filename to avoid overwriting
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = log_path / f"papercopilot_{timestamp}.log"
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)  # File logs can be more verbose
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
        self.info(f"Log file created at: {log_file}")
        return log_file
    
    def set_level(self, level):
        """
        Set the logging level.
        
        Args:
            level (str or int): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        if isinstance(level, str):
            level = getattr(logging, level.upper(), logging.INFO)
        
        self.logger.setLevel(level)
        for handler in self.logger.handlers:
            if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
                handler.setLevel(level)
        
        self.debug(f"Log level set to: {logging.getLevelName(level)}")
    
    def _log(self, level, msg, *args, **kwargs):
        """
        Generic logging method with color formatting for console.
        
        Args:
            level: Logging level
            msg: Message to log
            *args, **kwargs: Additional arguments passed to logger
        """
        # Use color for console output
        if os.isatty(sys.stdout.fileno()):
            level_name = logging.getLevelName(level)
            color = self.COLORS.get(level_name, self.COLORS['RESET'])
            reset = self.COLORS['RESET']
            colored_msg = f"{color}{msg}{reset}"
            
            # For console (StreamHandler)
            if level >= self.logger.level:
                for handler in self.logger.handlers:
                    if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
                        record = self.logger.makeRecord(
                            self.logger.name, level, "", 0, colored_msg, args, None
                        )
                        handler.handle(record)
        
        # Log the original message (without colors) to file handlers and other handlers
        getattr(self.logger, logging.getLevelName(level).lower())(msg, *args, **kwargs)
    
    def debug(self, msg, *args, **kwargs):
        """Log a debug message."""
        self._log(logging.DEBUG, msg, *args, **kwargs)
    
    def info(self, msg, *args, **kwargs):
        """Log an info message."""
        self._log(logging.INFO, msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        """Log a warning message."""
        self._log(logging.WARNING, msg, *args, **kwargs)
    
    def error(self, msg, *args, **kwargs):
        """Log an error message."""
        self._log(logging.ERROR, msg, *args, **kwargs)
    
    def critical(self, msg, *args, **kwargs):
        """Log a critical message."""
        self._log(logging.CRITICAL, msg, *args, **kwargs)
    
    def exception(self, msg, *args, **kwargs):
        """Log an exception with stack trace."""
        self.logger.exception(msg, *args, **kwargs)


# Create a singleton instance for easy import
log = Logger()

# Convenience functions for importing
debug = log.debug
info = log.info
warning = log.warning
error = log.error
critical = log.critical
exception = log.exception
set_level = log.set_level
setup_file_handler = log.setup_file_handler