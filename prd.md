# Product Requirements Document (PRD)
## Laporan Praktikum Strategi Algoritma — LaTeX Repository on Antigravity

**Version:** 2.0  
**Date:** 2026-05-10  
**Author:** Raditya Rizki Raharja  
**Status:** Draft  
**Repo Base:** https://github.com/bukped/latex

---

## 1. Overview

### 1.1 Latar Belakang
Mahasiswa memiliki kebutuhan untuk menyusun laporan praktikum mata kuliah Strategi Algoritma (Praktikum 1–6) dalam format LaTeX. Repository LaTeX mengacu pada template `bukped/latex` (template laporan ULBI) dan diimplementasikan menggunakan Antigravity sebagai coding AI agent. Sebelum menyusun laporan, Antigravity terlebih dahulu membuat source code Python untuk setiap praktikum berdasarkan langkah praktikum dan post test sesuai modul.

### 1.2 Tujuan
- Menghasilkan source code Python per praktikum (Praktikum 1–6) berdasarkan langkah praktikum dan post test dari modul.
- Menghasilkan laporan praktikum dalam format PDF melalui LaTeX mengacu pada struktur template `bukped/latex`.
- Memanfaatkan Antigravity sebagai AI agent untuk mengotomasi seluruh proses dari pembuatan kode hingga kompilasi laporan.

### 1.3 Ruang Lingkup
| No | Topik | Algoritma Utama |
|----|-------|-----------------|
| 1 | Kompleksitas Algoritma | Selection Sort, Insertion Sort |
| 2 | Algoritma Brute Force | Pencarian Elemen Terbesar, Uji Bilangan Prima |
| 3 | Algoritma Greedy | Coin Exchange |
| 4 | Algoritma Divide & Conquer | MinMaks D&C, Merge Sort, Quick Sort |
| 5 | Algoritma Decrease & Conquer | Selection Sort D&C |
| 6 | Algoritma BFS dan DFS | BFS, DFS pada Graf |

---

## 2. Stakeholder

| Role | Nama | Tanggung Jawab |
|------|------|----------------|
| Author / User | Raditya Rizki Raharja | Memberikan instruksi, review, dan validasi konten |
| AI Agent | Antigravity | Generate source code Python, file `.tex`, dan kompilasi PDF |

---

## 3. Struktur Repository

Mengacu pada struktur template `bukped/latex` dengan penambahan folder `src/` untuk source code Python.

```
strategi-algoritma-laporan/
│
├── bukped.tex                  # File utama LaTeX (entry point kompilasi)
├── compile-latex.ps1           # Script kompilasi PowerShell (dari bukped/latex)
├── indonesian.lbx              # Localization Bahasa Indonesia (dari bukped/latex)
├── logo.png                    # Logo institusi
├── references.bib              # Referensi utama
├── all.bib                     # Semua referensi gabungan
├── include.bib                 # Referensi tambahan
├── .gitignore                  # Exclude file LaTeX auxiliary
│
├── chapters/                   # Konten laporan per praktikum
│   ├── praktikum1/
│   │   ├── definisi.tex        # I. Definisi
│   │   ├── pretest.tex         # II. Pre Test
│   │   ├── analisis.tex        # III. Analisis Praktikum (Langkah + Post Test)
│   │   └── implementasi.tex    # IV. Implementasi Nyata
│   ├── praktikum2/
│   │   ├── definisi.tex
│   │   ├── pretest.tex
│   │   ├── analisis.tex
│   │   └── implementasi.tex
│   ├── praktikum3/
│   │   └── ...
│   ├── praktikum4/
│   │   └── ...
│   ├── praktikum5/
│   │   └── ...
│   └── praktikum6/
│       └── ...
│
├── figures/                    # Semua gambar dan flowchart
│   ├── praktikum1/
│   │   ├── flowchart_selection_sort.png
│   │   └── flowchart_insertion_sort.png
│   ├── praktikum2/
│   │   ├── flowchart_pencarian_terbesar.png
│   │   └── flowchart_uji_prima.png
│   ├── praktikum3/
│   │   └── flowchart_coin_exchange.png
│   ├── praktikum4/
│   │   ├── flowchart_minmaks.png
│   │   ├── flowchart_mergesort.png
│   │   └── flowchart_quicksort.png
│   ├── praktikum5/
│   │   └── flowchart_selection_sort_dc.png
│   └── praktikum6/
│       ├── flowchart_bfs.png
│       └── flowchart_dfs.png
│
└── src/                        # Source code Python per praktikum
    ├── praktikum1/
    │   ├── selection_sort.py       # Langkah Praktikum
    │   └── insertion_sort.py       # Post Test
    ├── praktikum2/
    │   ├── pencarian_terbesar.py   # Langkah Praktikum (a)
    │   └── uji_bilangan_prima.py   # Langkah Praktikum (b) + Post Test
    ├── praktikum3/
    │   ├── coin_exchange.py        # Langkah Praktikum
    │   └── coin_exchange_tester.py # Post Test
    ├── praktikum4/
    │   ├── sorting_program.py          # Langkah Praktikum
    │   └── merge_sort_standalone.py    # Post Test
    ├── praktikum5/
    │   ├── selection_sort_dc.py        # Langkah Praktikum
    │   └── selection_sort_input.py     # Post Test (user input)
    └── praktikum6/
        ├── bfs.py                  # Langkah Praktikum - BFS
        ├── dfs.py                  # Langkah Praktikum - DFS
        └── bfs_dfs_pretest.py      # Post Test
```

---

## 4. Struktur Konten Per Praktikum (Outline Laporan)

Setiap praktikum mengikuti template yang seragam:

```
I.   Definisi
     - Konsep utama & teori pendukung
     - Nama Algoritma: definisi, cara kerja, fungsi, kelebihan & kekurangan

II.  Pre Test
     - Jawaban sesuai soal modul

III. Analisis Praktikum
     3.1 Langkah Praktikum — [Nama Algoritma Utama]
         - Flowchart
         - Source Code Python (referensi ke src/)
         - Analisis jawaban sesuai soal langkah praktikum
     3.2 Post Test
         - Source Code Python (referensi ke src/)
         - Jawaban sesuai soal post test

IV.  Implementasi Nyata
     - Contoh kasus nyata
     - Kelebihan & kekurangan algoritma di konteks tersebut
```

---

## 5. Requirements

### 5.1 Functional Requirements — Source Code Python

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| FR-SC-01 | Antigravity men-generate file Python per algoritma per praktikum di folder `src/` | High |
| FR-SC-02 | Kode Python merupakan konversi dari pseudocode/C++ modul, bukan terjemahan literal | High |
| FR-SC-03 | Setiap file Python dapat dijalankan standalone dan menghasilkan output yang benar | High |
| FR-SC-04 | Kode Python dilengkapi komentar penjelasan per blok logika | Medium |
| FR-SC-05 | Kode mencakup tester/kasus uji sesuai yang diminta soal langkah praktikum | High |
| FR-SC-06 | Post Test diimplementasikan dalam file Python terpisah dari Langkah Praktikum | Medium |

### 5.2 Functional Requirements — Laporan LaTeX

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| FR-LX-01 | Antigravity men-generate file `.tex` per section per praktikum di `chapters/` | High |
| FR-LX-02 | Kode Python disisipkan dalam environment `lstlisting` di laporan | High |
| FR-LX-03 | Flowchart disisipkan dari folder `figures/` | High |
| FR-LX-04 | Tabel perbandingan algoritma disusun menggunakan `booktabs` | Medium |
| FR-LX-05 | `bukped.tex` memanggil semua chapter menggunakan `\input{}` | High |
| FR-LX-06 | Dokumen dikompilasi menggunakan `compile-latex.ps1` menjadi `bukped.pdf` | High |

### 5.3 Non-Functional Requirements

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| NFR-01 | Struktur folder konsisten dengan spesifikasi di bagian 3 | High |
| NFR-02 | Penamaan file menggunakan `snake_case` | Medium |
| NFR-03 | Tidak ada package konflik di `bukped.tex` | High |
| NFR-04 | Kode Python menggunakan Python 3, hanya stdlib | High |
| NFR-05 | Styling laporan konsisten mengikuti template `bukped/latex` | Medium |

---

## 6. Spesifikasi LaTeX

### 6.1 Engine & Kompilasi
Menggunakan script `compile-latex.ps1` dari repo `bukped/latex`:
```powershell
.\compile-latex.ps1
# Urutan otomatis:
# 1. pdflatex bukped.tex
# 2. bibtex bukped
# 3. pdflatex bukped.tex
# 4. pdflatex bukped.tex
```
Output: `bukped.pdf`

### 6.2 Instalasi Package via TinyTeX
```
tlmgr install inputenc fontenc mathptmx courier helvet amsmath babel geometry
tlmgr install setspace titlesec graphicx hyperref booktabs array caption
tlmgr install enumitem parskip fancyhdr tocloft tabularx longtable ragged2e
tlmgr install biblatex bibtex logreq xstring listings
```

### 6.3 Konvensi Kode Python di LaTeX
```latex
\begin{lstlisting}[language=Python, caption={Nama Algoritma}]
def selection_sort(arr):
    # kode python di sini
    pass
\end{lstlisting}
```

### 6.4 Konvensi Gambar Flowchart
```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.75\textwidth]{figures/praktikum1/flowchart_selection_sort.png}
  \caption{Flowchart Selection Sort}
  \label{fig:flowchart_selection_sort}
\end{figure}
```

### 6.5 Struktur Input di `bukped.tex`
```latex
\input{chapters/praktikum1/definisi}
\input{chapters/praktikum1/pretest}
\input{chapters/praktikum1/analisis}
\input{chapters/praktikum1/implementasi}
% ulangi untuk praktikum2–6
```

---

## 7. Alur Kerja Antigravity (Workflow)

```
TAHAP 1 — SOURCE CODE PYTHON
──────────────────────────────────────────
1. User: "Generate source code Praktikum [N]"
2. Antigravity membaca soal langkah praktikum & post test dari modul
3. Antigravity men-generate file Python di src/praktikumN/
4. User menjalankan & memvalidasi output
5. Revisi jika output tidak sesuai modul

          ↓

TAHAP 2 — LAPORAN LATEX
──────────────────────────────────────────
6. User: "Generate laporan Praktikum [N]"
7. Antigravity men-generate .tex per section di chapters/praktikumN/
8. Kode dari src/ disisipkan ke analisis.tex
9. Flowchart dari figures/ disisipkan ke analisis.tex
10. User review konten, revisi jika perlu

          ↓

TAHAP 3 — KOMPILASI
──────────────────────────────────────────
11. Antigravity menjalankan .\compile-latex.ps1
12. Cek & perbaiki error kompilasi
13. User validasi bukped.pdf final

          ↓ Ulangi untuk praktikum berikutnya
```

---

## 8. Instruksi Prompt untuk Antigravity

### 8.1 Generate Source Code Python
```
Generate source code Python untuk Praktikum [N] — [Nama Topik].

Langkah Praktikum: [salin soal dari modul]
Post Test: [salin soal dari modul]

Ketentuan:
- Simpan di src/praktikum[N]/
- File terpisah untuk langkah praktikum dan post test
- Konversi pseudocode/C++ modul ke Python 3
- Sertakan komentar per blok logika
- Tampilkan output eksekusi di komentar bawah kode
- Hanya gunakan Python stdlib
```

### 8.2 Generate Section LaTeX
```
Generate file chapters/praktikum[N]/[section].tex
untuk Praktikum [N] — [Nama Topik].

Section: [definisi / pretest / analisis / implementasi]
Konten: [sesuai outline yang disepakati]

Ketentuan:
- Gunakan lstlisting untuk kode Python
- Sisipkan gambar dari figures/praktikum[N]/
- Gunakan \subsection{} untuk sub-bagian
- Bahasa Indonesia, gaya analisis
```

### 8.3 Kompilasi
```
Jalankan compile-latex.ps1 dan periksa error.
Jika ada error package, install dengan tlmgr install [nama].
Kompilasi ulang sampai bukped.pdf berhasil dihasilkan.
```

---

## 9. Rincian Source Code Per Praktikum

### Praktikum 1 — Kompleksitas Algoritma
| File | Isi | Sumber Soal |
|------|-----|-------------|
| `selection_sort.py` | Selection Sort + hitung perbandingan & pertukaran per pass + derivasi T(n) | Langkah Praktikum |
| `insertion_sort.py` | Insertion Sort + hitung kompleksitas + perbandingan dengan Selection Sort | Post Test |

### Praktikum 2 — Brute Force
| File | Isi | Sumber Soal |
|------|-----|-------------|
| `pencarian_terbesar.py` | Pencarian elemen terbesar + analisis output | Langkah Praktikum (a) |
| `uji_bilangan_prima.py` | Uji bilangan prima + hitung kompleksitas T(n) | Langkah Praktikum (b) + Post Test |

### Praktikum 3 — Greedy
| File | Isi | Sumber Soal |
|------|-----|-------------|
| `coin_exchange.py` | CoinExchange + pengujian satu kasus | Langkah Praktikum |
| `coin_exchange_tester.py` | CoinExchange + multiple kasus + analisis output + kompleksitas | Post Test |

### Praktikum 4 — Divide & Conquer
| File | Isi | Sumber Soal |
|------|-----|-------------|
| `sorting_program.py` | MinMaks D&C + Merge Sort + Quick Sort dalam satu program | Langkah Praktikum |
| `merge_sort_standalone.py` | Merge Sort mandiri dengan D&C + eksekusi + output | Post Test |

### Praktikum 5 — Decrease & Conquer
| File | Isi | Sumber Soal |
|------|-----|-------------|
| `selection_sort_dc.py` | Selection Sort D&C + analisis output | Langkah Praktikum |
| `selection_sort_input.py` | Selection Sort D&C dengan user input array | Post Test |

### Praktikum 6 — BFS dan DFS
| File | Isi | Sumber Soal |
|------|-----|-------------|
| `bfs.py` | BFS pada graf contoh modul + output urutan traversal | Langkah Praktikum |
| `dfs.py` | DFS pada graf contoh modul + output + analisis perbedaan dengan BFS | Langkah Praktikum |
| `bfs_dfs_pretest.py` | BFS & DFS pada graf pre test + analisis vs jawaban manual | Post Test |

---

## 10. Batasan & Asumsi

- Flowchart di-generate dengan Graphviz secara terpisah, di-export ke PNG, disimpan di `figures/`.
- Tidak ada grafik empiris (Matplotlib) — di luar scope.
- Laporan bergaya analisis, bukan paper ilmiah formal.
- Kompilasi via `compile-latex.ps1` (TinyTeX) di VS Code + ekstensi `vscode-pdf`.
- Kode Python menggunakan Python 3, hanya stdlib.
- File utama: `bukped.tex`, output: `bukped.pdf`.

---

## 11. Kriteria Selesai (Definition of Done)

| Kriteria | Keterangan |
|----------|------------|
| ✅ Source code Python Praktikum 1–6 berjalan tanpa error | Output sesuai soal modul |
| ✅ Semua file `.tex` Praktikum 1–6 ter-generate di `chapters/` | Sesuai outline yang disepakati |
| ✅ `bukped.tex` mengompilasi menjadi `bukped.pdf` tanpa error | Via `compile-latex.ps1` |
| ✅ Kode Python tampil dengan syntax highlighting di laporan | Menggunakan `lstlisting` |
| ✅ Flowchart terpasang di setiap algoritma | Gambar dari `figures/` tidak pecah |
| ✅ Konten sesuai soal modul praktikum | Tidak menyimpang dari pertanyaan modul |
| ✅ Struktur folder sesuai spesifikasi bagian 3 | Konsisten dengan `bukped/latex` |