# Contributing to the Academic Research Paper Project

Thank you for your interest in contributing! Please follow these guidelines to help us maintain a high-quality, professional, and collaborative project.

## How to Contribute

- **Bug Reports & Feature Requests:**
  - Use GitHub Issues to report bugs or request features.
  - Provide clear, detailed descriptions and steps to reproduce issues.

- **Pull Requests:**
  - Fork the repository and create a new branch for your changes.
  - Ensure your code follows the project’s style and documentation standards.
  - Reference related issues in your pull request description.
  - Include tests and update documentation as needed.
  - Ensure all checklist items in `CHECKLIST.md` are complete for new features or major changes.

- **Documentation:**
  - Update `README.md`, guideline files, and templates as needed.
  - Document all major decisions in `DECISIONS.md` and learnings in `LEARNINGS.md`.

- **Templates & Styles:**
  - When adding new writing styles or chapter templates, update `GUIDELINES.md` and `.github/copilot-instructions.md`.

## Academic Paper Contributions: Single-File Requirement

- All new and updated papers must use a single-file approach: all content and references in `paper.md`.
- When updating outlines, checklists, or requirements, ensure they specify the single-file workflow.

## Academic Paper & Essay Workflow (2025-05-14 Update)

- All required and optional chapters/sections (as specified in `input_requirements.md` and the canonical order for the selected style) must exist before export. The assembly script halts and prints a clear error if any are missing.
- The Python script (`assemble_and_convert.py`) dynamically assembles the document in canonical order, always using the latest content from each section file.
- Advanced markdown features (fenced code blocks, tables, raw HTML, footnotes, definition lists, smart punctuation, etc.) are supported for high-fidelity Word output.
- Always use a reference .docx template for consistent formatting. References and citations are handled via Pandoc filters, with support for further customization.
- See `LEARNINGS.md` for best practices and troubleshooting tips for Markdown-to-Word conversion.
- If you update the Pandoc arguments or add new markdown features, update `LEARNINGS.md` accordingly.
- Preview exports regularly and ensure all content is professional, fact-checked, and style-compliant.

## Recursive Section Structure for Case Studies and Similar Sections

If your paper includes multiple case studies (or other repeated section types), each section should be structured using the relevant template and guidelines (e.g., Title, Description, Analysis, Discussion, Conclusion for case studies). This ensures consistency and standards compliance for all repeated sections.

When contributing or reviewing outlines, always check for sections that represent repeated units (such as case studies, experiments, or profiles) and apply the appropriate template recursively within those sections.

## Code of Conduct

All contributors must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

*Thank you for helping us build a robust, professional academic writing workflow!*
