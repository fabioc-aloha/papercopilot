# Architectural and Strategic Decisions

## 2025-05-14: Version 2 — Outline-Driven, Style-Agnostic Workflow
- All automation and Copilot workflows now use outline selection logic instead of hardcoded chapter selection.
- Each paper or essay type is defined by a style-agnostic outline in outlines/ (e.g., researchpaper_general.md, essay_general.md). Outlines specify only the canonical structure (order and names of required/optional sections).
- All style, citation, and formatting rules are enforced by the corresponding file in guidelines/ (e.g., ieee.md, apa7.md). Outlines never include style rules.
- The automation and assembly scripts use the selected outline to determine which section files to assemble and in what order, ensuring flexibility and style-agnostic structure.
- Contributors (human and AI) must never hardcode style rules in outlines/ or templates/.
- All documentation, templates, and scripts have been updated to reflect this logic. See README.md and .github/copilot-instructions.md for details.
- To-do: Expand outlines/ to support additional popular academic structures (see list below).

## 2025-05-14: Documentation Consistency and Streamlining
- The outline-driven, style-agnostic workflow is the single source of truth for all academic paper and essay automation in this repository.
- All contributors (human and AI) must follow the same workflow, compliance, and file handling rules, as described in `README.md` and `.github/copilot-instructions.md`.
- Outlines in `outlines/` define structure only; all style, citation, and formatting rules are enforced by the corresponding file in `guidelines/`.
- For operational rules and automation requirements, see `.github/copilot-instructions.md`.
- For workflow, commands, and user instructions, see `README.md`.
- For style and formatting, see `guidelines/GUIDELINES.md` and the appropriate style file.
- This decision supersedes any previous documentation or workflow that contradicts the outline-driven, style-agnostic approach.

## May 2025: PDF Export and Page Breaks
- Decision: Remove direct Markdown-to-PDF script (`convert_to_pdf.py`).
- Rationale: LaTeX dependency is heavy and not required for most users; Word export is more reliable for academic formatting.
- Standard: All PDF exports must be performed via Microsoft Word's "Save as PDF" feature to ensure fidelity.
- Page breaks in Markdown are now handled using Pandoc's DOCX raw XML for compatibility.

## 2025-05-15: Page Break Handling Reliability Update
- Improved the regex in `convert_to_word.py` to robustly match all variants of `\\pagebreak` and `\\newpage` (including extra spaces and case differences) and convert them to DOCX raw XML page breaks.
- Updated guidelines to instruct users to insert a line with `\\pagebreak` (or `\\newpage`) after each major section in markdown for correct pagination in Word export.

# Decision: Paper Content vs. Documentation of Workflow/Methodology

**Date:** 2025-05-19

**Decision:**

Workflow, methodology, and template structure details (such as the use of recursive, template-driven case studies or section templates) are to be documented only in repository documentation (e.g., copilot-instructions.md, README.md, WORKFLOW.md, DECISIONS.md). These details must not be included, referenced, or discussed in the academic paper itself (e.g., paper.md, abstract, introduction, or conclusion). The academic paper should focus solely on its substantive academic content, analysis, and findings, without reference to the internal workflow or automation processes used to generate or structure the content.

**Rationale:**
- Academic standards require that papers present only substantive research, analysis, and findings, not internal workflow or automation details.
- Workflow and template requirements are for internal consistency, quality control, and automation, and are not relevant to the reader or reviewers of the academic paper.
- This separation ensures clarity, professionalism, and compliance with academic publishing norms.

**Action Items:**
- Updated copilot-instructions.md to explicitly prohibit inclusion of workflow/methodology/template details in academic papers.
- All contributors must review and comply with this policy.
- Review existing and future papers to ensure compliance.

**Related Files Updated:**
- .github/copilot-instructions.md

**Related Issues:**
- User request, 2025-05-19

---

*This file is the single source of truth for all architectural, strategic, and workflow decisions for this project. Update it with every major change to ensure clarity and traceability.*
