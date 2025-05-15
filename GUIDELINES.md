# Academic Writing Guidelines Index

This project supports multiple academic writing and citation styles. Select the appropriate guideline file for your paper:

| Style      | Guideline File              | Typical Use Cases                                      |
|------------|----------------------------|--------------------------------------------------------|
| ABNT       | GUIDELINES_ABNT.md         | Academic work in Brazil                                |
| APA 7      | GUIDELINES_APA7.md         | Social sciences, health sciences                       |
| Chicago    | GUIDELINES_CHICAGO.md      | Humanities, some social sciences                       |
| Harvard    | GUIDELINES_HARVARD.md      | Social sciences, business, STEM                        |
| IEEE       | GUIDELINES_IEEE.md         | Engineering, computer science, technical fields        |
| MLA        | GUIDELINES_MLA.md          | Language, literature, humanities                       |
| Turabian   | GUIDELINES_TURABIAN.md     | Student papers in the US (based on Chicago style)      |
| Vancouver  | GUIDELINES_VANCOUVER.md    | Medical, scientific research                           |

## How to Use
- Always follow the guideline file that matches your required writing style.
- If unsure which style to use, consult your instructor, supervisor, or project lead.
- All contributors and tools (including Copilot) must reference the correct guideline file for every academic writing task.

## Workflow & Export (2025-05-14 Update)

- All required and optional sections (as specified in `input_requirements.md` and the canonical order for the selected style) must exist in the single `paper.md` file before export. The conversion scripts halt and print a clear error if any are missing.
- The Python script (`convert_to_word.py`) dynamically export the document from the single `paper.md` file, always using the latest content.
- Advanced markdown features (fenced code blocks, tables, raw HTML, footnotes, definition lists, smart punctuation, LaTeX math, etc.) are supported for high-fidelity Word and PDF output.
- Always use the appropriate style-specific Pandoc template for consistent formatting. References and citations are handled via Pandoc's built-in citeproc.
- See `LEARNINGS.md` for best practices and troubleshooting tips for Markdown-to-Word/PDF conversion.
- All contributors and automation must follow these rules for every academic writing task to ensure compliance, reliability, and publication-ready output.

---

*For detailed rules, see the linked guideline files above. Update this index as new styles are added.*
