# PRD: LaTeX Template Proposal PKM Internal ULBI

## Overview

Mengadaptasi struktur branch `proposal_pkm` (di-branch dari `main` repo `radit-latex`)
menjadi template siap pakai untuk Proposal Usulan PKM Internal ULBI 2026.

Karena branch dibuat dari `main`, semua file asal sudah ada di root branch:
`bukped.tex`, `compile-latex.ps1`, `logo.png`, `indonesian.lbx`, `references.bib`,
`all.bib`, `include.bib`, `chapters/`, `figures/`, `out/`, dst.

Agent bekerja langsung dari **root branch** — bukan subfolder.

Referensi panduan: `Panduan_Hibah_PKM_Internal_ULBI_2026.pdf`

---

## Kondisi Awal Branch (dari main)

```
(root branch proposal_pkm)
├── chapters/               ← dari main, akan diganti isinya
├── figures/                ← dari main, akan dikosongkan
├── out/
├── .gitignore
├── all.bib
├── bukped.pdf              ← hapus
├── bukped.tex              ← rename jadi proposal_pkm.tex
├── compile-latex.ps1       ← update isinya
├── include.bib
├── indonesian.lbx          ← tetap
├── LICENSE
├── logo.png                ← tetap
├── README.md               ← update deskripsi
└── references.bib          ← tetap, siap diisi
```

---

## Struktur Target Setelah Agent Selesai

```
(root branch proposal_pkm)
├── chapters/
│   ├── sampul.tex
│   ├── pengesahan.tex
│   ├── keterlibatan_mahasiswa.tex
│   ├── ringkasan.tex
│   ├── bab1_pendahuluan.tex
│   ├── bab2_solusi_luaran.tex
│   ├── bab3_landasan_teori.tex
│   ├── bab4_metode.tex
│   └── bab5_biaya_jadwal.tex
│
├── lampiran/               ← folder baru
│   ├── lampiran_a_jadwal.tex
│   ├── lampiran_b_organisasi.tex
│   ├── lampiran_c_anggaran.tex
│   ├── lampiran_d_biodata.tex
│   ├── lampiran_e_surat_pernyataan.tex
│   ├── lampiran_f_logbook.tex
│   ├── lampiran_g_kerjasama.tex
│   └── lampiran_h_kuasa.tex
│
├── figures/                ← kosongkan isi dari main
├── out/                    ← gitignored
├── .gitignore
├── all.bib
├── include.bib
├── indonesian.lbx
├── logo.png
├── references.bib
├── LICENSE
├── README.md
├── proposal_pkm.tex        ← file utama (rename dari bukped.tex)
└── compile-latex.ps1
```

---

## Aturan Format (Sumber: Panduan ULBI 2026)

### Tipografi
- Font: Times New Roman → package `mathptmx`
- Ukuran font body: 12pt
- Judul BAB: 16pt, cetak tebal
- Sub BAB: 14pt, cetak tebal

### Spasi
- Body: 1.5 spasi (`\onehalfspacing`)
- Ringkasan: 1 spasi (dibungkus `\begin{singlespace}` di main file)

### Halaman
- Ukuran kertas: A4
- Margin: atas 3cm, bawah 3cm, kiri 4cm, kanan 3cm
- Maks halaman isi: 20 halaman (tidak termasuk sampul, pengesahan, lampiran)

### Penomoran Halaman
- Bagian awal (sampul s.d. daftar isi): romawi kecil (`\pagenumbering{roman}`)
- Bagian isi dan daftar pustaka: angka arab (`\pagenumbering{arabic}`)
- Posisi nomor halaman: sudut kanan bawah
- Lampiran: label "Lampiran 1", "Lampiran 2" di kiri atas — bukan nomor halaman biasa

### Footer
- Wajib ada di setiap halaman isi
- Teks: `Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 20XX`
- Font: Times New Roman 11pt, cetak miring
- Implementasi: `\fancyhdr` dengan `\fancyfoot`

### Referensi
- Style: IEEE
- Backend: bibtex
- Minimal 10 acuan
- 80% jurnal ilmiah
- Kemutakhiran: maksimal 10 tahun terakhir
- Hanya pustaka yang dikutip di teks yang masuk daftar referensi

---

## Spesifikasi `proposal_pkm.tex` (Main File)

### Package wajib
```
mathptmx, fontenc, inputenc, babel (bahasa),
geometry, setspace, titlesec, graphicx,
hyperref, booktabs, array, caption, enumitem,
parskip, fancyhdr, tocloft, tabularx, longtable,
ragged2e, biblatex (style=ieee, backend=bibtex)
```

### Urutan input
```
1. chapters/sampul
2. chapters/pengesahan
3. chapters/keterlibatan_mahasiswa
4. \tableofcontents
5. chapters/ringkasan              ← dibungkus \begin{singlespace}
--- \pagenumbering{arabic} ---
6. chapters/bab1_pendahuluan
7. chapters/bab2_solusi_luaran
8. chapters/bab3_landasan_teori
9. chapters/bab4_metode
10. chapters/bab5_biaya_jadwal
11. \printbibliography
--- \appendix ---
12. lampiran/lampiran_a s.d. lampiran_h
```

---

## Aturan per File Chapter

### `chapters/sampul.tex`
- Format: Lampiran 1.1 panduan
- Memuat: label USULAN, label PKM, judul, logo (`logo.png`), nama & NUPTK pengusul, nama prodi, nama universitas, tahun
- Tidak ada nomor halaman

### `chapters/pengesahan.tex`
- Tidak dibuat di LaTeX
- Diunduh dari APTIMAS (http://aptimas.ulbi.ac.id) dan disisipkan manual ke PDF akhir
- File hanya berisi komentar penjelasan + `\newpage`

### `chapters/keterlibatan_mahasiswa.tex`
- Format tabel: Lampiran 1.2 panduan
- Kolom: No, Nama, NPM, Bentuk Keterlibatan, Tanda Tangan
- Minimal 2 baris (ketentuan: minimal 2 mahasiswa)

### `chapters/ringkasan.tex`
- Maksimal 1 halaman
- Spasi 1 (sudah diatur di main file)

### `chapters/bab1_pendahuluan.tex`
- Section: `\section{PENDAHULUAN}`
- Subsection: Analisis Situasi, Permasalahan Mitra

### `chapters/bab2_solusi_luaran.tex`
- Section: `\section{SOLUSI DAN TARGET LUARAN}`
- Luaran harus terukur/kuantitatif
- Sertakan nama jurnal target, URL, akreditasi SINTA

### `chapters/bab3_landasan_teori.tex`
- Section: `\section{LANDASAN TEORI}`
- Pustaka mutakhir maks 10 tahun terakhir

### `chapters/bab4_metode.tex`
- Section: `\section{METODE PELAKSANAAN}`
- Subsection: tahapan solusi, metode pendekatan, partisipasi mitra, evaluasi & keberlanjutan

### `chapters/bab5_biaya_jadwal.tex`
- Section: `\section{BIAYA DAN JADWAL PKM}`
- Subsection: Anggaran Biaya, Jadwal Kegiatan
- Total dana maks Rp 7.500.000
- Batas komponen anggaran:
  - Gaji dan Upah: maks 25%
  - Bahan Habis Pakai: maks 25%
  - Perjalanan: maks 15%
  - Lain-lain: maks 35%
- Jadwal: tabel `longtable` 6 kolom bulan (bar chart via sel terisi)

---

## Aturan per File Lampiran

Setiap file mengikuti format resmi dari panduan (Lampiran A s.d. H).
Implementasi berupa tabel `longtable` sesuai kolom yang ada di panduan.

| File | Sumber di Panduan |
|------|-------------------|
| `lampiran_a_jadwal.tex` | Lampiran A: Jadwal Kegiatan (bar chart 6 bulan) |
| `lampiran_b_organisasi.tex` | Lampiran B: Susunan Organisasi & Pembagian Tugas |
| `lampiran_c_anggaran.tex` | Lampiran C: Justifikasi Anggaran (4 komponen) |
| `lampiran_d_biodata.tex` | Lampiran D: Biodata Ketua & Anggota (format DIKTI) |
| `lampiran_e_surat_pernyataan.tex` | Lampiran E: Surat Pernyataan Ketua PKM |
| `lampiran_f_logbook.tex` | Lampiran F: Catatan Harian (Logbook) |
| `lampiran_g_kerjasama.tex` | Lampiran G: Surat Kesediaan Kerjasama Mitra |
| `lampiran_h_kuasa.tex` | Lampiran H: Surat Kuasa |

---

## Spesifikasi `compile-latex.ps1`

- `Set-Location $PSScriptRoot` di baris pertama
- Nama file utama yang dikompilasi: `proposal_pkm`
- Urutan: `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`
- Output directory: `out/`
- Setelah selesai, copy `out/proposal_pkm.pdf` ke root sebagai `proposal_pkm.pdf`

---

## Update `.gitignore`

Tambahkan entri berikut jika belum ada:

```
out/
$OutDir/
*.aux
*.bbl
*.bcf
*.blg
*.lof
*.log
*.lot
*.out
*.run.xml
*.toc
*.fls
*.fdb_latexmk
*-blx.bib
```

---

## Catatan Penting tentang Branch

Branch `proposal_pkm` dibuat dari `main`, sehingga semua file dari `main` sudah
otomatis tersedia di root. Agent tidak perlu copy file — langsung modifikasi dan
tambah file/folder yang diperlukan.

---

## Instruksi untuk AI Agent

1. Pastikan berada di branch `proposal_pkm`
2. Hapus `bukped.pdf`
3. Rename `bukped.tex` → `proposal_pkm.tex`
4. Kosongkan isi `chapters/` dan `figures/` dari file bawaan main
5. Buat folder `lampiran/`
6. Buat semua file chapter dan lampiran sesuai struktur target
7. Implementasikan `proposal_pkm.tex` sesuai spesifikasi
8. Update `compile-latex.ps1` sesuai spesifikasi
9. Update `.gitignore`
10. Jalankan `compile-latex.ps1` untuk verifikasi tidak ada error
11. Pastikan `proposal_pkm.pdf` berhasil digenerate

## Yang Tidak Boleh Dilakukan Agent

- Mengubah file di branch `main`
- Membuat halaman pengesahan di LaTeX (diunduh dari APTIMAS, disisipkan manual)