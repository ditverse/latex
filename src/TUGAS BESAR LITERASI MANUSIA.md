# TUGAS BESAR LITERASI MANUSIA

**Dosen Pengampu:** Supriady, S.T., M.T.

**Disusun oleh:**

| Nama | NIM |
| --- | --- |
| ZAHRA RAMANAYSHILLA SOPIAN | 714240003 |
| RADITYA RIZKI RAHARJA | 714240041 |
| KEYLA SUN | 714240048 |
| RIDWAN HAKIM RAMADHAN | 714240050 |

**Kelas:** 2A D4 Teknik Informatika  
**Mata Kuliah:** Literasi Manusia

PROGRAM STUDI DIV TEKNIK INFORMATIKA  
SCHOOL OF INFORMATION TECHNOLOGY  
UNIVERSITAS LOGISTIK DAN BISNIS INTERNASIONAL  
BANDUNG  
2026

## DAFTAR ISI

- [BAB I PENDAHULUAN](#bab-i-pendahuluan)
  - [1.1 Latar Belakang](#11-latar-belakang)
  - [1.2 Rumusan Masalah](#12-rumusan-masalah)
  - [1.3 Tujuan Penelitian](#13-tujuan-penelitian)
  - [1.4 Manfaat Penelitian](#14-manfaat-penelitian)
    - [1.4.1 Manfaat Teoretis](#141-manfaat-teoretis)
    - [1.4.2 Manfaat Praktis](#142-manfaat-praktis)
- [BAB II KAJIAN MASALAH](#bab-ii-kajian-masalah)
  - [2.1 Kesulitan Masyarakat dalam Menemukan Jasa Kebersihan yang Terpercaya](#21-kesulitan-masyarakat-dalam-menemukan-jasa-kebersihan-yang-terpercaya)
  - [2.2 Permasalahan Transparansi Harga dalam Industri Jasa Kebersihan](#22-permasalahan-transparansi-harga-dalam-industri-jasa-kebersihan)
  - [2.3 Analisis Kebutuhan Target Penelitian: Masyarakat Perkotaan](#23-analisis-kebutuhan-target-penelitian-masyarakat-perkotaan)
- [BAB III SOLUSI TEKNOLOGI](#bab-iii-solusi-teknologi)
  - [3.1 Gambaran Umum Platform CleanConnect](#31-gambaran-umum-platform-cleanconnect)
  - [3.2 Fitur Booking Cleaning Service](#32-fitur-booking-cleaning-service)
  - [3.3 Fitur Tracking Petugas Berbasis Lokasi/GPS](#33-fitur-tracking-petugas-berbasis-lokasigps)
  - [3.4 Fitur Rating dan Review](#34-fitur-rating-dan-review)
  - [3.5 Fitur Estimasi Biaya Otomatis](#35-fitur-estimasi-biaya-otomatis)
  - [3.6 Fitur Jadwal Rutin Mingguan/Bulanan](#36-fitur-jadwal-rutin-mingguanbulanan)
- [BAB IV IMPLEMENTASI](#bab-iv-implementasi)
- [BAB V EVALUASI](#bab-v-evaluasi)
- [BAB VI KESIMPULAN DAN SARAN](#bab-vi-kesimpulan-dan-saran)
  - [6.1 Kesimpulan](#61-kesimpulan)
  - [6.2 Saran](#62-saran)

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

Perkembangan kehidupan masyarakat perkotaan (urban) di Indonesia dalam dua dekade terakhir menunjukkan transformasi yang signifikan, baik dari segi pola kerja, struktur keluarga, maupun gaya hidup secara umum. Urbanisasi yang terus meningkat menyebabkan kepadatan penduduk di kota-kota besar semakin tinggi, sehingga berdampak pada perubahan tuntutan hidup masyarakat yang tinggal di dalamnya. Salah satu fenomena yang menonjol adalah meningkatnya jumlah rumah tangga dengan pasangan yang sama-sama bekerja (dual-income households), meningkatnya jumlah pekerja lepas (freelancer) dengan jam kerja fleksibel namun padat, serta meningkatnya jumlah individu yang tinggal sendiri (single living) akibat tuntutan pekerjaan atau pendidikan di kota besar.

Kondisi tersebut secara langsung memengaruhi alokasi waktu yang dimiliki oleh masyarakat perkotaan untuk mengurus kebutuhan domestik, termasuk di antaranya kebersihan rumah. Pekerjaan rumah tangga seperti membersihkan rumah, menyapu, mengepel, membersihkan kamar mandi, hingga merapikan ruangan, pada dasarnya membutuhkan waktu dan tenaga yang tidak sedikit. Namun, bagi masyarakat perkotaan yang memiliki jam kerja panjang dan mobilitas tinggi, waktu yang tersisa untuk mengurus pekerjaan rumah tangga menjadi semakin terbatas. Sebagai akibatnya, kebutuhan terhadap jasa kebersihan rumah tangga (home cleaning service) mengalami peningkatan permintaan yang cukup signifikan, khususnya di kawasan-kawasan padat penduduk seperti Jakarta, Surabaya, Bandung, dan kota-kota besar lainnya.

Di sisi lain, model penyediaan jasa kebersihan rumah tangga di Indonesia sebagian besar masih bersifat konvensional dan informal. Masyarakat umumnya mengandalkan informasi dari mulut ke mulut (word of mouth), rekomendasi tetangga, atau pencarian secara manual melalui grup media sosial dan papan iklan lokal untuk mendapatkan jasa kebersihan. Pendekatan semacam ini memiliki sejumlah kelemahan, antara lain ketiadaan standar kualitas yang jelas, minimnya jaminan keamanan, serta tidak adanya transparansi harga yang dapat diverifikasi sebelum layanan diberikan. Akibatnya, masyarakat sering dihadapkan pada risiko ketidakpastian, baik dari segi kualitas pekerjaan, keandalan petugas, maupun kewajaran biaya yang dikenakan.

Perkembangan teknologi informasi, khususnya pada sektor aplikasi berbasis lokasi (location-based service) dan platform on-demand, telah membuka peluang besar untuk menjawab permasalahan tersebut. Model bisnis yang telah berhasil diterapkan pada sektor transportasi dan pengantaran makanan menunjukkan bahwa pendekatan digital mampu meningkatkan efisiensi, transparansi, dan kepercayaan antara penyedia jasa dan pengguna jasa. Berdasarkan latar belakang tersebut, muncul gagasan untuk mengembangkan sebuah platform digital bernama "CleanConnect", yaitu sebuah platform pemesanan jasa kebersihan rumah tangga berbasis lokasi yang dirancang untuk menjawab kebutuhan masyarakat perkotaan akan layanan kebersihan rumah tangga yang praktis, terpercaya, transparan, dan dapat dipantau secara real-time.

Penelitian ini disusun pada tahap awal pengembangan proyek, yaitu tahap pengumpulan data dan wawancara dengan calon pengguna serta pemangku kepentingan terkait, dengan tujuan untuk memperoleh gambaran kebutuhan, permasalahan, dan harapan masyarakat perkotaan terhadap layanan kebersihan rumah tangga, sebagai dasar perancangan sistem CleanConnect yang sesuai dengan kondisi nyata di lapangan.

### 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah dipaparkan, maka rumusan masalah dalam penelitian ini dapat dirinci sebagai berikut:

1. Bagaimana proses pencarian dan pemilihan jasa kebersihan rumah tangga yang dilakukan oleh masyarakat perkotaan saat ini, serta apa saja kendala yang dihadapi dalam menemukan penyedia jasa yang terpercaya dan berkualitas?
2. Bagaimana tingkat transparansi informasi harga pada layanan jasa kebersihan rumah tangga konvensional, dan sejauh mana ketidakjelasan harga tersebut memengaruhi kepercayaan serta keputusan masyarakat dalam menggunakan jasa kebersihan?
3. Bagaimana rancangan fitur dan mekanisme kerja platform CleanConnect (booking, pelacakan lokasi petugas, rating dan review, estimasi biaya otomatis, serta penjadwalan rutin) dapat dirumuskan agar mampu menjawab kebutuhan masyarakat perkotaan terhadap layanan kebersihan rumah tangga yang praktis, transparan, dan dapat dipertanggungjawabkan?

### 1.3 Tujuan Penelitian

Berdasarkan rumusan masalah di atas, tujuan dari penelitian ini adalah sebagai berikut:

1. Mengidentifikasi dan menganalisis pola perilaku, kebiasaan, serta kendala yang dihadapi oleh masyarakat perkotaan dalam mencari dan memilih jasa kebersihan rumah tangga yang terpercaya.
2. Menganalisis tingkat permasalahan transparansi harga pada layanan jasa kebersihan rumah tangga yang ada saat ini, beserta dampaknya terhadap tingkat kepercayaan dan kepuasan pengguna.
3. Merancang dan mendeskripsikan secara rinci fitur-fitur teknologi pada platform CleanConnect sebagai solusi atas permasalahan kepercayaan, transparansi harga, dan kemudahan akses layanan kebersihan rumah tangga berbasis lokasi bagi masyarakat perkotaan.

### 1.4 Manfaat Penelitian

Penelitian ini diharapkan dapat memberikan manfaat baik secara teoretis maupun praktis, sebagaimana diuraikan berikut.

#### 1.4.1 Manfaat Teoretis

Secara teoretis, penelitian ini diharapkan dapat memperkaya kajian di bidang sistem informasi dan teknologi layanan berbasis lokasi (location-based service), khususnya dalam konteks penerapan model bisnis on-demand pada sektor jasa kebersihan rumah tangga. Penelitian ini juga dapat menjadi referensi bagi penelitian-penelitian selanjutnya yang berkaitan dengan perancangan platform layanan rumah tangga digital, analisis kebutuhan pengguna, serta evaluasi usability dan kepuasan pengguna terhadap aplikasi berbasis seluler.

#### 1.4.2 Manfaat Praktis

1. **Bagi Masyarakat (Pengguna Jasa)**

   Penelitian ini diharapkan dapat memberikan gambaran solusi nyata berupa platform yang memudahkan masyarakat perkotaan dalam menemukan, memesan, dan memantau jasa kebersihan rumah tangga secara transparan, aman, dan efisien dari segi waktu maupun biaya.

2. **Bagi Penyedia Jasa Kebersihan**

   Hasil penelitian ini dapat membantu para pekerja atau penyedia jasa kebersihan untuk memperoleh akses pasar yang lebih luas melalui kanal digital, sekaligus membangun reputasi profesional melalui sistem rating dan review yang transparan.

3. **Bagi Pengembang dan Pemangku Kebijakan**

   Penelitian ini dapat menjadi bahan masukan bagi pengembang sistem dalam merancang fitur-fitur yang relevan dengan kebutuhan riil pengguna, serta menjadi referensi bagi pemangku kebijakan terkait pengembangan ekonomi digital di sektor jasa rumah tangga.

## BAB II KAJIAN MASALAH

### 2.1 Kesulitan Masyarakat dalam Menemukan Jasa Kebersihan yang Terpercaya

Salah satu permasalahan fundamental yang dihadapi oleh masyarakat perkotaan dalam memenuhi kebutuhan kebersihan rumah tangga adalah minimnya akses terhadap informasi yang valid dan dapat dipercaya mengenai penyedia jasa kebersihan. Berdasarkan hasil pengamatan awal dan proses wawancara pendahuluan, ditemukan bahwa sebagian besar masyarakat masih mengandalkan metode pencarian tradisional, seperti rekomendasi mulut ke mulut (word of mouth), grup percakapan lingkungan perumahan, maupun papan iklan jasa kebersihan yang terpasang di area publik. Metode-metode tersebut memiliki tingkat keterandalan yang sangat bervariasi dan sulit diverifikasi secara objektif.

Ketidakpastian mengenai kredibilitas penyedia jasa menimbulkan beberapa risiko bagi pengguna, antara lain risiko keamanan, karena petugas yang datang ke rumah tidak memiliki identitas atau riwayat kerja yang dapat diakses; risiko kualitas, karena tidak adanya standar baku mengenai cakupan pekerjaan, durasi, maupun hasil akhir pembersihan; serta risiko ketidaksesuaian waktu, di mana petugas yang dijanjikan datang pada jam tertentu sering mengalami keterlambatan tanpa adanya mekanisme pemberitahuan atau pelacakan.

Selain itu, tidak adanya basis data terpusat mengenai reputasi penyedia jasa menyebabkan pengguna baru kesulitan membandingkan kualitas antar penyedia jasa. Pengguna cenderung harus melalui proses trial and error, yaitu mencoba menggunakan jasa dari beberapa penyedia hingga menemukan yang sesuai dengan preferensi mereka, suatu proses yang memakan waktu, biaya, dan berpotensi menimbulkan pengalaman negatif yang berulang. Kondisi ini menunjukkan adanya kebutuhan akan suatu sistem yang dapat mengumpulkan, menyimpan, dan menampilkan rekam jejak kinerja penyedia jasa secara transparan dan dapat diakses oleh publik, sehingga proses pengambilan keputusan oleh calon pengguna menjadi lebih terinformasi (informed decision).

### 2.2 Permasalahan Transparansi Harga dalam Industri Jasa Kebersihan

Permasalahan kedua yang menjadi sorotan dalam penelitian ini adalah ketidaktransparanan informasi harga pada layanan jasa kebersihan rumah tangga. Pada model bisnis konvensional, penentuan harga umumnya dilakukan melalui negosiasi langsung antara konsumen dan penyedia jasa, yang sangat dipengaruhi oleh faktor subjektif seperti kemampuan tawar-menawar masing-masing pihak, hubungan personal, maupun kondisi pasar setempat. Akibatnya, terjadi disparitas harga yang signifikan untuk jenis dan volume pekerjaan yang relatif sama, baik antara satu penyedia jasa dengan penyedia jasa lainnya, maupun antar wilayah dalam satu kota yang sama.

Ketidakjelasan struktur harga ini menimbulkan beberapa konsekuensi. Pertama, konsumen mengalami kesulitan dalam melakukan perencanaan anggaran rumah tangga (household budgeting), karena tidak adanya acuan harga standar yang dapat dijadikan referensi sebelum melakukan pemesanan. Kedua, terbuka peluang terjadinya praktik penetapan harga yang tidak wajar (overpricing), terutama terhadap konsumen yang baru pertama kali menggunakan jasa tersebut atau yang berada dalam kondisi mendesak. Ketiga, dari sisi penyedia jasa, ketidakjelasan harga juga dapat merugikan mereka apabila terjadi kesalahpahaman mengenai cakupan pekerjaan yang seharusnya dikerjakan sesuai dengan nilai yang dibayarkan, sehingga berpotensi menimbulkan konflik antara kedua belah pihak.

Hasil wawancara awal dengan beberapa calon pengguna menunjukkan bahwa salah satu faktor utama yang menyebabkan keraguan dalam menggunakan jasa kebersihan rumah tangga, terutama dari penyedia yang belum dikenal, adalah ketidaktahuan mengenai besaran biaya yang harus dikeluarkan sebelum proses pemesanan dilakukan. Hal ini menunjukkan bahwa transparansi harga bukan hanya menjadi isu administratif, tetapi juga merupakan salah satu faktor psikologis yang memengaruhi tingkat kepercayaan (trust) konsumen terhadap suatu layanan. Oleh karena itu, diperlukan suatu mekanisme estimasi biaya yang dapat dihitung secara otomatis berdasarkan parameter yang jelas dan konsisten, seperti luas area, jenis layanan, dan durasi pengerjaan, sehingga pengguna dapat mengetahui perkiraan biaya sebelum memutuskan untuk melakukan pemesanan.

### 2.3 Analisis Kebutuhan Target Penelitian: Masyarakat Perkotaan

Masyarakat perkotaan dipilih sebagai target penelitian dengan pertimbangan karakteristik demografis, sosial, dan gaya hidup yang relevan dengan kebutuhan terhadap layanan jasa kebersihan rumah tangga berbasis teknologi. Beberapa karakteristik utama masyarakat urban yang menjadi dasar analisis kebutuhan dalam penelitian ini adalah sebagai berikut.

Pertama, dari segi keterbatasan waktu, masyarakat perkotaan umumnya memiliki rutinitas pekerjaan dengan jam kerja yang panjang serta waktu tempuh perjalanan (commuting time) yang signifikan, sehingga ketersediaan waktu untuk mengelola pekerjaan rumah tangga, termasuk kebersihan, menjadi sangat terbatas. Kondisi ini mendorong munculnya kebutuhan akan layanan yang dapat dipesan secara cepat (on-demand) tanpa memerlukan proses pencarian dan negosiasi yang memakan waktu lama.

Kedua, dari segi adopsi teknologi, masyarakat perkotaan secara umum memiliki tingkat literasi digital dan penetrasi penggunaan perangkat seluler pintar (smartphone) yang relatif tinggi, sehingga lebih siap untuk mengadopsi platform berbasis aplikasi dalam memenuhi kebutuhan layanan sehari-hari. Hal ini menjadi faktor pendukung utama bagi penerapan solusi berbasis teknologi seperti CleanConnect, karena target pengguna sudah memiliki keterbiasaan dalam menggunakan aplikasi sejenis pada sektor lain, seperti transportasi daring dan pengantaran makanan.

Ketiga, dari segi tipologi hunian, masyarakat perkotaan banyak yang tinggal pada hunian vertikal seperti apartemen, rumah susun, maupun perumahan dengan sistem keamanan tertutup (gated community), yang memiliki kebutuhan spesifik terkait akses petugas ke dalam area hunian. Hal ini memunculkan kebutuhan akan fitur pelacakan lokasi petugas secara real-time, sehingga penghuni dapat mengetahui posisi dan estimasi waktu kedatangan petugas, serta memastikan keamanan akses ke dalam unit hunian.

Keempat, dari segi pola kebutuhan layanan, masyarakat perkotaan, khususnya keluarga dengan kedua pasangan yang bekerja maupun individu yang tinggal sendiri, cenderung memerlukan layanan kebersihan secara berkala dengan frekuensi tertentu, misalnya mingguan atau dua minggu sekali, dibandingkan dengan pemesanan yang bersifat satu kali (one-time service). Hal ini menunjukkan adanya kebutuhan akan fitur penjadwalan rutin yang memungkinkan pengguna menetapkan jadwal layanan secara berulang tanpa harus melakukan pemesanan ulang setiap kali membutuhkan layanan.

Berdasarkan keempat karakteristik tersebut, dapat disimpulkan bahwa kebutuhan masyarakat perkotaan terhadap platform jasa kebersihan rumah tangga berbasis lokasi tidak hanya terbatas pada aspek kemudahan pemesanan, tetapi juga mencakup aspek kepercayaan terhadap petugas, transparansi biaya, kemampuan pemantauan secara real-time, serta fleksibilitas dalam pengaturan jadwal layanan secara berkelanjutan. Kebutuhan-kebutuhan tersebut menjadi dasar perumusan fitur-fitur teknologi yang akan dijelaskan secara rinci pada bab selanjutnya.

## BAB III SOLUSI TEKNOLOGI

### 3.1 Gambaran Umum Platform CleanConnect

CleanConnect dirancang sebagai sebuah platform digital berbasis aplikasi seluler (mobile application) yang berfungsi sebagai penghubung antara pengguna jasa (konsumen) dengan penyedia jasa kebersihan rumah tangga (mitra petugas kebersihan) melalui mekanisme pemesanan berbasis lokasi. Platform ini dikembangkan dengan pendekatan model bisnis on-demand service, yang mengadaptasi prinsip-prinsip dari platform layanan berbasis lokasi yang telah berhasil diterapkan pada sektor lain, namun disesuaikan dengan karakteristik dan kebutuhan spesifik layanan kebersihan rumah tangga.

Secara umum, CleanConnect terdiri atas dua antarmuka utama, yaitu antarmuka pengguna (customer application) dan antarmuka mitra petugas (partner application), yang keduanya terhubung melalui sistem backend terpusat yang mengelola data pemesanan, lokasi, harga, serta riwayat transaksi. Berdasarkan hasil kajian permasalahan pada Bab II, terdapat lima fitur utama yang menjadi fokus pengembangan CleanConnect, yaitu fitur booking cleaning service, tracking petugas berbasis lokasi/GPS, rating dan review, estimasi biaya otomatis, serta jadwal rutin mingguan/bulanan. Kelima fitur tersebut dirancang secara terintegrasi untuk menjawab permasalahan kepercayaan, transparansi harga, dan efisiensi waktu yang telah diidentifikasi sebelumnya.

### 3.2 Fitur Booking Cleaning Service

Fitur booking cleaning service merupakan fitur inti yang memungkinkan pengguna untuk melakukan pemesanan layanan kebersihan rumah tangga secara langsung melalui aplikasi, tanpa perlu melalui proses komunikasi manual seperti telepon atau pesan singkat kepada penyedia jasa.

Proses pemesanan dirancang melalui beberapa tahapan, yaitu pertama, pengguna memilih jenis layanan yang dibutuhkan, misalnya pembersihan umum (general cleaning), pembersihan mendalam (deep cleaning), pembersihan pasca-renovasi, atau pembersihan area khusus seperti dapur dan kamar mandi. Kedua, pengguna menentukan lokasi layanan, yang secara otomatis dapat terisi berdasarkan lokasi perangkat pengguna (geolocation) atau dapat dipilih secara manual melalui peta digital. Ketiga, pengguna memilih waktu pelaksanaan layanan, baik untuk waktu terdekat yang tersedia maupun untuk waktu tertentu di masa mendatang. Keempat, sistem akan menampilkan daftar petugas yang tersedia di sekitar lokasi pengguna beserta informasi profil, rating, dan estimasi biaya, sehingga pengguna dapat memilih petugas berdasarkan preferensi tertentu, misalnya berdasarkan rating tertinggi atau jarak terdekat.

Setelah pengguna memilih petugas dan mengonfirmasi detail pesanan, sistem akan mengirimkan permintaan kepada petugas terkait. Apabila petugas menerima permintaan tersebut, status pesanan akan berubah menjadi terkonfirmasi, dan pengguna akan menerima notifikasi yang berisi informasi mengenai identitas petugas, estimasi waktu kedatangan, serta rincian biaya. Apabila petugas tidak merespons dalam jangka waktu tertentu atau menolak permintaan, sistem secara otomatis akan mengalihkan permintaan kepada petugas alternatif berikutnya yang tersedia, sehingga proses pemesanan tetap dapat berjalan tanpa intervensi manual dari pengguna.

Fitur ini dirancang untuk menjawab permasalahan kesulitan masyarakat dalam menemukan penyedia jasa, sebagaimana dibahas pada Bab II, dengan menghadirkan basis data penyedia jasa yang telah terverifikasi, lengkap dengan informasi profil dan rekam jejak kinerja yang dapat diakses sebelum keputusan pemesanan dibuat.

### 3.3 Fitur Tracking Petugas Berbasis Lokasi/GPS

Fitur tracking petugas berbasis lokasi atau GPS dirancang untuk memberikan visibilitas secara real-time mengenai posisi dan perjalanan petugas kebersihan menuju lokasi layanan, sejak pesanan dikonfirmasi hingga petugas tiba di lokasi.

Secara teknis, fitur ini memanfaatkan layanan lokasi (location services) yang terdapat pada perangkat seluler petugas untuk mengirimkan data koordinat secara periodik ke sistem backend, yang selanjutnya ditampilkan pada antarmuka aplikasi pengguna dalam bentuk titik lokasi yang bergerak pada peta digital. Selain menampilkan posisi petugas, sistem juga menghitung dan menampilkan estimasi waktu kedatangan (estimated time of arrival/ETA) berdasarkan jarak dan kondisi lalu lintas yang diperoleh melalui integrasi dengan layanan pemetaan digital.

Fitur ini memberikan beberapa manfaat bagi pengguna. Pertama, dari aspek perencanaan waktu, pengguna dapat mengatur aktivitas pribadi berdasarkan estimasi waktu kedatangan petugas, sehingga tidak perlu menunggu tanpa kepastian. Kedua, dari aspek keamanan, pengguna dapat memverifikasi bahwa petugas yang datang merupakan petugas yang sesuai dengan yang telah dikonfirmasi melalui aplikasi, dengan mencocokkan posisi dan identitas yang ditampilkan pada sistem. Ketiga, dari aspek akuntabilitas, riwayat perjalanan petugas dapat tersimpan sebagai data pendukung apabila terjadi keluhan terkait keterlambatan atau ketidaksesuaian waktu kedatangan, sehingga dapat digunakan sebagai bahan evaluasi kinerja petugas oleh sistem.

Fitur ini secara langsung menjawab permasalahan ketidakpastian waktu kedatangan petugas yang telah diidentifikasi sebagai salah satu sumber ketidakpercayaan masyarakat terhadap layanan jasa kebersihan konvensional, sebagaimana diuraikan pada Bab II.

### 3.4 Fitur Rating dan Review

Fitur rating dan review berfungsi sebagai mekanisme evaluasi kualitas layanan berbasis umpan balik pengguna (user-generated feedback), yang bertujuan untuk membangun sistem reputasi yang transparan bagi setiap petugas yang terdaftar pada platform CleanConnect.

Setelah setiap sesi layanan selesai dilaksanakan, pengguna diberikan kesempatan untuk memberikan penilaian terhadap kinerja petugas dalam bentuk skor numerik, misalnya menggunakan skala bintang satu hingga lima, serta dapat menambahkan ulasan tertulis yang menjelaskan pengalaman penggunaan layanan secara lebih spesifik, seperti ketepatan waktu, kualitas hasil pembersihan, sikap dan keramahan petugas, serta kesesuaian pekerjaan dengan kategori layanan yang dipesan.

Akumulasi nilai rating dari seluruh pengguna akan ditampilkan pada profil masing-masing petugas dalam bentuk skor rata-rata, yang dapat dilihat oleh calon pengguna lain pada saat proses pemilihan petugas di fitur booking. Selain itu, sistem juga dapat menampilkan beberapa ulasan terbaru atau ulasan yang dianggap paling relevan, sehingga calon pengguna memperoleh gambaran kualitatif mengenai pengalaman pengguna sebelumnya.

Dari sisi penyedia jasa, fitur ini juga berfungsi sebagai mekanisme insentif untuk menjaga dan meningkatkan kualitas layanan, karena skor rating yang tinggi akan meningkatkan visibilitas dan kemungkinan untuk dipilih oleh pengguna baru, sedangkan skor yang rendah dapat menjadi indikator bagi pihak pengelola platform untuk melakukan evaluasi atau pembinaan terhadap petugas terkait. Dengan demikian, fitur rating dan review berperan penting dalam mengatasi permasalahan minimnya informasi mengenai kredibilitas penyedia jasa yang selama ini menjadi kendala utama masyarakat dalam memilih layanan kebersihan rumah tangga.

### 3.5 Fitur Estimasi Biaya Otomatis

Fitur estimasi biaya otomatis dirancang untuk menjawab permasalahan ketidaktransparanan harga yang telah dibahas pada Bab II, dengan menyediakan perhitungan perkiraan biaya layanan secara instan berdasarkan parameter-parameter yang dimasukkan oleh pengguna sebelum proses pemesanan dikonfirmasi.

Beberapa parameter yang digunakan dalam perhitungan estimasi biaya antara lain meliputi jenis layanan yang dipilih, misalnya pembersihan umum atau pembersihan mendalam, yang masing-masing memiliki tarif dasar berbeda; luas area atau jumlah ruangan yang akan dibersihkan, yang memengaruhi estimasi durasi pengerjaan; durasi layanan, baik yang dihitung berdasarkan estimasi waktu standar per jenis pekerjaan maupun durasi yang dipilih secara manual oleh pengguna; serta lokasi layanan, yang dapat memengaruhi biaya tambahan tertentu, misalnya biaya transportasi petugas berdasarkan jarak.

Berdasarkan parameter-parameter tersebut, sistem akan menghitung dan menampilkan rincian estimasi biaya secara transparan kepada pengguna sebelum pemesanan dikonfirmasi, yang umumnya terdiri atas komponen biaya layanan dasar, biaya tambahan apabila terdapat permintaan khusus, serta total estimasi biaya yang harus dibayarkan. Dengan adanya rincian tersebut, pengguna dapat memahami dasar perhitungan biaya secara jelas dan dapat melakukan perencanaan anggaran sebelum memutuskan untuk menggunakan layanan.

Selain memberikan manfaat bagi pengguna dari sisi kejelasan biaya, fitur ini juga berperan dalam menstandardisasi struktur harga di antara para petugas yang terdaftar pada platform, sehingga mengurangi potensi terjadinya disparitas harga yang signifikan untuk jenis pekerjaan yang setara, sebagaimana sering terjadi pada model layanan konvensional.

### 3.6 Fitur Jadwal Rutin Mingguan/Bulanan

Fitur jadwal rutin mingguan/bulanan dirancang untuk mengakomodasi kebutuhan masyarakat perkotaan yang memerlukan layanan kebersihan rumah tangga secara berkelanjutan dengan frekuensi tertentu, sebagaimana telah diidentifikasi pada analisis kebutuhan target penelitian di Bab II.

Melalui fitur ini, pengguna dapat menetapkan pola pemesanan layanan yang berulang, misalnya setiap minggu pada hari dan jam tertentu, setiap dua minggu sekali, atau setiap bulan, tanpa harus melakukan proses pemesanan dari awal pada setiap periode layanan. Setelah pengguna menetapkan jadwal rutin, sistem akan secara otomatis membuat pesanan baru sesuai dengan jadwal yang telah ditentukan, serta mengirimkan permintaan kepada petugas yang sama apabila petugas tersebut tersedia pada waktu yang dijadwalkan, guna menjaga konsistensi dan kenyamanan pengguna terhadap petugas yang telah dikenal sebelumnya.

Apabila petugas yang biasa digunakan tidak tersedia pada jadwal tertentu, sistem akan memberikan notifikasi kepada pengguna beserta opsi untuk memilih petugas pengganti yang tersedia, sehingga kontinuitas layanan tetap dapat terjaga. Pengguna juga diberikan fleksibilitas untuk mengubah, menunda, atau membatalkan jadwal rutin pada periode tertentu sesuai dengan kebutuhan, misalnya pada saat pengguna sedang tidak berada di rumah.

Fitur ini memberikan nilai tambah berupa efisiensi waktu bagi pengguna, karena proses pemesanan tidak perlu dilakukan secara berulang untuk kebutuhan layanan yang bersifat rutin, sekaligus memberikan kepastian pendapatan bagi petugas melalui jadwal kerja yang lebih terstruktur dan dapat diprediksi.

## BAB IV IMPLEMENTASI

## BAB V EVALUASI

## BAB VI KESIMPULAN DAN SARAN

### 6.1 Kesimpulan

### 6.2 Saran
