![PaperCopilot Banner](banner.png)

# PaperCopilot: Automated Academic Paper Workflow

> **Purpose:** This project provides a fully automated, outline-driven, style-agnostic workflow for academic paper and essay creation, review, and export. It ensures compliance with professional academic standards, supports multiple citation styles, and streamlines collaboration between human and AI contributors.

> **Important:** This project contains **NO CODE**. Instead, it uses VS Code as the interface with GitHub Copilot following a structured series of prompts, outlines, templates, and instructions to guide researchers through the entire academic writing process. The system helps with research, content generation, citation management, and document formatting—all through intelligent prompts and documentation-driven automation.

> **Note:** This README is the single source of truth for all academic paper and essay automation in this repository. All contributors (human and AI) must follow the same workflow, compliance, and file handling rules described herein. For architectural decisions, consult `DECISIONS.md`.

## How PaperCopilot Works (No Code Required)

This system operates entirely through structured documentation and AI guidance:

### The Interface: VS Code + GitHub Copilot
- **VS Code** serves as the writing environment and file manager
- **GitHub Copilot** acts as your intelligent research and writing assistant
- **No programming knowledge** required—everything works through natural language commands

### The Process: Documentation-Driven Automation
1. **Structured Prompts**: Copilot follows detailed instructions in `.github/copilot-instructions.md`
2. **Research Guidance**: AI helps you research topics, find sources, and validate information
3. **Content Generation**: Outlines in `outlines/` guide section-by-section writing
4. **Style Compliance**: Guidelines in `guidelines/` ensure proper academic formatting
5. **Quality Control**: Built-in peer review and fact-checking processes

### What You Get
- **Intelligent Research Assistant**: Helps find and evaluate academic sources
- **Writing Coach**: Guides you through proper academic writing techniques
- **Citation Manager**: Ensures proper in-text citations and reference formatting
- **Quality Reviewer**: Acts as peer reviewer and academic evaluator
- **Format Expert**: Handles all technical formatting and export requirements

### Your Role as Researcher
- Define your research topic and requirements
- Guide the research direction and content focus
- Review and refine AI-generated content
- Make final decisions on arguments and conclusions

---

### For New Papers
1. **Initialize**: Use `initiate [folder] with [requirements]` command
2. **Create Content**: Use `create content` to generate all sections
3. **Review**: Use `peer review [folder]` for quality assessment
4. **Export**: Use `save to word` to generate final document

### Key Commands
- `list commands` - Show all available commands
- `initiate [folder] with [requirements]` - Set up new paper
- `create content` - Generate sections using outline
- `peer review [folder]` - Comprehensive paper review
- `fact-check [folder]` - Verify claims and sources
- `save to word` - Export to Word format

## Core Architecture

### Workflow Principles
- All contributors must follow the outline-driven, style-agnostic workflow described in `DECISIONS.md`.
- Outlines in `outlines/` define only structure (section order/names/instructions). Style, citation, and formatting are enforced by the corresponding file in `guidelines/`.
- Never hardcode style rules in outlines or templates.
- Do not change `input_requirements.md` in any paper folder if it exists.
- Document all major changes in `LEARNINGS.md` and `DECISIONS.md`.

### Template Folder Deprecation (May 2025)
**All outlines in `outlines/` are now fully self-contained and do not require or reference any files from the `template/` folder.**

- All section instructions and content guidance are embedded directly in the outlines.
- The `template/` folder is no longer required for any workflow, automation, or content generation.
- You may safely delete the `template/` folder after confirming all custom content has been migrated to the outlines.

See each outline in `outlines/` for the latest, embedded section templates and instructions.

## Current Version: Outline-Driven Workflow (2025)

This project uses an outline-driven, style-agnostic approach:
- **Structure**: Defined by outlines in `outlines/` (e.g., `researchpaper_general.md`, `essay_general.md`)
- **Style**: Enforced by guideline files in `guidelines/` (e.g., `ieee.md`, `apa7.md`)
- **Separation**: Outlines specify only structure; guidelines handle citations, formatting, and style rules
- **Flexibility**: Easy to add new paper types or citation styles without changing existing files

## Key Features

### Automation & Workflow
- Automated paper initialization with all required files
- AI-powered content generation using structured outlines
- Integrated peer review and fact-checking capabilities
- Single-file workflow with consolidated references

### Style & Format Support
- Multiple academic citation styles (APA, IEEE, MLA, Chicago, etc.)
- Professional PDF and Word export via Pandoc
- Automatic page breaks and formatting
- Style-specific templates for consistent output

### Quality Control
- Checklist-driven validation process
- Comprehensive fact-checking tools
- Publication readiness assessment
- Azure best practices integration for technical content

## Supported Citation Styles

| Style      | Guideline File          | Primary Use Cases                    |
|------------|-------------------------|--------------------------------------|
| **APA 7**  | `guidelines/apa7.md`    | Psychology, social sciences, health  |
| **IEEE**   | `guidelines/ieee.md`    | Engineering, computer science, tech  |
| **MLA**    | `guidelines/mla.md`     | Literature, humanities, languages    |
| **Chicago**| `guidelines/chicago.md` | History, literature, arts            |
| **Harvard**| `guidelines/harvard.md` | Business, social sciences, STEM      |
| **Vancouver** | `guidelines/vancouver.md` | Medical, life sciences             |
| **Turabian** | `guidelines/turabian.md` | Student papers (Chicago-based)    |
| **ABNT**   | `guidelines/abnt.md`    | Brazilian academic standards         |

For detailed formatting rules, see the corresponding guideline file.

## Supported Paper Types

### Research Papers
| Outline File                    | Structure Type                           |
|---------------------------------|------------------------------------------|
| `researchpaper_imrad.md`        | Empirical research (IMRaD format)       |
| `researchpaper_literature_review.md` | Literature reviews                 |
| `researchpaper_systematic_review.md` | Systematic reviews                 |
| `researchpaper_case_study.md`   | Case study research                      |
| `researchpaper_humanities.md`   | Humanities research (argument-driven)   |
| `researchpaper_dissertation.md` | Dissertations and theses                 |
| `researchpaper_general.md`      | General research papers                  |

### Essays & Reports  
| Outline File                    | Structure Type                           |
|---------------------------------|------------------------------------------|
| `essay_analytical.md`           | Analytical essays                        |
| `essay_argumentative.md`        | Argumentative essays                     |
| `essay_reflective.md`           | Reflective essays                        |
| `essay_general.md`              | General essays                           |
| `researchpaper_project.md`      | Project/capstone reports                 |
| `researchpaper_short_communication.md` | Brief reports/communications      |

## How It Works

### Outline Selection Process
1. **Requirements Analysis**: System reads `input_requirements.md` to determine paper type and style
2. **Outline Selection**: Appropriate outline chosen from `outlines/` folder (e.g., `researchpaper_general.md`)
3. **Style Application**: Formatting rules applied from corresponding guideline file (e.g., `guidelines/apa7.md`)  
4. **Content Generation**: Sections created following outline structure with style compliance
5. **Export**: Final document assembled and exported with proper formatting

### File Structure
```
paper_folder/
├── input_requirements.md    # Paper specifications
├── paper.md                # Main content file
├── CHECKLIST.md            # Quality control
└── outline.md              # Selected outline copy
```

---

## Key User Commands and Automation Triggers

This repository supports the following user commands for automated academic paper workflows:

- **list commands**: Display a list of all available user commands for this repository.
- **initiate [folder] with [requirements]**: Create the folder if it does not exist, then set up the paper with all required files and select the outline. No need to create a workspace or perform any additional setup beyond preparing the necessary templates for the paper.
- **create content**: Generate all required sections using the selected outline and requirements.
- **review content**: Review for academic quality and compliance. Subcommands: `review section [name]`, `review references`, `review checklist`.
- **dive [section name]**: Provide a detailed breakdown or critique of a section.
- **save to word**: Assemble and export as `.docx` with all style requirements.
- **checklist**: Display or update the completion checklist.
- **show outline**: Show the structure and instructions from the selected outline.
- **show requirements**: Show the current `input_requirements.md`.
- **peer review [folder]**: Perform a comprehensive peer review of the paper in the specified folder. This includes:
    - Ensuring the paper does not mention templates, workflow, or methodology.
    - Verifying all in-text citations have corresponding entries in the References section.
    - Alphabetizing the References section.
    - Ensuring the research question is clearly stated and answered.
    - Improving academic tone, flow, and quality throughout.
    - Acting as a peer reviewer to provide publication-ready content.
- **professor [folder]**: Perform a rigorous academic evaluation of the paper in the specified folder, acting as a professor. This includes:
    - Assigning a grade based on academic rigor and quality.
    - Providing detailed observations and recommendations for improvement.
    - Saving the evaluation as `Professor.md` in the paper folder.
- **submit [folder] to [publication]**: Submit the paper in the specified folder to the named journal or publication. This includes:
    - Evaluating if the target publication is a good fit for the paper’s topic, structure, and quality.
    - Providing a diagnostic on the likelihood of acceptance and rationale (e.g., scope match, style, novelty, rigor).
    - Saving the evaluation as `[publication].md` in the paper folder, so users can test multiple publication possibilities.
- **fact-check [folder]**: Perform a comprehensive fact-check of the paper in the specified folder. This includes:
    - Verifying all figures, statistics, and claims mentioned in the paper against the cited sources.
    - Checking the legitimacy and credibility of all references in the References section.
    - Flagging any unsupported, outdated, or questionable claims or sources.
    - Providing a summary report of fact-checking results and recommendations for corrections or improvements. The output is saved as `fact_check.md` in the paper folder.

Each command ensures professional, fact-checked, style-compliant output with proper reference management.

---

## Getting Started

### Basic Workflow
1. **Setup**: Use `initiate [folder] with [requirements]` to create new paper
2. **Requirements**: Specify paper type and citation style in `input_requirements.md`
3. **Generate**: Use `create content` to build all sections
4. **Review**: Apply `peer review [folder]` and `fact-check [folder]`
5. **Export**: Use `save to word` for final formatted document

### File Structure
Each paper folder contains:
- `input_requirements.md` - Paper specifications and requirements
- `paper.md` - Single file containing all content and references
- `CHECKLIST.md` - Quality control and validation checklist
- `outline.md` - Copy of selected structural outline

---

## Project Documentation

- **`README.md`** - This overview and user guide
- **`WORKFLOW.md`** - Detailed process documentation
- **`DECISIONS.md`** - Architectural decisions and rationale
- **`LEARNINGS.md`** - Best practices and troubleshooting
- **`GUIDELINES.md`** - Style guide index and usage instructions

For contributor guidelines and automation rules, see `.github/copilot-instructions.md`

---

*Last updated: June 2025. For the most current information, see the individual documentation files.*

- Page breaks in the Markdown source (e.g., `\pagebreak` or `\newpage`) are now converted to DOCX-compatible page breaks using Pandoc's raw XML (`<w:br w:type="page"/>`). This ensures that each major section starts on a new page in the generated Word document.
- For PDF output, use Word's export feature to preserve these page breaks.
>>>>>>> fb76016581c4c81734f1f7fbe1e8a175aeaa37f5

## Multiple Document Format Conversions

- The system now generates three separate output files for each paper:
  1. A Word document (`.docx`) generated from the Markdown source, with filename based on the short title.
  2. A LaTeX document (`paper.latex`) preserving complex mathematical formulas.
  3. A second Word document (with suffix `_latex.docx`) generated from the LaTeX source.
- This allows users to compare the different renderings and choose the one that best preserves formatting.
- To generate these files, simply run the conversion script as usual: `python convert_to_word.py <paper_folder>`
- Compare the two `.docx` files to identify any differences in formatting, especially for complex mathematical formulas.

---

## Best Practices

### For Contributors
- Follow the selected outline structure exactly
- Never hardcode style rules in outlines
- Document significant changes in `LEARNINGS.md` and `DECISIONS.md`
- Always fact-check claims and verify references

### For Academic Quality
- Ensure clear research questions and answers
- Maintain professional academic tone throughout
- Use proper in-text citations with corresponding references
- Complete all checklist items before submission

---

## Getting Help

- Check existing files: `DECISIONS.md`, `LEARNINGS.md`, `WORKFLOW.md`
- Review style guidelines: `guidelines/[style].md`
- Examine test papers: `test_paper_1/`, `test_paper_2/`
- Use the `list commands` command for all available operations

---

*For detailed automation rules and compliance requirements, see the Copilot instructions file.*
