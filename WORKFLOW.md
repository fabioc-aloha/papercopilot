# WORKFLOW.md

## Template Folder Deprecation (May 2025)
- All outlines in `outlines/` are now fully self-contained and do not require or reference any files from the `template/` folder.
- All section instructions and content guidance are embedded directly in the outlines.
- The `template/` folder is no longer required for any workflow, automation, or content generation.
- You may safely delete the `template/` folder after confirming all custom content has been migrated to the outlines.

---

## Version 2: Outline-Driven, Style-Agnostic Workflow (2025+)
- All automation and Copilot workflows use outline selection logic instead of hardcoded chapter selection.
- Each paper or essay type is defined by a style-agnostic outline in outlines/ (e.g., researchpaper_general.md, essay_general.md). Outlines specify only the canonical structure (order and names of required/optional sections).
- All style, citation, and formatting rules are enforced by the corresponding file in guidelines/ (e.g., ieee.md, apa7.md). Outlines never include style rules.
- The automation and assembly scripts use the selected outline to determine which section files to assemble and in what order, ensuring flexibility and style-agnostic structure.
- Contributors (human and AI) must never hardcode style rules in outlines/ or templates/.
- All documentation, templates, and scripts have been updated to reflect this logic. See README.md and .github/copilot-instructions.md for details.
- To-do: Expand outlines/ to support additional popular academic structures (see DECISIONS.md for the list).

---

### Structure vs. Style
- **outlines/**: Provides the canonical order and required/optional sections for each paper/essay type. Outlines are style-agnostic and do not contain formatting or citation rules.
- **guidelines/**: Enforces all style-specific requirements, including section naming, formatting, citation, and reference style. Each guidelines file corresponds to a citation style (e.g., ieee.md, apa7.md).

### Workflow Steps
1. **Identify Requirements**
   - Read `input_requirements.md` to determine paper/essay type and citation style.
2. **Select Outline**
   - Use the appropriate outline from `outlines/` for structure.
3. **Apply Guidelines**
   - Use the corresponding file in `guidelines/` to enforce all style rules.
4. **Content Generation**
   - For each section in the outline, generate content using templates from `template/` as needed, ensuring compliance with the selected style.
5. **Assembly and Export**
   - Assemble the document in the order specified by the outline, applying all style rules from the guidelines file.
   - Export to .docx using the assembly script.

### Notes
- Never hardcode style rules in outlines/ or templates/.
- All style enforcement must reference the appropriate guidelines/ file.
- Document all workflow changes in `LEARNINGS.md` and `DECISIONS.md`.