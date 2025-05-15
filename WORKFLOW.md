# WORKFLOW.md

## Academic Paper & Essay Workflow (2025-05-14 Update)

### Steps
1. Define requirements in `input_requirements.md` (specify style, required/optional chapters, objectives).
2. Ensure all required and optional chapters are present in the target folder.
3. Draft content using supported markdown features (see `LEARNINGS.md`).
4. Review and fact-check all content for academic quality and compliance.
5. Run: `python assemble_and_convert.py <paper_folder>`
6. If any required chapter is missing, the script will halt and print an error.
7. The assembled document will be exported as a .docx file in the same folder, using the reference .docx template for formatting.
8. Preview the export and address any formatting or content issues as needed.

- See `LEARNINGS.md` for best practices and troubleshooting tips for Markdown-to-Word conversion.