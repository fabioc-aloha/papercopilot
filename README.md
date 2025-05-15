# Academic Research Paper Project

This project provides a modular, automated workflow for creating professional, publication-ready academic research papers using IMRaD structure and a wide range of academic writing styles.

## Supported Writing Styles

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

For each style, see the corresponding guideline file for authoritative rules on structure, citations, references, and formatting.

## Key User Instructions

- **Specify the required writing style in `input_requirements.md` for each paper.**
- Follow the human workflow:
  1. Complete or review `input_requirements.md` in the paper's folder, including the writing style.
  2. Draft each chapter using the provided templates and follow the structure required by the selected style.
  3. Add all cited sources to `references.md` (or Works Cited/Bibliography as required by the style).
  4. Peer review each chapter and complete `CHECKLIST.md` before final assembly.
  5. Assemble and export the paper as a `.docx` file using the provided script.
  6. Double-check all requirements, formatting, and references before submission.

- **Automation & Copilot/AI Rules:**
  - All detailed automation, file handling, and Copilot/AI compliance instructions are maintained in `.github/copilot-instructions.md`. Refer to that file for operational rules and automation requirements.
  - Never change or delete the `input_requirements.md` file in any paper folder if it already exists. This preserves user instructions and requirements for the paper.
  - If user instructions are missing, ambiguous, or contradictory, always ask clarifying questions before proceeding. Do not make assumptions—seek explicit guidance from the user to ensure correct and expected behavior.
  - Always follow the selected style's guideline file (see above) and project guidelines as described in `GUIDELINES.md`.
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
| **Title Page**                | APA 7, Chicago/Turabian, ABNT        | Included if required by style or journal. Not used in MLA by default.                            |
| **Abstract**                  | APA 7, ABNT                          | Included if required by style or journal.                                                        |
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
- Core chapters are always included for every paper.
- Style-dependent chapters are included based on the selected writing style in `input_requirements.md`.
- Optional and supplementary chapters can be added or removed by editing `input_requirements.md` or upon user request.
- Each chapter template contains usage instructions to guide inclusion.
- All chapter templates are maintained in the project root and referenced automatically or manually as needed.

*This table ensures that every academic paper is initialized with the appropriate structure for its style and requirements, while allowing for flexibility and user customization.*

---

## How to Use the Copilot Instructions File

- `.github/copilot-instructions.md` contains all operational, automation, and compliance rules for GitHub Copilot and other AI tools in this project.
- **Do not edit or remove this file unless you are updating project-wide automation or workflow rules.**
- All contributors and tools must follow the instructions in this file to ensure:
  - Consistent file handling and automation
  - Compliance with academic and architectural standards
  - Proper use of writing styles and guideline files
- If you are a user or contributor:
  1. Review `.github/copilot-instructions.md` to understand how Copilot and automation will behave in this repository.
  2. Specify the required writing style in `input_requirements.md` for each paper.
  3. Reference the correct guideline file for your chosen style (see `GUIDELINES.md`).
  4. If you add a new writing style or update workflow rules, update `.github/copilot-instructions.md` accordingly.
- If you are using Copilot or another AI tool:
  - Always check `.github/copilot-instructions.md` before performing any automated action or generating content.
  - Ask clarifying questions if user instructions are missing, ambiguous, or contradictory.
  - Never change or delete `input_requirements.md` if it already exists in a paper folder.
  - Follow all file handling, workflow, and academic compliance rules as described there.
- For more information on Copilot behavior and configuration, see the official documentation: https://docs.github.com/en/copilot

- **For full operational and workflow details, see:**
  - `.github/copilot-instructions.md` (automation, file handling, Copilot/AI rules)
  - `WORKFLOW.md` (human workflow overview)
  - `GUIDELINES.md` (index of academic writing and formatting standards)
  - `DECISIONS.md` (architectural and strategic decisions)

---

*This ensures all contributors and tools follow a consistent, high-quality workflow for academic research paper creation across multiple writing styles.*
