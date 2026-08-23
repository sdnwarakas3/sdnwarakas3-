FITUR WALLPAPER SDN WARAKAS 3
- Admin dapat mengatur wallpaper khusus untuk setiap Kelas 1-6 dan setiap menu administrasi.
- Pilih Kelas dan Menu di Panel Admin.
- Masukkan URL gambar atau upload gambar.
- Simpan Wallpaper. Data wallpaper disimpan dalam schoolSetting PostgreSQL dan tersinkron otomatis ke semua perangkat.
- Jika wallpaper khusus belum ada, sistem menggunakan wallpaper global (jika tersedia) atau latar standar.
- Guru tidak dapat mengubah wallpaper karena endpoint penyimpanan schoolSetting tetap dilindungi token Admin.
