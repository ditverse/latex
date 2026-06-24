# SOFTWARE REQUIREMENTS SPECIFICATION
## Platform PasarKita — Marketplace Digital UMKM

| Atribut | Nilai |
|---|---|
| Nama Dokumen | Software Requirements Specification (SRS) Platform PasarKita Marketplace Digital UMKM |
| Versi | 1.0 — Initial Requirements Baseline |
| Tanggal | [Tanggal Penyelesaian] |
| Sistem | PasarKita / Demand Generator B2C — Ekosistem UMKM RPL 2 |
| Pemilik Produk | Kelompok 2 — Mata Kuliah Rekayasa Perangkat Lunak 2 |
| Dosen Pembimbing | M. Yusril Helmi Setyawan, S.Kom., M.Kom. |
| Target Pembaca | Product owner, developer, QA engineer, maintainer, dan administrator operasional |
| Status | Dokumen kerja untuk baseline requirement dan validasi implementasi |

**Basis Penyusunan**

SRS ini disusun dari kode dan konfigurasi aplikasi yang aktif: modul backend pada `backend/src/modules/` (auth, products, orders, checkout, integrations); skema database Supabase PostgreSQL pada `backend/database/schema/000_full_schema.sql`; konfigurasi deployment Vercel; serta kontrak integrasi dengan API Gateway (Kelompok 7), SmartBank (Kelompok 1), dan LogistiKita (Kelompok 5). Struktur dokumen mengikuti pola SRS standar: tujuan, scope, konteks sistem, aktor, constraint, kebutuhan spesifik, interface, data, business rules, risiko, acceptance criteria, dan traceability.

---

## Daftar Isi

| Bagian | Isi |
|---|---|
| 1 | Pendahuluan dan Konteks Dokumen |
| 2 | Gambaran Produk dan Batas Sistem |
| 3 | Konteks Operasional dan Arsitektur |
| 4 | Domain Data dan Aturan Bisnis |
| 5 | Kebutuhan Fungsional |
| 6 | Kebutuhan Non-Fungsional |
| 7 | Antarmuka Eksternal |
| 8 | Workflow Operasional |
| 9 | Risiko, Kontrol, dan Acceptance Criteria |
| 10 | Matriks Ketertelusuran |
| Lampiran | Glosarium, Referensi Internal, dan Catatan Implementasi |

---

## 1. Pendahuluan dan Konteks Dokumen

### 1.1 Tujuan Dokumen

**Dokumen ini mendefinisikan kebutuhan perangkat lunak untuk PasarKita sebagai komponen Demand Generator B2C dalam ekosistem microservices UMKM RPL 2.**

SRS ini berfungsi sebagai baseline bersama antara pemilik produk, pengembang, penguji, dan pengelola sistem. Dokumen tidak dimaksudkan sebagai uraian konseptual, melainkan sebagai spesifikasi yang menerjemahkan perilaku aplikasi ke dalam kebutuhan yang dapat dibangun, diuji, dan dipelihara. Setiap kebutuhan dirumuskan agar memiliki ruang lingkup yang jelas, dasar implementasi yang dapat ditelusuri, dan kriteria penerimaan yang dapat diverifikasi.

Rujukan format yang digunakan adalah praktik SRS yang umum dipakai di lingkungan pengembangan perangkat lunak: dokumen dimulai dari tujuan dan scope, dilanjutkan dengan product perspective, user classes, constraints, asumsi, kebutuhan fungsional, kebutuhan non-fungsional, external interfaces, data requirements, business rules, acceptance criteria, dan traceability matrix. Dengan struktur tersebut, dokumen dapat dipakai sebagai kontrak kerja teknis tanpa bergantung pada penjelasan lisan.

### 1.2 Ruang Lingkup Produk

PasarKita adalah platform marketplace digital B2C yang memfasilitasi transaksi produk UMKM antara seller dan buyer. Sistem berjalan sebagai aplikasi web fullstack dengan frontend Next.js 16.2 (di-deploy ke `pasarkita.vercel.app`) dan backend Express.js berbasis serverless (di-deploy ke `pasarkita-api.vercel.app`), menggunakan Supabase PostgreSQL sebagai database.

Dalam arsitektur ekosistem, PasarKita berperan sebagai **Demand Generator** — inisiator transaksi di sisi permintaan. Semua transaksi keuangan diproses oleh SmartBank (Kelompok 1), semua komunikasi antar service melewati API Gateway (Kelompok 7), dan pengiriman dikoordinasikan oleh LogistiKita (Kelompok 5). PasarKita tidak mengambil alih fungsi pembayaran, routing, atau logistik dari service partner tersebut.

Sistem PasarKita bertanggung jawab pada siklus transaksi marketplace: registrasi/autentikasi user, pengelolaan katalog produk UMKM, keranjang belanja, proses checkout dengan kalkulasi fee, koordinasi pembayaran ke SmartBank, trigger pengiriman ke LogistiKita, manajemen status order, dan dashboard analytics untuk superadmin.

### 1.3 Out of Scope

Dokumen ini tidak menspesifikasikan logika pembayaran internal SmartBank, mekanisme routing JWT API Gateway, algoritma penentuan tarif pengiriman LogistiKita, ataupun manajemen akun dari service partner lain.

| Area | Status Scope | Rasional |
|---|---|---|
| Pemrosesan pembayaran | Di luar scope | Seluruh transaksi keuangan diproses SmartBank melalui API Gateway. PasarKita hanya mengirim payment request dan membaca response. |
| Routing dan JWT validation (inter-service) | Di luar scope | API Gateway (Kelompok 7) bertanggung jawab atas routing, JWT issuance antar service, dan logging inter-service. |
| Kalkulasi tarif dan tracking pengiriman internal | Di luar scope | LogistiKita (Kelompok 5) mengelola logika pengiriman. PasarKita hanya men-trigger dan membaca tracking_id. |
| Manajemen stok supplier | Di luar scope | SupplierHub (Kelompok 4) mengelola supply chain. PasarKita hanya membaca stok lokal dari database sendiri. |
| Laporan keuangan konsolidasi ekosistem | Di luar scope | UMKM Insight (Kelompok 6) mengonsumsi ledger dari SmartBank. PasarKita hanya menyediakan data transaksi lokal via analytics endpoint. |
| Manajemen produk CRUD seller (WarungPOS) | Di luar scope | WarungPOS (Kelompok 3) memiliki katalog tersendiri. PasarKita mengelola katalog produk seller yang terdaftar di platformnya sendiri. |
| Manajemen saldo dompet user | Di dalam scope (partial) | PasarKita menyimpan snapshot saldo lokal dari SmartBank untuk keperluan validasi awal, namun authoritative balance tetap di SmartBank. |
| Katalog produk, order, dan ulasan | Di dalam scope | PasarKita adalah system of record untuk produk, order, order_items, dan ratings dalam ekosistemnya. |

---

## 2. Gambaran Produk dan Batas Sistem

### 2.1 Product Perspective

Aplikasi ini menempati posisi sebagai **Demand Generator B2C** dalam ekosistem microservices UMKM RPL 2. Secara teknis, frontend berjalan di `pasarkita.vercel.app` (Next.js 16.2) dan backend di `pasarkita-api.vercel.app` (Express.js serverless), keduanya di-deploy terpisah dari repo monorepo yang sama. Database menggunakan Supabase PostgreSQL yang diakses eksklusif oleh backend PasarKita.

Semua komunikasi ke service eksternal (SmartBank, LogistiKita) melewati API Gateway (Kelompok 7) dengan JWT. Untuk keperluan development lokal, tersedia mock server di direktori `mock/` yang mensimulasikan SmartBank (:4001) dan LogistiKita (:4002).

> *[Gambar 1: Diagram konteks sistem — posisi PasarKita dalam ekosistem, relasi ke API Gateway, SmartBank, LogistiKita, SupplierHub, WarungPOS, dan UMKM Insight]*

### 2.2 User Classes dan Karakteristik

Sistem melayani beberapa kelas pengguna dengan hak dan ekspektasi yang berbeda. Kebutuhan sistem harus menjaga perbedaan tersebut agar transaksi marketplace dapat berjalan tanpa mencampuri domain service lain dalam ekosistem.

| User Class | Tanggung Jawab | Ekspektasi Sistem | Kontrol Akses |
|---|---|---|---|
| Buyer | Menelusuri produk, menambahkan ke keranjang, melakukan checkout, memantau status order, dan memberikan ulasan. | Alur belanja yang mudah, status order real-time, konfirmasi pembayaran jelas, riwayat pesanan tersedia. | JWT role `buyer`; tidak dapat mengelola produk atau melihat analytics. |
| Seller | Mengelola katalog produk sendiri (CRUD), memantau order masuk, mengelola stok, dan membalas ulasan. | Dashboard produk yang efisien, notifikasi order baru, visibilitas stok rendah. | JWT role `seller`; hanya dapat CRUD produk milik sendiri; tidak dapat mengakses data seller lain. |
| Superadmin | Memantau seluruh operasional platform: manajemen user, order, analytics, moderasi konten, dan audit log. | Dashboard analytics lengkap, kemampuan ban/aktifkan user, update status order manual, akses audit log. | JWT role `superadmin`; dibuat via insert manual ke Supabase; akses penuh ke semua endpoint admin. |
| API Gateway | Memvalidasi JWT antar service, meneruskan payment request ke SmartBank, dan trigger ke LogistiKita. | Kontrak JSON stabil, error response deterministik, idempotency key pada checkout. | Service-to-service via header JWT ekosistem; bukan user biasa. |
| SmartBank | Memproses pembayaran dan mengembalikan transaction_id atau failure response. | Format request konsisten, idempotency terjaga, rollback stok saat pembayaran gagal. | Akses melalui API Gateway; tidak ada akses langsung ke database PasarKita. |

### 2.3 Operating Environment

| Komponen | Spesifikasi Saat Ini | Implikasi Requirement |
|---|---|---|
| Frontend | Next.js 16.2, App Router, TypeScript, Tailwind CSS, shadcn/ui, di-deploy ke Vercel (`frontend/`). | Routing berbasis App Router; komponen UI harus konsisten dengan shadcn/ui design system. |
| Backend | Express.js dengan serverless-http, di-deploy ke Vercel serverless function (`backend/api/index.js`). | Tidak ada persistent in-memory state; semua state harus tersimpan di database. |
| Database | Supabase PostgreSQL, diakses via Supabase SDK dan service role key dari backend. | Skema harus menjaga users, products, orders, order_items, ratings, notifications, vouchers, dan audit logs. |
| State Management | Zustand (auth, cart) dan TanStack Query di frontend. | Cart state bersifat client-side; sinkronisasi stok terjadi saat checkout di backend. |
| Auth | JWT yang di-generate backend PasarKita saat login; validasi JWT antar service via API Gateway. | Token harus menyertakan role; middleware auth harus memvalidasi sebelum setiap protected route. |
| Integrasi Ekosistem | API Gateway di `GATEWAY_BASE_URL`; SmartBank dan LogistiKita diakses via Gateway. | Koneksi eksternal harus gagal secara terkendali dan tidak merusak data order lokal. |
| Mock Server (dev) | Express.js lokal di `mock/smartbank/:4001` dan `mock/logistikita/:4002`. | Hanya digunakan saat `NODE_ENV=development`; production selalu melalui `GATEWAY_BASE_URL`. |
| Deploy | Dua project Vercel terpisah dari satu repo monorepo (`frontend/` dan `backend/`). | Environment variables harus dikonfigurasi terpisah per project di Vercel. |

---

## 3. Konteks Operasional dan Arsitektur

### 3.1 Architectural Overview

Aplikasi menggunakan arsitektur **monorepo dua-tier** dengan pemisahan frontend dan backend yang di-deploy secara independen. Backend menggunakan pola modular berbasis domain (`src/modules/`) dengan middleware terpusat untuk auth, validasi, dan error handling. Frontend menggunakan App Router Next.js dengan komponen shadcn/ui dan state management Zustand.

| Lapisan | Artefak Utama | Tanggung Jawab |
|---|---|---|
| Frontend — Routing | `frontend/app/` (App Router) | Mengarahkan halaman ke komponen React berdasarkan URL. |
| Frontend — UI Components | `frontend/components/` | Menyajikan halaman buyer (katalog, cart, checkout, order), seller (dashboard, CRUD produk), dan admin (analytics, user management). |
| Frontend — State | `frontend/store/` (Zustand) | Mengelola auth state (user, token) dan cart state (items, quantity) secara client-side. |
| Frontend — API Client | `frontend/lib/` | Wrapper Axios/fetch ke backend API dengan token injection dari Zustand auth store. |
| Backend — Entry Point | `backend/api/index.js` | Serverless entry point; mounting semua router Express. |
| Backend — Modules | `backend/src/modules/` (auth, products, orders, checkout, integrations) | Business logic per domain: autentikasi, katalog produk, manajemen order, alur checkout, dan komunikasi ke service eksternal. |
| Backend — Middlewares | `backend/src/middlewares/` (auth, validate, errorHandler) | Validasi JWT, validasi Zod schema request body, dan centralized error response. |
| Backend — Integrations | `backend/src/integrations/` (smartbank, logistikita) | Adapter HTTP untuk komunikasi ke SmartBank dan LogistiKita via API Gateway. |
| Backend — Utils | `backend/src/utils/` (fee, response) | Kalkulasi fee marketplace (2%), helper format response JSON standar. |
| Database | Supabase PostgreSQL | Penyimpanan persisten untuk semua entitas domain PasarKita. |

### 3.2 Data Flow

Alur utama dimulai dari registrasi atau login user di frontend. Setelah autentikasi, buyer menelusuri produk, menambahkan ke cart (state Zustand), dan melakukan checkout. Saat checkout, backend memvalidasi stok, menghitung total + fee 2%, membuat order dengan status `pending`, lalu mengirim payment request ke SmartBank via API Gateway.

> *[Gambar 2: Sequence diagram alur checkout — dari Buyer submit → Backend → Supabase → API Gateway → SmartBank → (sukses) LogistiKita → konfirmasi order `paid`]*

Jika pembayaran sukses, backend memperbarui order ke status `paid`, mengirim trigger pengiriman ke LogistiKita, menerima `tracking_id`, dan mencatat notifikasi. Jika gagal, stok di-rollback dan order diperbarui ke `payment_failed`. Superadmin dapat memantau seluruh alur melalui analytics endpoint dan audit log.

---

## 4. Domain Data dan Aturan Bisnis

### 4.1 Core Domain Entities

| Entitas | Deskripsi | Field Penting | Catatan Ownership |
|---|---|---|---|
| `users` | Akun buyer, seller, dan superadmin. | `id`, `name`, `email`, `password_hash`, `role`, `is_active`, `phone`, `avatar_url` | PasarKita adalah system of record untuk akun user dalam ekosistemnya. Saldo dikelola SmartBank. |
| `seller_profiles` | Profil toko milik seller. | `seller_id`, `store_name`, `logo_url`, `description` | Dibuat otomatis saat seller register; dapat diedit oleh seller bersangkutan. |
| `products` | Katalog produk yang dijual seller. | `id`, `seller_id`, `name`, `description`, `category`, `price`, `stock`, `is_active`, `image_url`, `minimum_stock`, `is_low_stock` | Dikelola seller; superadmin dapat menonaktifkan. |
| `orders` | Transaksi pembelian dari buyer. | `id`, `buyer_id`, `status`, `subtotal`, `fee_marketplace`, `total`, `shipping_address`, `transaction_id`, `tracking_id`, `idempotency_key` | Dibuat saat checkout; status diperbarui berdasarkan respons SmartBank dan LogistiKita. |
| `order_items` | Detail item dalam satu order. | `order_id`, `product_id`, `qty`, `price_at_purchase`, `product_name_at_purchase`, `product_discount_per_unit` | Snapshot harga saat transaksi; tidak berubah meski harga produk berubah setelah order. |
| `order_status_history` | Riwayat perubahan status order. | `order_id`, `status`, `actor_id`, `source`, `note`, `created_at` | Digunakan untuk audit trail setiap perubahan status order. |
| `ratings` | Ulasan buyer terhadap produk setelah order selesai. | `order_id`, `product_id`, `buyer_id`, `rating`, `comment`, `image_urls`, `seller_reply` | Hanya dapat dibuat oleh buyer yang memiliki order `delivered` untuk produk bersangkutan. |
| `notifications` | Notifikasi in-app untuk semua role. | `user_id`, `order_id`, `type`, `title`, `message`, `href`, `read_at` | Di-generate backend saat event order (paid, shipped, delivered, rating). |
| `vouchers` | Kode diskon untuk buyer. | `code`, `discount_type`, `discount_value`, `min_purchase`, `max_uses`, `valid_until` | Dikelola superadmin; dapat berupa persentase atau nominal tetap. |
| `product_discounts` | Diskon langsung pada produk tertentu. | `product_id`, `discount_type`, `discount_value`, `valid_from`, `valid_until` | Dikelola seller; diperhitungkan saat kalkulasi subtotal. |
| `admin_audit_logs` | Catatan aksi administratif superadmin. | `actor_id`, `action`, `target_type`, `target_id`, `reason`, `before_data`, `after_data` | Di-generate otomatis setiap aksi sensitif superadmin (ban user, update status, dsb). |
| `integration_logs` | Log komunikasi ke service eksternal. | `service`, `operation`, `success`, `duration_ms`, `order_id`, `status_code`, `error_code` | Digunakan untuk monitoring kesehatan integrasi SmartBank dan LogistiKita. |

### 4.2 Business Rules

| ID | Aturan Bisnis | Dampak Implementasi |
|---|---|---|
| BR-01 | Fee marketplace adalah 2% dari subtotal, dibebankan ke buyer pada setiap transaksi. | `backend/src/utils/fee.js` menghitung `fee_marketplace = Math.ceil(subtotal * 0.02)`; frontend menampilkan rincian fee sebelum konfirmasi. |
| BR-02 | Saldo awal setiap user baru yang didaftarkan di SmartBank adalah Rp 50.000. | Backend harus memanggil SmartBank untuk inisiasi saldo saat registrasi berhasil; failure handling jika SmartBank tidak tersedia. |
| BR-03 | Maksimum transaksi adalah 10x per user per hari dengan cooldown 10–30 detik antar transaksi. | Backend memvalidasi frekuensi transaksi via query `orders` sebelum proses checkout; rate limiting diterapkan di middleware. |
| BR-04 | Stok harus divalidasi dan di-reserve sebelum payment request dikirim ke SmartBank. | Checkout module memvalidasi stok per item, men-set `stock_reserved = true` pada order `pending`, dan me-rollback stok jika pembayaran gagal. |
| BR-05 | Semua komunikasi ke SmartBank dan LogistiKita pada environment production harus melalui `GATEWAY_BASE_URL`. | Integrations module membaca `NODE_ENV`; jika `development` menggunakan mock URL, jika production menggunakan `GATEWAY_BASE_URL`. |
| BR-06 | Idempotency key wajib digunakan pada setiap checkout request untuk mencegah double order. | Backend menghasilkan dan menyimpan `idempotency_key` (UUID) per checkout; request duplikat dengan key yang sama mengembalikan order yang sudah ada. |
| BR-07 | Buyer hanya dapat memberikan rating setelah order memiliki status `delivered`. | Ratings module memvalidasi status order sebelum menerima rating submission; satu order satu rating per produk. |
| BR-08 | Seller hanya dapat mengelola (CRUD) produk miliknya sendiri. | Products module memvalidasi `seller_id` dari JWT sama dengan `seller_id` pada produk sebelum izinkan update/delete. |
| BR-09 | Superadmin tidak dapat mendaftarkan diri sendiri via API registrasi publik. | Role `superadmin` hanya dapat dibuat via insert manual ke Supabase; endpoint `/api/auth/register` hanya menerima role `buyer` atau `seller`. |
| BR-10 | Harga `price_at_purchase` pada `order_items` adalah snapshot harga saat transaksi dan tidak boleh berubah. | Saat order dibuat, harga produk disalin ke `price_at_purchase`; perubahan harga produk setelahnya tidak memengaruhi order yang sudah ada. |

---

## 5. Kebutuhan Fungsional

Kebutuhan fungsional ditulis dengan bentuk *shall statement* agar dapat menjadi dasar implementasi dan pengujian. Prioritas **Must** menunjukkan kemampuan inti rilis operasional; **Should** menunjukkan kemampuan penting yang memperkuat operasi; **Could** menunjukkan peningkatan lanjutan.

| ID | Area | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|---|
| FR-01 | Authentication — Register | Sistem shall menyediakan endpoint registrasi user dengan role `buyer` atau `seller`, memvalidasi input dengan Zod, dan menyimpan password dalam bentuk hash. | Must | User baru tersimpan di `users` dengan `password_hash`; role selain `buyer`/`seller` ditolak dengan pesan eksplisit. |
| FR-02 | Authentication — Login | Sistem shall menyediakan endpoint login yang memverifikasi kredensial dan mengembalikan JWT berisi `user_id`, `role`, dan `exp`. | Must | Login dengan kredensial valid mengembalikan JWT; kredensial salah mengembalikan 401 tanpa membocorkan detail database. |
| FR-03 | Seller Profile | Sistem shall membuat seller_profile secara otomatis saat seller berhasil registrasi, dan memungkinkan seller memperbarui `store_name`, `logo_url`, dan `description`. | Must | `seller_profiles` terisi setelah registrasi seller; update profil tersimpan dan terbaca di halaman toko. |
| FR-04 | Product Catalog — Browse | Sistem shall menyediakan endpoint GET `/api/products` dengan filter kategori, search nama, dan pagination untuk semua role termasuk guest. | Must | Response mengembalikan array produk aktif dengan field lengkap; filter dan pagination berfungsi sesuai parameter query. |
| FR-05 | Product Catalog — Detail | Sistem shall menyediakan endpoint GET `/api/products/:id` yang mengembalikan detail produk termasuk informasi seller dan rata-rata rating. | Must | Response berisi data produk, `store_name` seller, `avg_rating`, dan `total_reviews`. |
| FR-06 | Product Management — CRUD | Sistem shall memungkinkan seller membuat, memperbarui, dan menghapus (soft delete via `is_active = false`) produk miliknya sendiri, dengan validasi `price > 0` dan `stock >= 0`. | Must | Seller hanya dapat CRUD produk dengan `seller_id` miliknya; akses ke produk seller lain menghasilkan 403. |
| FR-07 | Product Discount | Sistem should memungkinkan seller mengatur diskon langsung pada produk (`product_discounts`) dengan periode validitas dan tipe (persentase/nominal). | Should | Diskon aktif terperhitungkan dalam kalkulasi subtotal saat checkout; diskon kedaluwarsa diabaikan. |
| FR-08 | Cart | Sistem shall mengelola keranjang belanja di sisi frontend (Zustand), termasuk tambah item, ubah kuantitas, dan hapus item, dengan validasi stok saat checkout. | Must | Cart state tersimpan di Zustand; stok divalidasi ulang di backend saat checkout request dikirim. |
| FR-09 | Checkout & Payment | Sistem shall memproses checkout dengan langkah: validasi stok → kalkulasi total + fee 2% → buat order pending → kirim payment request ke SmartBank via Gateway → update status order berdasarkan response. | Must | Order `paid` muncul setelah SmartBank sukses; order `payment_failed` dan stok di-rollback jika SmartBank gagal. |
| FR-10 | Idempotency Checkout | Sistem shall menerapkan idempotency key pada setiap checkout untuk mencegah double order akibat retry request. | Must | Request checkout duplikat dengan key yang sama mengembalikan order yang sudah ada tanpa membuat order baru. |
| FR-11 | Shipping Trigger | Sistem shall mengirimkan trigger pengiriman ke LogistiKita via API Gateway setelah order berhasil dibayar, dan menyimpan `tracking_id` yang diterima. | Must | Order `paid` memiliki `tracking_id` terisi; kegagalan trigger pengiriman dicatat di `integration_logs` dan tidak membatalkan order. |
| FR-12 | Fee Simulation | Sistem should menyediakan endpoint POST `/api/fee/calculate` untuk simulasi kalkulasi fee tanpa melakukan transaksi nyata. | Should | Response mengembalikan `subtotal`, `fee_marketplace`, `fee_discount`, `voucher_discount`, dan `total` berdasarkan input. |
| FR-13 | Voucher | Sistem should memungkinkan buyer menggunakan kode voucher saat checkout dengan validasi `min_purchase`, `max_uses`, dan `valid_until`. | Should | Diskon voucher terperhitungkan pada field `voucher_discount` di order; voucher habis/kedaluwarsa ditolak dengan pesan eksplisit. |
| FR-14 | Order Management — Buyer | Sistem shall menyediakan endpoint GET `/api/orders` dan GET `/api/orders/:id` bagi buyer untuk melihat daftar dan detail order miliknya. | Must | Buyer hanya melihat order milik sendiri; akses ke order buyer lain menghasilkan 403. |
| FR-15 | Order Management — Seller | Sistem shall menyediakan akses seller ke order yang mengandung produk miliknya, termasuk status dan informasi pengiriman. | Must | Seller dapat melihat order masuk yang berisi produknya; informasi buyer ditampilkan sesuai kebutuhan fulfillment. |
| FR-16 | Order Status Update | Sistem shall memungkinkan superadmin memperbarui status order secara manual dan mencatat perubahan ke `order_status_history`. | Must | Perubahan status tersimpan di `orders` dan `order_status_history` dengan `actor_id` superadmin dan timestamp. |
| FR-17 | Ratings & Reviews | Sistem shall memungkinkan buyer memberikan rating (1–5) dan komentar untuk produk yang sudah diterima (`status = delivered`), dan memungkinkan seller membalas ulasan. | Must | Rating tersimpan setelah validasi status order; `seller_reply` dapat diperbarui seller; rata-rata rating terhitung di endpoint produk. |
| FR-18 | Notifications | Sistem should men-generate notifikasi in-app untuk event order (paid, shipped, delivered) dan rating, dapat ditandai sebagai sudah dibaca. | Should | Notifikasi muncul di daftar user yang relevan; endpoint PATCH menandai `read_at`; notifikasi tidak dibaca ditampilkan sebagai badge. |
| FR-19 | Admin — User Management | Sistem shall menyediakan superadmin kemampuan untuk melihat semua user, ban (set `is_active = false`), dan mengaktifkan kembali user dengan alasan yang tercatat di `admin_audit_logs`. | Must | Status user berubah setelah aksi admin; aksi tercatat di audit log dengan `before_data` dan `after_data`. |
| FR-20 | Admin — Analytics Dashboard | Sistem shall menyediakan endpoint GET `/api/admin/analytics` yang mengembalikan metrik platform: total revenue, total order, distribusi status order, produk terlaris, dan revenue per seller. | Must | Response mengembalikan data agregat akurat; dashboard admin menampilkan visualisasi metrik tanpa query manual. |
| FR-21 | Integration Health Check | Sistem should menyediakan endpoint internal admin untuk memeriksa status koneksi ke API Gateway, SmartBank, dan LogistiKita. | Should | Endpoint mengembalikan status `online`/`offline`, `http_code`, `response_ms`, dan `last_checked_at` per service. |
| FR-22 | Low Stock Alert | Sistem should menampilkan indikator stok rendah pada produk yang memiliki `stock <= minimum_stock` di dashboard seller. | Should | `is_low_stock` ter-update secara otomatis; dashboard seller menampilkan badge peringatan pada produk yang relevan. |

---

## 6. Kebutuhan Non-Fungsional

Kebutuhan non-fungsional menentukan kualitas sistem yang harus dipenuhi di luar perilaku fitur langsung. Kategori ini penting karena sistem memproses transaksi keuangan nyata dalam ekosistem microservices multi-kelompok.

| ID | Quality Attribute | Requirement | Verification |
|---|---|---|---|
| NFR-01 | Security — Password | Sistem shall menyimpan password dalam bentuk hash (bcrypt) dan tidak pernah mengembalikan `password_hash` dalam response API. | Audit endpoint user; tidak ada `password_hash` di response. |
| NFR-02 | Security — JWT | Sistem shall memvalidasi JWT pada setiap protected route sebelum memproses request; token kedaluwarsa atau tidak valid mengembalikan 401. | Request tanpa token atau dengan token tidak valid ditolak secara konsisten. |
| NFR-03 | Access Control | Buyer hanya mengakses resource miliknya; seller hanya mengelola produk miliknya; superadmin memiliki akses penuh; endpoint admin dilindungi middleware role check. | Cross-role access menghasilkan 403; test dengan token berbeda role. |
| NFR-04 | Data Integrity — Checkout | Sistem shall memastikan atomicity pada proses checkout: stok tidak berkurang jika payment gagal; order tidak dibuat jika validasi stok gagal. | Simulasi payment failure; verifikasi stok tidak berubah dan order tidak terbuat. |
| NFR-05 | Interoperability | Kontrak JSON API PasarKita shall mempertahankan backward compatibility; field yang dikonsumsi service lain tidak boleh dihapus atau diubah tipenya tanpa koordinasi. | Service partner masih dapat membaca response API setelah perubahan; field baru bersifat additive. |
| NFR-06 | Availability | Sistem shall dapat di-deploy dan berjalan di Vercel (frontend + backend project terpisah) dengan environment variables yang terdokumentasi. | `vercel.json` mengonfigurasi routing dengan benar; kedua project dapat di-deploy dari repo yang sama. |
| NFR-07 | Failure Handling | Kegagalan koneksi ke API Gateway, SmartBank, atau LogistiKita shall menghasilkan error response yang terkendali dan dicatat di `integration_logs`; tidak menghentikan seluruh sistem. | Matikan mock service; verifikasi error response bermakna dan log tercatat. |
| NFR-08 | Maintainability | Kode backend shall mempertahankan pemisahan modular berbasis domain sehingga logika bisnis, integrasi eksternal, dan middleware tidak bercampur. | Modul domain tetap berada di `src/modules/`; integrasi di `src/integrations/`; middleware di `src/middlewares/`. |
| NFR-09 | Auditability | Setiap aksi sensitif superadmin shall menulis `admin_audit_logs` dengan `before_data` dan `after_data` untuk keperluan audit trail. | Aksi ban user dan update status order menghasilkan entri audit log yang dapat ditelusuri. |
| NFR-10 | Usability | Alur checkout shall menampilkan rincian harga (subtotal, fee, diskon, total) secara eksplisit sebelum konfirmasi pembayaran. | Fee breakdown terlihat di halaman review order; tidak ada biaya tersembunyi. |
| NFR-11 | Performance | Endpoint katalog produk should mengembalikan response di bawah 2 detik untuk halaman pertama dengan 50 item tanpa filter berat. | Load test dengan 50 produk; response time diukur dari client. |
| NFR-12 | Privacy | Data sensitif user (email, phone, password_hash) shall tidak ditampilkan kepada user lain kecuali superadmin pada konteks manajemen user yang sah. | Endpoint produk dan order tidak mengembalikan data sensitif seller/buyer secara berlebihan. |

---

## 7. Antarmuka Eksternal

### 7.1 User Interface Requirements

UI harus mendukung pekerjaan operasional yang berbeda per role: buyer menelusuri dan membeli produk, seller mengelola katalog dan order masuk, superadmin memantau platform secara keseluruhan. Karena itu halaman tidak hanya berfungsi sebagai form, tetapi juga sebagai control surface untuk status transaksi, stok, dan kesehatan integrasi.

| UI / Route | Primary User | Requirement |
|---|---|---|
| `/` | Semua / Guest | Landing page harus menampilkan katalog produk unggulan, banner promo, dan akses login/register. |
| `/auth/login` dan `/auth/register` | Semua | Halaman auth harus jelas membedakan opsi register sebagai buyer atau seller; tidak ada opsi superadmin. |
| `/products` | Buyer / Guest | Halaman katalog harus mendukung filter kategori, search, sorting harga, dan pagination. |
| `/products/:id` | Buyer / Guest | Halaman detail produk harus menampilkan gambar, deskripsi, harga, stok, info toko, dan daftar ulasan. |
| `/cart` | Buyer | Halaman keranjang harus menampilkan item, kuantitas (editable), subtotal per item, dan tombol checkout. |
| `/checkout` | Buyer | Halaman checkout harus menampilkan ringkasan order, kolom alamat pengiriman, input voucher, fee breakdown lengkap, dan tombol konfirmasi bayar. |
| `/orders` dan `/orders/:id` | Buyer | Halaman order harus menampilkan status terkini, tracking info, dan opsi review setelah `delivered`. |
| `/seller/dashboard` | Seller | Dashboard seller harus menampilkan ringkasan produk aktif, stok rendah, dan order masuk terbaru. |
| `/seller/products` | Seller | Halaman manajemen produk harus mendukung CRUD produk dengan form validasi dan upload gambar. |
| `/seller/orders` | Seller | Halaman order seller menampilkan order masuk dengan filter status dan detail item per order. |
| `/admin` | Superadmin | Dashboard admin harus menampilkan metrik platform: total revenue, order count, user aktif, dan grafik tren. |
| `/admin/users` | Superadmin | Halaman manajemen user menampilkan semua user dengan aksi ban/aktifkan dan input alasan. |
| `/admin/orders` | Superadmin | Halaman order admin menampilkan semua order dengan kemampuan filter status dan update manual. |
| `/admin/analytics` | Superadmin | Halaman analytics menampilkan produk terlaris, revenue per seller, distribusi kategori, dan tren transaksi. |

### 7.2 API Requirements

| Endpoint | Method | Auth | Deskripsi |
|---|---|---|---|
| `/api/auth/register` | POST | — | Registrasi user baru; role `buyer` atau `seller`. |
| `/api/auth/login` | POST | — | Login; mengembalikan JWT. |
| `/api/products` | GET | — | Browse semua produk aktif; mendukung filter dan pagination. |
| `/api/products/:id` | GET | — | Detail produk termasuk rating agregat. |
| `/api/products` | POST | seller | Tambah produk baru milik seller. |
| `/api/products/:id` | PUT | seller / superadmin | Edit produk; seller hanya produk milik sendiri. |
| `/api/products/:id` | DELETE | seller / superadmin | Soft delete produk (`is_active = false`). |
| `/api/checkout` | POST | buyer | Proses checkout lengkap termasuk payment request ke SmartBank. |
| `/api/fee/calculate` | POST | — | Simulasi kalkulasi fee dan diskon tanpa transaksi. |
| `/api/orders` | GET | buyer / seller / superadmin | Daftar order; difilter berdasarkan role yang request. |
| `/api/orders/:id` | GET | buyer / seller / superadmin | Detail order termasuk items dan status history. |
| `/api/orders/:id/status` | PATCH | superadmin | Update status order manual. |
| `/api/orders/:id/ratings` | POST | buyer | Submit rating setelah order `delivered`. |
| `/api/admin/users` | GET | superadmin | Semua user dengan filter dan pagination. |
| `/api/admin/users/:id/status` | PATCH | superadmin | Ban atau aktifkan user. |
| `/api/admin/analytics` | GET | superadmin | Metrik platform: revenue, order, produk terlaris. |
| `/api/seller/profile` | GET / PUT | seller | Baca dan update profil toko seller. |
| `/api/notifications` | GET | semua role | Daftar notifikasi milik user yang sedang login. |
| `/api/notifications/:id/read` | PATCH | semua role | Tandai notifikasi sudah dibaca. |

### 7.3 Data Exchange Contract

Kontrak JSON pada checkout request dan response harus diperlakukan sebagai integration contract dengan API Gateway dan service partner. Perubahan nama field atau tipe data dapat memutus integrasi dengan SmartBank atau LogistiKita.

```json
// POST /api/checkout — Request Body
{
  "items": [
    { "product_id": "uuid", "qty": 2 }
  ],
  "shipping_address": "Jl. Contoh No. 1, Bandung",
  "voucher_code": "UMKM2026",
  "idempotency_key": "uuid-v4"
}

// POST /api/checkout — Response (sukses)
{
  "order_id": "uuid",
  "status": "paid",
  "subtotal": 100000,
  "fee_marketplace": 2000,
  "voucher_discount": 5000,
  "total": 97000,
  "transaction_id": "SB-TXN-XXXX",
  "tracking_id": "LK-TRACK-XXXX"
}
```

---

## 8. Workflow Operasional

Workflow berikut menggambarkan operasi sistem pada kondisi penggunaan nyata. Setiap workflow dapat dijadikan dasar test case end-to-end dan smoke test setelah perubahan fitur.

> *[Gambar 3: Use case diagram utama — aktor Buyer, Seller, Superadmin, dan batas sistem PasarKita terhadap service eksternal]*

| Workflow | Trigger | Main Success Scenario | Failure / Control |
|---|---|---|---|
| User Registration | User membuka `/auth/register`. | Sistem memvalidasi input, hash password, simpan user, inisiasi saldo Rp 50.000 ke SmartBank, kembalikan JWT. | Jika SmartBank tidak tersedia, user tersimpan namun saldo belum terinisiasi; perlu retry manual atau background job. |
| Product Listing | Seller membuka `/seller/products`. | Seller membuat produk dengan form valid; produk aktif dan tampil di katalog buyer. | Validasi Zod gagal mengembalikan daftar field error eksplisit; produk tidak tersimpan. |
| Checkout & Payment | Buyer menekan tombol "Bayar" di halaman checkout. | Backend validasi stok → kalkulasi fee → buat order pending → payment request ke SmartBank → update `paid` → trigger LogistiKita → kembalikan konfirmasi. | Stok tidak cukup: 400 INSUFFICIENT_STOCK. SmartBank gagal: 402 PAYMENT_FAILED, stok di-rollback, order `payment_failed`. |
| Order Tracking | Buyer membuka `/orders/:id`. | Sistem menampilkan status order terkini, `tracking_id`, estimasi pengiriman, dan riwayat status. | Jika `tracking_id` belum ada (shipping trigger gagal), tampilkan status "Menunggu Pengiriman" dengan notifikasi admin. |
| Review Submission | Buyer membuka detail order dengan status `delivered`. | Buyer mengisi rating dan komentar; sistem memvalidasi status order; rating tersimpan; rata-rata rating produk diperbarui. | Rating ditolak jika order belum `delivered` atau sudah pernah dirating; pesan error eksplisit ditampilkan. |
| Admin User Ban | Superadmin membuka `/admin/users`. | Superadmin memasukkan alasan ban; sistem men-set `is_active = false`, menulis `admin_audit_logs`, dan mengembalikan status terbaru. | User yang di-ban tidak dapat login; token aktif user tersebut diinvalidasi pada request berikutnya. |
| Integration Health Check | Superadmin membuka halaman status integrasi. | Sistem melakukan ping ke API Gateway, SmartBank, dan LogistiKita; menampilkan status `online`/`offline` dan `response_ms`. | Jika service eksternal offline, dashboard tetap berjalan; status ditampilkan sebagai `offline` dengan pesan error terakhir. |
| Analytics Pull | Superadmin membuka `/admin/analytics`. | Sistem mengembalikan metrik agregat: total revenue, order count, distribusi status, produk terlaris, dan revenue per seller. | Jika query timeout, dashboard menampilkan pesan error parsial; data lain yang berhasil dimuat tetap ditampilkan. |

---

## 9. Risiko, Kontrol, dan Acceptance Criteria

Karena sistem berada di antara proses transaksi keuangan dan logistik dalam ekosistem microservices, risiko utama bukan hanya bug UI, tetapi juga inkonsistensi stok, double charge, dan perubahan kontrak API yang tidak kompatibel.

| Risk ID | Risiko | Kontrol Wajib | Acceptance Criteria |
|---|---|---|---|
| R-01 | Double order akibat retry checkout. | Idempotency key wajib pada setiap checkout; backend mendeteksi dan mengembalikan order existing. | Checkout duplikat dengan key yang sama tidak membuat order baru; response mengembalikan order pertama. |
| R-02 | Stok berkurang meski pembayaran gagal. | Stok di-reserve saat order `pending`; rollback stok dilakukan segera setelah SmartBank mengembalikan failure. | Setelah payment failure, `stock` produk kembali ke nilai sebelum checkout; order berstatus `payment_failed`. |
| R-03 | Service SmartBank atau LogistiKita tidak tersedia saat checkout. | Failure handling dengan timeout, error response bermakna, pencatatan di `integration_logs`; checkout tidak menggantung tanpa batas. | Timeout ke SmartBank menghasilkan 503 SERVICE_UNAVAILABLE dengan pesan yang dapat dimengerti buyer; order tidak terbuat. |
| R-04 | Perubahan kontrak API memutus integrasi dengan service partner. | Backward compatibility wajib; field baru bersifat additive; perubahan breaking didiskusikan lintas kelompok sebelum deploy. | Service partner dapat membaca response API setelah update tanpa perubahan kode di sisi mereka untuk field yang sudah ada. |
| R-05 | Akses tidak sah ke data user atau order lain. | Role-based middleware memvalidasi kepemilikan resource; buyer hanya melihat order sendiri; seller hanya kelola produk sendiri. | Request akses ke resource user lain menghasilkan 403 Forbidden; tidak ada data user lain yang ter-expose. |
| R-06 | Harga produk berubah setelah order dibuat, memengaruhi laporan. | `price_at_purchase` adalah snapshot immutable saat transaksi; kalkulasi revenue menggunakan field ini. | Update harga produk tidak memengaruhi nilai `subtotal` pada order yang sudah ada. |
| R-07 | Superadmin tidak dapat diaudit. | `admin_audit_logs` menulis setiap aksi sensitif dengan `before_data` dan `after_data`. | Setiap aksi ban user dan update status order menghasilkan entri audit log yang dapat ditelusuri oleh aktor. |

---

## 10. Matriks Ketertelusuran

Traceability matrix menghubungkan objective produk dengan requirement dan bukti verifikasi. Matriks ini membantu developer dan QA memastikan perubahan kode tetap menjaga tujuan sistem.

| Objective | Requirement IDs | Evidence / Verification |
|---|---|---|
| User dapat mendaftar dan login dengan role yang tepat. | FR-01, FR-02, FR-03, NFR-01, NFR-02 | Test register buyer/seller/superadmin; test login valid/invalid; test token expired. |
| Buyer dapat menelusuri dan membeli produk UMKM. | FR-04, FR-05, FR-08, FR-09, FR-10, NFR-04 | Test katalog dengan filter; test checkout sukses; test checkout dengan stok habis; test idempotency. |
| Seller dapat mengelola katalog produk secara mandiri. | FR-06, FR-07, FR-22, NFR-03, NFR-08 | Test CRUD produk seller; test akses ke produk seller lain; test diskon produk. |
| Transaksi keuangan terintegrasi dengan SmartBank via API Gateway. | FR-09, FR-10, FR-12, BR-01, BR-03, NFR-05, NFR-07 | Test checkout sukses dan gagal; test fee calculation; test rate limiting; simulasi SmartBank offline. |
| Pengiriman terkoordinasi dengan LogistiKita. | FR-11, R-03, NFR-07 | Test trigger pengiriman setelah payment sukses; simulasi LogistiKita offline; verifikasi `tracking_id` tersimpan. |
| Admin dapat mengelola platform dan memantau analytics. | FR-16, FR-19, FR-20, FR-21, NFR-09 | Test ban/aktifkan user; test update status order; test analytics endpoint; verifikasi audit log. |
| Sistem tetap tangguh saat dependency eksternal gagal. | NFR-06, NFR-07, R-03, R-04 | Matikan mock SmartBank/LogistiKita; verifikasi error handling; verifikasi `integration_logs` tercatat. |
| Data transaksi terlindungi dan teradit. | NFR-01, NFR-03, NFR-09, NFR-12, R-05, R-06 | Test akses lintas user; verifikasi `password_hash` tidak ter-expose; verifikasi snapshot harga immutable. |

---

## Lampiran A. Glosarium

| Istilah | Definisi Operasional |
|---|---|
| PasarKita | Platform marketplace digital B2C untuk produk UMKM; Demand Generator dalam ekosistem RPL 2. |
| Ekosistem UMKM RPL 2 | Kumpulan microservices antar kelompok yang saling terintegrasi: SmartBank, WarungPOS, SupplierHub, LogistiKita, UMKM Insight, dan API Gateway. |
| API Gateway | Service Kelompok 7 yang bertindak sebagai routing layer, JWT validator antar service, dan logging inter-service. |
| SmartBank | Service Kelompok 1 sebagai core keuangan; memproses pembayaran dan mengelola saldo user. |
| LogistiKita | Service Kelompok 5 yang mengelola pengiriman dan menghasilkan `tracking_id`. |
| Demand Generator | Peran PasarKita sebagai inisiator permintaan (buyer melakukan checkout) dalam ekosistem. |
| Idempotency Key | UUID unik yang dikirimkan pada setiap checkout request untuk mencegah pemrosesan duplikat. |
| Snapshot Harga | Nilai `price_at_purchase` pada `order_items` yang diambil saat transaksi dan tidak berubah meskipun harga produk diperbarui. |
| Soft Delete | Penghapusan logis dengan mengubah `is_active = false` tanpa menghapus record dari database. |
| Fee Marketplace | Biaya platform sebesar 2% dari subtotal order yang dibebankan ke buyer setiap transaksi. |
| Mock Server | Implementasi lokal di `mock/` yang mensimulasikan SmartBank dan LogistiKita untuk keperluan development tanpa bergantung pada service nyata. |
| System of Record | Sistem otoritatif untuk satu jenis data. PasarKita adalah system of record untuk produk, order, dan ulasan dalam ekosistemnya; SmartBank adalah system of record untuk saldo dan transaksi keuangan. |

---

## Lampiran B. Referensi Internal

| Artefak | Relevansi |
|---|---|
| `README.md` | Deskripsi umum aplikasi, arsitektur ekosistem, tech stack, API endpoints, role & akses, dan aturan keuangan ekosistem. |
| `backend/database/schema/000_full_schema.sql` | Skema lengkap semua tabel Supabase PostgreSQL: users, products, orders, order_items, ratings, notifications, vouchers, integration_logs, admin_audit_logs, dan lainnya. |
| `backend/src/modules/` | Business logic per domain: auth, products, orders, checkout, dan integrations. |
| `backend/src/middlewares/` | Middleware auth (JWT validation), validate (Zod schema), dan errorHandler (centralized error response). |
| `backend/src/integrations/` | Adapter HTTP untuk SmartBank dan LogistiKita; konfigurasi `GATEWAY_BASE_URL` vs mock URL. |
| `backend/src/utils/fee.js` | Implementasi kalkulasi fee marketplace 2%; digunakan oleh checkout module dan fee simulation endpoint. |
| `backend/vercel.json` | Konfigurasi routing Vercel untuk backend serverless; memetakan semua path ke `api/index.js`. |
| `frontend/store/` | Zustand store untuk auth state (user, token, login/logout) dan cart state (items, add, remove, clear). |
| `mock/smartbank/` dan `mock/logistikita/` | Implementasi mock server lokal; digunakan hanya saat `NODE_ENV=development`. |

---

## Lampiran C. Catatan Perubahan Versi

| Versi | Tanggal | Keterangan |
|---|---|---|
| 1.0 | [Tanggal] | Initial baseline SRS; disusun dari README, skema database, dan struktur kode aktif. Mencakup semua bagian: pendahuluan, gambaran produk, arsitektur, domain data, kebutuhan fungsional (FR-01 s/d FR-22), kebutuhan non-fungsional (NFR-01 s/d NFR-12), antarmuka eksternal, workflow operasional, risiko, dan traceability matrix. |