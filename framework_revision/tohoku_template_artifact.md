# Tohoku University Template Distillation

## Reference

- Archive: `/Users/darin/Downloads/Tohoku_University_Thesis_Template__M_Sc____Ph_D__.zip`
- SHA-256: `d82d248662082484373ddb1648708ea7ab891c65b5a694dadd42ae3b4170d6c9`
- Format: LaTeX `book` project, not a DOCX template.
- Inspected files: `main.tex`, `Chapter1.tex`, `AppendixA.tex`, `reference.bib`, and `logo.png`.
- Logo: 512 x 512 RGBA PNG.

## Page system

- Two-sided `book` layout.
- `executivepaper` geometry, translated to 7.25 x 10.5 inches in Word.
- Left and right margins: 1.25 inches.
- Top and bottom margins: 1.1 inches.
- Page number in the outside header: left on even pages and right on odd pages.
- Chapter names omitted from running headers.
- Chapters and appendices begin on a new page.

## Typography and structure

- The LaTeX template relies on the default book type system and does not specify a transferable Word font family.
- Existing dissertation-framework Word styles remain the typography authority.
- Chapter, section, appendix, bibliography, figure, and table roles map to real Word heading/caption styles where available.
- The source template limits the table of contents to chapter and section depth; the Word framework retains a concise chapter-level front-matter list until pagination stabilizes.

## Title-page slots

- University logo.
- Graduate school and university identity.
- Dissertation title and author.
- Submission statement, degree, and field.
- Supervisor and referee block where names are available.
- Submission date.

The framework preserves the project's verified Graduate School of Arts and Letters identity rather than copying the Economics example text from the template.

## Fidelity decisions

- Adopted: logo, book geometry, mirrored page-number placement, clean running headers, chapter page breaks, and title-page hierarchy.
- Not copied: example dissertation title, example author/examiners, Economics faculty identity, theorem packages, mathematical environments, hyperlink colors, and LaTeX-only commands.
- The ZIP remains unchanged and is not committed into the repository.
