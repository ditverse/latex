# Template Proposal PKM Internal ULBI 2026

Template LaTeX untuk **Proposal Pengabdian Kepada Masyarakat (PKM) Internal ULBI 2026**.  
Studi kasus: Workshop Machine Learning untuk Prediksi Awal Kesehatan Tanaman SMKN 2 Cimahi.

---

## Prasyarat

| Kebutuhan | Versi | Keterangan |
|---|---|---|
| [MiKTeX](https://miktex.org/download) | 25.x | Distribusi LaTeX untuk Windows |
| [Git](https://git-scm.com) | ≥ 2.x | Version control |
| PowerShell | 5.1 (bawaan Windows) | Menjalankan skrip kompilasi |
| PDF viewer | bebas | Untuk membuka hasil PDF |

> **MiKTeX** mengunduh paket LaTeX secara otomatis saat pertama kali kompilasi — tidak perlu instalasi paket manual.

---

## Clone Repository

Project ini berada di branch **`proposal_pkm`**, bukan `main`.

```powershell
git clone -b proposal_pkm <url-repository>
cd latex
```

Atau jika sudah clone sebelumnya:

```powershell
git checkout proposal_pkm
git pull
```

---

## Instalasi Dependensi

### 1. MiKTeX (distribusi LaTeX)

Unduh dan instal dari [miktex.org/download](https://miktex.org/download).  
Pilih **"Install for all users"** agar `pdflatex` dan `bibtex` tersedia di PATH.

Setelah instal, buka **MiKTeX Console** dan aktifkan *automatic package installation*:  
`Settings → General → Always install missing packages on-the-fly`

### 2. Paket LaTeX

MiKTeX mengunduh paket secara otomatis saat compile pertama (perlu koneksi internet).  
Untuk menginstal semua paket sekaligus tanpa menunggu, jalankan perintah ini di PowerShell:

```powershell
miktex packages install `
  mathptmx babel-indonesian geometry setspace titlesec `
  graphics hyperref booktabs caption enumitem fancyhdr `
  tocloft tools ragged2e csquotes biblatex bibtex logreq `
  xstring amssymb multirow indentfirst
```

> Paket `tools` sudah mencakup `tabularx`, `longtable`, `array`, dan `multirow`.  
> Paket `amssymb` adalah bagian dari `amsfonts`.

Verifikasi instalasi berhasil:

```powershell
pdflatex --version
bibtex --version
```

---

## Struktur Proyek

```
latex/
├── proposal_pkm.tex              # File utama — entry point kompilasi
├── references.bib                # Daftar referensi format IEEE (BibTeX)
├── compile-latex.ps1             # Skrip kompilasi PowerShell
├── logo.png                      # Logo ULBI (diperlukan untuk sampul)
├── indonesian.lbx                # Lokalisasi bahasa Indonesia untuk biblatex
│
├── chapters/
│   ├── sampul.tex                # Halaman sampul
│   ├── pengesahan.tex            # Halaman pengesahan
│   ├── keterlibatan_mahasiswa.tex
│   ├── ringkasan.tex             # Ringkasan / abstrak
│   ├── bab1_pendahuluan.tex      # BAB 1 – Pendahuluan
│   ├── bab2_solusi_luaran.tex    # BAB 2 – Solusi dan Target Luaran
│   ├── bab3_landasan_teori.tex   # BAB 3 – Landasan Teori
│   ├── bab4_metode.tex           # BAB 4 – Metode Pelaksanaan
│   └── bab5_biaya_jadwal.tex     # BAB 5 – Biaya dan Jadwal PKM
│
├── lampiran/
│   ├── lampiran_a_jadwal.tex     # Jadwal kegiatan
│   ├── lampiran_b_organisasi.tex # Susunan organisasi & tugas
│   ├── lampiran_c_anggaran.tex   # Justifikasi anggaran
│   ├── lampiran_d_biodata.tex    # Biodata ketua & anggota
│   ├── lampiran_e_surat_pernyataan.tex
│   ├── lampiran_f_logbook.tex    # Catatan harian
│   ├── lampiran_g_kerjasama.tex  # Surat kesediaan mitra
│   └── lampiran_h_kuasa.tex      # Surat kuasa
│
└── out/                          # Hasil kompilasi (di-ignore git)
    ├── proposal_pkm.aux
    ├── proposal_pkm.log
    └── proposal_pkm.pdf          # PDF internal (di-copy ke root)
```

File PDF final selalu ada di **root** (`proposal_pkm.pdf`).  
Semua file hasil kompilasi (`.aux`, `.log`, `.bbl`, dll.) masuk ke `out/` dan tidak di-track git.

---

## Kompilasi

Jalankan skrip dari folder `latex/`:

```powershell
.\compile-latex.ps1
```

Skrip otomatis menjalankan tiga tahap yang diperlukan biblatex:

```
pdflatex pass 1  →  bibtex  →  pdflatex pass 2  →  pdflatex pass 3
```

Output terminal yang diharapkan:

```
Compiling proposal_pkm.tex ...
  pdflatex pass 1... OK
  bibtex... OK
  pdflatex pass 2... OK
  pdflatex pass 3... OK
Done -> proposal_pkm.pdf
```

> **Jika ada error**, skrip otomatis menampilkan 40 baris terakhir dari `out/proposal_pkm.log`.  
> Log lengkap selalu tersedia di `out/proposal_pkm.log`.

---

## Mengedit Konten

### Identitas dan sampul

Edit `chapters/sampul.tex` untuk mengubah judul, nama tim, dan tahun.

### Bab-bab proposal

| File | Konten |
|---|---|
| `chapters/ringkasan.tex` | Ringkasan / abstrak (maks. 200 kata) |
| `chapters/bab1_pendahuluan.tex` | Analisis situasi, permasalahan mitra |
| `chapters/bab2_solusi_luaran.tex` | Solusi, target luaran, indikator capaian |
| `chapters/bab3_landasan_teori.tex` | Landasan teori + studi literatur |
| `chapters/bab4_metode.tex` | Metode pelaksanaan, tahapan, evaluasi |
| `chapters/bab5_biaya_jadwal.tex` | Anggaran dan jadwal kegiatan |

### Lampiran

Semua lampiran ada di folder `lampiran/`. Isi dengan data aktual sesuai nama file.  
**Lampiran D** (`lampiran_d_biodata.tex`) berisi template biodata untuk tiga anggota tim — ganti nama dan data kosong dengan data nyata.

---

## Manajemen Referensi

Referensi disimpan di `references.bib` dengan format BibTeX. Sitasi menggunakan gaya **IEEE** (penomoran `[1]`, `[2]`, ...).

### Menambah referensi baru

Tambahkan entri ke `references.bib`:

```bibtex
@article{NamaKunci2024,
  author  = {Nama, Penulis},
  title   = {Judul Artikel},
  journal = {Nama Jurnal},
  year    = {2024},
  volume  = {1},
  pages   = {1--10}
}
```

### Menyitasi dalam teks

```latex
Penelitian ini menunjukkan bahwa PjBL efektif \cite{NamaKunci2024}.

% Beberapa referensi sekaligus:
Hal ini dikonfirmasi oleh sejumlah penelitian \cite{Ref1,Ref2,Ref3}.
```

### Daftar Pustaka

Daftar Pustaka dicetak otomatis dan sudah masuk ke Daftar Isi. Tidak perlu diedit manual.

---

## Troubleshooting

**`pdflatex: major issue: So far, you have not checked for MiKTeX updates`**  
→ Bukan error, hanya peringatan. Buka **MiKTeX Console → Updates → Check for updates** sekali, pesan hilang permanen.

**PDF tidak terupdate setelah compile**  
→ Tutup file `proposal_pkm.pdf` di PDF viewer sebelum compile. Windows mengunci file PDF yang sedang dibuka.

**Sitasi muncul sebagai `[?]`**  
→ Referensi belum diproses bibtex. Jalankan `.\compile-latex.ps1` sekali lagi dari awal.

**MiKTeX mengunduh paket saat compile pertama**  
→ Normal. MiKTeX mengunduh paket yang belum terinstal secara otomatis. Perlu koneksi internet di compile pertama.

**`! Undefined control sequence` pada lampiran A**  
→ Pastikan `\usepackage{amssymb}` ada di `proposal_pkm.tex` (sudah ada secara default, untuk simbol `\checkmark`).

---

## Workflow Git

```powershell
# Sebelum mulai kerja
git pull

# Setelah mengedit
git add chapters/bab1_pendahuluan.tex   # tambah file yang diubah
git commit -m "feat: lengkapi bab 1 pendahuluan"
git push
```

> File `proposal_pkm.pdf` **tidak di-track git** secara default (ada di `.gitignore`).  
> Untuk berbagi PDF, upload manual atau share langsung filenya.

---

## Paket LaTeX yang Digunakan

| Paket | Fungsi |
|---|---|
| `mathptmx` | Font Times New Roman |
| `babel` (indonesian) | Bahasa Indonesia |
| `geometry` | Margin halaman (3/3/4/3 cm) |
| `biblatex` + `bibtex` | Sitasi dan daftar pustaka IEEE |
| `titlesec` | Format judul BAB/subbab |
| `tocloft` | Format daftar isi/tabel/gambar |
| `fancyhdr` | Header dan footer kustom |
| `tabularx`, `longtable` | Tabel responsif dan multi-halaman |
| `setspace` | Spasi 1.5 baris |
| `amssymb` | Simbol matematika (`\checkmark`) |
| `hyperref` | Link internal dan URL |
