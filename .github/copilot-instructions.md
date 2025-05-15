# GitHub Copilot Instructions for This Repository

// For human usage instructions, see the 'How to Use the Copilot Instructions File' section in README.md. This file is for Copilot/AI and automation compliance.

## Architectural and Strategic Guidelines

- You must consult `DECISIONS.md` before proposing or making any architectural or strategic changes.
- Do not suggest changes that contradict `DECISIONS.md` unless explicitly instructed by a human contributor.
- `DECISIONS.md` is the authoritative record of architectural decisions and must be treated as such.
- Do not make changes to `PAPER.md` without explicit user consent.

## Knowledge Sharing and Documentation

- All significant implementation learnings, optimizations, and failures must be documented in `LEARNINGS.md`.
- Use `LEARNINGS.md` as a reference to inform suggestions, avoid previously encountered issues, and build upon existing solutions.

## Azure Development Standards

- This project adheres to Microsoft Azure best practices.
- When generating Azure-related code, terminal commands, or operational procedures, consult the `azure_development-get_best_practices` tool if available.

## Continuous Learning and Documentation

- When you have a major breakthrough, implementation idea, or key lesson (especially when developing or refining tools such as document converters), you must automatically record it in `LEARNINGS.md`.
- Ensure that all significant insights, optimizations, and failures are captured in `LEARNINGS.md` to support continuous improvement and knowledge sharing.

## Professional Academic Content Instructions

- GitHub Copilot must always reference `GUIDELINES.md` when generating, revising, or reviewing academic content in this repository.
- All content must adhere to:
  - Academit-recommended outlines (e.g., IMRaD, literature review, etc.)
  - In-text citations and references in APA 7 style
  - Professional, publication-ready standards as described in `GUIDELINES.md`
- When in doubt, consult `GUIDELINES.md` for authoritative rules on structure, style, citations, and revision.
- All contributors and tools must ensure compliance with these guidelines for every academic writing task.

## Academic Writing Style Compliance

- Always check the `input_requirements.md` file in each paper folder for the required writing style (e.g., APA 7, Chicago, ABNT, MLA, Harvard, Vancouver, IEEE, Turabian).
- Reference the corresponding guideline file (e.g., `GUIDELINES_APA7.md`, `GUIDELINES_CHICAGO.md`, etc.) for all content generation, revision, and formatting.
- Ensure all citations, references, and formatting strictly follow the selected style's rules.
- If the style is not specified or unclear, ask the user for clarification before proceeding.
- Update and maintain the style index in `GUIDELINES.md` as new styles are added.

## Automated Research Paper Workflow

- When initializing a new paper, create all required files (e.g., chapter files, references.md, CHECKLIST.md) using the latest templates, but never change or delete `input_requirements.md` if it already exists in the folder.
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
     - Ensure all sources are cited in APA 7 style and fact-checked.
  3. **Draft Remaining Chapters:**
     - Use insights from the literature review to guide the drafting of:
       - `introduction.md`
       - `methods.md`
       - `results.md`
       - `discussion.md`
       - `conclusion.md`
     - Follow the structure and style in `GUIDELINES.md` and use chapter templates.
  4. **References:**
     - As you write, add all cited sources to `references.md`.
     - Ensure every in-text citation has a corresponding, fact-checked APA 7 entry.
     - Do not include reference lists in individual chapters; consolidate all references in `references.md` and organize alphabetically by author surname.
     - All references must strictly follow APA 7 standards for formatting, including:
       - Author names (last name, initials)
       - Year in parentheses
       - Full article/book/report title in sentence case
       - Journal/book titles in italics (handled in Word export)
       - Volume(issue), page numbers, and DOI/URL as required
       - Group authors spelled out in full (e.g., "U.S. Food and Drug Administration")
       - Hanging indent in the final exported document
  5. **Peer Review & Checklist:**
     - Each chapter must be peer reviewed for academic quality and compliance.
     - Complete the `CHECKLIST.md` before final assembly.
  6. **Assembly & Export:**
     - Once all chapters are complete and reviewed, assemble them in the canonical order:
       1. introduction.md
       2. literature_review.md
       3. methods.md
       4. results.md
       5. discussion.md
       6. conclusion.md
       7. references.md
     - Export the assembled content as a `.docx` file in the same folder.
  7. **Final Validation:**
     - Double-check that all requirements from `input_requirements.md` are met.
     - Ensure no content from other folders is included.
  8. **Writing Quality and Consistency:**
     - Write well-developed, cohesive paragraphs in every section.
     - Fact-check all statements and support them with credible, up-to-date sources.
     - Use in-text citations and references in APA 7 style for all claims and data.
     - Ensure all content is professional, clear, and suitable for academic publication.
     - Use the provided chapter templates to maintain structure, style, and formatting consistency.
     - Review and revise each section for clarity, coherence, and adherence to GUIDELINES.md before peer review.
  9. **Final Review:**
     - Double-check that all formatting requirements (APA 7: double spacing, margins, font, page numbers, running head, title page, abstract, section headings) are met in the final .docx.
     - Ensure every in-text citation has a corresponding, fact-checked reference entry.
     - Use the CHECKLIST.md to verify all workflow and quality steps are completed before submission or publication.
  10. **Review Assembled Document for Instructional Text:**
      - After assembling the paper, review the generated assembled_paper.md (and .docx) to ensure no instructional, template, or formatting guideline text remains in the final document.
      - Remove any placeholder instructions, checklist items, or template notes before submission or publication.
  11. **Finalize Checklist:**
      - At the end of the workflow, check off all items in `CHECKLIST.md` in the paper folder to indicate project completion. This ensures the project is marked as finished, even if additional tasks are added to the checklist in the future.
  12. **Configure Assembly/Export Script:**
      - After initiating a new paper, verify that the assembly/export script (e.g., `assemble_and_convert.py`) is set to convert the content of the correct folder. Update the script arguments or configuration as needed to ensure the right paper folder is processed.

## Chapter Template Selection Logic

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

## File Handling and User Instruction Preservation

- Never change or delete the `input_requirements.md` file in any paper folder if it already exists. This preserves user instructions and requirements for the paper.

## Clarification and User Communication

- If user instructions are missing, ambiguous, or contradictory, always ask clarifying questions before proceeding. Do not make assumptions—seek explicit guidance from the user to ensure correct and expected behavior.

## Preparing for GitHub Submission

Before submitting this project to GitHub, ensure the following best practices and repository standards are met:

### 1. Repository Structure
- All chapter templates, guideline files, and automation scripts are present in the project root.
- Example paper folders (e.g., `test_paper`, `test_paper_2`, `test_paper_3`) are included for demonstration and testing.
- Documentation files (`README.md`, `GUIDELINES.md`, `.github/copilot-instructions.md`, `DECISIONS.md`, `LEARNINGS.md`, `CHECKLIST.md`) are up to date and cross-referenced.

### 2. Essential Files
- Add a `.gitignore` file to exclude unnecessary files (e.g., Python cache, temporary files, local exports).
- Add a `LICENSE` file to specify the repository's license (e.g., MIT, Apache 2.0, or as required).
- Add a `CONTRIBUTING.md` file with contribution guidelines for users and collaborators.
- Add a `CODE_OF_CONDUCT.md` file to set expectations for community behavior.

### 3. Documentation
- Ensure `README.md` provides a clear project overview, supported styles, workflow, and usage instructions.
- Ensure `.github/copilot-instructions.md` is referenced for automation and compliance.
- Ensure all guideline files are listed and described in `GUIDELINES.md`.
- Ensure all architectural decisions are recorded in `DECISIONS.md`.
- Ensure all major learnings and optimizations are in `LEARNINGS.md`.

### 4. Code and Template Quality
- All chapter templates include usage instructions and are up to date.
- The automation script (`assemble_and_convert.py`) is tested and documented.
- Example papers are style-compliant and demonstrate the workflow.

### 5. Final Checklist
- [ ] Add `.gitignore` (Python, VS Code, OS-specific, and export files)
- [ ] Add `LICENSE`
- [ ] Add `CONTRIBUTING.md`
- [ ] Add `CODE_OF_CONDUCT.md`
- [ ] Review and update all documentation for clarity and completeness
- [ ] Test the automation workflow end-to-end
- [ ] Remove any sensitive or personal data from example files
- [ ] Commit all changes and push to GitHub

---

*This section provides a clear, actionable checklist to ensure the repository is ready for public submission and collaboration on GitHub.*

*This ensures all generated content is professional, consistent, and suitable for academic publication.*
