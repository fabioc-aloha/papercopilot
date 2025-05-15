# PaperCopilot: Automated Academic Paper Workflow

## Purpose
PaperCopilot streamlines the creation, management, and export of academic research papers and essays, ensuring strict compliance with professional and publication-ready standards for multiple citation styles (APA 7, Chicago, ABNT, MLA, Harvard, Vancouver, IEEE, Turabian, and more).

## Features
- Automated initialization of new academic papers and essays with all required files and templates
- Support for multiple academic writing and citation styles
- Workflow automation for literature review, chapter/section drafting, peer review, and export
- Centralized reference management and style compliance
- Checklist-driven quality control and final validation
- Extensible template and guideline system (all templates are now in the `template/` folder, filenames do not include the word 'template')
- Azure best practices integration for technical content

## User Instructions

### Key Commands and Workflow

#### 1. `initiate [folder] with [descriptions and requirements for the paper or essay]`
- Initializes a new paper or essay in the specified folder.
- Creates all required files (e.g., `introduction.md`, `literature_review.md`, `essay_body.md`, etc.) using the latest templates from the `template/` folder.
- Reads and preserves any existing `input_requirements.md` file.
- Use this command to start a new project with custom requirements.

#### 2. `create content`
- Generates content for all required chapters/sections in the selected folder.
- Consults `input_requirements.md` to determine structure, style, and requirements.
- Follows the automated workflow and uses templates from the `template/` folder.
- Ensures all content is professional, fact-checked, and includes citations and references in the required style.

#### 3. `review content`
- Reviews the generated content for academic quality, guideline compliance, and completeness.
- Checks for adherence to the selected writing style and project requirements.
- Ensures all instructional/template text is removed before final assembly.

#### 4. `save to word`
- Assembles all chapters/sections in canonical order and exports the document as a `.docx` file in the same folder.
- Ensures all formatting and style requirements are met in the exported document.

#### 5. `checklist`
- Displays or updates the completion checklist for the folder.
- Ensures all workflow and quality steps are completed before submission or publication.

---

For more details on workflow and style compliance, see `.github/copilot-instructions.md`, `guidelines/GUIDELINES.md`, and the `guidelines/` folder.

## Supported Writing Styles

| Style      | Guideline File                  | Typical Use Cases                                      |
|------------|---------------------------------|--------------------------------------------------------|
| ABNT       | guidelines/abnt.md              | Academic work in Brazil                                |
| APA 7      | guidelines/apa7.md              | Social sciences, health sciences                       |
| Chicago    | guidelines/chicago.md           | Humanities, some social sciences                       |
| Harvard    | guidelines/harvard.md           | Social sciences, business, STEM                        |
| IEEE       | guidelines/ieee.md              | Engineering, computer science, technical fields        |
| MLA        | guidelines/mla.md               | Language, literature, humanities                       |
| Turabian   | guidelines/turabian.md          | Student papers in the US (based on Chicago style)      |
| Vancouver  | guidelines/vancouver.md         | Medical, scientific research                           |

For each style, see the corresponding guideline file for authoritative rules on structure, citations, references, and formatting.

## Key User Instructions

- **Specify the required writing style in `input_requirements.md` for each paper or essay.**
- Follow the human workflow:
  1. Complete or review `input_requirements.md` in the folder, including the writing style.
  2. Draft each chapter/section using the provided templates from the `template/` folder and follow the structure required by the selected style.
  3. Add all cited sources to `references.md` (or Works Cited/Bibliography as required by the style).
  4. Peer review each chapter/section and complete `CHECKLIST.md` before final assembly.
  5. Assemble and export the document as a `.docx` file using the provided script.
  6. Double-check all requirements, formatting, and references before submission.

- **Automation & Copilot/AI Rules:**
  - All detailed automation, file handling, and Copilot/AI compliance instructions are maintained in `.github/copilot-instructions.md`. Refer to that file for operational rules and automation requirements.
  - Never change or delete the `input_requirements.md` file in any folder if it already exists. This preserves user instructions and requirements for the document.
  - If user instructions are missing, ambiguous, or contradictory, always ask clarifying questions before proceeding. Do not make assumptions—seek explicit guidance from the user to ensure correct and expected behavior.
  - Always follow the selected style's guideline file (see above) and project guidelines as described in `guidelines/GUIDELINES.md`.
  - Reference `DECISIONS.md` before making architectural or strategic changes.
  - Document all significant implementation learnings, optimizations, and failures in `LEARNINGS.md`.

## Automatic Chapter Selection Logic

The following table summarizes how chapters are selected and included based on the writing style and user requirements:

| Chapter Type                  | Included For (Styles)                | Usage Guidelines                                                                                 |
|-------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------|
| **Introduction**              | All                                  | Always included as a core chapter.                                                               |
| **Literature Review**         | All                                  | Always included as a core chapter.                                                               |
| **Methods / Methodology**     | All                                  | Always included as a core chapter.                                                               |
| **Results**                   | All                                  | Always included as a core chapter.                                                               |
| **Discussion**                | All                                  | Always included as a core chapter.                                                               |
| **Conclusion**                | All                                  | Always included as a core chapter.                                                               |
| **References / Works Cited / Bibliography** | All (style-dependent)             | Always included; file name and format depend on style (see guideline file).                      |
| **Title Page**                | APA 7, Chicago/Turabian, ABNT, IEEE  | Included if required by style or journal. Not used in MLA by default.                            |
| **Abstract**                  | APA 7, ABNT, IEEE                    | Included if required by style or journal.                                                        |
| **Author Note**               | APA 7                                | Include if required by journal or instructor.                                                    |
| **Works Cited**               | MLA                                  | Used instead of References/Bibliography.                                                         |
| **Bibliography**              | Chicago/Turabian                     | Used instead of References/Works Cited.                                                          |
| **Footnotes/Endnotes**        | Chicago/Turabian, as needed          | Include if required by style or for additional commentary.                                       |
| **Table of Contents**         | Chicago/Turabian, ABNT               | Include if required by style or for long documents.                                              |
| **Cover Page**                | ABNT                                 | Include if required by institution.                                                              |
| **Resumo (Abstract in Portuguese)** | ABNT                         | Include if required by institution.                                                              |
| **Sumário (Summary)**         | ABNT                                 | Include if required by institution.                                                              |
| **Appendix / Appendices**     | All (optional)                       | Include if referenced in requirements or needed for supplementary material.                      |
| **Acknowledgments**           | All (optional)                       | Include if requested by user or required by institution.                                         |
| **Dedication**                | All (optional)                       | Include if requested by user.                                                                    |
| **Preface**                   | All (optional)                       | Include if requested by user.                                                                    |
| **List of Figures / Tables**  | All (optional)                       | Include if document contains multiple figures/tables and style requires a list.                  |
| **Glossary**                  | All (optional)                       | Include if document uses specialized terminology.                                                |
| **Executive Summary**         | All (optional)                       | Include for reports or as required by institution.                                               |
| **Statement of the Problem**  | All (optional)                       | Include if required by assignment or institution.                                                |
| **Background**                | All (optional)                       | Include if required by assignment or institution.                                                |
| **Recommendations**           | All (optional)                       | Include for reports or as required by assignment.                                                |
| **Limitations**               | All (optional)                       | Include if required by assignment or institution.                                                |
| **Future Work / Directions for Future Research** | All (optional)         | Include if required by assignment or institution.                                                |
| **Ethical Considerations**    | All (optional)                       | Include if required by assignment or institution.                                                |
| **Funding Statement**         | All (optional)                       | Include if required by journal or institution.                                                   |
| **Conflict of Interest Statement** | All (optional)                  | Include if required by journal or institution.                                                   |

**Usage Guidelines:**
- Core chapters are always included for every paper or essay.
- Style-dependent chapters are included based on the selected writing style in `input_requirements.md`.
- Optional and supplementary chapters can be added or removed by editing `input_requirements.md` or upon user request.
- Each chapter template contains usage instructions to guide inclusion.
- All chapter templates are maintained in the `template/` folder and referenced automatically or manually as needed.

*This table ensures that every academic paper or essay is initialized with the appropriate structure for its style and requirements, while allowing for flexibility and user customization.*

---

## Technical Implementation Details
- All templates are now in the `template/` folder at the project root. Filenames do not include the word 'template'.
- Example paper and essay folders (e.g., `test_paper_1`, `test_paper_2`, `test_paper_3`) are included for demonstration and testing.
- Documentation files (`README.md`, `guidelines/GUIDELINES.md`, `.github/copilot-instructions.md`, `DECISIONS.md`, `LEARNINGS.md`, `CHECKLIST.md`) are up to date and cross-referenced.
- The automation script (`assemble_and_convert.py`) is used for assembling and exporting documents.
- The repository includes a `.gitignore`, `LICENSE`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` for best practices and collaboration.

---

*For full workflow, compliance, and customization details, consult the Copilot instructions, guideline files in the `guidelines/` folder, and the `template/` folder.*
