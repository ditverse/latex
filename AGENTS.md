# AGENTS.md

## Project Overview

This repository contains two LaTeX templates for academic reports:

1. **`bukped.tex`** - General academic/thesis report template
2. **`laporan_praktikum_psa.tex`** - Practicum report template for "Srategi Algoritma" course

Report content lives in `.tex` files under `chapters/` organized by practicum number. Both templates use Indonesian academic formatting conventions.

## Two Templates, Two Workflows

| Template | Compile Script | Bibliography | Output | Key Features |
|----------|---------------|--------------|--------|--------------|
| `bukped.tex` | `.\compile-latex.ps1` | BibTeX | `bukped.pdf` | General purpose, custom equation list |
| `laporan_praktikum_psa.tex` | `.\compile-psa.ps1` | Biber | `laporan_praktikum_psa.pdf` | Python code listings, practicum structure |

**Critical**: Do not confuse the two. Each has its own compile script and bibliography backend.

## Compile Commands

For `bukped.tex`:
```powershell
.\compile-latex.ps1
```
Runs: `pdflatex` → `bibtex out/bukped` → `pdflatex` (×2)

For `laporan_praktikum_psa.tex`:
```powershell
.\compile-psa.ps1
```
Runs: `pdflatex` → `biber --output-directory=out` → `pdflatex` (×2)

Both scripts output auxiliary files to `out/` directory and prompt to clean them afterward.

## Repository Structure

- `bukped.tex`, `laporan_praktikum_psa.tex` - main template files
- `chapters/` - report content organized by section and practicum number
- `chapters/praktikum{N}/` - structure: `definisi.tex`, `pretest.tex`, `implementasi.tex`, `analisis.tex`
- `references.bib`, `include.bib`, `all.bib` - bibliography databases
- `figures/` - images and diagrams
- `out/` - auxiliary files (`.aux`, `.log`, `.toc`, etc.) - gitignored
- `logo.png` - institution logo for title page

## Template Architecture Rules

**Do not rewrite templates unless explicitly requested.** Edit content files in `chapters/` instead.

Both templates share these settings (preserve unless requested):
- A4 paper, 12pt font, 1.5 line spacing
- Margins: 4cm left, 3cm right/top/bottom
- Indonesian labels: `DAFTAR ISI`, `DAFTAR TABEL`, `DAFTAR GAMBAR`, `DAFTAR RUMUS`

**Bibliography backends** (do not change):
- `bukped.tex` uses `biblatex` with `backend=bibtex`
- `laporan_praktikum_psa.tex` uses `biblatex` with `backend=biber`

**Python code support**: The PSA template includes `listings` package with Python syntax highlighting pre-configured. Use `\begin{lstlisting}...\end{lstlisting}` for code blocks.

When adding LaTeX packages, explain why and note which template requires it.

## Writing Content

Use formal Indonesian academic language. Do not invent data, dates, names, or references - use placeholders if information is missing.

Practicum report structure (PSA template):
1. **Definisi** - definitions and theory
2. **Pretest** - pre-lab questions
3. **Implementasi** - procedure, tools, code
4. **Analisis** - results, observations, discussion

Keep sections coherent and structured. Avoid filler text.

## Citations and Bibliography

- Both templates alias `\cite` to `\parencite`
- Use entries from `references.bib`, `include.bib`, or `all.bib`
- Do not fabricate references - use valid academic sources
- Add new entries using BibTeX syntax
- Do not remove existing `.bib` files

## Tables, Figures, Code

Use `booktabs` for tables. Every table/figure/equation needs `\caption{}` and `\label{}`.

Label prefixes: `fig:`, `tab:`, `eq:`, `sec:`

For Python code in PSA template:
```latex
\begin{lstlisting}[caption={Description}, label=lst:label]
def example():
    pass
\end{lstlisting}
```

Keep image paths relative. Custom equation list: use `\myequations{}` after equation to add it to `DAFTAR RUMUS`.

## Manual Compilation

If scripts fail, compile manually:

**For bukped.tex**:
```powershell
pdflatex -interaction=nonstopmode -aux-directory=out bukped.tex
bibtex out/bukped
pdflatex -interaction=nonstopmode -aux-directory=out bukped.tex
pdflatex -interaction=nonstopmode -aux-directory=out bukped.tex
```

**For laporan_praktikum_psa.tex**:
```powershell
pdflatex -interaction=nonstopmode -aux-directory=out laporan_praktikum_psa.tex
biber --output-directory=out laporan_praktikum_psa
pdflatex -interaction=nonstopmode -aux-directory=out laporan_praktikum_psa.tex
pdflatex -interaction=nonstopmode -aux-directory=out laporan_praktikum_psa.tex
```

Run compile scripts after content edits when possible. If compilation fails in the agent environment, mention affected files clearly.

## Validation Before Committing

Check:
- Braces balanced, every `\begin{...}` has matching `\end{...}`
- Table column counts match
- Figure paths exist
- Citation keys exist in `.bib` files
- Labels are unique
- Document compiles with appropriate script

Auxiliary files in `out/` are gitignored. Both PDFs (`bukped.pdf` and `laporan_praktikum_psa.pdf`) appear to be intentionally committed in this repo.

## Do Not Touch Unless Requested

- Do not modify main `.tex` files for content changes - edit `chapters/` files instead
- Do not change margins, title formatting, bibliography backends, or package configuration
- Do not remove packages without verifying they're unused
- Do not delete `.bib` files
- Do not rename main files without updating compile scripts and README

## Agent Workflow

1. **Identify which template** the user is working with (`bukped.tex` or `laporan_praktikum_psa.tex`)
2. Read relevant files before editing
3. Make the smallest safe change
4. Preserve Indonesian academic formatting
5. Run or recommend the appropriate compile script
6. Summarize changes and affected files

When writing content, determine: which template, which practicum, what data is provided. Use placeholders for missing information.