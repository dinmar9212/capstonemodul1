import random # Impor modul random agar dapat digunakan dalam kode untuk menghasilkan angka acak dan operasi terkait.
import string # Impor modul string agar dapat digunakan dalam kode untuk bekerja dengan berbagai kumpulan karakter standar seperti huruf alfabet, angka, dan simbol.
from tabulate import tabulate # Dari modul tabulate, impor fungsi tabulate agar dapat digunakan dalam kode untuk menampilkan data dalam bentuk tabel yang rapi.

# Buat sebuah list bernama daftar_kiriman yang berisi beberapa dictionary.
# Setiap dictionary merepresentasikan satu kiriman dengan informasi seperti nomor resi, pengirim, penerima, berat, jarak, tipe layanan, biaya, dan status pengiriman.
daftar_kiriman = [
    {'No Resi': 'NR13579', 'Pengirim': 'Budi', 'Penerima': 'Ani', 'Berat (kg)': 3, 'Jarak (km)': 1,
     'Tipe Layanan': 'Reguler', 'Biaya': '32,000', 'Status': 'Dalam proses'},
    {'No Resi': 'NR02468', 'Pengirim': 'Siti', 'Penerima': 'Rudi', 'Berat (kg)': 5, 'Jarak (km)': 1,
     'Tipe Layanan': 'Reguler', 'Biaya': '52,000', 'Status': 'Dikirim'},
    {'No Resi': 'NR97531', 'Pengirim': 'Joko', 'Penerima': 'Tina', 'Berat (kg)': 2, 'Jarak (km)': 1,
     'Tipe Layanan': 'Reguler', 'Biaya': '22,000', 'Status': 'Transit gudang'},
    {'No Resi': 'NR86420', 'Pengirim': 'Dewi', 'Penerima': 'Fajar', 'Berat (kg)': 7, 'Jarak (km)': 1,
     'Tipe Layanan': 'Reguler', 'Biaya': '72,000', 'Status': 'Sampai di tujuan'}
]

# Buat sebuah list kosong bernama arsip_kiriman yang nantinya bisa digunakan untuk menyimpan data kiriman yang diarsipkan.
arsip_kiriman = []

# Buat sebuah dictionary bernama STATUS_KIRIMAN yang berisi daftar status pengiriman.
# Kunci berupa angka (1 hingga 6), dan nilainya adalah deskripsi status pengiriman.
STATUS_KIRIMAN = {
    1: "Dalam proses",
    2: "Dikirim",
    3: "Transit gudang",
    4: "Dibawa kurir",
    5: "Sampai di tujuan",
    6: "Selesai"
}

def tampilkan_kiriman(daftar): # Buat sebuah fungsi bernama tampilkan_kiriman yang menerima satu parameter daftar
    if not daftar:
        print("Tidak ada data kiriman.")
    else:
        print(tabulate(daftar, headers="keys", tablefmt="fancy_grid"))
        # Cetak data dalam daftar dalam bentuk tabel menggunakan tabulate(), 
        # dengan judul kolom diambil dari kunci dictionary dan format tabel menggunakan gaya fancy_grid.

# Buat sebuah fungsi bernama input_validated yang menerima beberapa parameter untuk meminta dan memvalidasi input dari pengguna.
# converter → Fungsi yang digunakan untuk mengonversi input (misalnya int, float, atau str).
def input_validated(prompt, converter, condition=None, error_message="Input tidak valid"):
# condition=None → Opsional, fungsi atau ekspresi untuk memvalidasi input.
# Jika tidak diberikan, input hanya akan dikonversi tanpa validasi tambahan.
    if condition is None: # Jika nilai condition adalah None, maka jalankan blok kode di bawahnya.
        def condition(x):
            return True
    while True:
        nilai = input(prompt).strip()
        try:
            converted = converter(nilai) # Gunakan fungsi converter untuk mengubah nilai, lalu simpan hasilnya ke dalam variabel converted.
        except Exception: # Tangkap semua jenis error yang merupakan turunan dari Exception dalam blok try-except.
            print("Error: Harap masukkan angka yang benar")
            continue
        if not condition(converted): # Jika converted tidak memenuhi kondisi condition, maka jalankan blok kode di dalam if.
            print(error_message)
        else:
            return converted

def cek_input_huruf(prompt):
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("Error: Input tidak boleh kosong")
        elif not all(c.isalpha() or c.isspace() or c in "-." for c in nilai):
        # Jika ada setidaknya satu karakter dalam nilai yang bukan huruf (A-Z atau a-z), bukan spasi ( ), dan bukan tanda - atau ., maka jalankan blok kode di bawahnya.
            print("Error: Input hanya boleh mengandung huruf, spasi, tanda hubung (-), atau titik (.)")
        else:
            return nilai.title()

def cek_input_angka(prompt):
    def validasi(x):
        return x > 0
    return input_validated(prompt, int, validasi, "Error: Angka harus lebih dari 0")

def cek_input_float(prompt):
    def validasi(x):
        return x > 0
    return input_validated(prompt, float, validasi, "Error: Angka harus lebih dari 0")

def cek_input_yn(prompt):
    while True:
        nilai = input(prompt).strip().lower() # Ambil input dari pengguna, hilangkan spasi di awal dan akhir,
        # ubah menjadi huruf kecil, lalu simpan ke dalam variabel nilai.
        if nilai in ["y", "n"]:
            return nilai
        print("Input salah! Harap masukkan hanya huruf 'y' atau 'n'.")

def pilih_status(izinkan_selesai=True):
    # Buat dictionary baru status_tersedia yang berisi semua pasangan kunci-nilai dari STATUS_KIRIMAN
    # kecuali jika izinkan_selesai bernilai False, maka nilai 'Selesai' akan dikecualikan.
    status_tersedia = {k: v for k, v in STATUS_KIRIMAN.items() if izinkan_selesai or v != "Selesai"}
    print("Pilih status:")
    for key, value in status_tersedia.items():
        print(f"{key}. {value}")
    pilihan = cek_input_angka("Masukkan nomor status: ")
    while pilihan not in status_tersedia:
        print("Error: Pilihan tidak tersedia!")
        pilihan = cek_input_angka("Masukkan nomor status: ")
    return status_tersedia[pilihan]

def buat_no_resi(daftar):
    while True:
        no_resi = "NR" + "".join(random.choices(string.digits, k=5)) # Buat nomor resi yang diawali dengan 'NR', diikuti oleh 5 digit angka acak.
        if no_resi not in [item["No Resi"] for item in daftar]:
            return no_resi

def hitung_biaya(berat, jarak, tipe_layanan):
    tarif_per_kg = 10000
    tarif_per_km = 2000
    biaya = berat * tarif_per_kg + jarak * tarif_per_km
    if tipe_layanan.lower() == "ekspres": # Jika tipe_layanan (dengan semua huruf diubah menjadi huruf kecil) sama dengan 'ekspres',
        # maka jalankan blok kode di dalam if.
        biaya *= 1.5
    return f"{int(biaya):,}"

def cek_tipe_layanan():
    print("Pilih tipe layanan:")
    print("1. Reguler")
    print("2. Ekspres")
    pilihan = cek_input_angka("Masukkan pilihan (1 atau 2): ")
    while pilihan not in [1, 2]:
        print("Error: Pilihan salah! Silakan masukkan 1 untuk Reguler atau 2 untuk Ekspres")
        pilihan = cek_input_angka("Masukkan pilihan (1 atau 2): ")
    return "Reguler" if pilihan == 1 else "Ekspres" # Jika pilihan adalah 1, maka tipe layanan adalah 'Reguler'
    # jika pilihan adalah 2, maka tipe layanan adalah 'Ekspres'.

def tambah_kiriman(daftar):
    tampilkan_kiriman(daftar)
    no_resi = buat_no_resi(daftar)
    pengirim = cek_input_huruf("Masukkan nama pengirim: ")
    penerima = cek_input_huruf("Masukkan nama penerima: ")
    berat = cek_input_float("Masukkan berat barang (kg): ") # Mengizinkan desimal untuk berat
    jarak = cek_input_float("Masukkan jarak pengiriman (km): ")  # Mengizinkan desimal untuk jarak
    tipe_layanan = cek_tipe_layanan()
    biaya = hitung_biaya(berat, jarak, tipe_layanan)
    status = pilih_status(izinkan_selesai=False) # izinkan_selesai=False, jadi "Selesai" tidak muncul dalam pilihan.
    if cek_input_yn("Apakah kamu yakin ingin menambah data kiriman ini? (y/n): ") != "y":
        print("Penambahan data dibatalkan")
        return

    # Tambahkan sebuah dictionary (data kiriman) ke dalam list daftar.
    # Dictionary ini berisi informasi seperti nomor resi, pengirim, penerima, berat, jarak, tipe layanan, biaya, dan status.
    daftar.append({
        "No Resi": no_resi,
        "Pengirim": pengirim,
        "Penerima": penerima,
        "Berat (kg)": berat,
        "Jarak (km)": jarak,
        "Tipe Layanan": tipe_layanan,
        "Biaya": biaya,
        "Status": status
    })
    print("Data kiriman berhasil ditambahkan")
    tampilkan_kiriman(daftar)

def ubah_kiriman(daftar):
    # Perulangan untuk mengubah data kiriman secara berulang
    while True:
        tampilkan_kiriman(daftar)
        no_resi = input("Masukkan No Resi kiriman yang ingin diubah: ").upper().strip()
        item_to_update = None
        for item in daftar:
            if item["No Resi"] == no_resi:
                item_to_update = item
                break
        if not item_to_update:
            print("No Resi tidak ditemukan!")
            continue
        if cek_input_yn(f"Apakah kamu yakin ingin mengubah data kiriman dengan Resi {no_resi}? (y/n): ") != "y":
            print("Pengubahan data dibatalkan.")
            continue

        # Perulangan untuk update field pada kiriman yang dipilih
        while True:
            print("\nPilih field yang ingin diubah:")
            print("1. Pengirim")
            print("2. Penerima")
            print("3. Berat (kg)")
            print("4. Jarak (km)")
            print("5. Tipe Layanan")
            print("6. Status")
            print("7. Selesai mengubah")
            pilihan = cek_input_angka("Masukkan pilihan (1-7): ")

            if pilihan == 1:
                item_to_update["Pengirim"] = cek_input_huruf("Masukkan nama pengirim baru: ")
                print("Pengirim berhasil diubah.")
            elif pilihan == 2:
                item_to_update["Penerima"] = cek_input_huruf("Masukkan nama penerima baru: ")
                print("Penerima berhasil diubah.")
            elif pilihan == 3:
                new_berat = cek_input_float("Masukkan berat baru (kg): ")
                item_to_update["Berat (kg)"] = new_berat
                jarak = item_to_update.get("Jarak (km)", 0) # Ambil nilai dari kunci 'Jarak (km)' dalam dictionary item_to_update. Jika kunci tersebut tidak ada, gunakan nilai default 0.
                tipe = item_to_update.get("Tipe Layanan", "Reguler")
                item_to_update["Biaya"] = hitung_biaya(new_berat, jarak, tipe) # Perbarui nilai "Biaya" dalam item_to_update dengan hasil dari pemanggilan fungsi hitung_biaya()
                # yang menggunakan new_berat, jarak, dan tipe sebagai argumen.
                print("Berat berhasil diubah dan biaya diperbarui.")
            elif pilihan == 4:
                new_jarak = cek_input_float("Masukkan jarak baru (km): ")
                item_to_update["Jarak (km)"] = new_jarak
                berat = item_to_update.get("Berat (kg)", 0) # Ambil nilai dari kunci 'Berat (kg)' dalam dictionary item_to_update. Jika kunci tersebut tidak ada, gunakan nilai default 0.
                tipe = item_to_update.get("Tipe Layanan", "Reguler")
                item_to_update["Biaya"] = hitung_biaya(berat, new_jarak, tipe)
                print("Jarak berhasil diubah dan biaya diperbarui.")
            elif pilihan == 5:
                new_tipe = cek_tipe_layanan()
                item_to_update["Tipe Layanan"] = new_tipe
                berat = item_to_update.get("Berat (kg)", 0) 
                jarak = item_to_update.get("Jarak (km)", 0)
                item_to_update["Biaya"] = hitung_biaya(berat, jarak, new_tipe)
                print("Tipe Layanan berhasil diubah dan biaya diperbarui.")
            elif pilihan == 6:
                # Karena izinkan_selesai=True, opsi "Selesai" tersedia dalam daftar.
                new_status = pilih_status(izinkan_selesai=True) # Jika pengguna memilih nomor 6, maka new_status akan berisi "Selesai".
                item_to_update["Status"] = new_status
                print("Status berhasil diubah.")
                if new_status == "Selesai":
                    arsip_kiriman.append(item_to_update)
                    daftar.remove(item_to_update)
                    print(f"Karena status berubah menjadi 'Selesai', kiriman dengan Resi {item_to_update['No Resi']} dipindahkan ke arsip.")
                    # Keluar dari loop update field untuk kiriman ini
                    break
            elif pilihan == 7:
                print("Selesai mengubah data kiriman.")
                break
            else:
                print("Pilihan tidak valid!")

            print("\nData kiriman saat ini:")
            print(tabulate([item_to_update], headers="keys", tablefmt="fancy_grid"))
        
        if cek_input_yn("Apakah ingin mengubah data kiriman lainnya? (y/n): ") != "y":
            break

def hapus_kiriman(daftar):
    tampilkan_kiriman(daftar)
    no_resi = input("Masukkan No Resi kiriman yang ingin dihapus: ").upper().strip()
    for item in daftar:
        if item["No Resi"] == no_resi:
            if cek_input_yn(f"Apakah kamu yakin ingin menghapus kiriman dengan Resi {no_resi}? (y/n): ") == "y":
                arsip_kiriman.append(item) # Tambahkan item ke dalam list arsip_kiriman di posisi terakhir.
                daftar.remove(item) # Hapus item dari daftar daftar jika item ada di dalamnya.
                print("Data kiriman berhasil dihapus!")
                tampilkan_kiriman(daftar)
            else:
                print("Penghapusan dibatalkan.")
            return
    print("No Resi tidak ditemukan!")

def cari_kiriman(daftar):
    if not daftar:
        print("Tidak ada data kiriman.")
        return
    print("\n=== Cari Data Kiriman ===")
    print("Cari berdasarkan:")
    print("1. No Resi")
    print("2. Nama Pengirim")
    print("3. Nama Penerima")
    opsi = cek_input_angka("Pilih opsi (1-3): ")
    if opsi == 1:
        kata_kunci = input("Masukkan No Resi: ").upper().strip()
        hasil = [item for item in daftar if kata_kunci in item["No Resi"]]
        # Buat daftar hasil yang berisi semua item dari daftar yang memiliki kata_kunci di dalam nilai No Resi.
    elif opsi == 2:
        kata_kunci = input("Masukkan Nama Pengirim: ").lower().strip()
        hasil = [item for item in daftar if kata_kunci in item["Pengirim"].lower()]
    elif opsi == 3:
        kata_kunci = input("Masukkan Nama Penerima: ").lower().strip()
        hasil = [item for item in daftar if kata_kunci in item["Penerima"].lower()]
    else:
        print("Pilihan tidak benar")
        return
    if not hasil:
        print("Data tidak ditemukan.")
    else:
        print("\nHasil Pencarian:")
        print(tabulate(hasil, headers="keys", tablefmt="fancy_grid"))

def restore_kiriman(daftar, arsip):
    if not arsip:
        print("Tidak ada data kiriman yang diarsipkan.")
        return
    print("\n=== Data Kiriman yang Diarsipkan ===")
    print(tabulate(arsip, headers="keys", tablefmt="fancy_grid"))
    no_resi = input("Masukkan No Resi yang ingin direstore: ").upper().strip()
    if not no_resi:
        print("Error: Input tidak boleh kosong!")
        return
    if not (no_resi.startswith("NR") and len(no_resi) == 7 and no_resi[2:].isdigit()):
    # Jika no_resi tidak dimulai dengan 'NR', atau panjangnya bukan 7 karakter, atau setelah 'NR' tidak ada 5 digit angka, maka tampilkan pesan error.
        print("Error: Format No Resi tidak benar. Format yang benar adalah 'NR' diikuti 5 digit.")
        return
    for item in arsip:
        if item["No Resi"] == no_resi: # Nilai dari kunci 'No Resi' dalam item sama dengan no_resi
            if cek_input_yn(f"Apakah kamu yakin ingin merestore kiriman dengan No Resi {no_resi}? (y/n): ") == "y":
                # Ubah status kiriman menjadi "Dikirim"
                item["Status"] = "Dikirim"
                daftar.append(item)
                arsip.remove(item)
                print(f"Data kiriman dengan Resi {no_resi} berhasil direstore dengan status 'Dikirim'!")
                tampilkan_kiriman(daftar)
            else:
                print("Restore data dibatalkan.")
            return
    print("Data tidak ditemukan dalam arsip.")

def rangkuman_pengiriman(daftar, arsip):
    total_aktif = len(daftar)
    total_arsip = len(arsip)
    total_pengiriman = total_aktif + total_arsip
    # Hitung total pendapatan dengan menjumlahkan semua nilai Biaya dalam daftar, setelah menghapus tanda koma (',') dan mengonversinya menjadi integer.
    pendapatan_aktif = sum(int(item["Biaya"].replace(',', '')) for item in daftar)
    # Hitung total pendapatan dari arsip dengan menjumlahkan semua nilai Biaya dalam arsip, setelah menghapus tanda koma (',') dan mengonversinya menjadi integer.
    pendapatan_arsip = sum(int(item["Biaya"].replace(',', '')) for item in arsip)
    total_pendapatan = pendapatan_aktif + pendapatan_arsip
    rata_rata = total_pendapatan / total_pengiriman if total_pengiriman > 0 else 0
    # Jika total_pengiriman lebih dari 0, maka rata_rata adalah total_pendapatan dibagi total_pengiriman.
    # Jika tidak, maka rata_rata adalah 0.
    data = [
        ["Total Pengiriman Aktif", total_aktif],
        ["Total Pengiriman Arsip", total_arsip],
        ["Total Pengiriman Keseluruhan", total_pengiriman],
        ["Total Pendapatan Aktif", f"{pendapatan_aktif:,}"],
        ["Total Pendapatan Arsip", f"{pendapatan_arsip:,}"],
        ["Total Pendapatan Keseluruhan", f"{total_pendapatan:,}"],
        ["Rata-rata Biaya Pengiriman", f"{rata_rata:,.0f}"]
    ]
    print("\n=== Rangkuman Pengiriman ===")
    print(tabulate(data, headers=["Keterangan", "Nilai"], tablefmt="fancy_grid"))

def main():
    while True:
        print("\n=== Sistem Pengiriman Dinmar Logistik ===")
        print("1. Lihat Data Kiriman")
        print("2. Tambah Data Kiriman")
        print("3. Ubah Data Kiriman")
        print("4. Hapus Data Kiriman")
        print("5. Cari Data Kiriman")
        print("6. Restore Data Kiriman")
        print("7. Rangkuman Pengiriman")
        print("8. Keluar")
        pilihan = cek_input_angka("Pilih Nomor (1-8): ")
        if pilihan == 1:
            tampilkan_kiriman(daftar_kiriman)
        elif pilihan == 2:
            tambah_kiriman(daftar_kiriman)
        elif pilihan == 3:
            ubah_kiriman(daftar_kiriman)
        elif pilihan == 4:
            hapus_kiriman(daftar_kiriman)
        elif pilihan == 5:
            cari_kiriman(daftar_kiriman)
        elif pilihan == 6:
            restore_kiriman(daftar_kiriman, arsip_kiriman)
        elif pilihan == 7:
            rangkuman_pengiriman(daftar_kiriman, arsip_kiriman)
        elif pilihan == 8:
            print("Terima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Pilihan harus antara 1-8!")

if __name__ == "__main__": # Karena file ini dijalankan langsung, __name__ akan bernilai "__main__"
    # sehingga fungsi main() dipanggil.
    main()