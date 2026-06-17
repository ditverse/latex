# Proposal PKM 2026 - 11 Juni

> Hasil konversi otomatis dari file PDF: Proposal PKM 2026 - 11 Juni.pdf.

                   USULAN
     PENGABDIAN KEPADA MASYARAKAT (PKM)


     Workshop Machine Learning Untuk Prediksi Awal
    Kesehatan Tanaman Melalui Analisis Citra Daun Bagi
        Siswa SMK Negeri/Swasta Di Kota Cimahi
     (Studi Kasus: SMKN 2 Cimahi - Jurusan Rekayasa
                    Perangkat Lunak)




                              Oleh:
Dr. Syafrial Fachri Pane.,S.T.,M.TI.,EBDP.,CDSP.,SFPC 0416048803
M. Yusril Helmi Setyawan, S.Kom., M.Kom.,SFPC.        0407117405
Amri Yanuar,ST.,M.MoT                                 0415048901




        SARJANA TERAPAN TEKNIK INFORMATIKA
    UNIVERSITAS LOGISTIK DAN BISNIS INTERNASIONAL
                     TAHUN 2026


                                                                   I


---

                                       HALAMAN PENGESAHAN




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026   II


---

                            HALAMAN KETERLIBATAN MAHASISWA

   No     Nama                      NPM                   Bentuk Keterlibatan          Tanda Tangan
    1     Raditya Rizki Raharja 714240041                 Membantu persiapan teknis
                                                          workshop, pengecekan
                                                          perangkat dan koneksi
                                                          internet, konfigurasi Google
                                                          Colab, serta pendampingan
                                                          peserta pada tahap
                                                          eksplorasi dataset dan
                                                          praproses citra daun.
    2     Muhammad Arif                  714240008        Membantu fasilitasi praktik
          Rivaldi                                         Machine Learning,
                                                          pendampingan peserta
                                                          dalam pelatihan model
                                                          klasifikasi citra daun,
                                                          evaluasi hasil prediksi, dan
                                                          penyelesaian kendala teknis
                                                          selama workshop.
    3     Rifky Najra Adipura            714230025        Membantu dokumentasi
                                                          kegiatan, pengumpulan data
                                                          evaluasi melalui pre-test,
                                                          post-test, dan kuesioner,
                                                          serta membantu penyusunan
                                                          laporan kegiatan dan rekap
                                                          hasil pelaksanaan
                                                          workshop.
    4     Ode Andi Alamsyah              714230032        Membantu pendampingan
                                                          mini project peserta,
                                                          pengembangan aplikasi
                                                          prediksi sederhana berbasis
                                                          Streamlit, serta membantu
                                                          kelompok siswa dalam
                                                          penyusunan dan presentasi
                                                          hasil project.

                                                                                        Bandung, 20 Mei 2026




                                             Dr. Syafrial Fachri Pane.,S.T.,M.TI., EBDP.,CDSP.,SFPC
                                                                                           117.88.233




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                     III


---

                                                          DAFTAR ISI

HALAMAN PENGESAHAN .................................................................................................. II

HALAMAN KETERLIBATAN MAHASISWA.................................................................... III

DAFTAR ISI ............................................................................................................................IV

DAFTAR TABEL ..................................................................................................................... V

DAFTAR GAMBAR ...............................................................................................................VI

RINGKASAN ........................................................................................................................ VII

BAB I PENDAHULUAN .......................................................................................................... 1
    1.1   Analisis Situasi .................................................................................................... 1
    1.2   Permasalahan Mitra ............................................................................................. 3

BAB II SOLUSI DAN TARGET LUARAN............................................................................. 5
    2.1    Solusi ................................................................................................................... 5
    2.2    Target Luaran ....................................................................................................... 7

BAB III LANDASAN TEORI .................................................................................................. 8
    3.1    Machine Learning dalam Pendidikan Kejuruan ................................................... 8
    3.2    Computer Vision dan Klasifikasi Citra Daun Tanaman ....................................... 9
    3.3    Prediksi Awal sebagai Pendekatan Deteksi Dini Penyakit Tanaman ................. 10
    3.4    Project-Based Learning dalam Pendidikan Vokasional ..................................... 11
    3.5    Tools Pembelajaran: Google Colab, Kaggle, dan Streamlit ............................... 12
    3.6    Studi Literatur Penelitian Terdahulu .................................................................. 13
    3.7    Posisi dan Kebaruan Penelitian .......................................................................... 15

BAB IV METODE PELAKSANAAN .................................................................................... 16
    4.1   Tahapan Solusi ................................................................................................... 16
    4.2   Metode Pendekatan ............................................................................................ 17
    4.3   Partisipasi Mitra................................................................................................. 18
    4.4   Evaluasi dan Keberlanjutan Program ................................................................. 19

BAB V BIAYA DAN JADWAL PKM ..................................................................................... 21

        5.1          Anggaran Biaya ................................................................................................. 21

        5.2          Jadwal Kegiatan ................................................................................................ 21

DAFTAR PUSTAKA ............................................................................................................. 23

LAMPIRAN ............................................................................................................................ 25

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                                                IV


---

                                                         DAFTAR TABEL

Tabel 3. 1 Ringkasan Studi Literatur Penelitian Terdahulu ....................................................................13

Tabel 4. 1 Indikator Evaluasi Program PKM .........................................................................................19

Tabel 5. 1 Anggaran Biaya ....................................................................................................................21
Tabel 5. 2 Jadwal Kegiatan ...................................................................................................................21




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                                                        V


---

                                             DAFTAR GAMBAR

Gambar 2. 1 Arsitektur end-to-end sistem workshop Machine Learning. ...............................................6




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                            VI


---

                                                RINGKASAN

                 Perkembangan teknologi Artificial Intelligence (AI) dan Machine
       Learning (ML) menuntut penguatan kompetensi baru dalam pendidikan vokasional,
       khususnya pada bidang Rekayasa Perangkat Lunak. Siswa SMK tidak hanya perlu
       menguasai dasar pemrograman, tetapi juga membutuhkan pengalaman praktis
       dalam membangun solusi berbasis data yang relevan dengan kebutuhan industri
       digital saat ini. Mitra kegiatan Pengabdian kepada Masyarakat ini adalah SMKN 2
       Cimahi Jurusan Rekayasa Perangkat Lunak dengan permasalahan utama berupa
       terbatasnya akses pelatihan praktis Machine Learning dan Computer Vision, belum
       optimalnya pembelajaran berbasis proyek kecerdasan buatan, serta masih
       minimnya portofolio siswa yang dapat mendukung kesiapan kerja maupun studi
       lanjut di bidang teknologi informasi.

                 Untuk menjawab permasalahan tersebut, kegiatan ini menyelenggarakan
       Workshop Machine Learning untuk Prediksi Awal Kesehatan Tanaman melalui
       Analisis Citra Daun. Studi kasus dipilih karena bersifat visual, menggunakan
       dataset publik yang mudah diakses, tidak memerlukan perangkat keras khusus, serta
       relevan dengan penerapan teknologi dalam kehidupan sehari-hari. Sistem
       diposisikan sebagai alat screening awal, bukan diagnosis final, sehingga peserta
       dapat memahami keterbatasan model Machine Learning dan pentingnya
       interpretasi hasil prediksi secara kritis.

                 Pelaksanaan kegiatan menggunakan pendekatan Project-Based Learning
       yang mencakup penyusunan modul pelatihan, pengenalan konsep Artificial
       Intelligence dan Machine Learning, eksplorasi dataset citra daun tanaman, pelatihan
       model klasifikasi menggunakan Google Colab, evaluasi hasil prediksi model,
       hingga pengembangan aplikasi prediksi sederhana berbasis Streamlit. Evaluasi
       kegiatan dilakukan melalui pre-test dan post-test, penilaian mini project kelompok,
       serta kuesioner kepuasan peserta dengan dukungan mahasiswa ULBI sebagai
       fasilitator teknis selama pelaksanaan workshop berlangsung.

                 Hasil yang diharapkan dari kegiatan ini adalah meningkatnya pemahaman
       dan keterampilan siswa dalam menerapkan Machine Learning dan Computer
       Vision secara praktis, tersusunnya modul pembelajaran berbasis Machine Learning
       yang dapat digunakan kembali oleh pihak sekolah, serta publikasi ilmiah pada
       jurnal pengabdian kepada masyarakat terindeks nasional. Selain itu, kegiatan ini
       diharapkan mampu membentuk pengalaman belajar berbasis proyek yang dapat
       memperkuat kompetensi digital dan portofolio siswa SMK pada bidang Artificial
       Intelligence dan teknologi berbasis data.

       Kata Kunci : Machine Learning, Computer Vision, Project-Based Learning.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026        VII


---

                                                      BAB I
                                             PENDAHULUAN

       1.1    Analisis Situasi

              Perkembangan teknologi kecerdasan buatan atau Artificial Intelligence dan
       Machine Learning telah mendorong perubahan signifikan dalam kebutuhan
       kompetensi sumber daya manusia di bidang teknologi informasi [1]. Industri digital
       saat ini tidak hanya membutuhkan lulusan yang mampu membuat program
       komputer, tetapi juga tenaga kerja yang memiliki kemampuan mengolah data,
       membangun model prediksi, memahami pola dari citra atau teks, serta menerapkan
       solusi berbasis kecerdasan buatan pada permasalahan nyata. Kondisi ini menjadi
       tantangan bagi pendidikan vokasional, khususnya Sekolah Menengah Kejuruan,
       untuk menyesuaikan kompetensi siswa dengan kebutuhan industri [2], [3].
              SMKN 2 Cimahi merupakan salah satu sekolah kejuruan yang memiliki
       Jurusan Rekayasa Perangkat Lunak dan menjadi mitra dalam kegiatan Pengabdian
       kepada Masyarakat ini. Jurusan Rekayasa Perangkat Lunak memiliki karakteristik
       pembelajaran yang dekat dengan pemrograman, pengembangan aplikasi, basis data,
       dan praktik rekayasa perangkat lunak. Berdasarkan rancangan kegiatan, sasaran
       program ini adalah siswa Jurusan Rekayasa Perangkat Lunak SMKN 2 Cimahi yang
       telah memiliki dasar pemrograman. Selain itu, sekolah mitra juga telah memiliki
       hubungan kemitraan sebelumnya dengan ULBI melalui kegiatan PKM Workshop
       Bootcamp Laravel pada tahun 2025, sehingga kegiatan ini menjadi bentuk
       keberlanjutan penguatan kompetensi teknologi bagi siswa SMK [4].
               Pada kegiatan PKM sebelumnya, penguatan kompetensi siswa diarahkan pada
       pengembangan aplikasi web menggunakan Laravel melalui pendekatan Project
       Based Learning. Kegiatan tersebut menunjukkan bahwa siswa SMK dapat diarahkan
       untuk menghasilkan produk teknologi sederhana apabila diberikan modul,
       pendampingan, dan studi kasus yang sesuai dengan tingkat kemampuan mereka [5].
       Pola ini menjadi dasar penting dalam merancang kegiatan lanjutan yang lebih
       relevan dengan perkembangan teknologi terkini, yaitu pengenalan Machine
       Learning dan Computer Vision melalui studi kasus yang sederhana, visual, dan
       aplikatif [6].
               Berdasarkan identifikasi awal, siswa Jurusan Rekayasa Perangkat Lunak
       SMKN 2 Cimahi telah memiliki fondasi pemrograman dasar, logika pemrograman,
       serta pengalaman awal dalam pengembangan aplikasi. Namun, pembelajaran yang

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026       1


---

       diterima siswa belum secara khusus mengarah pada praktik Machine Learning
       dan Computer Vision secara terstruktur. Siswa belum memiliki pengalaman
       membangun alur kerja Machine Learning secara end-to-end, mulai dari pengenalan
       dataset, praproses data, pelatihan model, evaluasi hasil, hingga implementasi model
       ke dalam aplikasi sederhana. Kondisi ini menunjukkan adanya kesenjangan antara
       kemampuan pemrograman dasar yang sudah dimiliki siswa dengan kebutuhan
       kompetensi kecerdasan buatan yang semakin dibutuhkan dalam dunia kerja
       teknologi.

              Kesenjangan tersebut menjadi peluang bagi ULBI untuk melakukan transfer
       ilmu pengetahuan dan teknologi melalui kegiatan Workshop Machine Learning
       untuk Prediksi Awal Kesehatan Tanaman melalui Analisis Citra Daun. Studi kasus
       citra daun dipilih karena mudah divisualisasikan, dapat dipahami oleh siswa,
       menggunakan dataset publik yang tersedia secara gratis, serta tidak memerlukan
       perangkat keras khusus. Melalui kegiatan ini, siswa tidak hanya mempelajari
       konsep dasar Machine Learning, tetapi juga memperoleh pengalaman praktik dalam
       membangun model klasifikasi citra dan aplikasi sederhana yang dapat digunakan
       sebagai portofolio pembelajaran [6], [7].
                Pelatihan Machine Learning berbasis proyek ini diharapkan dapat
       memberikan manfaat langsung bagi mitra. Bagi siswa, kegiatan ini dapat
       meningkatkan pemahaman terhadap penerapan kecerdasan buatan, memperkaya
       portofolio proyek teknologi, dan meningkatkan kesiapan menghadapi dunia kerja
       maupun studi lanjut di bidang teknologi informasi. Bagi sekolah, kegiatan ini dapat
       menghasilkan modul pelatihan dan bahan ajar praktis yang dapat digunakan kembali
       dalam pembelajaran. Dengan demikian, kegiatan PKM ini tidak hanya berorientasi
       pada pelatihan sesaat, tetapi juga diarahkan untuk mendukung penguatan
       kompetensi digital siswa SMK secara berkelanjutan [8].
               Luaran dari kegiatan PKM ini mencakup peningkatan kompetensi siswa
       Jurusan Rekayasa Perangkat Lunak SMKN 2 Cimahi dalam bidang Machine
       Learning dan Computer Vision melalui pelatihan berbasis proyek dengan studi
       kasus klasifikasi citra daun tanaman. Selain itu, kegiatan ini menghasilkan modul
       pelatihan, notebook Google Colab, serta aplikasi prediksi sederhana berbasis
       Streamlit yang dapat dimanfaatkan sebagai bahan ajar tambahan di sekolah mitra.
       Luaran lainnya berupa laporan kegiatan, kuesioner evaluasi pembelajaran,
       dokumentasi mini project siswa, poster kegiatan PKM, serta publikasi ilmiah pada
       jurnal pengabdian kepada masyarakat yang memiliki ISSN dan terindeks nasional.
       Seluruh luaran tersebut diharapkan tidak hanya mendukung keberlanjutan
       pembelajaran teknologi kecerdasan buatan di lingkungan sekolah, tetapi juga

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026        2


---

       menjadi sarana penguatan portofolio siswa dan referensi pembelajaran praktis yang
       adaptif terhadap perkembangan industri digital.
       1.2 Permasalahan Mitra

             Berdasarkan analisis situasi yang telah diuraikan pada sub bab 1.1, beberapa
       permasalahan prioritas yang dihadapi mitra dan perlu diselesaikan melalui kegiatan
       Pengabdian kepada Masyarakat ini adalah sebagai berikut:


       1. Keterbatasan materi praktis Machine Learning dan Computer Vision
           Materi pembelajaran yang diterima siswa belum secara khusus mengarah pada
           praktik Machine Learning dan Computer Vision, sehingga siswa belum
           memperoleh pengalaman nyata dalam membangun model kecerdasan buatan
           yang sesuai dengan perkembangan industri digital.

       2. Minimnya akses terhadap tools, dataset, dan referensi pembelajaran
           Pembelajaran Machine Learning sering dianggap sulit karena membutuhkan
           pemahaman matematika, statistik, dan konfigurasi perangkat lunak tertentu.
           Siswa membutuhkan media pembelajaran yang lebih sederhana dan dapat
           diakses tanpa instalasi rumit, sehingga penggunaan tools berbasis browser
           seperti Google Colab dan dataset publik menjadi kebutuhan penting.

       3. Belum adanya pengalaman membangun pipeline Machine Learning secara
          end-to-end
           Siswa belum memiliki pengalaman membangun alur kerja Machine Learning
           secara end-to-end, mulai dari pengenalan data, praproses citra, pelatihan model,
           evaluasi, hingga implementasi ke dalam aplikasi sederhana. Pendekatan Project
           Based Learning dinilai relevan karena mendorong siswa memahami teori
           sekaligus menerapkannya melalui proyek yang membangun keterampilan
           praktis dan pemecahan masalah.
       4. Belum tersedianya portofolio siswa berbasis kecerdasan buatan

           Sebagian besar siswa belum memiliki portofolio berbasis Artificial Intelligence
           atau Machine Learning yang dapat mendukung kesiapan kerja, magang industri,
           maupun pendaftaran ke perguruan tinggi.

       5. Keterbatasan pemahaman terhadap penerapan Machine Learning pada ma-
          salah nyata
           Siswa membutuhkan contoh penerapan Machine Learning yang dekat dengan
           kehidupan sehari-hari agar konsep kecerdasan buatan tidak dipahami sebagai

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026         3


---

           materi abstrak. Studi kasus prediksi awal kesehatan tanaman melalui analisis
           citra daun dipilih karena bersifat visual dan mudah dipahami, sekaligus melatih
           siswa memahami manfaat dan keterbatasan model sebagai alat screening awal,
           bukan diagnosis final.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026        4


---

                                          BAB II
                                SOLUSI DAN TARGET LUARAN

       2.1    Solusi

              Menanggapi permasalahan yang telah diidentifikasi dalam sub bab 1.2, solusi
       utama yang ditawarkan dalam kegiatan Pengabdian kepada Masyarakat ini adalah
       penyelenggaraan Workshop Machine Learning untuk Prediksi Awal Kesehatan
       Tanaman melalui Analisis Citra Daun bagi siswa Jurusan Rekayasa Perangkat
       Lunak SMKN 2 Cimahi. Kegiatan ini dirancang sebagai transfer pengetahuan dan
       keterampilan praktis agar siswa tidak hanya memahami konsep dasar kecerdasan
       buatan, tetapi juga mampu membangun proyek sederhana berbasis Machine
       Learning dan Computer Vision.
               Workshop menggunakan pendekatan Project-Based Learning yang
       menempatkan siswa sebagai peserta aktif dalam proses belajar. Pendekatan ini
       sesuai dengan karakter pendidikan vokasional yang menekankan keterampilan
       praktik, penyelesaian masalah, kolaborasi, dan pembuatan produk nyata. Siswa
       diarahkan membangun alur kerja mulai dari pengenalan dataset, praproses gambar,
       pelatihan model klasifikasi, evaluasi hasil prediksi, hingga pembuatan aplikasi
       sederhana yang dapat menerima input foto daun dan menampilkan hasil prediksi,
       sehingga memperoleh pengalaman membangun pipeline Machine Learning secara
       end-to-end.
              Studi kasus klasifikasi citra daun dipilih berdasarkan beberapa
       pertimbangan: dataset tersedia secara publik, data berbentuk gambar lebih mudah
       divisualisasikan, topik kesehatan tanaman relevan dengan isu ketahanan pangan dan
       penerapan kecerdasan buatan dalam kehidupan sehari-hari, serta tidak memerlukan
       perangkat keras khusus sehingga cukup menggunakan laptop dan koneksi internet.
       Workshop memanfaatkan perangkat lunak gratis berbasis browser, yaitu Google
       Colab untuk pelatihan model, Kaggle sebagai sumber dataset, dan Streamlit untuk
       pengembangan aplikasi prediksi sederhana. Modul pelatihan dan notebook praktik
       disiapkan secara terstruktur agar siswa dapat mengulang materi secara mandiri
       setelah kegiat-an selesai.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026       5


---

              Gambar 2. 1 Arsitektur end-to-end sistem workshop Machine Learning.
               Pada Gambar 2. 1 memvisualisasikan rancangan iptek yang akan diterapkan
       pada kegiatan workshop. Visual tersebut menampilkan alur sistem pembelajaran
       Machine Learning dan Computer Vision secara end-to-end, mulai dari input citra
       daun, praproses gambar, pelatihan model klasifikasi menggunakan CNN, evaluasi
       hasil prediksi, hingga implementasi model ke dalam aplikasi sederhana berbasis
       Streamlit. Melalui gambar tersebut, solusi yang ditawarkan dapat dipahami secara
       lebih konkret karena menunjukkan hubungan antara dataset PlantVillage, Google
       Colab, model Machine Learning, dan aplikasi prediksi yang akan digunakan dalam
       praktik siswa. Dengan demikian, gambar Lampiran 2 tidak hanya berfungsi sebagai
       ilustrasi pendukung, tetapi juga menjadi representasi teknis dari pendekatan
       Project-Based Learning yang diterapkan dalam workshop untuk membantu siswa
       memahami alur pengembangan proyek kecerdasan buatan secara terstruktur dan
       aplikatif.
               Hasil prediksi sistem yang dibangun dijelaskan kepada siswa sebagai alat
       screening awal, bukan diagnosis final. Melalui penegasan ini, siswa tidak hanya
       belajar membangun model, tetapi juga memahami keterbatasan model, pentingnya
       kualitas data, dan perlunya interpretasi hasil secara kritis, sehingga kegiatan ini turut
       membangun kemampuan berpikir ilmiah dan literasi kecerdasan buatan. Solusi ini
       diharapkan menjawab permasalahan utama mitra terkait keterbatasan akses

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026              6


---

       pembelajaran Machine Learning yang praktis, minimnya pengalaman proyek
       berbasis kecerdasan buatan, serta belum tersedianya portofolio AI/ML siswa,
       sekaligus menghasilkan modul pelatihan yang dapat digunakan kembali oleh
       sekolah mitra.

       2.2    Target Luaran

              Target luaran dalam kegiatan Pengabdian kepada Masyarakat ini disusun
       untuk menjawab permasalahan mitra secara terukur dan berdampak. Adapun target
       luaran dari program ini meliputi:
        2.2.1     Luaran Produk/Jasa

        a) Peningkatan kompetensi siswa melalui pelatihan praktis Machine Learning dan
           Computer Vision berbasis klasifikasi citra daun tanaman. Pelatihan mencakup input
           citra daun melalui kamera smartphone pada web Streamlit, praproses citra, pelatihan
           CNN di Google Colab, evaluasi model, dan penyajian hasil prediksi awal. Gambaran
           arsitektur sistem disajikan pada Lampiran 2.

        b) Modul pelatihan Machine Learning, notebook Google Colab, dan aplikasi prediksi
           sederhana berbasis Streamlit sebagai bahan ajar tambahan bagi sekolah mitra.


        2.2.2     Luaran Artikel Ilmiah dan Dokumentasi

        a) Laporan Kegiatan dalam bentuk hard file dan soft file yang memuat seluruh
           proses pelaksanaan kegiatan.

        b) Kuesioner Evaluasi Pembelajaran untuk mengukur efektivitas pelatihan
           terhadap peningkatan kompetensi siswa.

        c) Dokumentasi hasil mini project siswa berupa proyek klasifikasi citra daun yang
           dikembangkan selama workshop.

        d) Poster kegiatan PKM dalam format A2 sebagai media informasi dan diseminasi
           pada tahap monitoring dan evaluasi.

        e) Publikasi Ilmiah berupa satu artikel ilmiah yang ditargetkan untuk diterbitkan
           di jurnal pengabdian masyarakat bereputasi (minimal memiliki ISSN dan
           terindeks dalam portal seperti Sinta).




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026       7


---

                                                      BAB III
                                          LANDASAN TEORI

       3.1    Machine Learning dalam Pendidikan Kejuruan

              Perkembangan teknologi informasi yang berlangsung sangat cepat dalam
       satu dekade terakhir telah membawa perubahan mendasar pada kebutuhan
       kompetensi tenaga kerja di bidang digital. Kondisi ini mendorong institusi
       pendidikan di berbagai jenjang, termasuk pendidikan vokasional, untuk
       menyesuaikan materi pembelajaran dengan tuntutan industri yang kian berorientasi
       pada kecerdasan buatan dan pengolahan data. Nadzinski et al. [9]menyatakan
       bahwa meningkatnya permintaan tenaga kerja yang terampil di bidang data science
       dan machine learning menciptakan kesenjangan serius di pasar kerja global, dan
       kesenjangan ini mendesak dunia pendidikan untuk segera bertindak melalui
       pengajaran keterampilan tersebut di semua jenjang secara efektif dan mutakhir.
              Machine Learning atau ML merupakan bagian dari Artificial Intelligence
       yang memanfaatkan algoritma komputasi untuk melatih sistem secara berulang dari
       data tanpa memerlukan pemrograman eksplisit pada setiap instruksi [10],
       [11].Pendekatan pembelajaran dalam ML terbagi menjadi tiga kategori utama.
       Pertama, supervised learning, yaitu model yang bekerja dengan melatih algoritma
       menggunakan data berlabel sehingga sistem mampu mempelajari pola dan
       memberikan prediksi yang akurat terhadap data baru. Pendekatan ini umumnya
       digunakan untuk tugas regresi maupun klasifikasi. Kedua, unsupervised learning,
       yakni model yang menganalisis data tanpa label untuk menemukan pola tersembunyi
       dan mengelompokkan titik-titik data yang memiliki kemiripan. Ketiga,
       reinforcement learning, yaitu pendekatan yang memungkinkan sistem belajar
       melalui coba-coba dengan berinteraksi terhadap lingkungan untuk mengambil
       keputusan yang memaksimalkan hasil secara kumulatif. Dalam konteks workshop
       ini, paradigma yang digunakan adalah supervised learning dengan tugas klasifikasi
       citra daun tanaman.
              Relevansi penguatan kompetensi ML di tingkat pendidikan kejuruan telah
       dikonfirmasi oleh berbagai penelitian. Nadzinski et al. [9] menegaskan bahwa
       pengajaran data science dan machine learning di lembaga pendidikan kejuruan atau
       Vocational Education and Training sama pentingnya dengan pengajaran di jenjang
       universitas, karena pasar data membutuhkan berbagai profil pekerjaan dari berbagai
       subdomain dan level kualifikasi. Ketersediaan program pembelajaran ML di
       sekolah kejuruan memperluas pilihan karier siswa sekaligus melayani kebutuhan

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026       8


---

       industri secara langsung. Perez et al. [12]yang mengkaji inovasi kurikulum di tiga
       SMK di Indonesia menemukan bahwa implementasi konten digital modular,
       pembelajaran berbasis proyek, dan platform blended learning secara signifikan
       meningkatkan keterlibatan siswa dan kompetensi di bidang analisis data, komputasi
       awan, dan kolaborasi digital. Temuan ini menunjukkan bahwa siswa SMK jurusan
       Rekayasa Perangkat Lunak yang telah memiliki dasar pemrograman dan logika
       komputasi memiliki bekal yang memadai untuk diperkenalkan pada konsep dan
       praktik machine learning secara terstruktur.

       3.2    Computer Vision dan Klasifikasi Citra Daun Tanaman

               Computer Vision merupakan cabang dari kecerdasan buatan yang memung-
       kinkan mesin untuk memahami, menginterpretasikan, dan menganalisis informasi
       visual dari dunia nyata dalam bentuk gambar atau video. Salah satu arsitektur deep
       learning yang paling dominan dan terbukti efektif dalam tugas-tugas computer
       vision adalah Convolutional Neural Network atau CNN. Lu et al. [13] menjelaskan
       bahwa CNN pada dasarnya tersusun dari tiga jenis lapisan utama yang bekerja
       secara hierarkis. Lapisan konvolusi bertugas mengekstraksi fitur visual dari gambar
       masukan menggunakan prinsip korelasi lokal, di mana lapisan dangkal menangkap
       informasi tepi dan tekstur sederhana, lapisan menengah mengidentifikasi pola
       tekstur yang lebih kompleks, dan lapisan dalam mengekstraksi representasi
       semantik tingkat tinggi. Lapisan pooling kemudian melakukan sampling untuk
       mempertahankan informasi penting dari peta fitur sambil membuat model tidak
       sensitif terhadap pergeseran, rotasi, dan perubahan skala pada gambar. Lapisan
       fully connected di ujung arsitektur mengintegrasikan seluruh fitur yang telah
       diekstraksi untuk menghasilkan keputusan klasifikasi akhir.
              Dalam konteks deteksi penyakit tanaman, pengenalan visual berbasis
       pengamatan mata secara tradisional membutuhkan keahlian khusus, bersifat
       subjektif, dan menyita waktu yang tidak sedikit. Pendekatan machine learning
       konvensional berbasis fitur tekstur, warna, atau bentuk daun juga memiliki
       keterbatasan berupa performa yang kurang optimal untuk aplikasi real-time. Deep
       learning berbasis CNN hadir sebagai solusi yang mampu mengatasi kelemahan
       tersebut karena dapat mengekstraksi fitur secara otomatis dari data gambar mentah
       tanpa memerlukan rekayasa fitur manual [13].
              Dataset utama yang digunakan dalam workshop ini adalah PlantVillage,
       sebuah repositori citra terbuka yang dikembangkan oleh Hughes dan SalathÃ© [14].
       Dataset ini berisi lebih dari 54.000 gambar daun tanaman yang terbagi ke dalam
       8 kelas kondisi, mencakup kondisi sehat maupun berbagai jenis penyakit pada lebih

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026        9


---

       dari 14 spesies tanaman. Gambar-gambar dalam PlantVillage diambil dalam kon-
       disi latar belakang terkontrol sehingga setiap citra hanya menampilkan satu helai
       daun tanpa gangguan eksternal. Keunggulan ini menjadikan PlantVillage sebagai
       dataset yang sangat sesuai untuk keperluan pembelajaran di tingkat pemula karena
       telah tersedia secara publik di platform Kaggle, formatnya sudah terstruktur per
       kelas, dan telah digunakan secara luas sebagai benchmark standar dalam penelitian
       ilmiah tentang klasifikasi penyakit tanaman. Kelas penyakit yang menjadi fokus
       studi kasus dalam workshop ini mencakup kondisi Early Blight, Late Blight, Leaf
       Mold, Bacterial Spot, dan Healthy.

       3.3    Prediksi Awal sebagai Pendekatan Deteksi Dini Penyakit Tanaman

              Sistem berbasis kecerdasan buatan untuk pengenalan penyakit tanaman pada
       dasarnya tidak dirancang sebagai pengganti diagnosa ahli, melainkan sebagai alat
       bantu identifikasi awal atau screening tool yang dapat mempercepat proses
       penanganan sebelum kerusakan meluas. Lu et al. [13] menegaskan bahwa deep
       learning berbasis CNN yang diterapkan pada klasifikasi penyakit daun tanaman
       berfungsi untuk mendeteksi indikasi visual yang tampak pada permukaan daun
       sebagai langkah awal dalam rantai pengelolaan kesehatan tanaman. Prediksi yang
       dihasilkan sistem merupakan penilaian berdasarkan fitur visual yang terlihat, bukan
       analisis komprehensif atas keseluruhan kondisi fisiologis tanaman.
               Penting untuk dipahami bahwa sejumlah jenis gangguan pada tanaman tidak
       menghasilkan gejala visual yang dapat terdeteksi dari permukaan daun pada fase
       awal, misalnya busuk akar, infeksi sistemik di batang, atau penyakit yang bermula
       dari jaringan dalam. Dengan demikian, model klasifikasi yang dibangun dalam
       workshop ini diposisikan secara ilmiah sebagai instrumen prediksi awal yang
       membantu mengidentifikasi potensi penyakit berdasarkan ciri-ciri visual pada daun,
       dengan tingkat keyakinan tertentu yang harus diinterpretasikan secara kritis oleh
       pengguna. Suthar et al. [10] menjelaskan bahwa dalam evaluasi model machine
       learning, sejumlah metrik digunakan untuk mengukur seberapa baik sebuah model
       klasifikasi bekerja. Salah satu metrik yang relevan adalah akurasi, yang secara
       matematis dinyatakan sebagai rasio antara prediksi yang benar terhadap total
       keseluruhan sampel pengujian. Selain itu, confusion matrix digunakan sebagai
       representasi yang paling jelas untuk memahami distribusi prediksi benar dan salah
       dari model berdasarkan kelas-kelas yang ada, mencakup True Positive, True
       Negative, False Positive, dan False Negative.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026        10


---

                Pemahaman atas keterbatasan model ini memiliki nilai pedagogis yang
       penting. Melalui diskusi kritis tentang batas kemampuan sistem, siswa tidak hanya
       belajar cara membangun model, tetapi juga mengembangkan kemampuan berpikir
       ilmiah dan literasi kecerdasan buatan yang semakin dibutuhkan di era transformasi
       digital.

       3.4    Project-Based Learning dalam Pendidikan Vokasional

               Project-Based Learning atau PjBL adalah model instruksional yang
       menempatkan siswa sebagai pelaku aktif dalam proses pembelajaran melalui
       penyelesaian proyek nyata yang menantang. Model ini pertama kali diusulkan oleh
       John Dewey pada tahun 1890-an dan sejak saat itu telah dikembangkan serta
       diterapkan pada berbagai bidang studi dan situasi pembelajaran. Dalam praktiknya,
       PjBL dilak-sanakan dengan membagi siswa ke dalam kelompok-kelompok kecil
       yang bekerja bersama untuk mencapai tujuan yang sama, memecahkan kasus nyata,
       atau menja-wab pertanyaan dengan kompleksitas tinggi dalam rentang waktu
       tertentu [15].

               Megayanti et al. [15] melalui tinjauan literatur sistematis terhadap sejumlah
       penelitian empiris menyimpulkan bahwa PjBL terbukti memberikan dampak positif
       dalam mengembangkan keterampilan siswa kejuruan sesuai kerangka kompetensi
       abad ke-21. Dampak tersebut mencakup peningkatan kemampuan berpikir kritis
       dan pemecahan masalah, kecakapan berkomunikasi, kapasitas kerja sama tim,
       kreativitas, serta motivasi belajar. Lebih lanjut, PjBL juga terbukti meningkatkan
       penguasaan konten pengetahuan, keterampilan vokasional produktif, dan
       kemandirian belajar pada siswa. Chiang dan Lee (2016, dalam [15]) secara spesifik
       menemukan bahwa penerapan PjBL pada siswa SMK meningkatkan motivasi
       belajar dan ke-mampuan pemecahan masalah secara signifikan dibandingkan
       metode pembelajar-an konvensional.
              Handayani et al. [16] dalam penelitian terbarunya di perguruan tinggi
       vokasional Indonesia menunjukkan bahwa PjBL yang melibatkan komunitas nyata
       secara signifikan mengembangkan keterampilan kolaborasi, literasi teknologi
       informasi, serta kecakapan pengambilan keputusan pada mahasiswa generasi Z.
       Keterampilan kolaborasi tercatat sebagai aspek yang mengalami peningkatan paling
       besar dengan rata-rata skor yang jauh melampaui nilai netral. Temuan ini
       menegaskan bahwa PjBL sangat relevan diterapkan pada konteks pendidikan
       kejuruan yang memang berorientasi pada kompetensi kerja, penyelesaian masalah
       dunia nyata, dan pembu-atan produk nyata yang dapat dipertanggungjawabkan.
       Dalam konteks workshop Machine Learning ini, pendekatan PjBL
Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026          11


---

       diimplementasikan melalui pembagian kelompok kecil yang masing-masing
       membangun alur kerja ML secara mandiri, mulai dari eksplorasi data hingga
       pengembangan aplikasi prediksi sederhana.

       3.5    Tools Pembelajaran: Google Colab, Kaggle, dan Streamlit

              Pemilihan platform dan perangkat yang digunakan dalam kegiatan
       workshop sangat menentukan aksesibilitas dan efektivitas pembelajaran, terutama
       di lingkungan dengan keterbatasan infrastruktur seperti sekolah menengah
       kejuruan. Han et al. [17] menyebutkan bahwa Google Colab dan Kaggle termasuk
       platform publik yang telah banyak dimanfaatkan untuk keperluan pendidikan data
       science dan machine learning, mengingat keduanya dapat diakses secara gratis
       melalui browser tanpa memerlukan proses instalasi yang rumit.

              Google Colab merupakan platform Jupyter Notebook berbasis cloud yang
       dikembangkan oleh Google dan dapat digunakan secara gratis oleh siapa saja
       melalui akun Google. Platform ini memungkinkan pengguna untuk menulis dan
       menjalankan kode Python langsung dari browser, termasuk memanfaatkan
       akselerasi GPU secara gratis untuk keperluan pelatihan model machine learning.
       Suthar et al. [10] dalam pelaksanaan workshop ML mereka menggunakan Google
       Colab sebagai media utama karena platform ini dikenal mampu memberikan
       pengalaman pengguna yang konsisten, serta menjembatani kesenjangan antara teori
       dan praktik melalui notebook interaktif yang menggabungkan kode, teks penjelasan,
       dan visualisasi dalam satu dokumen tunggal.
               Kaggle adalah platform data science yang menyediakan ribuan dataset
       publik berkualitas, termasuk dataset PlantVillage, yang dapat diakses secara gratis
       dan diintegrasikan langsung ke dalam Google Colab melalui Kaggle API. Suthar et
       al. [10] menyebutkan bahwa dataset publik dari Kaggle merupakan salah satu
       sumber data nyata yang penting dan cocok untuk keperluan pembelajaran berbasis
       proyek, karena memberikan pengalaman kerja dengan data yang relevan dengan
       aplikasi dunia nyata. Pendekatan berbasis data nyata ini sejalan dengan temuan
       bahwa papar-an peserta didik terhadap data real secara signifikan berkontribusi
       pada efektivitas pembelajaran dan interaksi antara peserta dengan fasilitator.
               Streamlit digunakan sebagai framework Python untuk membangun
       antarmuka aplikasi web interaktif secara sederhana tanpa memerlukan penguasaan
       frontend yang mendalam. Melalui Streamlit, model Machine Learning yang telah
       dilatih dapat dikemas menjadi aplikasi prediksi yang menerima input gambar daun
       dan menampilkan hasil klasifikasi secara langsung. Dengan demikian, siswa
       memperoleh pengalaman nyata yang dapat dijadikan portofolio hasil workshop.
Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026        12


---

     3.6    Studi Literatur Penelitian Terdahulu

            Berikut disajikan rangkuman penelitian-penelitian terdahulu yang relevan dengan program PKM ini beserta posisi perbedaan
     dengan kegiatan yang diusulkan.
                                         Tabel 3. 1 Ringkasan Studi Literatur Penelitian Terdahulu

No               Peneliti         Tahun         Fokus Kajian            Metode            Hasil Utama                  Relevansi
                                                                                    Kebutuhan ML di VET
1.         Nadzinski et al. [9]   2023    Pengajaran ML dan data      Survei dan                               Landasan pen-tingnya
                                          science di pendidikan       tinjauan      sangat tinggi namun        pelatihan ML di SMK
                                          vokasional, survei siswa    kurikulum     implementa
                                          VET
                                                                                    si terstruktur masih
                                                                                    sangat terbatas
                                                                                    CNN adalah pendekatan      Dasar teknis penggunaan
2.         Lu et al. [13]         2021    Tinjauan CNN untuk          Tinjauan
                                          klasifikasi penyakit daun   sistematis    terbaik saat ini untuk     CNN pada studi kasus
                                          tanaman                                   deteksi penyakit visual    workshop
                                                                                    pada tanaman
                                                                                    PjBL terbukti              Justifikasi penggunaan
3.         Megayanti et           2020    Efektivitas PjBL di         Tinjauan
           al.[15]                        pendidikan vokasional       literatur     meningkatkan               PjBL sebagai metode
                                                                      sistematis    keterampilan abad ke-21    workshop
                                                                                    siswa SMK secara
                                                                                    positif
                                                                                    PjBL meningkatkan
4.         Handayani et al.       2026    PjBL untuk keterampilan     Studi                                    Konfirmasi re-levansi PjBL
           [16]                           abad ke-21 mahasiswa        empiris       kolaborasi dan kecakapan   di konteks voka-sional
                                          vokasi Indonesia            kuantitatif   kerja lulusan vokasi       Indone-sia

                                                                                                                                            13


---

                                                                           Google Colab dan Kaggle
5.   Han et al. [17]      2022   Sistem pelatihan online     Pengembang                                Justifikasi pemilihan
                                 ML berbasis Jupyter         sistem        Layak dimanfaatkan          Google Colab dan Kaggle
                                 Notebook                                  namun memerlukan            sebagai tools workshop
                                                                           penyesuaian untuk
                                                                           konteks pendidikan
                                 Modul interaktif berbasis                 Modul berbasis data nyata
6.   Suthar et al. [10]   2021                               Pengembang                                Pendekatan desain modul
                                 data     nyata     untuk    modul dan     meningkatkan                workshop berbasis data
                                 pendidikan data science     studi kasus   keterlibatan dan            nyata
                                                                           pemahaman mahasiswa
                                                                           secara praktis

7.   Perez et al. [12]    2025   Inovasi kurikulum dan       Studi kasus   Konten digital modular      Konteks lokal Indonesia
                                 pembelajaran berbasis       kualitatif    dan PjBL meningkatkan       untuk penguatan
                                 teknologi di SMK                          kompetensi digital siswa    kompetensi digital siswa
                                 Indonesia                                 SMK secara signifikan       SMK




                                                                                                                                  14


---

       3.7    Posisi dan Kebaruan Penelitian

              Berdasarkan kajian terhadap penelitian terdahulu, dapat diidentifikasi
       beberapa celah yang belum terjawab oleh literatur yang ada. Penelitian-penelitian
       tentang CNN dan dataset PlantVillage pada umumnya berpusat pada optimasi
       performa model dalam konteks riset, tanpa mempertimbangkan bagaimana teknologi
       tersebut dapat ditransferkan kepada peserta didik di tingkat menengah yang baru
       mengenal konsep kecerdasan buatan. Di sisi lain, kajian-kajian tentang PjBL di
       SMK masih terbatas pada domain keterampilan teknis umum dan belum menyentuh
       ranah machine learning maupun computer vision secara langsung. Inisiatif
       pengajaran ML di lembaga vokasional yang telah terdokumentasi dengan baik,
       seperti proyek VALENCE di Eropa yang diulas oleh Nadzinski et al. [9], belum
       diadaptasi ke dalam konteks Indonesia dengan studi kasus yang relevan secara
       lokal.

              Kebaruan program PKM ini terletak pada perpaduan tiga elemen yang
       belum pernah disatukan dalam satu program pelatihan SMK di Indonesia secara
       bersamaan. Elemen pertama adalah pendekatan PjBL yang terstruktur dan telah
       terbukti efektif di konteks vokasional Indonesia. Elemen kedua adalah studi kasus
       machi-ne learning terapan berbasis computer vision dengan konteks pertanian lokal,
       yaitu deteksi penyakit tanaman melalui analisis citra daun menggunakan dataset
       PlantVillage. Elemen ketiga adalah pemanfaatan ekosistem tools berbasis cloud
       yang sepenuhnya gratis dan dapat direplikasi secara mandiri oleh peserta setelah
       workshop berakhir, sehingga dampak pembelajaran tidak berhenti pada hari
       pelaksanaan semata. Program ini secara strategis menjembatani kesenjangan antara
       kemampuan pemrograman dasar yang sudah dimiliki siswa RPL dengan kompetensi
       kecerdasan buatan yang semakin dibutuhkan industri teknologi digital.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026       15


---

                                          BAB IV
                                    METODE PELAKSANAAN
                  Metode pelaksanaan pada kegiatan Pengabdian kepada Masyarakat ini
       dirancang secara sistematis dengan pendekatan Project-Based Learning (PjBL) yang
       menekankan pembelajaran aktif dan praktik langsung dalam implementasi Machine
       Learning dan Computer Vision. Kegiatan workshop difokuskan pada pengembangan
       kemampuan peserta dalam memahami alur kerja Machine Learning mulai dari
       pengenalan konsep dasar, eksplorasi dataset, pelatihan model klasifikasi citra, hingga
       implementasi aplikasi prediksi sederhana berbasis web menggunakan Google Colab dan
       Streamlit. Pelaksanaan kegiatan disusun sesuai dengan kebutuhan mitra dan karakteristik
       pembelajaran vokasional pada bidang Rekayasa Perangkat Lunak sehingga peserta
       diharapkan tidak hanya memahami materi secara teoritis, tetapi juga mampu
       menghasilkan mini project berbasis Artificial Intelligence sebagai bentuk implementasi
       pembelajaran secara langsung.

       4.1    Tahapan Solusi
              a) Persiapan Teknis
                  Meliputi koordinasi dengan pihak sekolah, persiapan modul pelatihan,
                  konfigurasi Google Colab, persiapan dataset PlantVillage dari Kaggle, serta
                  pengecekan perangkat dan koneksi internet yang digunakan selama workshop
                  berlangsung.
              b) Pengenalan Konsep Machine Learning dan Computer Vision
                  Peserta diperkenalkan pada konsep dasar Artificial Intelligence, Machine
                  Learning,       supervised       learning,     Computer        Vision,   serta   penggunaan
                  Convolutional Neural Network (CNN) dalam klasifikasi citra daun tanaman.
              c) Eksplorasi Dataset dan Praproses Data
                  Peserta mempelajari struktur dataset citra daun tanaman, proses labeling data,
                  resizing gambar, pembagian data training dan testing, serta tahapan praproses
                  data sebelum model dilatih.
              d) Pelatihan Model Klasifikasi Citra
                  Peserta melakukan praktik pelatihan model Machine Learning menggunakan
                  Google Colab untuk melakukan klasifikasi citra daun tanaman serta memahami
                  proses evaluasi hasil prediksi model.

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                      16


---

              e) Pengembangan Mini Project dan Aplikasi Sederhana
                  Peserta secara berkelompok mengembangkan mini project berupa aplikasi
                  prediksi sederhana berbasis Streamlit yang dapat menerima input gambar daun
                  dan menampilkan hasil prediksi kondisi tanaman.
              f) Evaluasi dan Refleksi
                  Evaluasi dilakukan melalui pre-test dan post-test, presentasi hasil mini project,
                  observasi keterlibatan peserta, serta pengisian kuesioner untuk mengetahui
                  efektivitas pelaksanaan workshop dan tingkat pemahaman peserta terhadap
                  materi yang diberikan.

       4.2    Metode Pendekatan
                  Metode pendekatan yang digunakan dalam kegiatan Pengabdian kepada
              Masyarakat ini adalah pendekatan Project-Based Learning (PjBL) yang dipadukan
              dengan metode tutorial terbimbing dan praktik langsung (hands-on practice).
              Pendekatan ini dipilih agar peserta tidak hanya memahami konsep dasar Machine
              Learning secara teoritis, tetapi juga memperoleh pengalaman praktik dalam
              membangun model klasifikasi citra dan aplikasi sederhana berbasis Machine
              Learning.
                  Dalam pelaksanaannya, peserta dibimbing secara bertahap mulai dari
              pengenalan konsep Artificial Intelligence, eksplorasi dataset, praproses data,
              pelatihan model, hingga implementasi aplikasi prediksi sederhana menggunakan
              Google Colab dan Streamlit. Seluruh proses pembelajaran dilakukan secara
              interaktif dengan studi kasus klasifikasi citra daun tanaman agar materi lebih mudah
              dipahami dan relevan dengan kebutuhan pembelajaran vokasional. Metode
              pendekatan yang diterapkan pada kegiatan workshop ini meliputi:
              a) Project-Based Learning (PjBL)
                  Peserta belajar melalui pengembangan mini project secara berkelompok
                  sehingga dapat memahami penerapan Machine Learning melalui penyelesaian
                  studi kasus nyata secara langsung.
              b) Tutorial Terbimbing
                  Fasilitator memberikan pendampingan secara bertahap selama proses praktik
                  untuk membantu peserta memahami penggunaan Google Colab, dataset,
                  pelatihan model, dan implementasi aplikasi sederhana.

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026           17


---

              c) Praktik Langsung (Hands-on Practice)
                  Peserta melakukan praktik secara langsung mulai dari eksplorasi dataset,
                  praproses citra, training model, hingga pengembangan aplikasi prediksi berbasis
                  Streamlit.
              d) Diskusi dan Tanya Jawab
                  Peserta diberikan kesempatan untuk berdiskusi dan menyampaikan kendala
                  selama workshop berlangsung sehingga proses pembelajaran menjadi lebih
                  interaktif dan komunikatif.
              e) Presentasi Mini Project
                  Setiap kelompok mempresentasikan hasil mini project yang telah dikembangkan
                  sebagai bentuk evaluasi pemahaman peserta terhadap materi workshop.

       4.3    Partisipasi Mitra
                  Mitra dalam kegiatan Pengabdian kepada Masyarakat ini adalah SMKN 2
              Cimahi, khususnya Jurusan Rekayasa Perangkat Lunak, yang berperan aktif dalam
              mendukung seluruh rangkaian pelaksanaan workshop. Partisipasi mitra dilakukan
              sejak tahap persiapan kegiatan, pelaksanaan workshop, hingga proses evaluasi
              program agar kegiatan dapat berjalan secara efektif dan sesuai dengan kebutuhan
              peserta didik. Bentuk partisipasi mitra dalam kegiatan ini meliputi:
              a) Penyediaan Peserta Workshop
                  Pihak sekolah membantu dalam proses penentuan dan koordinasi peserta
                  workshop yang berasal dari siswa Jurusan Rekayasa Perangkat Lunak sesuai
                  dengan target kegiatan yang telah direncanakan.
              b) Penyediaan Sarana dan Prasarana
                  Mitra menyediakan fasilitas pendukung pelaksanaan kegiatan seperti ruang
                  laboratorium komputer, akses internet, LCD proyektor, serta perangkat
                  pendukung lainnya yang digunakan selama workshop berlangsung.
              c) Koordinasi Pelaksanaan Kegiatan
                  Pihak sekolah membantu koordinasi jadwal pelaksanaan workshop agar
                  kegiatan dapat disesuaikan dengan aktivitas pembelajaran di sekolah dan tidak
                  mengganggu kegiatan akademik peserta.
              d) Pendampingan Selama Kegiatan
                  Guru pendamping dari pihak sekolah turut membantu proses pendampingan
                  peserta selama workshop berlangsung, terutama dalam menjaga keterlibatan dan
Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026         18


---

                  kedisiplinan peserta pada setiap sesi pelatihan.
              e) Dukungan Evaluasi dan Tindak Lanjut
                  Mitra membantu pelaksanaan evaluasi kegiatan melalui koordinasi pengisian
                  kuesioner, dokumentasi kegiatan, serta pemanfaatan modul dan bahan ajar
                  workshop sebagai referensi pembelajaran lanjutan di lingkungan sekolah.

                  Melalui partisipasi aktif dari pihak mitra tersebut, kegiatan workshop diharapkan
              dapat terlaksana secara optimal dan memberikan manfaat berkelanjutan bagi
              peningkatan kompetensi digital siswa di bidang Machine Learning dan Computer
              Vision.

       4.4    Evaluasi dan Keberlanjutan Program
                  Evaluasi program dilakukan untuk mengetahui tingkat keberhasilan pelaksanaan
              workshop serta mengukur peningkatan pemahaman peserta terhadap materi
              Machine Learning dan Computer Vision yang telah diberikan. Proses evaluasi
              dilakukan secara bertahap mulai dari sebelum pelaksanaan kegiatan, selama proses
              workshop berlangsung, hingga setelah kegiatan selesai dilaksanakan.
                  Evaluasi kegiatan dilakukan menggunakan beberapa metode, yaitu pre-test dan
              post-test, observasi keterlibatan peserta, penilaian mini project kelompok, serta
              penyebaran kuesioner kepuasan peserta. Pre-test dan post-test digunakan untuk
              mengukur peningkatan pemahaman peserta terhadap konsep dasar Machine
              Learning, Computer Vision, dan implementasi model klasifikasi citra daun
              tanaman. Observasi dilakukan selama workshop berlangsung untuk melihat tingkat
              partisipasi, kemampuan kerja sama kelompok, serta keterlibatan peserta dalam
              praktik langsung menggunakan Google Colab dan Streamlit.
                  Selain itu, hasil mini project kelompok juga digunakan sebagai indikator
              keberhasilan pembelajaran berbasis proyek. Melalui mini project tersebut, peserta
              diharapkan mampu memahami alur kerja Machine Learning secara end-to-end
              mulai dari eksplorasi dataset hingga implementasi aplikasi prediksi sederhana.
              Tabel 2 berikut menunjukkan indikator evaluasi kegiatan workshop yang digunakan
              dalam program PKM ini.


                             Tabel 4. 1 Indikator Evaluasi Program PKM


Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026           19


---

                 No      Aspek Evaluasi                             Indikator Keberhasilan

                 1      Pemahaman                 Terjadi peningkatan nilai post-test dibandingkan pre-
                        peserta                   test

                 2      Keterampilan              Peserta mampu menjalankan pelatihan model dan
                        praktik                   implementasi aplikasi sederhana

                 3      Mini           project Kelompok mampu menyelesaikan mini project
                        kelompok                  klasifikasi citra daun

                 4      Partisipasi peserta       Peserta aktif mengikuti diskusi dan praktik workshop

                 5      Kepuasan peserta          Peserta      memberikan         respon   positif   terhadap
                                                  pelaksanaan workshop

                  Keberlanjutan program diarahkan agar hasil kegiatan tidak berhenti pada
              pelaksanaan workshop saja, tetapi dapat dimanfaatkan kembali oleh pihak sekolah
              dan peserta setelah program selesai dilaksanakan. Modul pembelajaran, notebook
              Google Colab, dataset, serta aplikasi sederhana berbasis Streamlit yang digunakan
              selama workshop akan diberikan kepada pihak sekolah sebagai bahan ajar
              tambahan dan media pembelajaran mandiri bagi siswa.
                  Selain itu, mini project yang dihasilkan peserta diharapkan dapat menjadi
              portofolio awal dalam bidang Artificial Intelligence dan Machine Learning yang
              dapat digunakan untuk mendukung kesiapan magang, dunia kerja, maupun studi
              lanjut di bidang teknologi informasi. Dengan adanya pendekatan berbasis project
              dan penggunaan tools berbasis cloud yang mudah diakses, siswa juga diharapkan
              mampu melanjutkan proses eksplorasi dan pengembangan project Machine
              Learning secara mandiri setelah kegiatan workshop selesai dilaksanakan.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                      20


---

                                            BAB V
                                    BIAYA DAN JADWAL PKM

         5.1        Anggaran Biaya
              Anggaran pelaksanaan kegiatan Pengabdian Kepada Masyarakat (PkM) ini
         dirancang untuk mendukung kegiatan selama enam bulan penuh. Anggaran difokuskan
         pada kebutuhan pelatihan, operasional teknis, transportasi, serta publikasi hasil
         kegiatan. Rincian anggaran kegiatan PkM ditunjukkan pada Tabel 5.1 berikut:

                                        Tabel 5. 1 Anggaran Biaya

          No        Jenis Pengeluaran                                  Biaya yang Diusulkan (Rp)
          1         Honorarium                                         Rp 1.875.000,00
          2         Biaya Habis Pakai                                  Rp 1.875.000,00
          3         Perjalanan                                         Rp 1.125.000,00
          4         Lain-lain (Publikasi, Dokumentasi)                 Rp 2.125.000,00
                                        Total Usulan Anggaran Rp.7.000.000,00


         5.2        Jadwal Kegiatan
              Jadwal kegiatan PkM dirancang selama 6 bulan dimulai dari bulan Juli hingga
         Desember, yang mencakup tahap persiapan, pelaksanaan, dokumentasi, dan
         penyusunan laporan. Rincian kegiatan dapat dilihat pada Tabel 5.2 berikut:

                                             Tabel 5. 2 Jadwal Kegiatan
              No         Nama Kegiatan               Jul      Agt        Sep       Okt   Nov   Des
               1.     Survei Awal                    â—      â—
                      Studi Literatur                â—      â—
                      Studi Pendahuluan              â—      â—
                      Identifikasi Masalah                  â—
                      Penentuan Solusi                      â—
                      Mitra
                      Pengumpulan Data                                 â—
                      Lapangan
               2.     Pelaksanaan Workshop                             â—          â—

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                21


---

                     Machine Learning
             3.      Dokumentasi                                                  â—
             4.      Pengolahan Data                                                    â—
                     Analisis Data                                                      â—
                     Kesimpulan dan Saran                                                   â—
                     Publikasi                                                              â—




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026           22


---

                                          DAFTAR PUSTAKA
[1]    Tofan Dwi Tjahyono, Kustiyowati, and Eges Triwahyuni, â€œUsing Gemini AI on the
       Interest and Learning Outcomes of Computer and Network Engineering Students
       in Vocational High Schools,â€ JST (Jurnal Sains dan Teknologi), vol. 14, no. 2, pp.
       370â€“378, 2025, doi: 10.23887/jst-undiksha.v14i2.102807.

[2]    S. Wardoyo et al., â€œPengaruh Transformasi Digital Terhadap,â€ JITET (Jurnal
       Informatika dan Teknik Elektro Terapan), vol. 13, no. 1, 2025, doi:
       https://doi.org/10.23960/jitet.v13i1.5669.

[3]    A. D. Hastutiningsih, sugiyono sugiyono, suyanto suyanto, and vezir ashyrnepesov,
       â€œEvaluation of Vocational Education Management in the Era of the Fourth
       Industrial Revolution and Society 5.0 at SMKN 2 Pengasih,â€ Jurnal Pendidikan
       Teknologi dan Kejuruan, vol. 30, no. 1, pp. 51â€“61, May 2024, doi:
       10.21831/jptk.v30i1.70013.

[4]    S. F. PANE et al., â€œIMPROVING WEB PROGRAMMING COMPETENCE
       THROUGH LARAVEL,â€ ULBI Community Service Publication Media, vol. 7, no.
       1, pp. 47â€“53, 2025, doi: https://doi.org/10.36618/merpati.v7i1.4520.

[5]    Y. Wahyudi, Ana, I. Widiaty, and C. Yulia, â€œIdentifikasi Pendekatan Project Based
       Learning dalam Konteks Pembelajaran di Pendidikan Vokasional: Analisis
       Bibliometrik,â€ Jurnal Penelitian Pendidikan (JPP), vol. 24, no. 3, pp. 421â€“451,
       2024,                              [Online].                           Available:
       https://ejournal.upi.edu/index.php/JER/article/view/80405

[6]    Marwan Ramdhany Edy, Muh. Ihsan Zulfikar, Nurfauziah, Putri Nirmala, and
       Nurrahmah Agusnaya, â€œTransformasi Pembelajaran Vokasi Pertanian melalui
       Integrasi IoT dan Computer Vision pada Smart Greenhouse di SMKN 4 Barru,â€
       Jurnal Pengabdian Masyarakat dan Riset Pendidikan, vol. 4, no. 2, pp. 11622â€“
       11630, 2025, doi: 10.31004/jerkin.v4i2.3765.

[7]    Triana Dewi Salma and Amat Basri, â€œLeveraging Artificial Intelligence for
       Creativity Development in Visual Communication Design at SMKN 5 Kota
       Tangerang,â€ KRESNA: Jurnal Riset dan Pengabdian Masyarakat, vol. 5, no. 1, pp.
       115â€“122, 2025, doi: 10.36080/kresna.v5i1.194.

[8]    Riki Satia Muharam, Ufa Anita Afrilia, and S. Sudarma, â€œRevitalisasi Pendidikan
       Vokasi Berbasis Kebutuhan Industri 4.0: Implikasi Kebijakan Pendidikan di Daerah
       Sub-Urban,â€ DIAJAR: Jurnal Pendidikan dan Pembelajaran, vol. 4, no. 3, pp. 425â€“
       436, 2025, doi: 10.54259/diajar.v4i3.4440.

[9]    G. Nadzinski et al., â€œData Science and Machine Learning Teaching Practices with
       Focus on Vocational Education and Training,â€ Informatics in Education, vol. 22,
       no. 4, pp. 671â€“690, 2023, doi: 10.15388/infedu.2023.28.

[10] K. Suthar et al., â€œReal Data and Application-based Interactive Modules for Data
     Science Education in Engineering,â€ ASEE Annual Conference and Exposition,
     Conference Proceedings, 2021, doi: 10.18260/1-2--37640.

Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026       23


---

[11] D. O. Obada et al., â€œTeaching Basic Concepts in Machine Learning to Engineering
     Students: A Hands-on Approach,â€ ASEE Annual Conference and Exposition,
     Conference Proceedings, 2024, doi: 10.18260/1-2--48058.

[12] C. Perez, F. N. Khasanah, Y. Ismiyanti, and H. Herman, â€œCurriculum Innovation
     and Technology Based Learning for Digital Skills in Vocational Education,â€ Jurnal
     MENTARI: Manajemen, Pendidikan dan Teknologi Informasi, vol. 4, no. 1, pp. 94â€“
     104, 2025, doi: 10.33050/mentari.v4i1.904.

[13] J. Lu, L. Tan, and H. Jiang, â€œReview on convolutional neural network (CNN)
     applied to plant leaf disease classification,â€ Agriculture (Switzerland), vol. 11, no.
     8, pp. 1â€“18, 2021, doi: 10.3390/agriculture11080707.

[14] David. P. Hughes and M. Salathe, â€œAn open access repository of images on plant
     health to enable the development of mobile disease diagnostics,â€ 2015, [Online].
     Available: http://arxiv.org/abs/1511.08060

[15] T. Megayanti, T. Busono, and J. Maknun, â€œProject-based learning efficacy in
     vocational education: Literature review,â€ IOP Conf. Ser. Mater. Sci. Eng., vol. 830,
     no. 4, 2020, doi: 10.1088/1757-899X/830/4/042075.

[16] A. Handayani, W. K. Wienanda, and W. Winarto, Project-based Learning to
     Develop the 21st-century Skills for Vocational College Students, vol. 2025, no. Irole
     2025. Atlantis Press SARL, 2026. doi: 10.2991/978-2-38476-563-8.

[17] S. Han, W. Li, E. Zhang, J. Shi, W. Wang, and X. Lu, MLadder: An Online Training
     System for Machine Learning and Data Science Education, vol. 1, no. 1.
     Association for Computing Machinery, 2022. doi: 10.1145/3511808.3557201.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026         24


---

                                                 LAMPIRAN

Lampiran 1 Biodata Ketua dan Anggota
A. Identitas Diri Ketua
  1      Nama Lengkap (dengan gelar)             Dr. Syafrial Fachri Pane, S.T., M.TI., EBDP., CDSP., SFPC
  2      Jenis Kelamin                           Laki-laki
  3      Jabatan Fungsional                      Lektor
  4      NIP/NIK/NIDN                            117.88.233 / 0416048803
  5      Tempat dan Tanggal Lahir                Medan, 16 April 1988
  6      E-mail                                  syafrial.fachri@ulbi.ac.id
  7      Nomor Telepon/HP                        085362383988
  8      Alamat Kantor                           Universitas Logistik dan Bisnis Internasional, Jln. Sari Asih No.
                                                 54, Bandung
  9      Nomor Telepon/Faks Kantor               Tlp. 022-2009570 / Fax. 022-2009568
  10     Mata Kuliah yang Diampu                 1. Database / Basis Data I & II
                                                 2. DSS (Decision Support System)
                                                 3. Big Data
                                                 4. Data Science
                                                 5. Machine Learning
                                                 6. Metaheuristic Multi-Objektif Optimalisasi
                                                 7. Metodologi Penelitian
                                                 8. Probabilitas Statistik



B. Riwayat Pendidikan
                               D-3                    S-1                   S-2                  S-3
  Nama Perguruan               Politeknik Pos         Universitas           Universitas Bina     Telkom University
  Tinggi                       Indonesia              Pasundan              Nusantara
  Bidang Ilmu                  Teknik                 Teknik                Teknik Informatika   Teknik Informatika
                               Informatika            Informatika
  Tahun Lulus                  2009                   2013                  2017                 2026



C. Rekam Jejak Tri Dharma PT
1. Pendidikan/Pengajaran
  No     Nama Mata Kuliah                                                       Wajib/Pilihan           SKS
  1      Basis Data I / Database I                                              Wajib                   3




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       25


---

  2      Basis Data II / Database II                                            Wajib                      3
  3      DSS (Decision Support System) / Sistem Pendukung                       Wajib                      3
         Keputusan
  4      Big Data                                                               Wajib                      3
  5      Data Science                                                           Wajib                      3
  6      Machine Learning                                                       Wajib                      3
  7      Metaheuristic Multi-Objektif Optimalisasi                              Wajib                      3
  8      Metodologi Penelitian                                                  Wajib                      2
  9      Probabilitas Statistik                                                 Wajib                      3
  10     Fundamental SAP / Manajemen Accounting II berbasis                     Pilihan                    3
         SAP
  11     Matematika Diskrit                                                     Wajib                      3
  12     Database + Praktek                                                     Wajib                      4

2. Penelitian
  No Judul Penelitian                                                        Peran        Lembaga              Tahun
  1     Perancangan Sistem Penerimaan Mahasiswa Baru                         Ketua        Politeknik Pos       2014
        Berbasis Website                                                                  Indonesia
  2     Analisis Kinerja Proses Bisnis dengan Pendekatan                     Anggota Politeknik Pos            2015
        BPMN Menggunakan Bizagi                                                      Indonesia
  3     Mengevaluasi Pengelolaan dan Perencanaan Investasi TI                Ketua        Politeknik Pos       2016
        dari Sumber Dana Hibah Pemerintah Menggunakan                                     Indonesia
        COBIT 5
  4     Prototype RFID Conveyor Belt pada Warehouse                          Anggota Politeknik Pos            2018
        Management System Berbasis IoT                                               Indonesia
  5     Implementasi Middleware pada Evomo dengan Metode                     Ketua        Politeknik Pos       2021
        Web Service Restfull dan Pengujian CI/CD, Coverage                                Indonesia
        serta Simulasi Protokol Grafana
  6     Analisa Warehouse Management System di Center of                     Anggota Politeknik Pos            2021
        Technology                                                                   Indonesia
  7     Pemodelan Berbasis Data untuk Memprediksi Gaji                       Ketua        Politeknik Pos       2022
        Berdasarkan Faktor-Faktor Spesifik dengan Pendekatan                              Indonesia
        Machine Learning
  8     Pemodelan Berbasis Data untuk Memprediksi Durasi                     Anggota Politeknik Pos            2022
        dan Perkiraan Risiko Keterlambatan Pengiriman Barang                         Indonesia
        Menggunakan Machine Learning
  9     Pemodelan Berbasis Data untuk Penentuan Regional                     Ketua        ULBI                 2023
        Best Pricing di PT. Pos Indonesia dengan Pendekatan




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                          26


---

        Machine Learning
  10    Greedy Algorithm untuk Menyelesaikan Storage                         Anggota ULBI                     2024
        Location Assignment Problem (SLAP) dengan
        Dedicated Storage
  11    Analisis Pengaruh PDB per Kapita terhadap Kepuasan                   Ketua      ULBI                  2024
        Hidup di Indonesia dengan Pendekatan Machine
        Learning
  12    Perancangan Aplikasi E-Recruitment Beasiswa                          Anggota Politeknik Pos           2017
        Mahasiswa Kurang Mampu dengan Teknologi                                      Indonesia (Dikti)
        Geospatial Intelligence dan Webservice (OAUTH)
        Metode Electre
  13    PROFIT-WMS: Prototype RFID Conveyor Belt pada                        Ketua      Politeknik Pos        2018
        Warehouse Management System Berbasis IoT                                        Indonesia (Dikti)
  14    Simulasi Auto Turn Sign Pengantar Pos Menggunakan                    Anggota Politeknik Pos           2019
        Aktivitas Gelombang Otak dengan Metode Bayesian                              Indonesia (Dikti)
        Learning dan Logistic Regression
  15    Perancangan Simulasi Warehouse Management System                     Ketua      Politeknik Pos        2019
        (WMS) Berbasis Internet of Things pada Center of                                Indonesia (Dikti)
        Technology
  16    Straglog: Analisis Strategi Pengadaan Barang dan Jasa                Ketua      Politeknik Pos        2020
        Menggunakan Algoritma Heuristic Miner                                           Indonesia (Dikti)

3. Pengabdian Kepada Masyarakat
  No Judul Pengabdian Kepada Masyarakat                                          Lembaga/Mitra         Tahun
  1     Pelatihan Penyusunan Proposal Penelitian Tindakan Kelas                  SD Panorama           2015
                                                                                 Bandung
  2     Pelatihan Penyusunan Laporan Penelitian Tindakan Kelas                   SD Panorama           2016
                                                                                 Bandung
  3     Pelatihan Publikasi Penelitian Tindakan Kelas                            SD Panorama           2017
                                                                                 Bandung
  4     Pelatihan Tata Cara Pengajuan Perubahan Peta Desa                        Desa Wangunharja,     2019
        Wangunharja di Google Map                                                Lembang
  5     Penyuluhan Mitigasi Satgas Bencana Virus Corona                          Kelurahan Sarijadi,   2020
        (COVID-19) di Kelurahan Sarijadi                                         Kota Bandung
  6     Sosialisasi Penggunaan SIAP OPA                                          â€“                     2021
  7     Implementasi logware untuk Meningkatkan Pemahaman      Sumedang, Jawa                          2023
        Optimasi Rantai Pasok pada Siswa SMK Logistik Sumedang Barat
  8     Peningkatan Kompetensi Pemrograman Web melalui                           SMK Negeri 2          2025
        Workshop Bootcamp Laravel bagi Siswa SMK                                 Cimahi, Jawa Barat
        Negeri/Swasta di Kota Cimahi




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                         27


---

4. Publikasi Artikel Ilmiah dalam Jurnal
  No Judul Artikel                                                  Nama Jurnal / Prosiding          Tahun
  1     Qualitative Evaluation of RFID Implementation               Telkomnika Vol.16 No.3 â€“         2018
        on Warehouse Management System                              Scopus (Dikti A)
  2     K Means Clustering and Meanshift Analysis for               Telkomnika Vol.16 No.3 â€“         2018
        Grouping the Data of Coal Term in Puslitbang                Scopus (Dikti A)
        tekMIRA
  3     Sireuboh â€“ Klasifikasi Data Lokasi Barang                   Tekno Insentif LLDIKTI IV        2018
        Menggunakan Region of Interest (ROI) dan
        Algoritma RANSAC
  4     Implementation of Web Scraping on Github Task               Telkomnika Vol.17 No.1 â€“         2019
        Monitoring System                                           Scopus (Dikti A)
  5     Ontology Design of Family Planning Field                    Telkomnika Vol.17 No.1 â€“         2019
        Officer Using OWL and RDF                                   Scopus (Dikti A)
  6     RFID-based Conveyor Belt for Improve                        Telkomnika Vol.17 No.2 â€“         2019
        Warehouse Operations                                        Scopus (Dikti A)
  7     Implementasi Algoritma Genetika untuk                       Tekno Insentif LLDIKTI IV        2019
        Optimalisasi Pelayanan Kependudukan                         (Terindeks DOAI)
  8     Collaboration FMADM and K-Means Clustering EMITTER International Journal                     2019
        to Determine the Activity Proposal in Operational of Engineering Technology â€“
        Management Activity                               Scopus
  9     Implementasi Algoritma Genetika untuk                       Tekno Insentif 13(2): 36-43      2019
        Optimalisasi Pelayanan Kependudukan
  10    MILA: Low-cost BCI Framework for Acquiring                  Telkomnika 18(2): 846-852        2020
        EEG Data with IoT
  11    OVMP: Operational Vehicle Management                        Tekno Insentif 14(1): 9-16       2020
        Application Using Extreme Programming (XP)
        Method
  12    Sistem Informasi Absensi Pegawai Menggunakan Media Informatika Budidarma                     2020
        Metode RAD dan LBS pada Koordinat Absensi    4(1): 59-64
  13    AMCF: A Novel Archive Modeling Based on                     Technomedia Journal 4(2): 139-   2020
        Data Cluster and Filtering                                  152
  14    Analisa Profit dan Loss pada Sistem Manajemen               Jurnal SITECH: Sistem            2021
        Aset Menggunakan Algoritma Multiple Linear                  Informasi dan Teknologi
        Regression
  15    Studi Komparasi Metode Entropy dan ROC                      Tekno Insentif 15(1): 1-14       2021
        dalam Menentukan Bobot Kriteria
  16    Mapping Log Data Activity Using Heuristic                   Telkomnika Vol.19 No.4 â€“         2021




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                   28


---

        Miner Algorithm in Manufacture and Logistics                Scopus Q3 (Dikti A)
        Company
  17    Implementasi Middleware pada Evomo dengan                   Tekno Insentif 15(2): 110-121 â€“    2021
        Metode Web Service Restfull dan Pengujian                   Sinta 3
        CI/CD, Coverage serta Simulasi Protokol
        Grafana
  18    Cryptography: Perancangan Middleware Web                    Tekno Insentif 15(2): 65-75 â€“      2021
        Service Encryptor menggunakan Triple Key                    Sinta 3
        MD5, Base64, dan AES
  19    Prediksi Jumlah Penjualan Rumah di                          Media Informatika Budidarma        2021
        Bojongsoang ditengah Pandemi Covid-19 dengan                5(4): 1479-1487 â€“ Sinta 3
        Metode ARIMA
  20    Analisis Sentimen UU Omnibus Law pada                       InComTech: Jurnal                  2021
        Twitter Menggunakan Metode Support Vector                   Telekomunikasi dan Komputer
        Machine                                                     11(2): 130-142 â€“ Sinta 3
  21    Meningkatkan Akurasi Long-Short Term                        Jurnal Telematika 16(2): 85-90     2021
        Memory (LSTM) pada Analisis Sentimen Vaksin
        Covid-19 di Twitter dengan GloVe
  22    Multi-Temporal Factors to Analyze Indonesian                ICAITI 2021 â€“ Scopus IEEE          2021
        Government Policies regarding Restrictions on
        Community Activities during COVID-19
        Pandemic
  23    Pemodelan Machine Learning: Analisis Sentimen               Jurnal Sistem Cerdas 5(1): 12-20   2022
        Masyarakat Terhadap Kebijakan PPKM                          â€“ Sinta 3
        Menggunakan Data Twitter
  24    Analisis Ketercapaian Vaksinasi Terhadap                    Jurnal Terakreditasi Sinta 3       2022
        Penyebaran COVID-19 Menggunakan Machine
        Learning
  25    Komparasi Model Klasifikasi NaÃ¯ve Bayes dan                 Jurnal Informatika Upgris          2022
        C4.5 pada Data Prestasi Kerja PNS
  26    GRU-MF: A Novel Appliance Classification                    COMNETSAT 2022 â€“ Scopus            2022
        Method for Non-Intrusive Load Monitoring Data               IEEE
  27    Reevaluating Synthesizing Sentiment Analysis                ICITSI 2022 â€“ Scopus IEEE          2022
        on COVID-19 Fake News Detection using Spark
        Dataframe
  28    XGBoost for IDS on WSN Cyber Attacks with                   ISESD 2022 â€“ Scopus IEEE           2022
        Imbalanced Data
  29    Autoencoder Image Denoising to Increase OCR                 ICACNIS 2022 â€“ Scopus IEEE         2022
        Performance in Text Conversion
  30    PCA-AdaBoost Method for a Low Bias and Low                  ICACNIS 2022 â€“ Scopus IEEE         2022
        Dimension Toxic Comment Classification




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                     29


---

  31    The Influence of The COVID-19 Pandemics in                  ICIC 2022 â€“ Scopus IEEE          2022
        Indonesia on Predicting Economic Sectors
  32    LSTM and ARIMA for Forecasting COVID-19                     ICIC 2022 â€“ Scopus IEEE          2022
        Positive and Mortality Cases in DKI Jakarta and
        West Java
  33    A PSO-GBR Solution for Association Rule                     ICIC 2022 â€“ Scopus IEEE          2022
        Optimization on Supermarket Sales
  34    A Hybrid CNN-LSTM Model with Word-Emoji                     ICITISEE 2022 â€“ Scopus IEEE      2022
        Embedding for Improving the Twitter Sentiment
        Analysis on Indonesia's PPKM Policy
  35    Non-Academic Factors Analysis Impacting                     ICICyTA 2022 â€“ Scopus IEEE       2022
        Students' Online Learning During COVID-19
        Pandemic in ULBI
  36    TPOT on Increasing the Performance of Credit                ICICyTA 2022 â€“ Scopus IEEE       2022
        Card Application Approval Classification
  37    Implementasi Spelling Corrector untuk                       Jurnal Keilmuan dan Aplikasi     2023
        Mengatasi Typographical Error pada Fitur                    Bidang Teknik
        Pencarian Aplikasi Kamus Istilah Informatika
  38    Pemetaan Profil Mahasiswa untuk Memprediksi                 Petir â€“ Sinta 3                  2023
        Peminatan Mahasiswa
  39    NS-SVM: Bolstering Chicken Egg Harvesting                   JUITA â€“ Sinta 2                  2023
        Prediction with Normalization and
        Standardization
  40    Confirmatory Factor Analysis for The Impact of              ICCoSITE 2023 â€“ Scopus IEEE      2023
        Students' Social Media on University Digital
        Marketing
  41    Systematic Literature Review: Analisa Sentimen              Journal of Applied Computer      2023
        Masyarakat Terhadap Penerapan Peraturan ETLE                Science and Technology â€“ Sinta
                                                                    3
  42    Knowledge Distillation for a Lightweight Deep               ISITIA 2023 â€“ Scopus IEEE        2023
        Learning-based Indoor Positioning System on
        Edge Environments
  43    AUC Maximization for Flood Attack Detection                 ICITRI 2023 â€“ Scopus IEEE        2023
        on MQTT with Imbalanced Dataset
  44    Feature Importance on Text Analysis for a Novel             ICoICT 2023 â€“ Scopus IEEE        2023
        Indonesian Movie Recommender System
  45    Deteksi Spam Bot pada Komentar Youtube:                     CSRID â€“ Sinta 3                  2023
        Tinjauan Literatur Sistematis
  46    Predictive Maintenance Application on Machine               COMNETSAT 2023 â€“ Scopus          2023
        Overstrain Failure with Node-RED and Isolation              IEEE
        Forest Anomaly Detection




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                   30


---

  47    Deteksi Emosi pada Teks Berbahasa Indonesia                 JTT (Jurnal Teknologi Terapan)    2024
        Menggunakan Pendekatan Ensemble                             â€“ Sinta 3
  48    Pengaruh Hyperparameter Tuning untuk                        Tekno Insentif â€“ Sinta 3          2024
        Efektivitas pada Pendekatan Hybrid dalam
        Mendiagnosis Stres dan Depresi
  49    Optimizing Search Efficiency in Ordered Data: A             Journal of Dinda â€“ Sinta 4        2025
        Hybrid Approach Using Jump Binary Search
  50    Security Analysis of Two-Factor Authentication              Mobile Forensic â€“ Sinta 3         2025
        Applications: Vulnerabilities in Data Storage and
        Management
  51    Predicting the Happiness Index Based on the HDI NUANSA INFORMATIKA â€“                          2025
        Indicator in Indonesia Using the Ensemble       Sinta 5
        Learning Approach
  52    Enhancing Prediction Accuracy of the Happiness              Journal of Dinda â€“ Sinta 4        2025
        Index Using Multi-Estimator Stacking Regressor
        and Web Application Integration


D. Terbitan Buku
  No Judul Buku                                                 Tahun Jml Hal.            Penerbit / ISBN
  1     Big Data: Classification Behavior                       2020       253            Kreatif / 9786025389795
        Menggunakan Python
  2     Big Data: Forecasting Menggunakan Python                2020       235            Kreatif / 9786239323417
  3     Smart Conveyor pada Outbound dengan                     2020       230            Kreatif / 9786239323424
        Arduino
  4     Membangun Aplikasi Peminjaman Jurnal                    2020       237            Kreatif / 9786237898160
        Menggunakan Oracle Apex Online
  5     Dasar-Dasar OpenCV                                      2020       254            Kreatif / 9786025389740
  6     Oracle Apex For Beginner                                2020       174            Kreatif / 9786237898184
  7     Membuat Aplikasi Pengolahan Data                        2020       239            Kreatif / 9786237898030
        Administrasi Barang Menggunakan Oracle
        Apex Online
  8     Membangun Aplikasi Peminjaman Ruangan                   2020       242            Kreatif / 9786239334130
        Menggunakan Oracle Apex Online
  9     Pengembangan dan Optimalisasi Internet                  2020       â€“              Kreatif / 9786237898924
        Warga Menggunakan Kombinasi Queue
        Type dan Pihole
  10    Algoritma Nasa-TLX untuk Analisa Beban                  2020       â€“              Kreatif / 9786236762028
        Kerja




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       31


---

  11    Algoritma C4.5 dan KNN untuk Memetakan                  2020        â€“               Kreatif / 9786236762035
        Matakuliah dan Keterlambatan Kelulusan
  12    Big Data: Implementasi Hadoop Mapreduce                 2020        â€“               Kreatif / 9786237898771
        pada Pemetaan Sekolah Menggunakan
        Python
  13    Cara Cepat Recruitment Karyawan                         2020        â€“               Kreatif / 9786237898757
        Perbankan Menggunakan Algoritma Naive
        Bayes
  14    Studi Komparasi Metode Entropy dan ROC                  2020        â€“               Kreatif / 9786237898665
        sebagai Penentu Bobot Kriteria SPK
  15    Monograf: Analisis Strategi Pengadaan                   2020        â€“               Kreatif / 9786237898542
        Barang dan Jasa Menggunakan Algoritma
        Heuristic Miner dan Python
  16    Panduan Pembuatan SMART CONVEYOR                        2019        â€“               Kreatif / 9786025389733
  17    Tutorial Pembuatan Prototype Pendeteksi                 2020        â€“               Kreatif / 9786237898986
        Kebakaran (FIDO) Berbasis IoT Metode
        Naive Bayes
  18    Pengembangan Smart Conveyor pada                        2020        â€“               Kreatif / 9786237898382
        Tracking Barang Berbasis IoT
  19    Pengembangan Smart Conveyor dengan                      2023        â€“               Buku Pedia /
        Arduino (GPS Tracking Berbasis Android)                                             9786230906886
  20    Analisis Hubungan Harga Bahan Bakar                     2023        134             Buku Pedia /
        Terhadap Bahan Pangan Menggunakan                                                   9786230929984
        GARCH
  21    Analisis Sentimen Masyarakat Terhadap                   2023        128             Buku Pedia /
        Kebijakan Polisi Tilang Manual di Indonesia                                         9786230928147
  22    Deteksi Spam Bot pada Komentar Youtube                  2023        142             Buku Pedia /
        Menggunakan Artificial Neural Network                                               9786230928123
        (ANN)
  23    Tutorial Membuat Sistem Informasi                       2023        156             Buku Pedia /
        Pendaftaran Rawat Jalan Klinik                                                      9786238854950
  24    Tutorial Integrasi API dalam Katalog Musik              2023        148             Buku Pedia /
        Online                                                                              9786238854967



E. Sertifikat HAKI
  No Judul/Tema HKI                                                  Tahun Jenis             Nomor P/ID
  1     Program Komputer Game Basic Math                             2019         Program    000171829 /
                                                                                             EC00201991583
  2     Panduan Pembuatan Aplikasi Pengadaan Barang                  2019         Buku       000167859 /




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       32


---

        dan Jasa Menggunakan Algoritma Heuristic                                           EC00201984639
        Miner dengan Python
  3     Panduan Kenaikan Pangkat IRC                                 2019      Buku        000167860 /
                                                                                           EC00201984652
  4     Program Pendidikan Integritas Informatika                    2019      Buku        000167850 /
                                                                                           EC00201984653
  5     Panduan Cara Penggunaan Kepo                                 2019      Program     000167851 /
                                                                                           EC00201984654
  6     Panduan Keahlian Penanganan Error                            2019      Buku        000167852 /
                                                                                           EC00201984665
  7     Algoritma Penentuan Prosedur Pengadaan Barang 2020                     Program     000197773 /
        dan Jasa dengan Pemrograman Python                                                 EC00202026386
  8     Smart Parking Berbasis IoT Menggunakan                       2021      Program     000235266 /
        Raspberry Pi dan Metode OpenCV                                                     EC00202107856
  9     Aplikasi QRcode Scanner Warehouse                            2021      Program     000233837 /
        Management System (WMS)                                                            EC00202106779
  10    Aplikasi Attendance System Based on GPS                      2021      Program     000232332 /
        (ATENG)                                                                            EC00202105731
  11    Aplikasi APEM Speech to Text ke Sistem                       2021      Program     000235265 /
        Akademik                                                                           EC00202107750
  12    Aplikasi MusiCroot                                           2021      Program     000235264 /
                                                                                           EC00202108192



F. Jabatan Struktural
  No Nama Jabatan                                      Tahun              Institusi            Tugas Pokok
  1     Kepala Bidang Kemahasiswaan,                   2018â€“2019          Politeknik Pos       Mengelola kegiatan
        Alumni dan Kerjasama                                              Indonesia            kemahasiswaan dan
                                                                                               kerjasama
  2     Kepala TIK-TUK dan SAP                         2019â€“2021          Politeknik Pos       Mengelola TIK dan
                                                                          Indonesia            TUK
  3     Kabag. Riset dan Layanan Informasi             2019â€“2021          ULBI                 Mengelola riset dan
                                                                                               layanan informasi
  4     Kabag. Riset dan Layanan Informasi             2021â€“2023          ULBI                 Mengelola riset dan
                                                                                               layanan informasi
  5     Manager Riset dan Pengembangan                 2024â€“2026          ULBI                 Mengembangkan
        Sistem Informasi                                                                       sistem informasi
                                                                                               berbasis riset




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                    33


---

G. Penghargaan
  No Nama Penghargaan                                                       Lembaga          Tahun
  1     Dosen Terbaik Tingkat Prodi D4 Teknik Informatika                   Politeknik Pos   2017
                                                                            Indonesia
  2     Dosen Terbaik Tingkat Perguruan Tinggi                              Politeknik Pos   2018
                                                                            Indonesia
  3     Dosen Terbaik Tingkat Perguruan Tinggi                              Politeknik Pos   2019
                                                                            Indonesia
  4     Dosen Terbaik Tingkat Perguruan Tinggi                              Politeknik Pos   2020
                                                                            Indonesia
  5     Dosen Terbaik Score Sinta 3 Tahun Tingkat Universitas ULBI                           2021
  6     Dosen Terbaik Score Sinta 3 Tahun Tingkat Universitas ULBI                           2022
  7     Dosen Terbaik Score Sinta 3 Tahun Tingkat Universitas ULBI                           2023
  8     Dosen Terbaik Score Sinta 3 Tahun Tingkat Universitas ULBI                           2024

H. Seminar Nasional/Internasional
  No Nama Seminar/Konferensi                         Judul Artikel                           Waktu & Tempat
  1     International Conference on                  [Artikel IoT & WMS]                     Medan, 6â€“8 Des 2017
        Mechanical Electronics, Computer
        and Industrial Technology
        (MECnIT)
  2     2nd Scientific Writing Workshop              [Artikel Telkomnika]                    Yogyakarta, 21â€“22 Mar
        on TELKOMNIKA (2nd TEAM                                                              2018
        2018)
  3     International Conference â€“                   An Analysis of Customer                 Batam, 3â€“4 Okt 2018
        Politeknik Negeri Batam                      Agrotourism Resort Behaviour
                                                     based on RFM and Mean Shift
                                                     Clustering
  4     ICAITI 2021 â€“ Scopus IEEE                    Multi-Temporal Factors to Analyze       Lombok, 15 Mar 2022
        (Telkom University, Politeknik               Indonesian Government Policies
        Padang, Mataram)                             during COVID-19 Pandemic



I. Keanggotaan Profesi
  No Nama Keanggotaan                                                         Lembaga                Tahun
  1     Anggota APTIKOM (AP-12.00389)                                         APTIKOM                2026
  2     Anggota IEEE (# 94799707)                                             IEEE                   2018
  3     Anggota Asosiasi Ilmuwan Data Indonesia â€“ AIDI                        AIDI                   2020




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       34


---

         Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan dapat
 dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
 ketidaksesuaian dengan kenyataan, saya sanggup menerima risikonya. Demikian biodata ini
 saya buat dengan sebenarnya


                                                                                   Bandung, Mei 2026
                                                                                       Pengusul,




                                                                        (Dr. Syafrial Fachri Pane, S.T., M.TI.,
                                                                               EBDP., CDSP., SFPC)
                                                                                 NIDN. 0416048803




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                         35


---

Biodata Anggota
A. Identitas Diri
  1      Nama Lengkap (dengan gelar)             Muhammad Yusril Helmi Setyawan, S.Kom., M.Kom.
  2      Jenis Kelamin                           Laki-laki
  3      NIP/NIK/NIDN                            113.74.163 / 0407117405
  4      Sertifikasi Dosen / No. Reg.            15104500910488
         Pendidik
  5      Tempat dan Tanggal Lahir                Rembang, 07 November 1974
  6      E-mail                                  yusrilhelmi@ulbi.ac.id
  7      Nomor Telepon/HP                        085221441761
  8      Alamat Kantor                           Universitas Logistik dan Bisnis Internasional, Jln. Sari Asih No.
                                                 54, Bandung
  9      Nomor Telepon/Faks Kantor               Tlp. 022-2009570 / Fax. 022-2009568
  10     Mata Kuliah yang Diampu                 1. Administrasi Jaringan Komputer
                                                 2. Network Security
                                                 3. Network Programming
                                                 4. Kecerdasan Buatan
                                                 5. Cloud Computing

B. Riwayat Pendidikan
                               D-3                     S-1                      S-2                S-3
  Nama Perguruan               -                       STMIK                    STMIK LIKMI        -
  Tinggi                                               Tasikmalaya
  Bidang Ilmu                  -                       Teknik                   Sistem Informasi   -
                                                       Informatika
  Tahun Lulus                  -                       2006                     2012               -

C. Rekam Jejak Tri Dharma PT
1. Pendidikan/Pengajaran
  No     Nama Mata Kuliah                                                       Wajib/Pilihan            SKS
  1      Administrasi Jaringan Komputer                                         Wajib                    3
  2      Network Security                                                       Wajib                    3
  3      Network Programming                                                    Wajib                    3
  4      Kecerdasan Buatan                                                      Wajib                    3
  5      Cloud Computing                                                        Wajib                    3




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                        36


---

2. Penelitian
  No Judul Penelitian                                                         Peran     Lembaga                 Tahun
  1     Simulasi Interopabilitas IPv4 dan IPv6 pada Perangkat-                Ketua     PDP DIKTI               2018
        Perangkat Jaringan Komputer
  2     Actspot (Activity Tracker on the Internship Spot): Sistem             Ketua     Politeknik Pos          2019
        Identifikasi Kehadiran Mahasiswa Internship melalui                             Indonesia
        Penelusuran Lokasi GPS Ponsel
  3     Penanganan User Typo pada Chatbot Akademik dengan                     Ketua     Politeknik Pos          2019
        Metode Seq2Seq dan Jaro Winkler                                                 Indonesia
  4     Integrasi Pendekatan IDT dan TAM untuk Pengukuran                     Ketua     Politeknik Pos          2021
        Persepsi Manfaat Sistem Informasi di PT. Pos Logistik                           Indonesia
        Indonesia
  5     Optimasi Presensi Praktikan Berbasis GPS dengan Fuzzy                 Ketua     PDP DIKTI               2021
        Logic dan K-Mean
  6     Kombinasi IDT-TAM untuk Analisis Faktor-Faktor yang                   Ketua     Politeknik Pos          2022
        Mempengaruhi Penggunaan Aplikasi Perusahaan                                     Indonesia
  7     Eksperimen Pengembangan Simulasi Visual Interaktif                    Ketua     ULBI                    2024
        sebagai Alat Pembelajaran Operasi Qubit dan Gerbang
        Kuantum
  8     Sistem Cerdas Personalisasi Pembelajaran: Pendekatan                  Ketua     Penelitian Terapan-     2024
        Inklusif untuk Mengoptimalkan Motivasi dan                                      P2V DIKSI
        Keterlibatan Siswa
  9     Motivational Engine Berbasis AI dan Data-Driven                       Ketua     Penelitian              2025
        Gamification untuk Ekosistem Pembelajaran Adaptif                               Fundamental-
                                                                                        Reguler



3. Pengabdian Kepada Masyarakat
  No Judul Pengabdian Kepada Masyarakat                                          Lembaga/Mitra           Tahun
  1     Implementasi Platform Forum Diskusi Online sebagai Media PKMS DIKTI                              2019
        untuk Meningkatkan Kemandirian Pembelajaran di SD
        Negeri Adetex Bandung
  2     Sosialisasi Pencegahan Virus Corona di Kelurahan Sarijadi                Politeknik Pos          2020
                                                                                 Indonesia
  3     Pelatihan Advanced Logistics bagi Pegawai PT. Pos                        Politeknik Pos          2021
        Logistik Indonesia                                                       Indonesia
  4     Pelatihan Dasar Blockchain untuk UMKM                                    Politeknik Pos          2022
                                                                                 Indonesia
  5     Pelatihan Software Development Berbasis No Code                          ULBI                    2024
        Programming




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                           37


---

  6     Simulasi Eksperimen Drone Modular untuk Literasi STEM                    ULBI                   2025
        Digital Natives



4. Publikasi Artikel Ilmiah dalam Jurnal
  No Judul Artikel                                                  Nama Jurnal / Prosiding              Tahun
  1     Ontology Design of Influential People                       Journal of Physics: Conference       2018
        Identification Using Centrality                             Series 1007(1), 012012
  2     Dashboard Settings Design In SVARA Using                    TELKOMNIKA 17(2): 615-619            2019
        User-Centred Design Method
  3     K-Nearest Neighbor Algorithm on Implicit                    TELKOMNIKA 17(3): 1425-              2019
        Feedback to Determine SOP                                   1431
  4     Comparison of Multinomial Naive Bayes                       International Conference on          2018
        Algorithm and Logistic Regression for Intent                Applied Engineering
        Classification in Chatbot                                   (ICAE2018)
  5     KAFA: A Novel Interoperability Open                         TELKOMNIKA 17(2): 712-718            2019
        Framework to Utilize Indonesian Electronic
        Identity Card
  6     KANSA: High Interoperability e-KTP                          TELKOMNIKA 17(3): 1360-              2019
        Decentralised Database Network Using                        1366
        Distributed Hash Table
  7     ActSPOTâ„¢: Smart Monitor Kegiatan Mahasiswa Teknik Informatika 11(3): 8-12                        2019
        Internship Menggunakan Global Positioning
        System
  8     Implementation of AHP and SAW Methods on                    Teknik Informatika 12(3): 6-13       2020
        Decision Support Information System of
        Selection for Fleet of Goods Delivery
  9     Optimasi Presensi Praktikan Berbasis GPS                    JUSTIN (Jurnal Sistem dan            2021
        dengan Fuzzy Logic dan K-Mean                               Teknologi Informasi) 9(2): 108-
                                                                    112
  10    Virtualisasi Kinerja HTTP dan HTTPS pada                    Teknik Informatika 13(3): 10-15      2021
        Video Streaming melalui Tunneling
  11    Studi Komparasi Metode Entropy dan ROC                      Jurnal Tekno Insentif 15(1): 1-14    2021
        dalam Menentukan Bobot Kriteria
  12    Pemanfaatan Learning Management System                      Jurnal INTIMAS 2(1): 18-24           2022
        untuk Pelatihan Advance Freight Management di
        PT. Pos Logistik Indonesia
  13    Menentukan Prioritas Bantuan Keluarga Angkat                JATI 6(2): 578-582                   2022
        dengan Mengukur Tingkat Akurasi Antara
        Metode TOPSIS dan COMET




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                          38


---

  14    Membangun Perspektif Tata Kelola Data                       Merpati 4(1): 21-27                2022
        Mutakhir melalui Pelatihan Blockchain Dasar
        bagi UMKM Kota Bandung
  15    Pemetaan Profil Mahasiswa untuk Memprediksi                 PETIR: Jurnal Pengkajian dan       2023
        Peminatan Mahasiswa                                         Penerapan Teknik Informatika
                                                                    16(1): 1-7
  16    Optimizing Blockchain Network Creation:                     Journal of Informatics and         2023
        Automation with Ansible on Private Blockchain               Telecommunication Engineering
        Hyperledger Fabric Using Simplified RAFT                    7(1): 340-355
        Consensus Method
  17    Rekognisi Huruf Tulisan Tangan Menggunakan                  Jurnal Sistem Cerdas 6(3): 262-    2023
        Convolutional Neural Network                                276
  18    Optimalisasi Jarak Pembacaan Tag RFID                       Jurnal Teknik Informatika 16(2):   2024
        Menggunakan Adaptive Neuro-Fuzzy Inference                  57-62
        System
  19    Analisis Sentimen Terhadap Aplikasi Pospay                  Jurnal Teknologi dan Sistem        2024
        Menggunakan Algoritma Support Vector                        Informasi Bisnis 6(3): 514-521
        Machine dan Naive Bayes
  20    Implementasi Linear Programming pada Model                  JIKA (Jurnal Informatika) 8(4):    2024
        CVRPP untuk Pengelolaan Operasional Logistik                391-401
  21    Peningkatan Literasi Teknologi melalui Pelatihan            MERPATI 6(2): 53-63                2025
        Software Development Berbasis No Code
        Programming



D. Terbitan Buku
  No Judul Buku                                                 Tahun Jml Hal.            Penerbit
  1     Monograf: Pengendalian Anggaran dengan                  2020       51             Kreatif Industri Nusantara
        Metode Fuzzy Logic Sugeno dan Fuzzy
        Logic Mamdani dan Implementasinya pada
        Aplikasi Web
  2     Panduan Lengkap Membangun Sistem                        2020       238            Kreatif Industri Nusantara
        Monitoring Kinerja Mahasiswa Internship
        Berbasis Web dan Global Positioning System
  3     CodeIgniter: Implementasi Metode Entropy                2020       244            Kreatif Industri Nusantara
        pada Pemrograman PHP (Belajar dengan
        Praktek)
  4     Membuat Sistem Informasi Gadai Online                   2020       229            Kreatif Industri Nusantara
        Menggunakan CodeIgniter serta Kelola
        Proses Pemberitahuannya
  5     Seleksi Calon Kelulusan Tepat Waktu                     2020       215            Kreatif Industri Nusantara




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                      39


---

        Mahasiswa Teknik Informatika
        Menggunakan Metode NaÃ¯ve Bayes (edisi 1)
  6     Seleksi Calon Kelulusan Tepat Waktu                     2020       203          Kreatif Industri Nusantara
        Mahasiswa Teknik Informatika
        Menggunakan Metode NaÃ¯ve Bayes (edisi 2)
  7     Memahami Metode OMAX dan                                2020       249          Kreatif Industri Nusantara
        PROMETHEE pada Sistem Pendukung
        Keputusan
  8     Penerapan Metode AHP pada Penilaian                     2020       226          Kreatif Industri Nusantara
        Kepuasan Pelanggan Berdasarkan Pelayanan
        Divisi (CV Tirta Kencana)
  9     Panduan Lengkap Algoritma Haversine                     2020       340          Kreatif Industri Nusantara
        Formula pada Sistem Monitoring Mahasiswa
        Internship Berbasis GPS
  10    Studi Komparasi Metode Entropy dan                      2020       243          Kreatif Industri Nusantara
        Metode ROC sebagai Penentu Bobot Kriteria
        SPK
  11    Pengembangan Dashboard Laporan Bulanan                  2023       69           Buku Pedia
        untuk Monitoring Kinerja Perusahaan


E. Pemakalah Seminar Ilmiah
  No     Nama Temu Ilmiah/                               Judul Artikel Ilmiah                  Waktu
             Seminar                                                                         danTempat
                                               Utilization     of    K-Nearest
        2018 International                     Neighbor
                                               Algorithm      to    Determine          September 18-
        Conference and
                                               Standard            Operational         21, 2018 at Royal
        Workshop on
        Telecommunication,                     User  Log Data
                                               Procedures      Acquisition
                                                            Based          Based on Ambarukmo
                                                                   on Implicit
   1                                                                                   Hotel, Yogyakarta,
        Computing, Electrical,                 Implicit
                                               FeedbackFeedback Using
                                               Collaborative                           Indonesia
        Electronics and Control                Design      Feature Application Setting
                                               FilteringOfMethod
        (ICW-TELKOMNIKA                        Dashboard On Svara Using
        2018)                                  User- Centred Design Method
                                                                                       October 3-4,
                                                                                       2018. Grands Hotel,
                                                                                       Jalan Teuku Umar,
        International Conference               Comparison Of Multinomial Naive         Bukit Nagoya, Lubuk
   2    on Applied Engineering                 Bayes Algorithm And Logistic            Baja, Lubuk Baja
        (ICAE2018)                             Regression For Intent                   Kota, Lubuk Baja,
                                               Classification In Chatbot               Batam, Kepulauan
                                                                                       Riau




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                    40


---

                                                                                             26 Januari 2019.
                                                                                             Green Hall Lt. 7
                                               Simulasi Interoperabilitas                    STMIK Budi
        Seminar Nasional                                                                     Darma. Siantar
   3                                           Sistem Pengalamatan IPv4 dan
        Teknologi Komputer &                                                                 Barat
                                               IPv6 Pada Perangkat -
        Sains (SAINTEKS)                                                                     Kota Pematang
                                               Perangkat Jaringan Komputer
                                                                                             Siantar, Sumatera
                                                                                             Utara


E. Sertifikat HAKI
  No Judul/Tema HKI                                                  Tahun Jenis             Nomor P/ID
  1     MAC-WD (Pengendali Aliran Air Secara                         2019       Program      000168934
        Bertahap)                                                               Komputer
  2     RumahDiskusi.id untuk SD Negeri Adetex                       2019       Video        000170959
        Bandung
  3     Aplikasi MusiCroot                                           2021       Program      000235264
                                                                                Komputer
  4     Smart Parking Berbasis IoT Menggunakan                       2021       Program      000235266
        Raspberry Pi dan Metode OpenCV                                          Komputer
  5     Aplikasi APEM Speech to Text ke Sistem                       2021       Program      000235265
        Akademik                                                                Komputer



F. Jabatan Struktural
  No Nama Jabatan                                      Tahun              Institusi           Tugas Pokok
  1     Manajer Aset                                   2010â€“2019          Cisco Local         Mengelola aset Cisco
                                                                          Academy             Local Academy
                                                                          Politeknik TEDC
  2     Ketua Program Studi DIV Teknik                 2017â€“2022          Politeknik Pos      Memimpin program
        Informatika                                                       Indonesia           studi DIV Teknik
                                                                                              Informatika
  3     Wakil Dekan 1 Bidang Akademik,                 2022â€“2023          Fakultas Sekolah    Memimpin bidang
        Kemahasiswaan dan Riset                                           Vokasi ULBI         akademik,
                                                                                              kemahasiswaan, dan
                                                                                              riset

G. Keanggotaan Profesi
  No Nama Keanggotaan                                                         Lembaga                Tahun
  1     Anggota APTIKOM                                                       APTIKOM                2019â€“2025
  2     Anggota IEEE                                                          IEEE                   2018




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       41


---

  3     Anggota Asosiasi Dosen Indonesia                                      ADI                      2025
  4     Pengurus APTIKOM Jawa Barat                                           APTIKOM Jawa             2022â€“2026
                                                                              Barat



H. Seminar Nasional/Internasional
  No Nama Seminar/Konferensi                        Judul Artikel                            Waktu & Tempat
  1     ICW-TELKOMNIKA 2018                         Utilization of K-NN Algorithm to         September 18-21, 2018,
                                                    Determine SOP Based on Implicit          Royal Ambarukmo
                                                    Feedback; User Log Data                  Hotel, Yogyakarta
                                                    Acquisition Based on Implicit
                                                    Feedback; Design of Dashboard
                                                    Application Setting on SVARA
  2     International Conference on                 Comparison of Multinomial Naive          Oktober 3-4, 2018,
        Applied Engineering (ICAE2018)              Bayes Algorithm and Logistic             Grands Hotel, Batam
                                                    Regression for Intent Classification
                                                    in Chatbot
  3     Seminar Nasional Teknologi                  Simulasi Interoperabilitas Sistem        26 Januari 2019, STMIK
        Komputer & Sains (SAINTEKS)                 Pengalamatan IPv4 dan IPv6 pada          Budi Darma, Pematang
                                                    Perangkat-Perangkat Jaringan             Siantar
                                                    Komputer
         Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan dapat
dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
ketidaksesuaian dengan kenyataan, saya sanggup menerima risikonya. Demikian biodata ini
saya buat dengan sebenarnya.


                                                                                   Bandung, Mei 2026
                                                                                       Pengusul,




                                                                   (Muhammad Yusril Helmi Setyawan, S.Kom.,
                                                                                 M.Kom.)
                                                                             NIDN. 0407117405




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                         42


---

Biodata Anggota
A. Identitas Diri
  1      Nama Lengkap (dengan gelar)             Amri Yanuar, S.T., M.MoT
  2      Jenis Kelamin                           Laki-laki
  3      NIP/NIK/NIDN                            0415048901 / 0412018603
  4      Tempat dan Tanggal Lahir                Bandung, 12 Januari 1986
  5      E-mail                                  amri@ulbi.ac.id
  6      Nomor Telepon/HP                        081910027205
  7      Alamat Kantor                           Universitas Logistik dan Bisnis Internasional, Jln. Sari Asih No.
                                                 54, Bandung
  8      Nomor Telepon/Faks Kantor               Tlp. 022-2009570 / Fax. 022-2009568
  9      Mata Kuliah yang Diampu                 1. Manajemen Pergudangan
                                                 2. Manajemen Logistik
                                                 3. Sistem Informasi Pergudangan
  10     Sub Bidang Kepakaran                    Manajemen Pergudangan / Management of Technology

B. Riwayat Pendidikan
                             D-3                      S-1                      S-2                 S-3
  Nama Perguruan             -                        Universitas              Universiti          -
  Tinggi                                              Pasundan                 Teknologi
                                                                               Malaysia
  Bidang Ilmu                -                        Teknik Industri          Management of       -
                                                                               Technology
                                                                               (M.MoT)
  Tahun Lulus                -                        2009                     2012                -

C. Rekam Jejak Tri Dharma PT
1. Pendidikan/Pengajaran
  No     Nama Mata Kuliah                                                       Wajib/Pilihan            SKS
  1      Manajemen Pergudangan                                                  Wajib                    3
  2      Manajemen Logistik                                                     Wajib                    3
  3      Sistem Informasi Pergudangan                                           Wajib                    3

2. Penelitian
  No Judul Penelitian                                                         Peran     Lembaga              Tahun
  1     Analisis Pengendalian Persediaan pada Warehouse UKM                   Ketua     ULBI Internal        2020




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                        43


---

  2     Metode FSN Analysis dan Implementasinya pada Sistem                   Ketua     ULBI Internal          2021
        Informasi Pergudangan

3. Pengabdian Kepada Masyarakat
  No Judul Pengabdian Kepada Masyarakat                                          Lembaga/Mitra          Tahun
  1     Peningkatan Kompetensi Pemrograman Web melalui                           SMK Negeri 2           2025
        Workshop Bootcamp Laravel bagi Siswa SMK                                 Cimahi, Jawa Barat
        Negeri/Swasta di Kota Cimahi

4. Publikasi Artikel Ilmiah dalam Jurnal
  No Judul Artikel                                                   Nama Jurnal / Prosiding               Tahun
  1     Analisis Pengendalian Persediaan pada                        Jurnal Logistik Bisnis, Vol. 10       2020
        Warehouse UKM
  2     Metode FSN Analysis dan Implementasinya pada                 Jurnal Media Sisfo, Vol. 15           2021
        Sistem Informasi Pergudangan

D. Pengalaman Kerja
  No Pengalaman Kepakaran                              Tahun              Institusi                Peran
  1     Warehouse Supervisor                           2014               PT. Indofood Sukses      Supervisor
                                                                          Makmur
  2     Warehouse Development Team                     2021               Addorable Project        Tenaga Ahli

E. Sertifikat HAKI
  No Judul/Tema HKI                                                  Tahun Jenis              Nomor P/ID
  1     Warehouse Management System                                  â€“          Aplikasi      â€“
         Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan dapat
 dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
 ketidaksesuaian dengan kenyataan, saya sanggup menerima risikonya. Demikian biodata ini
 saya buat dengan sebenarnya


                                                                                   Bandung, Mei 2026
                                                                                       Pengusul,




                                                                             (Amri Yanuar, S.T., M.MoT)
                                                                                NIDN. 0412018603




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                           44


---

Lampiran 2 Biodata Mahasiswa

A. Identitas Diri
 1    Nama Lengkap                     Raditya Rizki Raharja
 2    Jenis Kelamin                    Laki-laki
 3    Program Studi                    Teknik Informatika
 4    NIM                              714240041
 5    Tempat dan Tanggal               Bandung, 31 Mei 2006
      Lahir
 6    Alamat E-mail                    radityarizki2309@gmail.com
 7 Nomor Telepon/HP        0858-6060-2948
B. Kegiatan Kemahasiswaan Yang Sedang/Pernah Diikuti
                                             Status dalam
 No      Jenis Kegiatan                                                   Waktu dan Tempat
                                             Kegiatan
 1       Himpunan Mahasiswa                  Staff Kominfo                Hingga Sekarang/ULBI
         Teknik Informatika
 2       Kunjungan Industri 1                Panitia                      Juli 2025/BSSN
C. Penghargaan Yang Pernah Diterima
                                                Pihak Pemberi
 No      Jenis Penghargaan                                                       Tahun
                                                Penghargaan
 1
 2
         Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan
dapat dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
ketidaksesuaian dengan kenyataan, saya sanggup menerima sanksi. Demikian biodata ini
saya buat dengan sebenarnya untuk memenuhi salah satu persyaratan dalam pengajuan
Penelitian Internal Tahun 2026.
                                                                                         Bandung, Mei 2026




                                                                                        Raditya Rizki Raharja
                                                                                            (714240041)




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                           45


---

A. Identitas Diri
    1     Nama Diri                            Rifky Najra Adipura
    2     Jenis Kelamin                        Laki â€“ Laki
    3     Program Studi                        DIV-Teknik Informatika
    4     NIM                                  714230025
    5     Tempat dan Tanggal Lahir             Cimahi, 03 Juli 2005
    6     Alamat Email                         rifkyadipura@gmail.com
    7     Nomor Telepon/HP                     089657140789


B. Kegiatan Kemahasiswaan Yang Sedang/Pernah Diikuti
                                                  Status dalam
 No             Jenis Kegiatan                                                   Waktu dan Tempat
                                                    Kegiatan

  1      Himpunan Mahasiswa                  Staff Ahli                   April 2025/ULBI
         Teknik Informatika

C. Penghargaan Yang Pernah Diterima
                                                      Pihak Pemberi
 No            Jenis Penghargaan                                                          Tahun
                                                       Penghargaan

  1

  2

         Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan
dapat dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
ketidaksesuaian dengan kenyataan, saya sanggup menerima sanksi. Demikian biodata ini
saya buat dengan sebenarnya untuk memenuhi salah satu persyaratan dalam pengajuan
Penelitian Internal Tahun 2025.

                                                                                        Bandung, Mei 2026




                                                                                        Rifky Najra Adipura
                                                                                            (714230025)




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                         46


---

A. Identitas Diri
 1 Nama Lengkap                        Ode Andi Alamsyah
 2       Jenis Kelamin                 Laki-laki
 3       Program Studi                 Teknik Informatika
 4       NIM                           714230032
 5       Tempat dan Tanggal            Busoa, 02 Maret 2005
         Lahir
 6       Alamat E-mail                 odeandialamsyah@gmail.com
 7       Nomor Telepon/HP              0813-5562-1802

B. Kegiatan Kemahasiswaan Yang Sedang/Pernah Diikuti
                                                   Status dalam
 No              Jenis Kegiatan                                                  Waktu dan Tempat
                                                     Kegiatan

     1     Himpunan Mahasiswa                Staff Ahli                   April 2025/ULBI
           Teknik Informatika

     2     UKM K-Radio                       Koordinator Public           Maret 2025/ULBI
                                             Relation

C. Penghargaan Yang Pernah Diterima
                                                      Pihak Pemberi
 No             Jenis Penghargaan                                                         Tahun
                                                       Penghargaan

     1
           Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan
dapat dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
ketidaksesuaian dengan kenyataan, saya sanggup menerima sanksi. Demikian biodata ini
saya buat dengan sebenarnya untuk memenuhi salah satu persyaratan dalam pengajuan
Penelitian Internal Tahun 2025.

                                                                                        Bandung, Mei 2026




                                                                                        Ode Andi Alamsyah
                                                                                           (714230032)




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       47


---

A. Identitas Diri
 1 Nama Lengkap                        Muhammad Arif Rivaldi
 2       Jenis Kelamin                 Laki-laki
 3       Program Studi                 Teknik Informatika
 4       NIM                           714240008
 5       Tempat dan Tanggal            Jakarta, 14 November 2005
         Lahir
 6       Alamat E-mail                 m.arifrivaldi141105@gmail.com
 7       Nomor Telepon/HP              0813-8262-6096

B. Kegiatan Kemahasiswaan Yang Sedang/Pernah Diikuti
                                                   Status dalam
 No              Jenis Kegiatan                                                  Waktu dan Tempat
                                                     Kegiatan

     1     Himpunan Mahasiswa                Staff Muda                   Hingga Sekarang/ULBI
           Teknik Informatika

     2     UKM Badminton                     Staff Peralatan              Hingga Sekarang/ULBI

C. Penghargaan Yang Pernah Diterima
                                                      Pihak Pemberi
 No             Jenis Penghargaan                                                           Tahun
                                                       Penghargaan

     1

     2
           Semua data yang saya isikan dan tercantum dalam biodata ini adalah benar dan
dapat dipertanggungjawabkan secara hukum. Apabila di kemudian hari ternyata dijumpai
ketidaksesuaian dengan kenyataan, saya sanggup menerima sanksi. Demikian biodata ini
saya buat dengan sebenarnya untuk memenuhi salah satu persyaratan dalam pengajuan
Penelitian Internal Tahun 2025.
                                                                                          Bandung, Mei 2026




                                                                                        Muhammad Arif Rivaldi
                                                                                            (714240008)




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                         48


---

Lampiran 3 Gambaran Iptek yang kan dilaksanakan pada mitra

       Program peningkatan kompetensi yang akan diberikan kepada siswa Jurusan Rekayasa
Perangkat Lunak SMKN 2 Cimahi berupa workshop Machine Learning dasar dengan studi
kasus prediksi awal kesehatan tanaman melalui analisis citra daun. Kegiatan ini menggunakan
pendekatan Project-Based Learning agar siswa tidak hanya memahami konsep, tetapi juga
mampu menghasilkan mini project berbasis kecerdasan buatan sebagai portofolio
pembelajaran.
Cakupan iptek yang akan dilaksanakan pada mitra adalah sebagai berikut:
   1. Pengenalan Machine Learning dan Computer Vision
       Siswa diperkenalkan pada konsep dasar Artificial Intelligence, Machine Learning,
       supervised learning, Computer Vision, serta penggunaan CNN dalam klasifikasi citra
       daun tanaman.
   2. Eksplorasi Dataset dan Praproses Citra
       Peserta mempelajari penggunaan dataset PlantVillage, struktur data citra, labeling,
       pembagian data, resize gambar, normalisasi, dan praproses sebelum pelatihan model.
   3. Pelatihan Model Klasifikasi Menggunakan Google Colab
       Siswa melakukan pelatihan model CNN sederhana menggunakan Google Colab,
       Python, dan TensorFlow Keras untuk mengklasifikasikan citra daun ke dalam beberapa
       kondisi, seperti Early Blight, Late Blight, Leaf Mold, Bacterial Spot, dan Healthy.
    4. Evaluasi Hasil Prediksi Model
       Peserta mempelajari evaluasi model melalui akurasi dan confusion matrix agar mampu
       memahami kualitas prediksi, potensi kesalahan klasifikasi, serta keterbatasan model
       sebagai alat screening awal.
    5. Implementasi Aplikasi Berbasis Streamlit
       Model yang telah dilatih dikemas menjadi aplikasi web sederhana berbasis Streamlit
       yang dapat menerima input gambar daun dan menampilkan hasil prediksi secara
       langsung.
    6. Penerapan Project-Based Learning
       Peserta bekerja secara berkelompok untuk menyelesaikan mini project klasifikasi citra
       daun dan mempresentasikan hasil aplikasi sebagai bentuk evaluasi pembelajaran.
       Secara umum, gambaran iptek pada Lampiran 2 menunjukkan bahwa kegiatan ini
diarahkan untuk memberikan pengalaman praktis kepada siswa dalam membangun sistem
prediksi awal berbasis citra, dengan memanfaatkan Kaggle, Google Colab, TensorFlow Keras,
dan Streamlit sebagai tools utama pembelajaran.




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026    49


---

Lampiran 3 Gambaran Lokasi Mitra dengan Universitas Logistik dan Bisnis
Internasional (ULBI)

       SMKN 2 Cimahi sebagai mitra kegiatan berlokasi sekitar 8,3 km dari Universitas
Logistik dan Bisnis Internasional (ULBI), dengan estimasi waktu tempuh sekitar 28â€“32 menit
melalui rute tercepat via Jalan Sariwangi Selatan. Akses yang mudah dan jarak yang relatif
dekat memungkinkan pelaksanaan program PKM berjalan efektif dengan pendampingan
langsung dari tim ULBI. Jarak SMKN 2 Cimahi dari Universitas Logistik dan Bisnis
Internasional seperti ditunjukkan dalam Gambar berikut ini:




Sumber: maps.google.com




Sumber: Google Maps (Foto Lokasi)




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026   50


---

Lampiran 4 Surat Pernyataan Kesediaan Bekerja Sama dengan Mitra PKM bermaterai
10.000




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026   51


---

Lampiran 5 Surat Kesediaan Kerjasama Mitra PKM bermaterai 10.000




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026   52


---

Lampiran 6 Surat Pernyataan Pengusul PKM bermaterai 10.000




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026   53


---

Lampiran 7 Justifikasi Anggaran

   1. Gaji dan Upah
                                           Honorarium /                Jumlah             Jumlah
             Jabatan                                                                                    TOTAL (Rp)
                                           Kegiatan (Rp)                 Sesi             Orang
  Pemateri Workshop (2
                                                         300.000           2                2              1.200.000
  pemateri Ã— 2 sesi)
  Asisten Teknis (2 asisten
                                                         168.750           2                2                675.000
  Ã— 2 sesi)
                                                                               SUB TOTAL (Rp)              1.875.000
   2. Bahan Habis Pakai
                                                                                           Harga
             Material                Justifikasi Pemakaian Kuantitas                                    TOTAL (Rp)
                                                                                        Satuan (Rp)
                                     Dibagikan kepada
  Modul pembelajaran
                                     seluruh 30 peserta
  Machine Learning                                                      30 eks               15.000          450.000
                                     workshop sebagai
  (cetak)
                                     referensi materi
                                     30 peserta + 7 panitia
  Sertifikat peserta dan             (3 dosen + 4
                                                                      37 lembar                 5.000        185.000
  panitia                            mahasiswa) sebagai
                                     bukti keikutsertaan
                                     Kertas HVS, spidol,
                                     bolpen, penghapus
  Alat Tulis Kantor (ATK)                                               1 paket             240.000          240.000
                                     untuk kebutuhan
                                     operasional workshop
                                     Snack/makan ringan
  Konsumsi peserta                   untuk 30 peserta
                                                                       60 porsi              11.500          690.000
  workshop                           selama 2 sesi
                                     workshop
                                     Snack/makan ringan
                                     untuk 7 panitia (3
  Konsumsi panitia
                                     dosen + 4 mahasiswa)              14 porsi              15.000          210.000
  workshop
                                     selama 2 sesi
                                     workshop
                                     1 buah spanduk
  Spanduk/backdrop
                                     backdrop ukuran                    1 buah              100.000          100.000
  kegiatan
                                     standar untuk




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                       54


---

                                     dokumentasi kegiatan
                                     workshop
                                                                              SUB TOTAL (Rp)             1.875.000
   3. Perjalanan
                                                                                           Harga
             Material                Justifikasi Pemakaian Kuantitas                                  TOTAL (Rp)
                                                                                        Satuan (Rp)
                                     Survei dan koordinasi
                                     awal dengan mitra, 3
  Perjalanan ke SMKN 2
                                     anggota tim, 1 kali               3 orang               75.000        225.000
  Cimahi Survei Awal
                                     (Â±8,3 km via Jl.
                                     Sariwangi Selatan)
                                     Transport PP seluruh
  Perjalanan ke SMKN 2               panitia (3 dosen + 4
  Cimahi Pelaksanaan                 mahasiswa) selama                 14 orang              50.000        700.000
  Workshop                           pelaksanaan 2 sesi
                                     workshop
                                     Transport PP tim inti
  Perjalanan ke SMKN 2               untuk monitoring dan
  Cimahi Monitoring &                evaluasi pasca-                   5 orang               40.000        200.000
  Evaluasi                           workshop, 5 anggota
                                     tim, 1 kali
                                                                              SUB TOTAL (Rp)             1.125.000
   4. Lain-Lain (publikasi, seminar, laporan, lainnya sebutkan)
                                                                                           Harga
             Material                Justifikasi Pemakaian Kuantitas                                  TOTAL (Rp)
                                                                                        Satuan (Rp)
                                     Biaya publikasi di
                                     jurnal pengabdian
  Publikasi artikel ilmiah           kepada masyarakat                  1 paket           1.300.000      1.300.000
                                     nasional terindeks
                                     Sinta
                                     Jasa
                                     fotografer/videografer
  Dokumentasi foto dan               selama pelaksanaan
                                                                        1 paket             400.000        400.000
  video kegiatan                     workshop untuk
                                     keperluan laporan dan
                                     luaran
  Penggandaan laporan                Cetak dan jilid laporan             2 eks              100.000        200.000




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026                     55


---

  kemajuan dan laporan               kemajuan dan laporan
  akhir                              akhir, masing-masing 2
                                     eksemplar
                                     Pulsa/internet
                                     koordinasi tim dan
  Biaya komunikasi dan
                                     kebutuhan administrasi             3 bulan         75.000    225.000
  administrasi
                                     selama 3 bulan
                                     pelaksanaan
                                                                              SUB TOTAL (Rp)     2.125.000
   TOTAL DANA YANG DIBUTUHKAN (Rp)                                                               7.000.000




Pengabdian Kepada Masyarakat Universitas Logistik dan Bisnis Internasional Tahun 2026             56


---


