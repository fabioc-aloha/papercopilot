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

## June 2025: Multiple Document Format Conversions
- Decision: Added functionality to convert both Markdown and LaTeX files to separate .docx outputs.
- Rationale: Different rendering engines may handle complex content (like mathematical formulas) differently. 
- Implementation: The `convert_to_word.py` script now generates three files: a .docx from Markdown, a .latex file, and a second .docx from the LaTeX source.
- Standard: Users should compare both Word documents to determine which better preserves their specific content and formatting requirements.

---

*This file is the single source of truth for all architectural, strategic, and workflow decisions for this project. Update it with every major change to ensure clarity and traceability.*
