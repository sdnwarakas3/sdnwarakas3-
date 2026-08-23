APLIKASI ADMINISTRASI GURU SDN WARAKAS 3 - DATABASE ONLINE BERSAMA

PENTING:
Versi online penuh membutuhkan satu database PostgreSQL cloud dan satu hosting.
Saya tidak dapat membuat akun hosting/database atas nama Anda dari sini.

Jika ingin langsung menjalankan di satu laptop/server sendiri:
1. Install Docker Desktop.
2. Buka folder ini.
3. Jalankan: docker compose up -d --build
4. Buka: http://localhost:8080
5. Semua HP/laptop yang satu jaringan dapat membuka IP laptop/server, misalnya:
   http://192.168.1.10:8080

Untuk internet dari mana saja, deploy folder ini ke hosting yang mendukung Docker dan isi DATABASE_URL dengan PostgreSQL cloud.
Aplikasi otomatis membuat tabel database dan sinkronisasi realtime melalui WebSocket.
