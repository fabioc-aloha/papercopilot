# GitHub Copilot Instructions for This Repository

// For human usage instructions, see the 'How to Use the Copilot Instructions File' section in README.md. This file is for Copilot/AI and automation compliance.

## 1. Architectural and Strategic Guidelines
- You must consult `DECISIONS.md` before proposing or making any architectural or strategic changes.
- Do not suggest changes that contradict `DECISIONS.md` unless explicitly instructed by a human contributor.
- `DECISIONS.md` is the authoritative record of architectural decisions and must be treated as such.
- Do not make changes to `PAPER.md` without explicit user consent.

## 2. Knowledge Sharing and Documentation
- All significant implementation learnings, optimizations, and failures must be documented in `LEARNINGS.md`.
- Use `LEARNINGS.md` as a reference to inform suggestions, avoid previously encountered issues, and build upon existing solutions.

## 3. Azure Development Standards
- This project adheres to Microsoft Azure best practices.
- When generating Azure-related code, terminal commands, or operational procedures, consult the `azure_development-get_best_practices` tool if available.

## 4. Academic Content and Writing Style Compliance
- Always check the `input_requirements.md` file in each paper folder for the required writing style (e.g., APA 7, Chicago, ABNT, MLA, Harvard, Vancouver, IEEE, Turabian).
- Reference the corresponding guideline file (e.g., `GUIDELINES_APA7.md`, `GUIDELINES_CHICAGO.md`, etc.) for all content generation, revision, and formatting.
- Ensure all citations, references, and formatting strictly follow the selected style's rules.
- If the style is not specified or unclear, ask the user for clarification before proceeding.
- Update and maintain the style index in `GUIDELINES.md` as new styles are added.
- All content must adhere to:
  - Academit-recommended outlines (e.g., IMRaD, literature review, etc.)
  - In-text citations and references in the required style
  - Professional, publication-ready standards as described in `GUIDELINES.md`
- When in doubt, consult `GUIDELINES.md` for authoritative rules on structure, style, citations, and revision.
- All contributors and tools must ensure compliance with these guidelines for every academic writing task.

## 5. Automated Research Paper Workflow
- When initializing a new paper, create all required files (e.g., chapter files, references.md, CHECKLIST.md) using the latest templates, but never change or delete `input_requirements.md` if it already exists in the folder.
- When initializing a new project or paper, determine if the requirements indicate an essay (argumentative, expository, analytical, etc.) rather than a research paper. If so, use the essay templates (e.g., `essay_introduction.md`, `essay_body.md`, `essay_conclusion.md`, `essay_references.md`) and the essay input requirements template. Only include sections relevant to the essay format and the selected style.
- All templates for papers and essays are now located in the `template/` folder at the project root. Template filenames do not include the word 'template'. For example: `template/introduction.md`, `template/essay_body.md`, `template/references.md`, etc.
- When initializing a new project, select templates from the `template/` folder based on the requirements in `input_requirements.md` (or `essay_input_requirements.md`).
- When generating or updating content, always use the correct template from the `template/` folder for the required section or chapter.
- Automate file creation and updates in the background, without opening files in the editor, to prevent file locking or save conflicts.
- The workflow for paper creation is as follows:
  1. **Define Paper Requirements:**
     - Start by completing or reviewing `input_requirements.md` in the paper's folder.
     - Clearly state the research goals, objectives, and any specific requirements.
  2. **Literature Review (First Step):**
     - Begin the writing process with the `literature_review.md` file.
     - Conduct a comprehensive review of relevant literature based on the goals in `input_requirements.md`.
     - Summarize, synthesize, and critically evaluate sources.
     - Identify gaps and trends to inform the rest of the paper.
     - Ensure all sources are cited in the required style and fact-checked.
  3. **Draft Remaining Chapters:**
     - Use insights from the literature review to guide the drafting of the remaining required chapters.
     - Select the appropriate chapter templates for each chapter based on the paper's requirements and the specified writing style in `input_requirements.md`.
     - For example, include only those chapters (e.g., `introduction.md`, `methods.md`, `results.md`, `discussion.md`, `conclusion.md`, etc.) that are required for the selected style and paper needs.
     - Follow the structure and style in `GUIDELINES.md` and the relevant guideline file (e.g., `GUIDELINES_APA7.md`).
     - Ensure all content is professional, fact-checked, and style-compliant.
  4. **References:**
     - As you write, add all cited sources to `references.md`.
     - Ensure every in-text citation has a corresponding, fact-checked reference entry.
     - Do not include reference lists in individual chapters; consolidate all references in `references.md` and organize alphabetically by author surname.
     - All references must strictly follow the selected style's standards for formatting.
  5. **Peer Review & Checklist:**
     - Each chapter must be peer reviewed for academic quality and compliance.
     - Complete the `CHECKLIST.md` before final assembly.
  6. **Assembly & Export:**
     - Once all chapters are complete and reviewed, assemble them in the canonical order required by the selected style.
     - Export the assembled content as a `.docx` file in the same folder.
     - When assembling a paper or essay, always consult `input_requirements.md` in the target folder to determine the required and optional chapters/sections for the selected style and user requirements.
     - Before assembly, check for the existence of each required and optional section file (e.g., introduction.md, body.md, conclusion.md, references.md, appendix.md, etc.) as specified in `input_requirements.md` and the canonical order for the style.
     - If any required section is missing, issue a clear error and halt the assembly/export process until the missing content is created. Do not proceed to export with missing required chapters.
     - Always use the latest content from each section file during assembly. Do not use cached, outdated, or placeholder content.
     - Assemble the document in the canonical order specified by the style and user requirements, including all required and present optional sections.
     - After assembly, verify that all sections are present and in the correct order. If any are missing, notify the user and do not proceed to export.
     - The Python assembly script (`assemble_and_convert.py`) enforces these requirements and will halt with an error if any required chapter is missing.
     - All required and optional chapters/sections (as specified in `input_requirements.md` and the canonical order for the selected style) must exist before assembly/export. The process halts with a clear error if any are missing.
     - The Python script (`assemble_and_convert.py`) dynamically assembles the document in canonical order, always using the latest content from each section file.
     - Advanced markdown features (fenced code blocks, tables, raw HTML, footnotes, definition lists, smart punctuation, etc.) are supported and should be used as documented in `LEARNINGS.md`.
     - Always use a reference .docx template for consistent formatting. References and citations are handled via Pandoc filters, with support for further customization.
     - If you update the Pandoc arguments or add new markdown features, update `LEARNINGS.md` accordingly.
     - All contributors and automation must follow these rules for every academic writing task to ensure compliance, reliability, and publication-ready output.
  7. **Final Validation:**
     - Double-check that all requirements from `input_requirements.md` are met.
     - Ensure no content from other folders is included.
  8. **Writing Quality and Consistency:**
     - Write well-developed, cohesive paragraphs in every section.
     - Fact-check all statements and support them with credible, up-to-date sources.
     - Use in-text citations and references in the required style for all claims and data.
     - Ensure all content is professional, clear, and suitable for academic publication.
     - Use the provided chapter templates to maintain structure, style, and formatting consistency.
     - Review and revise each section for clarity, coherence, and adherence to `GUIDELINES.md` before peer review.
  9. **Final Review:**
     - Double-check that all formatting requirements (e.g., double spacing, margins, font, page numbers, running head, title page, abstract, section headings) are met in the final .docx.
     - Ensure every in-text citation has a corresponding, fact-checked reference entry.
     - Use the `CHECKLIST.md` to verify all workflow and quality steps are completed before submission or publication.
  10. **Review Assembled Document for Instructional Text:**
      - After assembling the paper, review the generated assembled_paper.md (and .docx) to ensure no instructional, template, or formatting guideline text remains in the final document.
      - Remove any placeholder instructions, checklist items, or template notes before submission or publication.
  11. **Finalize Checklist:**
      - At the end of the workflow, check off all items in `CHECKLIST.md` in the paper folder to indicate project completion. This ensures the project is marked as finished, even if additional tasks are added to the checklist in the future.
  12. **Configure Assembly/Export Script:**
      - After initiating a new paper, verify that the assembly/export script (e.g., `assemble_and_convert.py`) is set to convert the content of the correct folder. Update the script arguments or configuration as needed to ensure the right paper folder is processed.
  - When generating content for any chapter, do NOT produce generic placeholders, template text, or vague summaries. All generated content must:
    - Synthesize real, relevant, and up-to-date academic knowledge for the topic, using credible sources and following the requirements in `input_requirements.md`.
    - Be written in a professional, publication-ready style, fully compliant with the selected citation and formatting guidelines.
    - Include specific, fact-checked information, critical analysis, and in-text citations in the required style (e.g., APA 7).
    - Avoid using bracketed placeholders (e.g., [insert topic], [theme 1]) or instructional comments in the output.
    - Only use instructional or placeholder text if the user explicitly requests a template or outline, not full content.
  - When you receive instructions from the user in the chat, you must ensure those instructions are incorporated into the Copilot instructions and workflow as appropriate. Update this file to reflect any new requirements, workflow changes, or user preferences provided in the chat, so that future automation and content generation fully align with user expectations.

## 6. Chapter Template Selection Logic
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

## 7. File Handling and User Instruction Preservation
- Never change or delete the `input_requirements.md` file in any paper folder if it already exists. This preserves user instructions and requirements for the paper.

## 8. Clarification and User Communication
- If user instructions are missing, ambiguous, or contradictory, always ask clarifying questions before proceeding. Do not make assumptions—seek explicit guidance from the user to ensure correct and expected behavior.

## 9. Key User Commands and Automation Triggers
This repository supports the following user commands for automated academic paper workflows:
- **initiate [folder] with [descriptions and requirements for the paper]**: Initialize a new paper folder with all required chapter files, references, and checklist, using the provided requirements. Never overwrite an existing `input_requirements.md`.
- **create content**: Generate content for all required chapters in the selected folder, following the workflow and consulting `input_requirements.md` for structure, style, and requirements.
- **review content**: Review generated content for academic quality, guideline compliance, and completeness. Ensure all instructional/template text is removed before final assembly.
- **save to word**: Assemble all chapters in canonical order and export the paper as a `.docx` file, ensuring all formatting and style requirements are met.
- **checklist**: Display or update the completion checklist for the paper folder, ensuring all workflow and quality steps are completed before submission or publication.

These commands are recognized by Copilot and automation tools. For each, the workflow will:
- Consult `input_requirements.md` for requirements and style
- Use chapter templates for structure
- Ensure all content is professional, fact-checked, and style-compliant
- Consolidate all references in `references.md`
- Remove instructional/template text before final output

See the main instructions above for full workflow and compliance details.
