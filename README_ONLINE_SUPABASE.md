# SDN WARAKAS 3 — ONLINE + DATABASE SUPABASE + SINKRON OTOMATIS

Paket ini sudah disiapkan agar aplikasi menggunakan **PostgreSQL online** sebagai database bersama.
Rekomendasi: **Supabase untuk database + Render untuk menjalankan server aplikasi**.

## Yang dilakukan
- Semua HP/laptop membuka 1 URL HTTPS yang sama.
- Data tersimpan di PostgreSQL, bukan hanya di HP.
- Sinkronisasi antar perangkat memakai API + WebSocket.
- Admin dapat mengubah pengaturan sekolah.
- Database dibuat otomatis saat server pertama kali hidup.
- Endpoint `/health` dan `/health/db` tersedia untuk pemeriksaan.

## Yang perlu dilakukan satu kali
1. Buat project PostgreSQL di Supabase.
2. Ambil **connection string PostgreSQL** dari Supabase.
3. Buat Web Service di Render dari folder/repository ini.
4. Tambahkan environment variable:
   - `DATABASE_URL` = connection string PostgreSQL Supabase
   - `ADMIN_USER` = username admin yang diinginkan
   - `ADMIN_PASS` = sandi admin yang kuat
5. Deploy.
6. Buka URL HTTPS Render. Semua perangkat memakai URL yang sama.

## Penting
Jangan memasukkan DATABASE_URL ke file HTML/JavaScript. DATABASE_URL hanya boleh berada di environment server.
Untuk pemakaian sekolah, lakukan backup database secara berkala.

## Menjalankan lokal
Node.js 18+:
```bash
npm install
npm start
```
Lalu buka `http://localhost:8080/`.

## Pemeriksaan
- `/health` menampilkan status server dan database.
- `/health/db` memeriksa koneksi PostgreSQL.

