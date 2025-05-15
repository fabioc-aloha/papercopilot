# GitHub Copilot Instructions for This Repository

> **Note:** This file, together with `README.md`, is the canonical source for all automation, workflow, and compliance rules for both human and AI contributors. For architectural or strategic changes, consult `DECISIONS.md`. For style and formatting, see `guidelines/GUIDELINES.md` and the appropriate style file.

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
- All content is generated and exported from a single, paginated `paper.md` file per project.
- When generating or updating content, always use the structure and instructions from the selected outline in `outlines/` for the required section or chapter.
- Automate file creation and updates in the background, without opening files in the editor, to prevent file locking or save conflicts.
- The workflow for paper creation is as follows:
  1. **Define Paper Requirements:**
     - Start by completing or reviewing `input_requirements.md` in the paper's folder.
     - Clearly state the research goals, objectives, and any specific requirements.
  2. **Outline Selection (New Logic):**
     - Read `input_requirements.md` to determine the paper or essay type (e.g., research paper, essay).
     - Select the appropriate outline from the `outlines/` folder (e.g., `researchpaper_general.md`, `essay_general.md`).
     - The outline provides the canonical structure: the order and names of required and optional sections, and all section instructions, but **never any style, citation, or formatting rules**.
  3. **Draft Sections:**
     - Use the outline to determine which sections to include in the single file and in what order.
     - Generate content for each section using the instructions embedded in the outline.
     - Ensure all content is professional, fact-checked, and style-compliant by referencing the selected guideline file in `guidelines/`.
  4. **References:**
     - As you write, add all cited sources to `references.md`.
     - Ensure every in-text citation has a corresponding, fact-checked reference entry.
     - Do not include reference lists in individual sections; consolidate all references in `references.md` and organize alphabetically by author surname.
     - All references must strictly follow the selected style's standards for formatting.
  5. **Peer Review & Checklist:**
     - Each section must be peer reviewed for academic quality and compliance.
     - Complete the `CHECKLIST.md` before final assembly.
  6. **Assembly & Export:**
     - Assemble the document in the order specified by the selected outline.
     - Apply all formatting and citation rules from the selected guideline file in `guidelines/`.
     - Export the assembled content as a `.docx` or PDF file in the same folder using the conversion scripts (`convert_to_word.py`, `convert_to_pdf.py`).
     - If any required section is missing, issue a clear error and halt the assembly/export process until the missing content is created. Do not proceed to export with missing required sections.
     - Always use the latest content from the single paper file during assembly. Do not use cached, outdated, or placeholder content.
     - After assembly, verify that all sections are present and in the correct order. If any are missing, notify the user and do not proceed to export.
  7. **Final Validation:**
     - Double-check that all requirements from `input_requirements.md` are met.
     - Ensure no content from other folders is included.
  8. **Writing Quality and Consistency:**
     - Write well-developed, cohesive paragraphs in every section.
     - Fact-check all statements and support them with credible, up-to-date sources.
     - Use in-text citations and references in the required style for all claims and data.
     - Ensure all content is professional, clear, and suitable for academic publication.
     - Use the provided section instructions in the outline to maintain structure, style, and formatting consistency.
     - Review and revise each section for clarity, coherence, and adherence to `GUIDELINES.md` before peer review.
  9. **Final Review:**
     - Double-check that all formatting requirements (e.g., double spacing, margins, font, page numbers, running head, title page, abstract, section headings) are met in the final .docx or PDF.
     - Ensure every in-text citation has a corresponding, fact-checked reference entry.
     - Use the `CHECKLIST.md` to verify all workflow and quality steps are completed before submission or publication.
  10. **Review Assembled Document for Instructional Text:**
      - After assembling the paper, review the generated output to ensure no instructional, outline, or formatting guideline text remains in the final document.
      - Remove any placeholder instructions, checklist items, or outline notes before submission or publication.
  11. **Finalize Checklist:**
      - At the end of the workflow, check off all items in `CHECKLIST.md` in the paper folder to indicate project completion. This ensures the project is marked as finished, even if additional tasks are added to the checklist in the future.
  12. **Configure Assembly/Export Script:**
      - After initiating a new paper, verify that the conversion scripts are set to process the correct folder. Update the script arguments or configuration as needed to ensure the right paper folder is processed.
  - When generating content for any section, do NOT produce generic placeholders, template text, or vague summaries. All generated content must:
    - Synthesize real, relevant, and up-to-date academic knowledge for the topic, using credible sources and following the requirements in `input_requirements.md`.
    - Be written in a professional, publication-ready style, fully compliant with the selected citation and formatting guidelines.
    - Include specific, fact-checked information, critical analysis, and in-text citations in the required style (e.g., APA 7).
    - Avoid using bracketed placeholders (e.g., [insert topic], [theme 1]) or instructional comments in the output.
    - Only use instructional or placeholder text if the user explicitly requests an outline, not full content.
- When you receive instructions from the user in the chat, you must ensure those instructions are incorporated into the Copilot instructions and workflow as appropriate. Update this file to reflect any new requirements, workflow changes, or user preferences provided in the chat, so that future automation and content generation fully align with user expectations.

## 6. Outline Selection Logic (Replaces Chapter Template Selection)
- Instead of hardcoding chapter or section selection based on style, the workflow now uses an **outline selection logic**:
  - Read `input_requirements.md` in the target folder to determine the paper or essay type (e.g., research paper, essay).
  - Select the appropriate outline from the `outlines/` folder (e.g., `researchpaper_general.md`, `essay_general.md`).
  - The outline provides the canonical structure: the order and names of required and optional sections, and all section instructions, but **never any style, citation, or formatting rules**.
  - All style enforcement (section naming, formatting, citation, etc.) is handled by the corresponding file in `guidelines/` (e.g., `ieee.md`, `apa7.md`).
- When generating or updating content, always use the structure and instructions from the selected outline in `outlines/` for the required section or chapter.
- When adding new outlines, keep them style-agnostic and focused on structure only. Never include style, citation, or formatting rules in outlines/.
- When updating or adding new guidelines, include all style-specific rules and requirements.
- Document all changes and decisions in `LEARNINGS.md` and `DECISIONS.md`.

## 7. File Handling and User Instruction Preservation
- Never change or delete the `input_requirements.md` file in any paper folder if it already exists. This preserves user instructions and requirements for the paper.

## 8. Clarification and User Communication
- If user instructions are missing, ambiguous, or contradictory, always ask clarifying questions before proceeding. Do not make assumptions—seek explicit guidance from the user to ensure correct and expected behavior.

## 9. Key User Commands and Automation Triggers
This repository supports the following user commands for automated academic paper workflows:

- **initiate [folder] with [requirements and customization]**: Initialize a new paper or essay by simply creating the necessary folder and all required section files, references, and checklist, using the provided requirements. The system will:
  - Create the target folder if it does not exist.
  - Read or create `input_requirements.md` in the target folder.
  - Select the appropriate outline from `outlines/` based on the requirements.
  - Create all required sections in a single file (e.g., `paper.md`) using the structure and instructions embedded in the selected outline. No content is copied from `template/`.
  - Never overwrite an existing `input_requirements.md`.

- **create content**: Generate content for all required sections in the selected folder, following the structure and instructions in the selected outline and consulting `input_requirements.md` for requirements and style.

- **review content**: Review generated content for academic quality, guideline compliance, and completeness. Optionally, use subcommands:
  - **review section [section name]**: Review a specific section for clarity, style, and completeness.
  - **review references**: Check that all in-text citations have corresponding, correctly formatted entries in `references.md`.
  - **review checklist**: Display or update the completion checklist for the paper folder, ensuring all workflow and quality steps are completed before submission or publication.

- **dive [section name]**: Provide a detailed breakdown, critique, or improvement suggestions for a specific section (e.g., "dive introduction").

- **save to word**: Assemble all sections in canonical order (as specified by the selected outline) and export the paper as a `.docx` or PDF file, ensuring all formatting and style requirements are met.

- **checklist**: Display or update the completion checklist for the paper folder, ensuring all workflow and quality steps are completed before submission or publication.

- **show outline**: Display the canonical structure and section instructions from the selected outline for the current paper or essay.

- **show requirements**: Display the current `input_requirements.md` for the selected folder.

These commands are recognized by Copilot and automation tools. For each, the workflow will:
- Consult `input_requirements.md` for requirements and style
- Use the selected outline for structure and section instructions
- Ensure all content is professional, fact-checked, and style-compliant
- Consolidate all references in `references.md`
- Remove instructional or outline text before final output

See the main instructions above for full workflow and compliance details.

## Version 2: Outline-Driven, Style-Agnostic Workflow (2025+)
- All automation and Copilot workflows use outline selection logic instead of hardcoded chapter selection.
- Each paper or essay type is defined by a style-agnostic outline in outlines/ (e.g., researchpaper_general.md, essay_general.md). Outlines specify only the canonical structure (order and names of required/optional sections).
- All style, citation, and formatting rules are enforced by the corresponding file in guidelines/ (e.g., ieee.md, apa7.md). Outlines never include style rules.
- The automation and assembly scripts use the selected outline to determine which section files to assemble and in what order, ensuring flexibility and style-agnostic structure.
- Contributors (human and AI) must never hardcode style rules in outlines/ or templates/.
- All documentation, templates, and scripts have been updated to reflect this logic. See README.md and .github/copilot-instructions.md for details.
- To-do: Expand outlines/ to support additional popular academic structures (see DECISIONS.md for the list).
