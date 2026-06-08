# AGENTS.md

## Project Overview

This repository is a LaTeX template for writing and compiling academic/practicum reports. The main goal of this project is to make report writing consistent, reusable, and easy to maintain.

The main LaTeX entry file is `bukped.tex`. Report content should primarily be written in `.tex` files under the `chapters/` directory when that structure is available. The generated output is `bukped.pdf`.

## Primary Use Case

This repository is commonly used for:

- Creating report templates.
- Writing practicum reports.
- Structuring academic documents.
- Managing references and bibliography files.
- Compiling LaTeX documents into PDF.

Agents should treat this repository as a document/template repository, not as a general software application.

## Tech Stack and Tools

- LaTeX engine: `pdflatex`
- Bibliography processor: `bibtex`
- Bibliography package: `biblatex` with `backend=bibtex`
- Main file: `bukped.tex`
- Compile script: `compile-latex.ps1`
- Recommended LaTeX distribution: TinyTeX
- Recommended editor workflow: Antigravity or VS Code with PDF preview extension

## Important Files

- `bukped.tex`: main LaTeX template and document configuration.
- `compile-latex.ps1`: PowerShell script for compiling the document.
- `references.bib`: primary bibliography database if present.
- `include.bib`: additional bibliography database if present.
- `chapters/`: preferred location for report content files if present.
- `logo.png`: institution/project logo used on the title page if present.
- `bukped.pdf`: generated PDF output.

## LaTeX Architecture Rules

- Keep `bukped.tex` as the main template entry point.
- Do not rewrite the whole template unless explicitly requested.
- Prefer editing report content files instead of changing global formatting in `bukped.tex`.
- Keep document formatting consistent with the existing template.
- Preserve the current paper setup unless the user asks for a different format:
  - A4 paper
  - 12pt font size
  - left margin 4 cm
  - right margin 3 cm
  - top margin 3 cm
  - bottom margin 3 cm
  - one-and-a-half spacing
- Preserve Indonesian academic document labels such as `DAFTAR ISI`, `DAFTAR TABEL`, `DAFTAR GAMBAR`, and `DAFTAR RUMUS` unless explicitly requested.
- Preserve `biblatex` with `backend=bibtex` unless the user explicitly wants to migrate to `biber`.
- Avoid adding unnecessary LaTeX packages.
- If a package is added, explain why it is needed and update the README package installation list if appropriate.

## Writing and Report Rules

When helping write report content:

- Use formal Indonesian academic language unless the user requests another style.
- Keep paragraphs clear, coherent, and not overly long.
- Prefer structured sections and subsections.
- Avoid vague filler text.
- Maintain logical flow between background, objective, method, result, and conclusion.
- Do not invent data, observation results, dates, names, document numbers, or references.
- If required data is missing, use placeholders or clearly mark assumptions.
- For practicum reports, prioritize:
  - objective of the practicum,
  - tools/materials used,
  - step-by-step procedure,
  - observation results,
  - analysis,
  - conclusion.

## Citation and Bibliography Rules

- Use bibliography entries from `.bib` files when available.
- Do not fabricate references.
- Keep citation commands compatible with the current setup.
- The project aliases `\cite` to `\parencite`; preserve this behavior unless explicitly requested.
- When adding references, use valid BibTeX syntax.
- Prefer stable academic or official sources for references.
- Do not remove existing bibliography resources unless explicitly requested.

## Tables, Figures, and Equations

- Use `table`, `tabularx`, or `longtable` depending on table size.
- Use `booktabs` style for clean academic tables when possible.
- Every important table should have a `\caption{}` and `\label{}`.
- Every important figure should have a `\caption{}` and `\label{}`.
- Use descriptive label prefixes:
  - `fig:` for figures,
  - `tab:` for tables,
  - `eq:` for equations,
  - `sec:` for sections.
- Keep image paths relative to the repository.
- Do not embed huge binary assets unless necessary.
- For equations that must appear in the custom list of equations, use the existing custom equation-list mechanism if appropriate.

## Compile Workflow

The preferred compile command on Windows PowerShell is:

```powershell
.\compile-latex.ps1
```

The compile script runs:

1. `pdflatex`
2. `bibtex`
3. `pdflatex`
4. `pdflatex`

If working manually, use:

```bash
pdflatex -interaction=nonstopmode bukped.tex
bibtex bukped
pdflatex -interaction=nonstopmode bukped.tex
pdflatex -interaction=nonstopmode bukped.tex
```

After edits, compile the document when possible. If compilation is not possible in the current environment, explain that clearly and mention the files most likely affected.

## Validation Checklist

Before finalizing a change, check:

- The LaTeX syntax is valid.
- Braces `{}` are balanced.
- Every `\begin{...}` has a matching `\end{...}`.
- Tables do not have mismatched column counts.
- Figure paths are correct.
- Citation keys exist in the `.bib` files.
- Labels are unique.
- The document can still compile with the existing PowerShell workflow.
- Generated auxiliary files are not accidentally committed unless intentionally required.

## Generated Files and Auxiliary Files

Avoid committing generated or temporary LaTeX files unless the user explicitly wants them included.

Common generated files include:

- `*.aux`
- `*.log`
- `*.out`
- `*.toc`
- `*.lot`
- `*.lof`
- `*.equ`
- `*.bbl`
- `*.blg`
- `*.bcf`
- `*.run.xml`
- `*-blx.bib`
- `*.synctex.gz`

The PDF output `bukped.pdf` may be committed only if the repository intentionally stores compiled output.

## Do Not Touch Unless Explicitly Requested

- Do not modify `bukped.tex` for simple content writing tasks if the content can be changed in chapter files.
- Do not remove existing packages without checking whether they are used.
- Do not change page margins, title formatting, table-of-contents formatting, bibliography backend, or title-page identity unless requested.
- Do not delete `.bib` files or bibliography resources.
- Do not rename the main file `bukped.tex` unless the compile script and README are updated together.
- Do not edit generated PDF or auxiliary files as a source of truth.

## Agent Workflow

For every task:

1. Inspect relevant files before editing.
2. Identify whether the request is about content, formatting, references, compilation, or repository maintenance.
3. Prefer the smallest safe change.
4. Preserve the existing LaTeX style and Indonesian academic formatting.
5. Avoid broad rewrites unless the user asks for restructuring.
6. If editing content, keep the writing coherent and academically appropriate.
7. If editing template configuration, explain the reason and potential impact.
8. Run or recommend the compile workflow after changes.
9. Summarize changed files, what changed, and any remaining risks.

## Prompting Guidance for Future Agents

When the user asks to write or revise a report, first determine:

- report topic,
- practicum/module title,
- required structure,
- provided observation data,
- required citation style,
- whether the change belongs in `chapters/` or `bukped.tex`.

When details are missing, make a reasonable best effort using placeholders rather than inventing factual data.

## Commit and Change Discipline

- Keep diffs small and reviewable.
- Do not make unrelated formatting changes.
- Do not mix content writing, template redesign, bibliography cleanup, and compile-script refactor in one change unless requested.
- Use clear commit messages such as:
  - `docs: revise practicum report chapter`
  - `docs: add bibliography entries`
  - `chore: update latex compile script`
  - `style: adjust report template formatting`
