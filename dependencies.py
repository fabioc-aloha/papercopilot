"""
Dependency checker for PaperCopilot.

This module verifies that all required dependencies are installed and
provides functions to check for specific dependencies.
"""

import importlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Import our logger
from logger import log


class DependencyChecker:
    """
    Checks for required dependencies and provides methods to verify them.
    """
    
    REQUIRED_MODULES = {
        'markdown': '3.0',
        'pypandoc': '1.11',
    }
    
    OPTIONAL_MODULES = {
        'python-docx': '0.8.10',
    }
    
    def __init__(self):
        """Initialize the dependency checker."""
        self._missing_required = []
        self._missing_optional = []
        self._version_mismatch = []
    
    def check_python_version(self, min_version=(3, 7)):
        """
        Check if the current Python version meets the minimum requirements.
        
        Args:
            min_version (tuple): Minimum required Python version (major, minor)
            
        Returns:
            bool: True if Python version is sufficient, False otherwise
        """
        current_version = sys.version_info[:2]
        result = current_version >= min_version
        
        if not result:
            log.error(f"Python version {'.'.join(map(str, current_version))} is lower than the required {'.'.join(map(str, min_version))}")
        else:
            log.debug(f"Python version check passed: {'.'.join(map(str, current_version))}")
            
        return result
    
    def check_module(self, module_name, min_version=None):
        """
        Check if a Python module is installed and meets version requirements.
        
        Args:
            module_name (str): Name of the module to check
            min_version (str, optional): Minimum required version
            
        Returns:
            bool: True if module is installed and meets version requirements, False otherwise
        """
        try:
            # Handle special case for python-docx which is imported as 'docx'
            import_name = 'docx' if module_name == 'python-docx' else module_name
            module = importlib.import_module(import_name)
            
            # If no version check is required
            if not min_version:
                log.debug(f"Module {module_name} is installed")
                return True
                
            # Get version from different possible attributes
            version = None
            for attr in ['__version__', 'version', 'VERSION']:
                if hasattr(module, attr):
                    version = getattr(module, attr)
                    break
            
            # If we couldn't find version information
            if version is None:
                log.warning(f"Could not determine version for {module_name}")
                return True
                
            # Check if version meets requirements
            if self._compare_versions(version, min_version) >= 0:
                log.debug(f"Module {module_name} version {version} meets requirements (>= {min_version})")
                return True
            else:
                log.warning(f"Module {module_name} version {version} is lower than required {min_version}")
                self._version_mismatch.append((module_name, version, min_version))
                return False
                
        except ImportError:
            log.warning(f"Module {module_name} is not installed")
            return False
    
    def _compare_versions(self, version1, version2):
        """
        Compare two version strings.
        
        Args:
            version1 (str): First version string
            version2 (str): Second version string
            
        Returns:
            int: 1 if version1 > version2, 0 if version1 == version2, -1 if version1 < version2
        """
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split('.')]
            
        v1 = normalize(str(version1))
        v2 = normalize(str(version2))
        
        for i in range(max(len(v1), len(v2))):
            n1 = v1[i] if i < len(v1) else 0
            n2 = v2[i] if i < len(v2) else 0
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0
    
    def check_external_tool(self, command, min_version=None, version_flag='--version', version_pattern=None):
        """
        Check if an external command-line tool is installed.
        
        Args:
            command (str): Command to check
            min_version (str, optional): Minimum required version
            version_flag (str): Flag to get version information
            version_pattern (str): Regex pattern to extract version
            
        Returns:
            bool: True if tool is installed and meets version requirements, False otherwise
        """
        # Check if command exists in PATH
        if not shutil.which(command):
            log.warning(f"{command} is not installed or not in PATH")
            return False
            
        # If no version check is required
        if not min_version:
            log.debug(f"{command} is installed")
            return True
            
        # Get version
        try:
            result = subprocess.run(
                [command, version_flag],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                log.warning(f"Failed to get {command} version: {result.stderr}")
                return False
                
            # Extract version using pattern or just use output
            version = result.stdout
            if version_pattern:
                match = re.search(version_pattern, version)
                if match:
                    version = match.group(1)
                else:
                    log.warning(f"Could not extract {command} version using pattern")
                    return False
                    
            # Check if version meets requirements
            if self._compare_versions(version.strip(), min_version) >= 0:
                log.debug(f"{command} version {version.strip()} meets requirements (>= {min_version})")
                return True
            else:
                log.warning(f"{command} version {version.strip()} is lower than required {min_version}")
                return False
                
        except Exception as e:
            log.error(f"Error checking {command} version: {e}")
            return False
    
    def check_pandoc(self, min_version='2.11'):
        """
        Check if Pandoc is installed with the minimum required version.
        
        Args:
            min_version (str): Minimum required Pandoc version
            
        Returns:
            bool: True if Pandoc is installed and meets version requirements, False otherwise
        """
        return self.check_external_tool('pandoc', min_version, version_pattern=r'pandoc\s+([0-9.]+)')
    
    def check_all_dependencies(self):
        """
        Check all required and optional dependencies.
        
        Returns:
            bool: True if all required dependencies are met, False otherwise
        """
        # Reset lists
        self._missing_required = []
        self._missing_optional = []
        self._version_mismatch = []
        
        # Check Python version
        python_ok = self.check_python_version()
        
        # Check required modules
        modules_ok = True
        for module, version in self.REQUIRED_MODULES.items():
            if not self.check_module(module, version):
                self._missing_required.append(module)
                modules_ok = False
        
        # Check optional modules
        for module, version in self.OPTIONAL_MODULES.items():
            if not self.check_module(module, version):
                self._missing_optional.append(module)
        
        # Check Pandoc
        pandoc_ok = self.check_pandoc()
        if not pandoc_ok:
            self._missing_required.append('pandoc')
        
        # Log results
        if not modules_ok or not pandoc_ok:
            log.warning("Some required dependencies are missing or have version mismatches")
            
            if self._missing_required:
                log.error(f"Missing required dependencies: {', '.join(self._missing_required)}")
                
            if self._version_mismatch:
                for module, current, required in self._version_mismatch:
                    log.warning(f"Version mismatch for {module}: found {current}, required {required}")
                    
        if self._missing_optional:
            log.warning(f"Missing optional dependencies: {', '.join(self._missing_optional)}")
        
        # Return True only if all required dependencies are met
        return python_ok and modules_ok and pandoc_ok
    
    def get_dependency_report(self):
        """
        Get a formatted report of dependency status.
        
        Returns:
            str: Formatted dependency report
        """
        lines = ["Dependency Status Report:", "-" * 25]
        
        # Python version
        current_python = '.'.join(map(str, sys.version_info[:3]))
        lines.append(f"Python: {current_python}")
        
        # Required modules
        lines.append("\nRequired Modules:")
        for module, version in self.REQUIRED_MODULES.items():
            try:
                # Handle special case for python-docx
                import_name = 'docx' if module == 'python-docx' else module
                mod = importlib.import_module(import_name)
                
                # Try to get version from different attributes
                mod_version = "Unknown"
                for attr in ['__version__', 'version', 'VERSION']:
                    if hasattr(mod, attr):
                        mod_version = getattr(mod, attr)
                        break
                
                status = "✓" if module not in self._missing_required else "✗"
                lines.append(f"  {status} {module}: {mod_version} (required: {version})")
            except ImportError:
                lines.append(f"  ✗ {module}: Not installed (required: {version})")
        
        # Optional modules
        lines.append("\nOptional Modules:")
        for module, version in self.OPTIONAL_MODULES.items():
            try:
                import_name = 'docx' if module == 'python-docx' else module
                mod = importlib.import_module(import_name)
                
                # Try to get version from different attributes
                mod_version = "Unknown"
                for attr in ['__version__', 'version', 'VERSION']:
                    if hasattr(mod, attr):
                        mod_version = getattr(mod, attr)
                        break
                
                status = "✓" if module not in self._missing_optional else "✗"
                lines.append(f"  {status} {module}: {mod_version} (suggested: {version})")
            except ImportError:
                lines.append(f"  ✗ {module}: Not installed (suggested: {version})")
        
        # External tools
        lines.append("\nExternal Tools:")
        pandoc_installed = shutil.which('pandoc') is not None
        pandoc_version = "Unknown"
        
        if pandoc_installed:
            try:
                result = subprocess.run(['pandoc', '--version'], capture_output=True, text=True, check=False)
                match = re.search(r'pandoc\s+([0-9.]+)', result.stdout)
                if match:
                    pandoc_version = match.group(1)
            except Exception:
                pass
                
        status = "✓" if pandoc_installed else "✗"
        lines.append(f"  {status} Pandoc: {pandoc_version}")
        
        return "\n".join(lines)
    
    def get_missing_required(self):
        """
        Get a list of missing required dependencies.
        
        Returns:
            list: Names of missing required dependencies
        """
        return self._missing_required.copy()
    
    def get_missing_optional(self):
        """
        Get a list of missing optional dependencies.
        
        Returns:
            list: Names of missing optional dependencies
        """
        return self._missing_optional.copy()
    
    def get_version_mismatches(self):
        """
        Get a list of dependencies with version mismatches.
        
        Returns:
            list: Tuples of (module_name, current_version, required_version)
        """
        return self._version_mismatch.copy()


# Create an instance for easy import
dependency_checker = DependencyChecker()

# For direct access to common methods
check_all_dependencies = dependency_checker.check_all_dependencies
get_dependency_report = dependency_checker.get_dependency_report