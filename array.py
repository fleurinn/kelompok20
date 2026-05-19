# ===========================================================
# Studi Kasus: Sistem Kategori Produk Toko Online
# Kelompok 20
# ===========================================================

nama_file = "kategori.txt"

def muat_data_kategori(nama_file):
    database_kategori = {}

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            
            if not baris or baris.startswith('#'):
                continue
            
            # split maks 5 bagian
            parts = baris.split(",", 4)
            
            if len(parts) < 5:
                continue

            kategori = parts[0].strip()
            merk = parts[1].strip()
            series = parts[2].strip()
            harga = int(parts[3].strip())
            deskripsi = parts[4].strip()

            if kategori not in database_kategori:
                database_kategori[kategori] = {}
            if merk not in database_kategori[kategori]:
                database_kategori[kategori][merk] = []
            
            database_kategori[kategori][merk].append({
                'series': series,
                'harga': harga,
                'deskripsi': deskripsi
            })

    return database_kategori

def format_rupiah(angka):
    return f"Rp {angka:,}".replace(",", ".")

def tampilkan_data(buka_data):
    print("\n" + "="*60)
    print("DATA KATEGORI PRODUK TOKO ONLINE")
    print("="*60)
    print(f"Total Kategori: {len(buka_data)}")
    
    total_produk = 0
    
    for kategori, daftar_merk in buka_data.items():
        print(f"\n[{kategori.upper()}]")
        
        for merk, daftar_produk in daftar_merk.items():
            print(f"  [{merk}]")
            
            for produk in daftar_produk:
                print(f"    * {produk['series']}")
                print(f"      Harga: {format_rupiah(produk['harga'])}")
                print(f"      Deskripsi: {produk['deskripsi']}")
                total_produk += 1
    
    print(f"\n[Total Produk: {total_produk}]")

# ==========================================================
# MAIN PROGRAM
# ==========================================================
buka_data = muat_data_kategori(nama_file)
tampilkan_data(buka_data)
#menambahkan data baru
def tambah_data(buka_data):
    print("\n=== TAMBAH DATA ===")

    kategori = input("Masukkan kategori (HP/Laptop): ").strip()
    merk = input("Masukkan merk: ").strip()
    series = input("Masukkan series: ").strip()

    # validasi kategori
    if kategori not in buka_data:
        print("Kategori belum ada, akan dibuat baru.")

    # buat kategori jika belum ada
    if kategori not in buka_data:
        buka_data[kategori] = {}

    # buat merk jika belum ada
    if merk not in buka_data[kategori]:
        buka_data[kategori][merk] = []

    # cek duplikasi series
    if series not in buka_data[kategori][merk]:
        buka_data[kategori][merk].append(series)
        print("Data berhasil ditambahkan!")
    else:
        print("Series sudah ada!")

#menyimpan data
def simpan_data(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kategori, merk_dict in data.items():
            for merk, series_list in merk_dict.items():
                for series in series_list:
                    file.write(f"{kategori},{merk},{series}\n")

# update data 
def update_data(buka_data):
    print("\n=== UPDATE DATA ===")

    daftar_kategori = list(buka_data.keys())

    # tampilkan kategori
    for i in range(len(daftar_kategori)):
        print(f"{i+1}. {daftar_kategori[i]}")

    pilih_kategori = int(input("Pilih kategori: ")) -1

    if 0 <= pilih_kategori < len(daftar_kategori):
        kategori_terpilih = daftar_kategori[pilih_kategori]

        daftar_merk = list(buka_data[kategori_terpilih].keys())
        
        # tampilkan merk
        for i in range(len(daftar_merk)):
            print(f"{i+1}. {daftar_merk[i]}")

        pilih_merk = int(input("Pilih merk: ")) - 1

        if 0 <= pilih_merk < len(daftar_merk):
            merk_terpilih = daftar_merk[pilih_merk]

            daftar_series = buka_data[kategori_terpilih][merk_terpilih]

            # tampilkan series 
            for i in range(len(daftar_series)):
                print(f"{i+1}. {daftar_series[i]}")

            pilih_series = int(input("Pilih series yang mau diupdate: ")) - 1

            if 0 <= pilih_series < len(daftar_series):
                series_baru = input("Masukkan nama series baru: ").strip()

                # update data
                buka_data[kategori_terpilih][merk_terpilih][pilih_series] = series_baru
                print("Data berhasil diupdate")
            else:
                print("Pilihan series tidak valid")
        else:
            print("Pilihan merk tidak valid")
    else:
        print("Pilihan Kategori tidak valid")

def hapus_data(buka_data):
    print("\n=== HAPUS DATA ===")
    print("1. Hapus Kategori")
    print("2. Hapus Merk")
    print("3. Hapus Series")

    pilihan = input("Pilih jenis yang ingin dihapus (1-3): ").strip()

    # hapus berdasarkan kategori elekronik
    if pilihan == "1":
        daftar_kategori = list(buka_data.keys())

        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        pilih = int(input("Pilih kategori: ")) - 1

        if 0 <= pilih < len(daftar_kategori):
            kategori = daftar_kategori[pilih]

            konfirmasi = input(f"Yakin hapus kategori '{kategori}'? (y/t): ").lower()
            if konfirmasi == "y":
                del buka_data[kategori]
                print("Kategori berhasil dihapus!")
            else:
                print("Dibatalkan")
        else:
            print("Pilihan tidak valid")

    # hapus berdasarkan merk elekronik
    elif pilihan == "2":
        daftar_kategori = list(buka_data.keys())

        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        pilih_kategori = int(input("Pilih kategori: ")) - 1

        if 0 <= pilih_kategori < len(daftar_kategori):
            kategori = daftar_kategori[pilih_kategori]
            daftar_merk = list(buka_data[kategori].keys())

            for i in range(len(daftar_merk)):
                print(f"{i+1}. {daftar_merk[i]}")

            pilih_merk = int(input("Pilih merk: ")) - 1

            if 0 <= pilih_merk < len(daftar_merk):
                merk = daftar_merk[pilih_merk]

                konfirmasi = input(f"Yakin hapus merk '{merk}'? (y/t): ").lower()
                if konfirmasi == "y":
                    del buka_data[kategori][merk]
                    print("Merk berhasil dihapus!")
                else:
                    print("Dibatalkan")
            else:
                print("Pilihan merk tidak valid")
        else:
            print("Pilihan kategori tidak valid")

    # hapus berdasarkan series elekronik
    elif pilihan == "3":
        daftar_kategori = list(buka_data.keys())

        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        pilih_kategori = int(input("Pilih kategori: ")) - 1

        if 0 <= pilih_kategori < len(daftar_kategori):
            kategori = daftar_kategori[pilih_kategori]
            daftar_merk = list(buka_data[kategori].keys())

            for i in range(len(daftar_merk)):
                print(f"{i+1}. {daftar_merk[i]}")

            pilih_merk = int(input("Pilih merk: ")) - 1

            if 0 <= pilih_merk < len(daftar_merk):
                merk = daftar_merk[pilih_merk]
                daftar_series = buka_data[kategori][merk]

                for i in range(len(daftar_series)):
                    print(f"{i+1}. {daftar_series[i]}")

                pilih_series = int(input("Pilih series: ")) - 1

                if 0 <= pilih_series < len(daftar_series):
                    series = daftar_series[pilih_series]

                    konfirmasi = input(f"Yakin hapus series '{series}'? (y/t): ").lower()
                    if konfirmasi == "y":
                        del buka_data[kategori][merk][pilih_series]
                        print("Series berhasil dihapus!")
                    else:
                        print("Dibatalkan")
                else:
                    print("Pilihan series tidak valid")
            else:
                print("Pilihan merk tidak valid")
        else:
            print("Pilihan kategori tidak valid")
    else:
        print("Pilihan tidak valid")

# ==========================================================
# MAIN PROGRAM
# ==========================================================
def main():
    buka_data = muat_data_kategori(nama_file)

    print("Jumlah Kategori Terbaca:", len(buka_data))

    while True:
        print("\n=== MENU KATEGORI TOKO ONLINE ===")
        print("1. Lihat Kategori Produk")
        print("2. Tambah Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")

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

                    try:
                        pilih_kategori = int(input("Pilih kategori: ")) - 1
                    except:
                        print("Input harus angka!")
                        continue

                    if 0 <= pilih_kategori < len(daftar_kategori):
                        kategori_terpilih = daftar_kategori[pilih_kategori]

                        daftar_merk = list(buka_data[kategori_terpilih].keys())

                        print(f"\nMerk untuk {kategori_terpilih}:")
                        for i in range(len(daftar_merk)):
                            print(f"{i+1}. {daftar_merk[i]}")

                        try:
                            pilih_merk = int(input("Pilih merk: ")) - 1
                        except:
                            print("Input harus angka!")
                            continue

                        if 0 <= pilih_merk < len(daftar_merk):
                            merk_terpilih = daftar_merk[pilih_merk]
                            produk_list = buka_data[kategori_terpilih][merk_terpilih]

                            print(f"\nSeries {merk_terpilih}:")
                            for produk in produk_list:
                                print(f"  - {produk['series']}")
                                print(f"    Harga: {format_rupiah(produk['harga'])}")
                                print(f"    Deskripsi: {produk['deskripsi']}")
                        else:
                            print("Pilihan merk tidak valid")
                    else:
                        print("Pilihan kategori tidak valid")

                elif sub_pilihan == "2":
                    break
                else:
                    print("Pilihan submenu tidak valid")

        elif pilihan == "2":
            tambah_data(buka_data)
            simpan_data(nama_file, buka_data)
            print("\n=== DATA BERHASIL DI TAMBAHKAN ===")

        elif pilihan == "3":
            update_data(buka_data)
            simpan_data(nama_file, buka_data)
            print("\n=== DATA BERHASIL DI UPDATE ===")
            
        elif pilihan == "4":
            hapus_data(buka_data)
            simpan_data(nama_file, buka_data)
            print("\n=== DATA BERHASIL DIHAPUS ===")

        elif pilihan == "5":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()