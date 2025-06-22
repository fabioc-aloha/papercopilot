# Academic Paper Outlines

This folder contains structured outlines for different types of academic papers and essays. Each outline defines the canonical structure and section requirements for a specific paper type.

## How Outlines Work

### Selection Process
Outlines are automatically selected based on specifications in `input_requirements.md`:
- **Paper type** (research paper, essay, report)
- **Academic discipline** (STEM, humanities, social sciences)
- **Structural needs** (empirical research, literature review, case study)

### Structure vs Style
- **Outlines define STRUCTURE**: Section order, required/optional sections, content guidelines
- **Guidelines define STYLE**: Citations, formatting, reference style, academic conventions
- This separation allows flexible combinations (e.g., IMRaD structure with IEEE style)

## Available Outlines

### Research Papers
| File | Structure Type | Best For |
|------|----------------|----------|
| `researchpaper_imrad.md` | Introduction, Methods, Results, Discussion | Empirical research, experiments |
| `researchpaper_literature_review.md` | Systematic literature analysis | Literature surveys, state-of-art reviews |
| `researchpaper_systematic_review.md` | Structured evidence synthesis | Medical research, meta-analyses |
| `researchpaper_case_study.md` | In-depth case analysis | Business, social sciences, applied research |
| `researchpaper_humanities.md` | Argument-driven analysis | History, literature, philosophy |
| `researchpaper_dissertation.md` | Comprehensive multi-chapter | Theses, dissertations, major works |
| `researchpaper_general.md` | Flexible research structure | General academic research |

### Essays & Reports
| File | Structure Type | Best For |
|------|----------------|----------|
| `essay_analytical.md` | Analysis and interpretation | Literary analysis, critical thinking |
| `essay_argumentative.md` | Position and evidence | Persuasive writing, debates |
| `essay_reflective.md` | Personal reflection and learning | Learning portfolios, self-assessment |
| `essay_general.md` | Flexible essay structure | General academic essays |
| `researchpaper_project.md` | Project documentation | Capstone projects, technical reports |
| `researchpaper_short_communication.md` | Concise research reporting | Brief reports, preliminary findings |

## Usage Guidelines

### For Writers
1. Your paper type in `input_requirements.md` determines outline selection
2. Follow the selected outline's section structure exactly
3. Refer to appropriate style guideline for formatting rules
4. All content goes in single `paper.md` file

### For Contributors
- Keep outlines **style-agnostic** (no formatting/citation rules)
- Focus on **structural requirements** only
- Include clear section descriptions and purposes
- Update this README when adding new outlines

### File Naming Convention
- Format: `<type>_<specialization>.md`
- Examples: `researchpaper_imrad.md`, `essay_analytical.md`
- Use `_general.md` for flexible/broad structures

## Quality Standards

All outlines must specify:
- **Required sections** with clear purposes
- **Optional sections** and when to include them
- **Section ordering** and logical flow
- **Content guidelines** for each section
- **Single-file approach** with references in `paper.md`

---

*This folder provides the structural foundation for all academic writing in PaperCopilot. Style and formatting rules are maintained separately in the `guidelines/` folder.*
