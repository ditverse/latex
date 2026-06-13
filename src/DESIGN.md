# design.md — CleanConnect UI/UX Prototype

## 1. Product Overview

CleanConnect adalah aplikasi mobile berbasis lokasi untuk pemesanan jasa kebersihan rumah tangga. Aplikasi ini menghubungkan pengguna dengan mitra petugas kebersihan secara praktis, transparan, dan mudah dipantau.

Tujuan utama aplikasi:

* Memudahkan pengguna mencari jasa kebersihan terpercaya.
* Menampilkan estimasi biaya sebelum pemesanan.
* Memberikan fitur tracking petugas secara real-time.
* Menyediakan rating dan review untuk membangun kepercayaan.
* Mendukung jadwal rutin mingguan atau bulanan.

## 2. Target User

### Primary User: Pengguna Jasa / Customer

Karakteristik:

* Tinggal di perkotaan.
* Memiliki aktivitas padat.
* Membutuhkan jasa kebersihan rumah, apartemen, kos, atau kantor kecil.
* Menginginkan layanan yang cepat, terpercaya, transparan, dan mudah dipesan.

### Secondary User: Mitra Petugas Kebersihan

Karakteristik:

* Menawarkan layanan kebersihan rumah tangga.
* Membutuhkan aplikasi untuk menerima pesanan, melihat lokasi pelanggan, mengubah status pekerjaan, dan menerima ulasan.

## 3. Design Goals

Desain UI/UX harus:

* Modern, bersih, dan mudah dipahami.
* Memberikan kesan terpercaya dan profesional.
* Menggunakan alur pemesanan yang sederhana.
* Menampilkan informasi harga secara transparan.
* Memudahkan pengguna memantau status petugas.
* Cocok untuk aplikasi mobile Android/iOS.

## 4. Visual Style

### Brand Personality

CleanConnect harus terasa:

* Bersih
* Aman
* Ramah
* Profesional
* Modern
* Terpercaya

### Color Palette

Gunakan warna utama yang memberi kesan bersih dan nyaman:

* Primary Color: Soft Blue / Teal
  Contoh: #2BB3A3 atau #1E88E5
* Secondary Color: White
  Contoh: #FFFFFF
* Background Color: Light Gray / Soft Blue Tint
  Contoh: #F5F9FA
* Accent Color: Green
  Contoh: #4CAF50
* Warning Color: Orange
  Contoh: #FF9800
* Error Color: Red
  Contoh: #E53935
* Text Primary: Dark Navy
  Contoh: #1F2937
* Text Secondary: Gray
  Contoh: #6B7280

### Typography

Gunakan font modern dan mudah dibaca:

* Inter
* Poppins
* SF Pro Display
* Roboto

Gaya teks:

* Heading: tebal, jelas, ukuran besar.
* Body text: sederhana dan mudah dibaca.
* Button text: tebal dan singkat.

## 5. UI Components

Gunakan komponen berikut:

* Bottom navigation bar
* Search bar
* Service category cards
* Location input card
* Date and time picker
* Price estimation card
* Cleaner profile card
* Rating stars
* Review list
* Order status timeline
* Map tracking screen
* Floating action button untuk bantuan/chat
* Primary button dengan rounded corners
* Success confirmation modal
* Notification card

## 6. Main User Flow — Customer App

### Flow 1: Onboarding

1. Splash screen dengan logo CleanConnect.
2. Onboarding screen 1: “Pesan jasa kebersihan dengan mudah.”
3. Onboarding screen 2: “Pantau petugas secara real-time.”
4. Onboarding screen 3: “Harga transparan dan petugas terpercaya.”
5. Login/Register screen.

### Flow 2: Booking Cleaning Service

1. User masuk ke Home.
2. User memilih jenis layanan kebersihan.
3. User mengisi alamat/lokasi.
4. User memilih tanggal dan jam.
5. User memilih luas ruangan atau jumlah kamar.
6. Sistem menampilkan estimasi biaya.
7. User memilih petugas yang tersedia.
8. User melakukan konfirmasi pesanan.
9. Sistem menampilkan halaman order success.

### Flow 3: Tracking Petugas

1. User membuka detail pesanan aktif.
2. User melihat status: “Petugas dalam perjalanan.”
3. User melihat peta lokasi petugas.
4. User melihat estimasi waktu kedatangan.
5. User dapat menghubungi petugas melalui tombol chat/call.

### Flow 4: Rating dan Review

1. Setelah layanan selesai, user mendapat notifikasi.
2. User memberi rating bintang 1–5.
3. User menulis ulasan singkat.
4. User mengirim review.
5. Sistem menampilkan pesan terima kasih.

### Flow 5: Jadwal Rutin

1. User memilih menu “Jadwal Rutin.”
2. User memilih frekuensi: mingguan, dua minggu sekali, atau bulanan.
3. User memilih layanan, alamat, tanggal, dan jam.
4. Sistem menampilkan ringkasan jadwal.
5. User mengonfirmasi jadwal rutin.

## 7. Required Screens — Customer App

### 1. Splash Screen

Isi:

* Logo CleanConnect
* Tagline: “Clean Home, Connected Service”
* Background putih atau soft blue

### 2. Onboarding Screens

Buat 3 halaman onboarding:

* Page 1: Booking mudah
* Page 2: Tracking petugas real-time
* Page 3: Harga transparan dan review terpercaya

### 3. Login/Register Screen

Isi:

* Logo
* Input email/nomor HP
* Input password
* Button login
* Link register
* Login dengan Google

### 4. Home Screen

Isi:

* Greeting: “Halo, Zahra”
* Current location card
* Search bar
* Service categories:

  * General Cleaning
  * Deep Cleaning
  * Bathroom Cleaning
  * Kitchen Cleaning
  * Kos/Apartment Cleaning
* Promo/Info card
* Active booking card jika ada pesanan aktif
* Bottom navigation:

  * Home
  * Booking
  * Schedule
  * History
  * Profile

### 5. Service Detail Screen

Isi:

* Nama layanan
* Deskripsi layanan
* Cakupan pekerjaan
* Estimasi durasi
* Harga mulai dari
* Button “Pesan Sekarang”

### 6. Booking Form Screen

Isi:

* Pilih alamat
* Pilih tanggal
* Pilih jam
* Pilih ukuran rumah/kamar
* Catatan tambahan
* Button “Lihat Estimasi Biaya”

### 7. Price Estimation Screen

Isi:

* Detail layanan
* Alamat
* Tanggal dan jam
* Estimasi durasi
* Estimasi biaya
* Biaya tambahan jika ada
* Total biaya
* Button “Pilih Petugas”

### 8. Cleaner Selection Screen

Isi:

* Daftar petugas terdekat
* Foto profil petugas
* Nama petugas
* Rating
* Jumlah pekerjaan selesai
* Estimasi waktu kedatangan
* Button “Pilih”

### 9. Order Confirmation Screen

Isi:

* Ringkasan pesanan
* Petugas terpilih
* Estimasi biaya
* Metode pembayaran
* Button “Konfirmasi Pesanan”

### 10. Active Order / Tracking Screen

Isi:

* Status pesanan
* Map view
* Lokasi petugas
* Estimasi waktu kedatangan
* Timeline status:

  * Pesanan diterima
  * Petugas menuju lokasi
  * Petugas tiba
  * Pekerjaan berlangsung
  * Selesai
* Button chat/call petugas

### 11. Rating & Review Screen

Isi:

* Foto/nama petugas
* Rating bintang
* Text area ulasan
* Checklist kualitas layanan:

  * Tepat waktu
  * Ramah
  * Bersih
  * Profesional
* Button “Kirim Review”

### 12. Routine Schedule Screen

Isi:

* Pilihan frekuensi:

  * Mingguan
  * Dua minggu sekali
  * Bulanan
* Pilih layanan
* Pilih alamat
* Pilih hari dan jam
* Ringkasan jadwal
* Button “Aktifkan Jadwal Rutin”

### 13. Booking History Screen

Isi:

* List riwayat pesanan
* Status selesai/dibatalkan
* Total biaya
* Tanggal layanan
* Button “Pesan Lagi”

### 14. Profile Screen

Isi:

* Foto profil
* Nama pengguna
* Nomor HP/email
* Alamat tersimpan
* Metode pembayaran
* Bantuan
* Tentang aplikasi
* Logout

## 8. Partner App Screens — Mitra Petugas

Buat versi sederhana untuk mitra petugas.

### 1. Partner Home Screen

Isi:

* Greeting petugas
* Status online/offline
* Jumlah pesanan hari ini
* Pendapatan hari ini
* Rating petugas
* Pesanan masuk

### 2. Incoming Order Screen

Isi:

* Nama pelanggan
* Lokasi pelanggan
* Jenis layanan
* Estimasi biaya
* Estimasi durasi
* Button “Terima Pesanan”
* Button “Tolak”

### 3. Job Detail Screen

Isi:

* Detail layanan
* Alamat pelanggan
* Catatan pelanggan
* Navigasi ke lokasi
* Button ubah status:

  * Menuju lokasi
  * Tiba di lokasi
  * Mulai pekerjaan
  * Selesai

### 4. Partner Review Screen

Isi:

* Daftar ulasan dari pelanggan
* Rating rata-rata
* Komentar pelanggan

## 9. Interaction Requirements

Prototype harus memiliki interaksi dasar:

* Button onboarding menuju login.
* Login menuju Home.
* Home menuju Service Detail.
* Service Detail menuju Booking Form.
* Booking Form menuju Price Estimation.
* Price Estimation menuju Cleaner Selection.
* Cleaner Selection menuju Order Confirmation.
* Order Confirmation menuju Tracking Screen.
* Tracking Screen menuju Rating Screen.
* Bottom navigation berpindah antar halaman utama.
* Routine Schedule dapat dikonfirmasi.
* History dapat membuka detail pesanan.

## 10. UX Writing

Gunakan bahasa Indonesia yang ramah dan jelas.

Contoh microcopy:

* “Pesan layanan kebersihan dengan mudah.”
* “Petugas terpercaya di sekitar lokasi Anda.”
* “Lihat estimasi biaya sebelum memesan.”
* “Pantau kedatangan petugas secara real-time.”
* “Jadwalkan kebersihan rutin tanpa ribet.”
* “Pesanan Anda berhasil dibuat.”
* “Bagaimana pengalaman Anda menggunakan layanan ini?”

## 11. Prototype Priority

Prioritas utama desain:

1. Customer app
2. Booking flow
3. Price estimation
4. Tracking petugas
5. Rating dan review
6. Jadwal rutin
7. Partner app sederhana

## 12. Output Expected

Buat prototype UI/UX mobile app dengan gaya modern, clean, dan profesional. Fokus pada pengalaman pengguna yang mudah, cepat, transparan, dan terpercaya. Gunakan layout mobile portrait dengan tampilan yang siap dipresentasikan untuk laporan akademik.
