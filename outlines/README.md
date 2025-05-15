# outlines/

This folder contains curated outlines for academic papers and essays, organized by paper type, topic, and general structure. Outlines are style-agnostic: all citation, formatting, and style enforcement is handled by referencing the appropriate file in the `guidelines/` folder (e.g., `guidelines/ieee.md`, `guidelines/apa7.md`).

## How It Works
- Copilot will select the most appropriate outline from this folder based on the requirements in `input_requirements.md` (paper type, topic, etc.).
- The outline provides the recommended section order and structure for the document.
- All style-specific rules (citations, headings, formatting, etc.) are enforced by referencing the selected style's guideline file in `guidelines/`.

## Outline File Naming
- Use the format: `<type>_<topic>.md` (e.g., `researchpaper_technology.md`, `essay_literature.md`).
- For general outlines, omit the topic (e.g., `essay_general.md`).

## Contribution Guidelines
- When adding a new outline, include a clear section order, section titles, and brief notes for each section.
- Reference the latest best practices in `LEARNINGS.md` and `GUIDELINES.md`.
- Do not include style-specific formatting or citation rules in outlines; keep those in the `guidelines/` folder.
- Update this README as new outline conventions or features are added.

---

*This folder is the authoritative source for all curated outlines used in automated academic writing workflows. All style enforcement is handled by the corresponding file in `guidelines/`.*
