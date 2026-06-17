# Penyesuaian Sitasi dan Referensi Laporan PSA PasarKita

## Pemetaan Referensi ke Dokumentasi Algoritma

| Bagian Laporan | Referensi Lokal | Alasan Pemakaian |
|---|---|---|
| Latar belakang aplikasi marketplace dan adopsi teknologi | Oliveira dan Martins (2011) | Menjelaskan model adopsi teknologi pada level organisasi melalui DOI dan TOE, cocok untuk alasan digitalisasi UMKM. |
| Greedy sebagai algoritma efisien untuk kebutuhan real-time | Tanujaya, Musyaffa, dan Yohannes (2026) | Membandingkan Greedy dan Dynamic Programming pada kasus optimasi e-commerce; mendukung argumen bahwa Greedy praktis untuk proses cepat. |
| Rekomendasi produk | Resnick dan Varian (1997) | Menjelaskan konsep dasar recommender systems dan cara sistem membantu pengguna memilih item. |
| Greedy pada optimasi marketing | Umami dan Rahmawati (2021) | Mendukung pembahasan Epsilon Greedy dan trade-off eksplorasi-eksploitasi dalam konteks marketing/e-commerce. |
| KMP pada pencarian produk | Marbun dkk. (2024) | Studi implementasi KMP pada e-katalog, sangat dekat dengan pencarian produk/katalog PasarKita. |
| Perbandingan algoritma string matching | Al-Howaide dkk. (2010) | Menjelaskan Naive, Rabin-Karp, KMP, dan algoritma string matching lain sebagai pembanding. |
| Dasar teori string/pattern matching | Crochemore dan Hancart (1998) | Memberi fondasi teoritis pattern matching in strings. |

## Rekomendasi Sitasi per Bab

### 1. Pendahuluan
Gunakan Oliveira dan Martins (2011) untuk menjelaskan bahwa adopsi teknologi informasi pada level organisasi dipengaruhi faktor teknologi, organisasi, dan lingkungan. Hubungkan dengan PasarKita sebagai aplikasi yang membantu UMKM masuk ke kanal digital.

### 2. Analisis Aplikasi PasarKita
Gunakan Oliveira dan Martins (2011) sebagai rujukan utama untuk kebutuhan digitalisasi UMKM. Tambahkan Resnick dan Varian (1997) ketika menjelaskan bahwa marketplace perlu membantu pengguna memilih produk dari banyak alternatif.

### 3. Dasar Teori Algoritma Greedy
Gunakan Tanujaya, Musyaffa, dan Yohannes (2026) sebagai referensi utama karena membahas Greedy pada kasus e-commerce. Gunakan Umami dan Rahmawati (2021) sebagai pendukung jika ingin membahas varian Epsilon Greedy pada optimasi marketing.

### 4. Penerapan Greedy di PasarKita
Gunakan Tanujaya, Musyaffa, dan Yohannes (2026) untuk argumen efisiensi Greedy pada fitur yang butuh respons cepat. Gunakan Resnick dan Varian (1997) untuk menguatkan fitur rekomendasi produk di `frontend/lib/product-recommendations.ts`.

### 5. Dasar Teori String Matching dan KMP
Gunakan Crochemore dan Hancart (1998) untuk dasar pattern matching. Gunakan Al-Howaide dkk. (2010) untuk pembanding Naive, Rabin-Karp, KMP, dan algoritma string matching lain.

### 6. Penerapan KMP di PasarKita
Gunakan Marbun dkk. (2024) karena membahas implementasi KMP pada e-katalog, paralel dengan pencarian produk PasarKita. Gunakan Al-Howaide dkk. (2010) untuk menjelaskan kompleksitas KMP dan keunggulannya dibanding pencarian naive.

### 7. Pembahasan dan Keterbatasan
Gunakan Umami dan Rahmawati (2021) untuk membuka pembahasan pengembangan rekomendasi yang lebih adaptif. Gunakan Al-Howaide dkk. (2010) dan Crochemore-Hancart (1998) untuk menjelaskan bahwa exact string matching bisa dikembangkan ke pendekatan string matching lain.

## Referensi Utama yang Paling Selaras

1. Tanujaya, Musyaffa, dan Yohannes (2026) - Greedy pada optimasi e-commerce.
2. Resnick dan Varian (1997) - sistem rekomendasi.
3. Marbun dkk. (2024) - implementasi KMP pada e-katalog.
4. Al-Howaide dkk. (2010) - perbandingan string matching.
5. Crochemore dan Hancart (1998) - teori pattern matching.
6. Oliveira dan Martins (2011) - adopsi teknologi organisasi/UMKM.

## Catatan Penyesuaian dari Plan Sebelumnya

- Referensi Boyer-Moore, Karp-Rabin, Navarro, dan Adomavicius tetap bagus, tetapi tidak ada di folder referensi lokal saat ini.
- Karena user sudah mengumpulkan PDF lokal, laporan sebaiknya memprioritaskan referensi yang tersedia di `src/references`.
- Untuk bagian Greedy, rujukan paling kuat dari koleksi lokal adalah paper Tanujaya dkk. karena langsung memakai konteks e-commerce.
- Untuk bagian String Matching, rujukan paling kuat dari koleksi lokal adalah Marbun dkk., Al-Howaide dkk., dan Crochemore-Hancart.
