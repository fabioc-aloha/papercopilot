# Architectural and Strategic Decisions

This file records all major architectural and strategic decisions for this project. Please update this file whenever a significant decision is made.

## 2025-05-14: Initial Architecture for AI Academic Research Assistant
- Build an AI assistant leveraging Azure OpenAI (model and endpoint from `.env`) to help users build, research, and review academic research papers.
- All generated and revised content must follow Academit-recommended outlines (e.g., IMRaD, literature review), use in-text citations and references in APA 7 style, and adhere to professional, publication-ready standards as described in `GUIDELINES.md`.
- Modular structure defined in `ARCHITECTURE.md`:
  - User Interface: Command-line or web interface for user interaction
  - Core Engine: Python backend that connects to Azure OpenAI, applies academic writing guidelines, and handles citation/reference formatting
  - Citation Manager: Module for in-text citations and reference list generation
  - Paper Structure Module: Enforces academic outlines (e.g., IMRaD, literature review, etc.)
  - Revision Engine: Suggests and applies improvements per academic and professional standards
  - Guidelines Integration: All content generation and revision must reference `GUIDELINES.md`
- File structure:
  - `main.py` — Entry point for the assistant
  - `guidelines.py` — Loads and applies rules from `GUIDELINES.md`
  - `citation.py` — Handles APA 7 citations and references
  - `structure.py` — Enforces academic outlines
  - `revision.py` — Suggests and applies revisions
  - `utils.py` — Helper functions
  - `GUIDELINES.md` — Authoritative writing and formatting rules
- `GUIDELINES.md` is the authoritative source for academic writing and revision rules. All contributors and tools (including GitHub Copilot) must reference this file for every academic writing task.
- All references must be fact-checked and included in a dedicated References section. Only sources cited in the chapters should appear in the References file, formatted in APA 7 style.

## 2025-05-14: Modular Document Structure for Academic Papers
- Each academic document will reside in its own folder within the project workspace.
- Key chapters (e.g., Introduction, Literature Review, Methods, Results, Discussion, Conclusion, References) will be split into separate files within the document's folder to enable modular review and updates.
- When a document is finalized, its chapter files will be programmatically assembled and exported as a single `.docx` file in the same directory.
- Content from different document folders must not be mixed at any stage of the process to ensure academic integrity and organizational clarity.

## 2025-05-14: Automated Validation and Quality Assurance
- Implement pre-submission checklist (`CHECKLIST.md`) to ensure all content meets project standards before assembly/export.
- Provide template files for each chapter to guide contributors in structure and citation formatting.
- Require peer review of each chapter file before final assembly.
- Plan to implement automated scripts for validating structure, citations, and references in the future.
- Enforce version control and regular testing of the assembly/export process.

## 2025-05-14: Reference Consolidation Policy
- All references must be consolidated in a single, alphabetized `references.md` file for each paper.
- Reference lists are not permitted in individual chapter files (e.g., introduction.md, methods.md, etc.).
- All chapter templates, `GUIDELINES.md`, and workflow documentation updated to enforce this policy.
- This ensures compliance with APA 7, improves consistency, and streamlines the assembly/export process.

## 2025-05-14: Paper Initialization Automation Policy
- When a user requests to "initiate paper in folder X", GitHub Copilot must:
  - Read the `input_requirements.md` in the specified folder.
  - Create all required chapter files (`introduction.md`, `literature_review.md`, `methods.md`, `results.md`, `discussion.md`, `conclusion.md`, `references.md`) using the latest templates.
  - Create or reset the `CHECKLIST.md` in the folder using the template.
- The user will then review the setup, add or modify actions in the checklist, and may request Copilot to generate the content for each section.
- This ensures a repeatable, user-driven, and fully automated paper setup process, supporting user customization and workflow compliance.

---

*This file is the single source of truth for all architectural, strategic, and workflow decisions for this project. Update it with every major change to ensure clarity and traceability.*
