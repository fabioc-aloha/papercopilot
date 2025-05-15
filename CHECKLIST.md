# Pre-Submission Checklist for Academic Papers

> **Note:** As of May 2025, the `template/` folder is deprecated. All outlines are now fully self-contained and do not require or reference any files from `template/`.

Before assembling and exporting your document, ensure the following:

- [ ] All chapters are present and follow Academit-recommended outlines (e.g., IMRaD, literature review)
- [ ] In-text citations are present and formatted in the selected style
- [ ] Reference list is complete and formatted in the selected style
- [ ] All content adheres to the rules in guidelines/GUIDELINES.md
- [ ] Each chapter file has been peer reviewed
- [ ] Formatting is consistent across all files
- [ ] No content from other document folders is included

---

*Use this checklist for every academic paper to ensure quality and compliance with project standards.*

---

## Improvement Recommendations (To Review)

- Consider moving paper-specific checklists into each paper/essay folder for better tracking of individual project progress.
- Add a section to the checklist for tracking peer review feedback and revision status for each chapter.
- Periodically review and update the template and guideline files to ensure alignment with the latest academic standards and user needs.
- Automate validation of chapter/template presence and guideline compliance as part of the export or build process.
- Provide a summary of outstanding checklist items before final export to help users catch missed steps.
- Expand the checklist to include accessibility and inclusivity checks (e.g., alt text for figures, plain language summaries).
- Encourage users to document any deviations from standard workflow or structure for transparency.
- **Enhance the conversion/export script (`assemble_and_convert.py`) to:**
    - Dynamically detect required chapters/sections based on `input_requirements.md` and the selected style.
    - Assemble only the chapters present and required for the specific paper or essay, in the correct canonical order.
    - Support both research paper and essay formats, using the correct templates and structure for each.
    - Allow for optional and user-added chapters to be included in the export if present in the folder.
    - Validate that all required chapters for the selected style are present before export, and warn if any are missing.
    - Reference the chapter selection logic in `README.md` to ensure consistency between documentation and code.
    - Make the export process robust to changes in template or guideline structure, so future updates are automatically supported.

---

## GitHub Submission Checklist (Pre-Publication)

- [ ] All chapter templates are present in the `template/` folder.
- [ ] All guideline files are present in the `guidelines/` folder.
- [ ] Automation scripts are present in the project root.
- [ ] Example paper folders (e.g., `test_paper`, `test_paper_2`, `test_paper_3`) are included for demonstration and testing.
- [ ] Documentation files (`README.md`, `guidelines/GUIDELINES.md`, `.github/copilot-instructions.md`, `DECISIONS.md`, `LEARNINGS.md`, `CHECKLIST.md`) are up to date and cross-referenced.
- [ ] `.gitignore` excludes Python cache, VS Code, OS-specific, and export files.
- [ ] `LICENSE` file is present (MIT License).
- [ ] `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` are present and up to date.
- [ ] All documentation reviewed for clarity and completeness.
- [ ] Automation workflow tested end-to-end.
- [ ] No sensitive or personal data in example files.
- [ ] All changes committed and ready to push to GitHub.

*This checklist confirms the repository is ready for public submission and collaboration.*
