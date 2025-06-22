# Academic Writing Guidelines Index

This project supports multiple academic writing and citation styles. Each style has specific rules for structure, citations, references, and formatting.

## Style Selection Guide

| Style      | Guideline File              | Primary Use Cases                                    |
|------------|----------------------------|------------------------------------------------------|
| **APA 7**  | `guidelines/apa7.md`       | Psychology, social sciences, health sciences        |
| **IEEE**   | `guidelines/ieee.md`       | Engineering, computer science, technical fields     |
| **MLA**    | `guidelines/mla.md`        | Literature, humanities, language studies             |
| **Chicago**| `guidelines/chicago.md`    | History, literature, arts, some social sciences     |
| **Harvard**| `guidelines/harvard.md`    | Business, social sciences, STEM fields              |
| **Vancouver** | `guidelines/vancouver.md` | Medical research, life sciences                    |
| **Turabian** | `guidelines/turabian.md`  | Student papers (based on Chicago style)            |
| **ABNT**   | `guidelines/abnt.md`       | Brazilian academic standards                         |

## Usage Instructions

### For Writers
1. **Identify your required style** from your institution, journal, or assignment requirements
2. **Reference the appropriate guideline file** throughout your writing process
3. **Follow all formatting rules** specified in your selected style guide
4. **Use the style consistently** throughout your entire document

### For AI/Automation
- Always reference the correct guideline file for every academic writing task
- Never mix style rules from different guidelines
- Ensure all citations, references, and formatting match the selected style
- Validate compliance before finalizing any document

## Export & Quality Control

### Pre-Export Validation
- All required sections must exist in `paper.md` before export
- References must be complete and properly formatted
- In-text citations must have corresponding reference entries
- Checklist items must be completed

### Export Process
- Uses single `paper.md` file as source
- Applies style-specific Pandoc templates
- Converts to high-fidelity Word format
- Supports advanced Markdown features (tables, code blocks, footnotes)
- Maintains proper formatting and page breaks

### Quality Standards
- Professional academic tone throughout
- Fact-checked content with verified sources
- Proper academic structure and flow
- Style-consistent formatting and citations
- Publication-ready output

---

## Troubleshooting

### Common Issues
- **Missing sections**: Check outline requirements and ensure all sections exist
- **Citation errors**: Verify all in-text citations have reference entries
- **Formatting problems**: Confirm you're using the correct style guideline
- **Export failures**: Ensure all required files exist and are properly formatted

### Best Practices
- Always specify the writing style in `input_requirements.md`
- Follow the workflow steps in order
- Complete peer review before finalizing
- Double-check all requirements before submission

---

*For detailed rules and examples, see the individual guideline files listed above.*
