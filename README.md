# Dinmar Logistik Delivery Management System

Aplikasi **Dinmar Logistik** adalah sebuah sistem manajemen pengiriman yang memungkinkan pengguna untuk mengelola data kiriman dengan berbagai fitur, seperti:

- **Menampilkan data kiriman**: Melihat semua data pengiriman dalam format tabel.
- **Menambah data kiriman**: Menambahkan data pengiriman baru, termasuk penginputan data seperti nama pengirim, penerima, berat, jarak, tipe layanan, dan status.
- **Mengubah data kiriman**: Memperbarui data kiriman yang sudah ada, termasuk perubahan status yang otomatis memindahkan kiriman ke arsip jika statusnya berubah menjadi "Selesai".
- **Menghapus data kiriman**: Menghapus kiriman dari daftar aktif dan memindahkannya ke arsip.
- **Mencari data kiriman**: Pencarian berdasarkan No Resi, nama pengirim, atau nama penerima.
- **Restore data kiriman**: Mengembalikan kiriman yang telah diarsipkan kembali ke daftar aktif.
- **Rangkuman pengiriman**: Menampilkan statistik dan perhitungan total pengiriman, pendapatan, dan rata-rata biaya pengiriman.

## Fitur Utama

1. **Input Validasi**
   - Validasi input untuk memastikan data yang dimasukkan sesuai dengan format yang diharapkan.
   - Fitur pengecekan agar input huruf, angka, dan format No Resi sesuai dengan ketentuan.

2. **Perhitungan Biaya Otomatis**
   - Sistem menghitung biaya pengiriman berdasarkan berat, jarak, dan tipe layanan (Reguler atau Ekspres).
   - Biaya ekspres dikenakan tarif tambahan sebesar 50%.

3. **Manajemen Arsip**
   - Pengiriman dengan status "Selesai" secara otomatis dipindahkan ke arsip.
   - Fitur restore untuk mengembalikan data pengiriman dari arsip ke daftar aktif.

4. **Antarmuka Pengguna Interaktif**
   - Menu utama yang mudah dipahami untuk mengakses semua fitur.
   - Tampilan data menggunakan library `tabulate` agar data lebih rapi dan mudah dibaca.

## Struktur Program

- **daftar_kiriman**: Menyimpan data pengiriman aktif.
- **arsip_kiriman**: Menyimpan data pengiriman yang telah diarsipkan.
- **STATUS_KIRIMAN**: Dictionary untuk status pengiriman.
- **Fungsi-fungsi Utama**:
  - `tampilkan_kiriman`: Menampilkan semua data pengiriman.
  - `tambah_kiriman`: Menambahkan pengiriman baru.
  - `ubah_kiriman`: Mengubah data pengiriman.
  - `hapus_kiriman`: Menghapus pengiriman dan memindahkannya ke arsip.
  - `cari_kiriman`: Mencari pengiriman berdasarkan kriteria tertentu.
  - `restore_kiriman`: Mengembalikan data pengiriman dari arsip ke daftar aktif.
  - `rangkuman_pengiriman`: Menampilkan statistik keseluruhan pengiriman.

## Cara Menjalankan Program

1. **Persyaratan**
   - Pastikan Python sudah terinstal (Python 3.6 atau lebih baru direkomendasikan).
   - Library `tabulate` harus diinstal. Jika belum, instal dengan perintah:
     ```bash
     pip install tabulate
     ```

2. **Menjalankan Program**
   - Simpan kode program dalam sebuah file, misalnya `dinmar_logistik.py`.
   - Buka terminal atau command prompt, navigasikan ke folder tempat file tersebut disimpan, dan jalankan:
     ```bash
     python dinmar_logistik.py
     ```
   - Ikuti instruksi yang muncul pada layar untuk menggunakan fitur-fitur dalam sistem.

## Panduan Penggunaan

1. **Menu Utama**
   - Saat program dijalankan, akan muncul menu utama dengan pilihan 1-8.
   - Masukkan nomor menu yang sesuai dengan aksi yang ingin dilakukan.

2. **Tambah Data Kiriman**
   - Pilih menu **2. Tambah Data Kiriman**.
   - Ikuti petunjuk untuk menginput data pengiriman baru, seperti nama pengirim, penerima, berat, jarak, tipe layanan, dan status.

3. **Ubah Data Kiriman**
   - Pilih menu **3. Ubah Data Kiriman**.
   - Masukkan No Resi pengiriman yang ingin diubah dan ikuti petunjuk untuk mengubah data yang diinginkan.
   - Jika status diubah menjadi "Selesai", pengiriman akan otomatis dipindahkan ke arsip.

4. **Hapus Data Kiriman**
   - Pilih menu **4. Hapus Data Kiriman**.
   - Masukkan No Resi pengiriman yang ingin dihapus. Data akan dipindahkan ke arsip jika penghapusan dikonfirmasi.

5. **Cari Data Kiriman**
   - Pilih menu **5. Cari Data Kiriman**.
   - Pilih kriteria pencarian (No Resi, nama pengirim, atau nama penerima) dan masukkan kata kunci pencarian.

6. **Restore Data Kiriman**
   - Pilih menu **6. Restore Data Kiriman**.
   - Lihat daftar pengiriman yang telah diarsipkan dan masukkan No Resi untuk mengembalikan data tersebut ke daftar aktif.

7. **Rangkuman Pengiriman**
   - Pilih menu **7. Rangkuman Pengiriman**.
   - Sistem akan menampilkan ringkasan statistik pengiriman, termasuk total pengiriman, pendapatan, dan rata-rata biaya.

8. **Keluar**
   - Pilih menu **8. Keluar** untuk mengakhiri program.

## Kontribusi

Kontribusi terhadap proyek ini sangat dipersilakan! Jika Anda menemukan bug atau ingin menambahkan fitur baru, silakan lakukan fork repository dan buat pull request.

---

Selamat menggunakan aplikasi **Dinmar Logistik** dan semoga sistem ini membantu dalam mengelola pengiriman dengan lebih efisien!
