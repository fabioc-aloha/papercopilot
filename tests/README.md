# PaperCopilot Tests

This directory contains automated tests for the PaperCopilot application.

## Running Tests

To run all tests:

```bash
python -m pytest
```

To run tests with coverage report:

```bash
python -m pytest --cov=. --cov-report=term
```

To run a specific test file:

```bash
python -m pytest tests/test_config.py
```

## Test Structure

- `test_config.py`: Tests for the configuration module
- `test_conversion.py`: Tests for the document conversion functionality
- `test_dependencies.py`: Tests for the dependency checker module

## Adding New Tests

When adding new tests:

1. Create a test file named `test_*.py`
2. Import the necessary modules
3. Create a test class that inherits from `unittest.TestCase`
4. Implement test methods named `test_*`
5. Use assertions to verify expected behavior

## Mocking Dependencies

Many tests use the `unittest.mock` module to simulate dependencies and external systems.
This allows testing components in isolation without relying on the actual filesystem
or external tools like Pandoc.