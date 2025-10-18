# The Lemon Book - Style Guide

This document outlines the official style, formatting, and structural conventions for *The Lemon Book*. Adhering to this guide ensures consistency across all markdown files and in the final PDF output.

---

## 1. Language and Spelling

- **Language:** British English (`en-GB`).
- **Spelling:** Use UK spelling conventions.
  - **-ise vs. -ize:** Prefer `-ise` (e.g., `organise`, `realise`, `polarisation`).
  - **-our vs. -or:** Prefer `-our` (e.g., `colour`, `labour`, `favour`).

This is configured in `scripts/metadata.yaml` with `lang: "en-GB"`.

---

## 2. Markdown and Formatting

### 2.1. Headings

Use the following hierarchy for structuring content within chapters:

- `# Title`: The main title for a file (e.g., `# Introduction`, `# Colophon`).
- `## Section Heading`: The primary heading for major sections within a chapter.
- `### Subsection Heading`: For sub-sections within a major section.
- `**Bolded Title:**`: For short, run-in headings that introduce a concept or list item, followed by a colon.

**Example:**
```markdown
## The Liberal Lexicon: A Glossary of Hope

### Freedom: The Power to Flourish

For liberals, freedom is not just the absence of constraint...
```

### 2.2. Emphasis

- Use `*italics*` for subtitles, emphasis, and introducing key terms.
- Use `**bold**` for strong emphasis and for run-in headings as noted above.

### 2.3. Page Markers

Page breaks are indicated with a specific marker format on its own line, followed by a horizontal rule. This is used by scripts to paginate the book.

```markdown
→ 15 ←

---
```

---

## 3. Citations and Bibliography

- **Citations:** The main body of the text does not use inline citations (e.g., `(Author, Year)`).
- **Bibliography:** All sources are listed in the `bibliography.md` file at the end of the book.
- **Format:** The bibliography follows a format similar to Chicago Style, with clear headings for different types of sources (e.g., "Classic Liberal Philosophy", "Contemporary Liberal Thought").

---

## 4. File Structure and Naming

- **Chapter Files:** Numbered sequentially to control the build order.
  - `00_front_matter.md`
  - `01_enlightenment_roots.md`
  - `...`
  - `18_liberal_lemonade.md`
- **Back Matter Files:** Named descriptively.
  - `bibliography.md`
  - `book_index_with_pages.md`
  - `colophon.md`

---

## 5. Typography (for PDF Build)

The following fonts are specified in `scripts/metadata.yaml` for the final PDF output:

- **Main Body Font:** Georgia
- **Sans-Serif Font:** Helvetica
- **Monospaced Font:** Menlo