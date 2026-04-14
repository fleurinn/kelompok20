# ===========================================================
# Studi Kasus: Sistem Kategori Produk Toko Online (File .txt)
# Kelompok 20
# ===========================================================

# 1. FILE HANDLING & DICTIONARY
nama_file = "kategori.txt"  # file berisi kategori produk

def muat_data_kategori(nama_file):
    """
    Fungsi membaca kategori.txt lalu menyimpannya
    ke dictionary bertingkat
    Format file: kategori,merk,series
    """

    database_kategori = {}  # dictionary utama

    # buka file kategori.txt mode baca
    with open(nama_file, "r", encoding="utf-8") as file:

        # baca file per baris
        for baris in file:
            baris = baris.strip()  # hapus enter/newline
            parts = baris.split(",")  # pisahkan berdasarkan koma

            # validasi harus 3 bagian
            if len(parts) != 3:
                continue

            kategori, merk, series = parts

            # jika kategori belum ada, buat dictionary baru
            if kategori not in database_kategori:
                database_kategori[kategori] = {}

            # jika merk belum ada, buat list baru
            if merk not in database_kategori[kategori]:
                database_kategori[kategori][merk] = []

            # tambahkan series ke merk
            database_kategori[kategori][merk].append(series)

    return database_kategori

# memanggil fungsi dan menyimpan hasilnya
buka_data = muat_data_kategori(nama_file)

# menampilkan jumlah kategori utama
print("Jumlah Kategori Terbaca:", len(buka_data))

# output lebih rapi dan terstruktur
print("\n=== Data Kategori Produk ===")

for kategori, daftar_merk in buka_data.items():
    print(f"\n• {kategori}")

    for merk, daftar_series in daftar_merk.items():
        print(f"   ├── {merk}")

        for series in daftar_series:
            print(f"   │    • {series}")

# ==========================================================
# MAIN PROGRAM
# ==========================================================
def main():
    buka_data = muat_data_kategori(nama_file)

    print("Jumlah Kategori Terbaca:", len(buka_data))

    while True:
        print("\n=== MENU KATEGORI TOKO ONLINE ===")
        print("1. Lihat Kategori Produk")
        print("2. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":

            while True:
                print("\n--- SUB MENU KATEGORI ---")
                print("1. Pilih Kategori")
                print("2. Kembali")

                sub_pilihan = input("Pilih submenu (1-2): ").strip()

                if sub_pilihan == "1":
                    daftar_kategori = list(buka_data.keys())

                    print("\nDaftar Kategori:")
                    for i in range(len(daftar_kategori)):
                        print(f"{i+1}. {daftar_kategori[i]}")

                    pilih_kategori = int(input("Pilih kategori: ")) - 1

                    if 0 <= pilih_kategori < len(daftar_kategori):
                        kategori_terpilih = daftar_kategori[pilih_kategori]

                        daftar_merk = list(buka_data[kategori_terpilih].keys())

                        print(f"\nMerk untuk {kategori_terpilih}:")
                        for i in range(len(daftar_merk)):
                            print(f"{i+1}. {daftar_merk[i]}")

                        pilih_merk = int(input("Pilih merk: ")) - 1

                        if 0 <= pilih_merk < len(daftar_merk):
                            merk_terpilih = daftar_merk[pilih_merk]

                            print(f"\nSeries {merk_terpilih}:")
                            for series in buka_data[kategori_terpilih][merk_terpilih]:
                                print(f"• {series}")
                        else:
                            print("Pilihan merk tidak valid")
                    else:
                        print("Pilihan kategori tidak valid")

                elif sub_pilihan == "2":
                    break

                else:
                    print("Pilihan submenu tidak valid")

        elif pilihan == "2":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()