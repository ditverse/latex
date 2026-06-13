# Latex Template Laporan

Repository ini digunakan untuk menyusun draft laporan akademik dengan LaTeX. File utama dokumen adalah `bukped.tex`, sedangkan isi laporan ditulis pada file `.tex` di dalam folder `chapters/`.

## Setup Awal

1. Install Git SCM dan clone repository.
2. Install R.
3. Install TinyTeX dari R:

```r
install.packages("tinytex")
tinytex::install_tinytex()

# Cek instalasi
tinytex::tinytex_root()
tinytex::tlmgr("--version")
```

4. Pastikan command berikut tersedia di terminal:

```powershell
where pdflatex
where bibtex
pdflatex --version
bibtex --version
```

5. Install package LaTeX yang diperlukan:

```bash
tlmgr install inputenc fontenc mathptmx courier helvet amsmath babel geometry setspace titlesec graphicx hyperref booktabs array caption enumitem indentfirst fancyhdr tocloft tabularx longtable ragged2e biblatex biblatex-ieee bibtex logreq xstring
```

6. Buka repository dengan Antigravity atau VS Code. Untuk preview PDF, gunakan ekstensi PDF preview seperti `vscode-pdf`.

## Catatan MiKTeX

Repository ini direkomendasikan menggunakan TinyTeX. MiKTeX tetap dapat digunakan apabila `pdflatex` dan `bibtex` berjalan normal serta semua package tersedia. Jangan mencampur PATH TinyTeX dan MiKTeX dalam satu environment karena dapat menyebabkan package dan format LaTeX tidak konsisten.

Jika menggunakan MiKTeX dan package belum tersedia, aktifkan auto-install package dari MiKTeX Console atau install package yang hilang melalui MiKTeX Package Manager.

## Compile LaTeX

Jalankan script PowerShell dari root repository:

```powershell
.\compile-latex.ps1
```

Script ini menjalankan:

1. `pdflatex -jobname=laporan_litma`
2. `bibtex laporan_litma`
3. `pdflatex -jobname=laporan_litma`
4. `pdflatex -jobname=laporan_litma`

File utama: `bukped.tex`  
Output: `laporan_litma.pdf`

Untuk menghapus file auxiliary setelah compile berhasil, jalankan:

```powershell
.\compile-latex.ps1 -CleanAux
```

## Struktur Laporan

Konten laporan CleanConnect berada di:

- `chapters/bab1.tex`
- `chapters/bab2.tex`
- `chapters/bab3.tex`
- `chapters/bab4.tex`
- `chapters/bab5.tex`
- `chapters/bab6.tex`
- `chapters/lampiran.tex`

Struktur utama laporan:

1. BAB I Pendahuluan
   - Latar Belakang
   - Rumusan Masalah
   - Tujuan
2. BAB II Kajian Masalah
   - Analisis Kondisi Masyarakat
   - Dampak Masalah
3. BAB III Solusi Teknologi
   - Deskripsi Solusi
   - Teknologi yang Digunakan
4. BAB IV Implementasi
   - Tahapan Pengerjaan
   - Screenshot Produk
5. BAB V Evaluasi
   - Hasil Pengujian
   - Kelebihan
   - Kekurangan
6. BAB VI Kesimpulan dan Saran
7. Daftar Pustaka

## Sitasi dan Bibliografi

Template menggunakan `biblatex` dengan:

- `backend=bibtex`
- `style=ieee`
- `citestyle=ieee`
- `sorting=none`

Gunakan sitasi dengan format:

```latex
\cite{key}
```

Sumber bibliografi utama:

- `references.bib`
- `include.bib`
