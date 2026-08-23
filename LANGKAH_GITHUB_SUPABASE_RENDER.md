# SDN WARAKAS 3 — GitHub + Supabase + Render

## Arsitektur
GitHub menyimpan kode → Render menjalankan server → Supabase menyimpan PostgreSQL → semua HP memakai satu URL Render.

## 1. GitHub
Upload semua file/folder di paket ini ke repository GitHub. Jangan upload file yang berisi rahasia/password.

## 2. Supabase
Buat project `SDN-WARAKAS-3`.

Buka SQL Editor lalu jalankan isi `schema.sql`.

Ambil PostgreSQL connection string dari Supabase. Connection string ini **JANGAN** dimasukkan ke GitHub atau HTML.

## 3. Render
Di Render pilih New → Web Service → Connect GitHub → pilih repository aplikasi.

Build Command:
`npm install`

Start Command:
`npm start`

Environment Variables:
- `DATABASE_URL` = PostgreSQL connection string Supabase
- `ADMIN_USER` = username admin
- `ADMIN_PASS` = password admin
- `PORT` = 10000 (Render biasanya menyediakan PORT otomatis; server juga mendukung PORT dari environment)

Setelah deploy, buka URL HTTPS Render. Semua HP menggunakan URL yang sama.

## 4. Pemeriksaan
Buka:
`https://URL-RENDER-KAMU/health`

Harus menunjukkan `ok: true` dan `databaseStatus: connected`.

## Catatan keamanan
- Jangan kirim `DATABASE_URL`, password database, atau token rahasia ke chat.
- Jangan commit `.env` ke GitHub.
- Ganti password admin bawaan dengan password kuat melalui environment variable.
