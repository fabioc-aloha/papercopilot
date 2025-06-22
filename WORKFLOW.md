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

## PDF Export Workflow (May 2025)
- The repository no longer includes a direct Markdown-to-PDF script. To generate a PDF, first use `convert_to_word.py` to create a `.docx` file, then open the file in Microsoft Word and use "Save as PDF".
- This approach ensures that all page breaks, formatting, and style requirements are preserved exactly as in the Word document.
- For documents with complex mathematical formulas, a LaTeX output (`paper.latex`) is automatically generated alongside the Word document, which can be used with a LaTeX compiler for high-quality PDF generation.

## Simple Word Document Conversion (2025+)
- The conversion script now generates clean Word documents from Markdown source
- Focus on reliability and simplicity over multiple format generation
- Clean converter ensures compatibility and eliminates corruption issues
- To generate Word document: `python convert_to_word.py <paper_folder>`

## Page Break Handling
- Page breaks in Markdown (`\pagebreak` or `\newpage`) are automatically converted to DOCX-compatible page breaks using Pandoc's raw XML (`<w:br w:type="page"/>`).
- This ensures that each major section starts on a new page in both the Word and exported PDF documents.

### Structure vs. Style
- **outlines/**: Provides the canonical order and required/optional sections for each paper/essay type. Outlines are style-agnostic and do not contain formatting or citation rules.
- **guidelines/**: Enforces all style-specific requirements, including section naming, formatting, citation, and reference style. Each guidelines file corresponds to a citation style (e.g., ieee.md, apa7.md).
- **templates/**: Contains LaTeX templates for advanced formatting needs:
  - **LaTeX Templates**: High-quality LaTeX templates for complex mathematical content
  - **Clean Converter**: Simple, reliable Word document generation
  - **Style Support**: All 8 major citation styles supported via guidelines

### Current Template Status
| Style | LaTeX Template | Guidelines | Status |
|-------|---------------|------------|---------|
| **APA 7** | ✅ apa7.latex | ✅ apa7.md | Ready |
| **IEEE** | ✅ ieee.latex | ✅ ieee.md | Ready |
| **MLA** | ✅ mla.latex | ✅ mla.md | Ready |
| **Chicago** | ✅ chicago.latex | ✅ chicago.md | Ready |
| **Harvard** | ✅ harvard.latex | ✅ harvard.md | Ready |
| **Vancouver** | ✅ vancouver.latex | ✅ vancouver.md | Ready |
| **Turabian** | ✅ turabian.latex | ✅ turabian.md | Ready |
| **ABNT** | ✅ abnt.latex | ✅ abnt.md | Ready |
| **APA 7** | ✅ apa7.latex | ✅ apa_pandoc_reference.docx | ✅ apa7.md |
| **IEEE** | ✅ ieee.latex | ✅ ieee_pandoc_reference.docx | ✅ ieee.md |
| **MLA** | ✅ mla.latex | ✅ mla_pandoc_reference.docx | ✅ mla.md |
| **Chicago** | ✅ chicago.latex | ✅ chicago_pandoc_reference.docx | ✅ chicago.md |
| **Harvard** | ✅ harvard.latex | ✅ harvard_pandoc_reference.docx | ✅ harvard.md |
| **Vancouver** | ✅ vancouver.latex | ✅ vancouver_pandoc_reference.docx | ✅ vancouver.md |
| **Turabian** | ✅ turabian.latex | ✅ turabian_pandoc_reference.docx | ✅ turabian.md |
| **ABNT** | ✅ abnt.latex | ✅ abnt_pandoc_reference.docx | ✅ abnt.md |

---

### Workflow Steps
1. **Identify Requirements**
   - Read `input_requirements.md` to determine paper/essay type and citation style.
2. **Select Outline**
   - Use the appropriate outline from `outlines/` for structure.
3. **Apply Guidelines**
   - Use the corresponding file in `guidelines/` to enforce all style rules.
4. **Content Generation**
   - For each section in the outline, generate content using the embedded instructions in the outline, ensuring compliance with the selected style.
5. **Assembly and Export**
   - Assemble the document in the order specified by the outline, applying all style rules from the guidelines file.
   - Export to .docx and LaTeX using the conversion script (`convert_to_word.py`).
   - The LaTeX output (`paper.latex`) preserves complex mathematical formulas.
   - No table of contents is generated by default; explicit pagination is handled via `\pagebreak` tags in markdown, converted to `\newpage` in LaTeX.

### Notes
- Never hardcode style rules in outlines/ or templates/.
- All style enforcement must reference the appropriate guidelines/ file.
- Document all workflow changes in `DECISIONS.md`.
- All contributors and automation must follow these rules for every academic writing task to ensure compliance, reliability, and publication-ready output.