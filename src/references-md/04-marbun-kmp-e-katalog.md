---
title: "
Implementasi Algoritma Knuth-Morris-Pratt Pada E-Katalog Perpustakaan
"
source_pdf: "
3026183X02022024-01-143.pdf
"
citation_short: "
Marbun dkk. (2024)
"
topic: "
KMP untuk pencarian data katalog
"
---

# 
Implementasi Algoritma Knuth-Morris-Pratt Pada E-Katalog Perpustakaan

## Metadata Singkat

- File sumber: `
3026183X02022024-01-143.pdf
`
- Sitasi singkat: 
Marbun dkk. (2024)
- Relevansi: 
KMP untuk pencarian data katalog

## Teks Hasil Konversi
                                                            KETIK : Jurnal Informatika
                                                          ISSN: 3026-183X (Media Online)
                                            Vol. 02, No. 02, November 2024 Hal. 01-04
                                                 Publisher: Faatuatua Media Karya
                                                   jurnal.faatuatua.com/index.php/KETIK
                                            DOI: doi.org/10.70404/ketik.v2i02.143



Implementasi Algoritma Knuth-Morris-Pratt Pada E-Katalog Perpustakaan

Nasib Marbun1*, Ahmad Rozy2, Sutrisno Arianto Pasaribu3, Efori Bu'ulolo4, Bister
Purba5, Nisma Novita Hasibuan6, Muhammad Riansyah7

1*
  Politeknik Cendana, Medan, Indonesia, e-mail: marbunnasib93@gmail.com
2
 Universitas Mahkota Tricom Unggul, Medan, Indonesia, e-mail: Poblesc@gmail.com
3
 Universitas Mahkota Tricom Unggul, Medan, Indonesia, e-mail: sutrisnopasaribu@gmail.com
4
 Universitas Budi Darma, Medan, Indonesia, e-mail: buuloloefori21@gmail.com
5
 Politeknik Negeri Medan, Medan, Indonesia, e-mail: bisterpurba@polmed.ac.id
6
 ITnB Carnegie, Medan, Indonesia, e-mail: nismanisma23@gmail.com
7
 Sekolah Tinggi Keguruan dan Ilmu Pendidikan AL Maksum, Medan, Indonesia, e-mail: riansyahmuhammad88@gmail.com
*coressponding author)


     Info Artikel                         Abstrak

     Diajukan: 03-11-2024                 E-katalog perpustakaan adalah salah satu aplikasi yang membantu pengguna untuk
     Diterima: 15-11-2024                 mencari koleksi buku atau informasi perpustakaan dengan lebih efisien melalui sistem
     Diterbitkan: 30-11-2024              berbasis elektronik. Salah satu tantangan dalam pengembangan e-katalog adalah
                                          meningkatkan kecepatan dan akurasi dalam pencarian data, khususnya dalam
                                          pencocokan string (teks) yang digunakan untuk mencari informasi katalog. Algoritma
     Kata Kunci:                          Knuth-Morris-Pratt (KMP) merupakan salah satu algoritma pencocokan string yang
     Implementasi;                        efisien untuk menyelesaikan masalah ini. Penelitian ini bertujuan untuk
     Algoritma;                           mengimplementasikan algoritma KMP dalam sistem e-katalog perpustakaan untuk
     Knuth-Morris-Pratt;                  meningkatkan performa pencarian data dan meminimalkan waktu respons. Hasil
     E-Katalog Perpustakaan;              penelitian ini menyimpulkan bahwa Algoritma knuth morris pratt dapat membantu
                                          mempercepat pencocokan string, sehingga memperbaiki waktu respons dan efisiensi
                                          sistem pencarian data. Dengan demikian, penerapan algoritma ini dapat menjadi
     Keywords:                            solusi yang baik dalam pengembangan e-katalog perpustakaan yang lebih cepat dan
     Implementation;                      efisien.
     Algorithm;
     Knuth-Morris-Pratt;                  Abstract
     Library E-Catalog;
                                          Library e-catalog is one of the applications that help users to search for book
                                          collections or library information more efficiently through an electronic-based system.
     Lisensi: cc-by-sa                    One of the challenges in e-catalog development is to increase the speed and accuracy
                                          of data search, especially in string (text) matching used to search catalog information.
                                          Knuth-Morris-Pratt (KMP) algorithm is one of the efficient string matching algorithms
     Copyright Â© 2024 by Author.          to solve this problem. This research aims to implement KMP algorithm in library e-
     Published by Faatuatua Media Karya   catalog system to improve data search performance and minimize response time. The
                                          results of this study conclude that Knuth Morris Pratt algorithm can help speed up
                                          string matching, thus improving the response time and efficiency of the data search
                                          system. Thus, the application of this algorithm can be a good solution in the
                                          development of a faster and more efficient library e-catalog.


1.        PENDAHULUAN
      Pencarian informasi dalam sistem e-katalog perpustakaan merupakan fitur utama yang
memudahkan pengunjung menemukan buku atau materi lainnya. Namun, seiring dengan pertumbuhan
koleksi dan jumlah data yang dikelola, kecepatan pencarian menjadi faktor yang krusial. Banyak sistem
e-katalog yang masih menggunakan metode pencarian berbasis sekuensial yang membutuhkan waktu
lama, terutama ketika jumlah data yang dicari sangat besar.
      Salah satu cara untuk mengatasi masalah ini adalah dengan menerapkan algoritma string
matching yang lebih efisien [1], [2], [3]. Salah satu algoritma string matching yang dapat digunakan

                                                                                         Copyright@2024, KETIK, Hlm | 1
                                                                   KETIK: JURNAL INFORMATIKA
                                                                       ISSN: 3026-183X (Media Online)
                                                                 Vol. 02, No. 02, November 2024 Hal. 01-04

adalah Knuth-Morris-Pratt, yang terkenal karena kemampuannya dalam memproses pencarian string
dengan waktu komputasi O(n + m), di mana n adalah panjang teks dan m adalah panjang pola [4]. Pada
penelitian terdahulu, algoritma knuth-morris-pratt telah berhasil digunakan pada banyak studi kasus
untuk meminimalisir waktu dalam pencarian data, seperti pencarian data sinopsis film bioskop [5], data
kamus bahasa isyarat [6], data kamus tanaman obat berbasis digital [7], dan lain sebagainya. Penelitian
ini bertujuan untuk menerapkan algoritma knuth-morris-pratt pada sistem e-katalog perpustakaan untuk
meningkatkan performa pencarian.

2.   METODE PENELITIAN
2.1 Tahapan Penelitian
     Tahapan penelitian yang digunakan dalam penelitian dapat terlihat pada gambar diagram di
bawah ini:

                                                                        Implementasi
                  Identifikasi               Pengumpulan
                                                                       Algoritma Knuth-
                   Masalah                       Data
                                                                         Morris-Pratt




                                              Kesimpulan                 Hasil Analisis


                                    Gambar 1. Tahapan Penelitian
2.2 Algoritma
     Algoritma adalah rangkaian instruksi yang terstruktur dan logis yang merinci suatu proses untuk
menyelesaikan situasi tertentu dan dapat ditulis secara sistematis menggunakan pseudocode atau
skema diagram alur. Algoritma merupakan hasil pemikiran konseptual, jika ingin diimplementasikan oleh
komputer harus diterjemahkan ke dalam representasi bahasa pemrograman [8], [9].

2.3 String Matching
       String matching adalah proses yang memecahkan masalah yang berkaitan dengan pengenalan
pola dan digunakan untuk mencocokkan dua karakter string (yaitu pola dan teks). Konsep kerja
algoritma string matching memegang peranan yang sangat penting dalam proses pencarian pola teks
pada suatu sistem atau aplikasi [1], [10], [11].

2.4 Knuth-Morris-Pratt
        Algoritma knuth-morris-pratt adalah algoritma pencarian string yang sangat efisien, dirancang
untuk menemukan lokasi kemunculan pola (pattern) dalam teks (text) tanpa perlu melakukan
perbandingan yang berulang. Algoritma ini ditemukan oleh Donald Knuth, Vaughan Pratt, dan James
H. Morris pada tahun 1977. Algoritma KMP berusaha untuk meminimalkan jumlah perbandingan
karakter dengan memanfaatkan informasi yang sudah ada selama pencocokan sebelumnya. Ketika
terjadi ketidakcocokan antara pola dan teks pada posisi tertentu, KMP menggunakan informasi yang
ada pada pola untuk melompat langsung ke posisi yang relevan, alih-alih memulai pencarian dari awal
lagi [4], [5], [7].

2.5 E-Katalog Perpustakaan
      E-katalog perpustakaan adalah sistem yang digunakan oleh perpustakaan untuk mengelola dan
menyediakan akses elektronik ke daftar koleksi buku, jurnal, artikel, atau sumber daya informasi lainnya.
Sistem ini memudahkan pengunjung atau pengguna perpustakaan untuk mencari, menemukan, dan
mengakses bahan pustaka dengan cara yang efisien, sering kali melalui antarmuka berbasis web.
Sistem e-katalog menggantikan katalog tradisional berbasis kartu atau manual, yang memerlukan
banyak waktu dan usaha untuk mencari informasi. Dengan e-katalog, pengguna dapat melakukan
pencarian dengan cepat berdasarkan berbagai kriteria, seperti judul buku, pengarang, tahun terbit,
subjek, atau kata kunci lainnya [12], [13].


Copyright@2024, KETIK, Page | 2
KETIK: JURNAL INFORMATIKA
ISSN: 3026-183X (Media Online)
Vol. 02, No. 02, November 2024 Hal. 01-04


3.    HASIL DAN ANALISIS
      Hasil penelitian penggunaan algoritma knuth morris pratt untuk menyelesaikan permasalahan
pencarian data pada E-Katalog Perpustakaan dapat dilihat pada uraian berikut:
1. Contoh Studi Kasus
   Studi kasus dalam penelitian yaitu pencarian data buku ilmu komputer berjudul Sistem Informasi
   pada sebuah E-Katalog, yang dimana kata MANAJEMEN digunakan sebagai Text dan EMEN
   digunakan sebagai Pattern.
2. Implementasi Algoritma Knuth Morris Pratt
   Adapun hasil penyelesaian studi kasus pencarian data buku ilmu komputer berjudul Sistem Informasi
   pada sebuah E-Katalog dengan algoritma Knuth Morris Pratt, yaitu:
   a. Iterasi 1
      Pada Iterasi 1, pattern 1 (E) dicocokan dengan text 1 (M) seperti yang terlihat pada Tabel 1.
                                           Tabel 1. Iterasi 1
                                  Text       M   A N A J       E M E N
                                  Pattern    E   M E N

        Hasil pencocokan string pada iterasi 1 diketahui bahwa pattern 1 (E) dengan text 1 (M) tidak
        cocok. Maka pattern digeser sebanyak satu langkah ke arah kanan seperti yang terlihat pada
        Tabel 2.
     b. Iterasi 2
        Pada Iterasi 2, pattern 1 (E) dicocokan dengan text 2 (A) seperti yang terlihat pada Tabel 2.
                                             Tabel 2. Iterasi 2
                                  Text       M   A N A J       E M E N
                                  Pattern        E M E N

        Hasil pencocokan string pada iterasi 2 diketahui bahwa pattern 1 (E) dengan text 2 (A) tidak
        cocok. Maka pattern digeser sebanyak satu langkah ke arah kanan seperti yang terlihat pada
        Tabel 3.
     c. Iterasi 3
        Pada Iterasi 3, pattern 1 (E) dicocokan dengan text 3 (N) seperti yang terlihat pada Tabel 3.
                                             Tabel 3. Iterasi 3
                                  Text       M   A N A J       E M E N
                                  Pattern          E M E       N

        Hasil pencocokan string pada iterasi 3 diketahui bahwa pattern 1 (E) dengan text 3 (N) tidak
        cocok. Maka pattern digeser sebanyak satu langkah ke arah kanan seperti yang terlihat pada
        Tabel 4.
     d. Iterasi 4
        Pada Iterasi 4, pattern 1 (E) dicocokan dengan text 4 (A) seperti yang terlihat pada Tabel 4.
                                             Tabel 4. Iterasi 4
                                  Text       M   A N A J E M E N
                                  Pattern            E M E N

        Hasil pencocokan string pada iterasi 4 diketahui bahwa pattern 1 (E) dengan text 4 (A) tidak
        cocok. Maka pattern digeser sebanyak satu langkah ke arah kanan seperti yang terlihat pada
        Tabel 5.

     e. Iterasi 5
        Pada Iterasi 5, pattern 1 (E) dicocokan dengan text 5 (J) seperti yang terlihat pada Tabel 5.
                                             Tabel 5. Iterasi 5
                                  Text       M   A N A J       E M E N
                                  Pattern              E       M E N

        Hasil pencocokan string pada iterasi 5 diketahui bahwa pattern 1 (E) dengan text 5 (J) tidak cocok.
        Maka pattern digeser sebanyak satu langkah ke arah kanan seperti yang terlihat pada Tabel 6.

     f. Iterasi 6
        Pada Iterasi 6, pattern 1 (E) dicocokan dengan text 6 (E) seperti yang terlihat pada Tabel 4.
                                             Tabel 4. Iterasi 6
                                  Text       M   A N A J       E M E N
                                  Pattern                      E M E N


                                                                        Copyright@2024, KETIK, Page | 3
                                                                     KETIK: JURNAL INFORMATIKA
                                                                        ISSN: 3026-183X (Media Online)
                                                                  Vol. 02, No. 02, November 2024 Hal. 01-04



       Hasil pencocokan string pada iterasi 6 diketahui bahwa pattern 1 (E) dengan text 6 (E) cocok.
       Maka pattern tidak digeser, namu dilakukan pencocokan kembali antara pattern selanjutnya
       dengan text selanjutnya. Dikarenakan pada tabel 4 terlihat bahwa seluruh pattern memiliki
       kecocokan dengan text maka prococokan string selesai di Iterasi yang ke 6 (enam).

4.     KESIMPULAN
       Algoritma knuth morris pratt dapat membantu mempercepat pencocokan string, sehingga
memperbaiki waktu respons dan efisiensi sistem pencarian data. Dengan demikian, penerapan
algoritma ini dapat menjadi solusi yang baik dalam pengembangan e-katalog perpustakaan yang lebih
cepat dan efisien. Sistem e-katalog perpustakaan masih dapat ditingkatkan lebih lanjut dengan
mengintegrasikan teknik optimisasi lainnya seperti indeksasi dan pemrograman paralel untuk
menangani data dalam jumlah besar. Penelitian lanjutan juga dapat dilakukan untuk mengeksplorasi
penerapan algoritma knuth morris pratt pada sistem pencarian teks lainnya, termasuk pencarian multi-
kata atau pencarian dalam dokumen yang lebih kompleks.

REFERENSI
[1]    Anggia Utami and A. Saehan, â€œPenerapan Algoritma Turbo Boyer Moore Pada Aplikasi
       PerbandinganHarga Laptop Menggunakan Web,â€ Bul. Ilm. Inform. Teknol., vol. 1, no. 2, pp. 37â€“
       42, 2022.
[2]    A. Azhar, N. Marbun, S. Aripin, and E. Buulolo, â€œImplementasi Algoritma Horspool Pada Aplikasi
       Istilah Fashion,â€ KOMIK (Konferensi Nas. Teknol. Inf. dan Komputer), vol. 3, no. 1, pp. 549â€“551,
       2019, doi: 10.30865/komik.v3i1.1641.
[3]    Y. Napitupulu, â€œPerancangan Aplikasi Kode Etik Profesi Dengan Menerapkan Algoritma Raita,â€
       KLIK Kaji. Ilm. Inform. dan Komput., vol. 2, no. 2, pp. 80â€“83, 2021, [Online]. Available:
       http://djournals.com/klik/article/view/222
[4]    R. Angelina, P. Hutabarat, J. S. Hutapea, D. Marlina, and M. Lubis, â€œPenerapan Algoritma String
       Matching Dalam Pencocokan Data String,â€ J. Tek. Inform., vol. 15, no. 2, 2023.
[5]    N. Novianti, R. C. G. I. Kembaren, D. M. Br Bangun, and N. Marbun, â€œImplementasi Algoritma
       Knuth Morris Pratt Pada Aplikasi Sinopsis Film Bioskop Berbasis Web,â€ KOMIK (Konferensi Nas.
       Teknol. Inf. dan Komputer), vol. 3, no. 1, pp. 398â€“401, 2019, doi: 10.30865/komik.v3i1.1619.
[6]    Andreansyah and N. Ratama, â€œImplementasi Algoritma Knuth Morris Pratt DalamPencarian
       Kamus Bahasa Isyarat,â€ JORAPI J. Res. Publ. Innov., vol. 1, no. 1, pp. 120â€“125, 2023.
[7]    A. Qurâ€™ania, Triastinurmiatiningsih, and E. Candra, â€œKamus Digital Tanaman Obat Menggunakan
       Algoritme Knuth Morris Pratt Berbasis Mobile,â€ KOMPUTASI J. Ilm. Ilmu Komput. dan Mat., vol.
       19, no. 1, pp. 354â€“361, 2022.
[8]    N. Marbun, M. Zarlis, D. Hartama, Mesran, and B. J. . Sitompul, â€œImplementasi Algoritma Raita
       Pada Pencarian Katalog Alkes,â€ Semin. Nas. Sains Teknol. Inf., pp. 520â€“523, 2019, [Online].
       Available: http://prosiding.seminar-id.com/index.php/sensasi/article/view/357
[9]    F. Fauzi Alvianda and Y. Sumaryana, â€œPerbandinganAlgoritma Brute Force Dengan Boyer-Moore
       Pada Aplikasi Pencarian Kerja Berbasis Web,â€ Inf. , vol. 87, no. 1, pp. 87â€“99, 2023.
[10]   N. Marbun, I. J. Sinaga, A. Azhar, A. Manik, and S. B. F. Ginting, â€œPenerapan Algoritma
       Levenshtein dalam Pencarian Arti Istilah Penelitian,â€ Pros. SINTAKS 2019, vol. 1, no. 1, pp. 51â€“
       55, 2019.
[11]   R. Kristianto Hondro, â€œImplementasi Algoritma Boyer Moore Pada Website Pencarian Jasa Servis
       Drone,â€ FIMERKOM J. Inf. Syst. Technol., vol. 1, no. 1, pp. 1â€“5, 2024.
[12]   W. Srihandoko, A. Mekaniwati, and Y. Taqyudin, â€œPelatihan Pembuatan E-Katalog Sebagai Media
       Penjualan Online Pada Usaha Mikro Kecil Menengah Kampung Cincau Kelurahan Gudang Kota
       Bogor,â€ J. Abdimas Dedik. Kesatuan, vol. 4, no. 1, pp. 67â€“70, 2023, doi:
       10.37641/jadkes.v4i1.2424.
[13]   D. Amanda, D. Hindarto, E. Hadianto, A. Sariwardani, and A. Makmur, â€œSmartphone untuk sistem
       katalog perpustakaan di era internet of things,â€ J. Tek. Inform. dan Sist. Inf., vol. 10, no. 2, pp.
       364â€“376, 2023, [Online]. Available: http://jurnal.mdp.ac.id




Copyright@2024, KETIK, Page | 4

