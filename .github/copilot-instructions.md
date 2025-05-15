# GitHub Copilot Instructions for This Repository

> **Note:** This file, with `README.md`, is the canonical source for automation, workflow, and compliance rules. For architecture, see `DECISIONS.md`. For style, see `guidelines/GUIDELINES.md` and the relevant style file.

## 1. Core Principles
- All contributors must follow the outline-driven, style-agnostic workflow described in `DECISIONS.md`.
- Outlines in `outlines/` define only structure (section order/names/instructions). Style, citation, and formatting are enforced by the corresponding file in `guidelines/`.
- Never hardcode style rules in outlines or templates.
- Do not change `input_requirements.md` in any paper folder if it exists.
- Document all major changes in `LEARNINGS.md` and `DECISIONS.md`.

## 2. Academic Paper Workflow (Summary)
1. **Define Requirements:**
   - Review or create `input_requirements.md` in the paper folder.
2. **Select Outline:**
   - Use `input_requirements.md` to select the correct outline from `outlines/`.
3. **Draft Sections:**
   - Generate content for each section in order, using outline instructions and style guidelines.
4. **References:**
   - Add all cited sources to `references.md`. No reference lists in sections; consolidate in `references.md`.
5. **Peer Review & Checklist:**
   - Review each section for quality and compliance. Complete `CHECKLIST.md` before assembly/export.
6. **Assembly & Export:**
   - Assemble sections in outline order. Apply style rules. Export as `.docx` using `convert_to_word.py`. Do not export if required sections are missing.
7. **Final Validation:**
   - Ensure all requirements are met and no content from other folders is included.
8. **Writing Quality:**
   - Write clear, fact-checked, publication-ready content with in-text citations and references in the required style.
9. **Final Review:**
   - Check formatting, references, and remove any instructional/outline text before submission.
10. **Finalize Checklist:**
    - Mark all items in `CHECKLIST.md` as complete.
11. **Configure Export Script:**
    - Ensure conversion scripts process the correct folder.

## 3. Key Commands
- **initiate [folder] with [requirements]**: Create a new paper/essay folder, all required files, and select the outline.
- **create content**: Generate all required sections using the selected outline and requirements.
- **review content**: Review for academic quality and compliance. Subcommands: `review section [name]`, `review references`, `review checklist`.
- **dive [section name]**: Provide a detailed breakdown or critique of a section.
- **save to word**: Assemble and export as `.docx` with all style requirements.
- **checklist**: Display or update the completion checklist.
- **show outline**: Show the structure and instructions from the selected outline.
- **show requirements**: Show the current `input_requirements.md`.

## 4. Azure Development
- Always use Microsoft Azure best practices for Azure-related code or operations.

## 5. Clarification
- If instructions are missing or unclear, ask for clarification before proceeding.

---

*For full details, see `README.md`, `DECISIONS.md`, and `guidelines/GUIDELINES.md`. This file supersedes any previous workflow or automation documentation.*
