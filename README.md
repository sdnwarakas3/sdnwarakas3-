# SDN WARAKAS 3 — GitHub + Cloudflare Pages Functions + Supabase

Versi ini tidak membutuhkan Render/Railway. GitHub menyimpan kode, Cloudflare Pages menjalankan frontend + Pages Functions, dan Supabase menjadi database pusat.

## Supabase
1. Jalankan `schema.sql` di SQL Editor.
2. Pastikan tabel `public.app_state` ada.
3. Di Settings → API Keys, gunakan **Secret key** untuk backend (format `sb_secret_...`). Jangan pernah memasukkannya ke GitHub atau browser.

## Cloudflare Pages
Hubungkan repository GitHub ke Workers & Pages → Create application → Pages → Import an existing Git repository.
- Production branch: `main`
- Framework preset: None
- Build command: kosong
- Build output directory: `/`

Setelah project dibuat, buka Settings → Variables and Secrets dan tambahkan:
- `SUPABASE_URL` = Project URL Supabase
- `SUPABASE_SECRET_KEY` = Secret key Supabase (`sb_secret_...`)
- `SCHOOL_CODE` = `SDN-WARAKAS-3`
- `ADMIN_USER` = username admin yang kamu inginkan
- `ADMIN_PASS` = password admin yang kamu inginkan
- `TOKEN_SECRET` = string acak panjang, minimal 32 karakter

Set variabel untuk Production. Secret key hanya boleh berada di server-side Function, tidak di `index.html` atau GitHub.

## Penting
Pages Functions hanya aktif ketika project dideploy dari Git provider; Direct Upload tidak mendukung Functions. Setelah deploy, buka URL Pages yang diberikan Cloudflare.
