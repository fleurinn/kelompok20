# ===========================================================
# Studi Kasus: Sistem Kategori Produk Toko Online (File .txt)
# Kelompok 20
# ===========================================================

# 1. FILE HANDLING & DICTIONARY
nama_file = "kategori.txt"  # file berisi kategori produk
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev

            tail.next = new_node
            new_node.prev = tail

            new_node.next = self.head
            self.head.prev = new_node

    def to_list(self):
        hasil = []
        if self.head is None:
            return hasil

        current = self.head
        while True:
            hasil.append(current.data)
            current = current.next
            if current == self.head:
                break
        return hasil

    def delete_at_index(self, index):
        if self.head is None:
            return

        current = self.head
        count = 0

        while True:
            if count == index:
                if current.next == current:  # hanya 1 node
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    if current == self.head:
                        self.head = current.next
                return

            current = current.next
            count += 1
            if current == self.head:
                break

    def update_at_index(self, index, data_baru):
        current = self.head
        count = 0

        while True:
            if count == index:
                current.data = data_baru
                return

            current = current.next
            count += 1
            if current == self.head:
                break

def muat_data_kategori(nama_file):  
    database_kategori = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                parts = baris.split(",")

                if len(parts) != 3:
                    continue

                kategori, merk, series = [x.strip() for x in parts]

                if kategori not in database_kategori:
                    database_kategori[kategori] = {}

                if merk not in database_kategori[kategori]:
                    database_kategori[kategori][merk] = DoubleCircularLinkedList()

                database_kategori[kategori][merk].append(series)

    except FileNotFoundError:
        print("File belum ada, akan dibuat saat penyimpanan.")

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

        for series in daftar_series.to_list():
            print(f"   │    • {series}")

#menambahkan data baru
def tambah_data(buka_data):
    print("\n=== TAMBAH DATA ===")

    kategori = input("Masukkan kategori (HP/Laptop): ").strip()
    merk = input("Masukkan merk: ").strip()
    series = input("Masukkan series: ").strip()

    kategori_key = cari_key_case_insensitive(buka_data, kategori)

    if kategori_key is None:
        print("Kategori belum ada, akan dibuat baru.")
        buka_data[kategori] = {}
        kategori_key = kategori

    merk_key = cari_key_case_insensitive(buka_data[kategori_key], merk)

    if merk_key is None:
        buka_data[kategori_key][merk] = DoubleCircularLinkedList()
        merk_key = merk

    # cek duplikasi series
    if series not in buka_data[kategori][merk].to_list():
        buka_data[kategori][merk].append(series)
        print("Data berhasil ditambahkan!")
    else:
        print("Series sudah ada!")

#pencarian tanpa case sensitive
def cari_key_case_insensitive(data_dict, key_input):
    for key in data_dict.keys():
        if key.lower() == key_input.lower():
            return key
    return None

#menyimpan data
def simpan_data(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kategori, merk_dict in data.items():
            for merk, series_list in merk_dict.items():
                for series in series_list.to_list():
                    file.write(f"{kategori},{merk},{series}\n")

# update data 
def update_data(buka_data):
    print("\n=== UPDATE DATA ===")

    while True:
        daftar_kategori = list(buka_data.keys())

        # tampilkan kategori
        print("\nDaftar Kategori:")
        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        print("0. Kembali")

        try:
            pilih_kategori = int(input("Pilih kategori: "))
        except ValueError:
            print("Input harus angka!")
            continue

        # kembali ke main menu
        if pilih_kategori == 0:
            return False

        pilih_kategori -= 1

        if not (0 <= pilih_kategori < len(daftar_kategori)):
            print("Pilihan kategori tidak valid!")
            continue

        kategori_terpilih = daftar_kategori[pilih_kategori]

        # =======================
        # MENU MERK
        # =======================
        while True:
            print("\n=== UPDATE KATEGORI ===")
            print("0. Update Nama Kategori")

            daftar_merk = list(
                buka_data[kategori_terpilih].keys()
            )

            # tampilkan merk
            print("\nDaftar Merk:")
            for i in range(len(daftar_merk)):
                print(f"{i+1}. {daftar_merk[i]}")

            nomor_kembali = len(daftar_merk) + 1
            print(f"{nomor_kembali}. Kembali")

            try:
                pilih_merk = int(
                    input(
                        "Pilih merk (0 = update kategori): "
                    )
                )
            except ValueError:
                print("Input harus angka!")
                continue

            # kembali ke kategori
            if pilih_merk == nomor_kembali:
                break

            # update kategori
            elif pilih_merk == 0:
                kategori_baru = input(
                    "Masukkan nama kategori baru: "
                ).strip()

                if kategori_baru == "":
                    print(
                        "Nama kategori tidak boleh kosong!"
                    )
                    continue

                buka_data[kategori_baru] = (
                    buka_data.pop(
                        kategori_terpilih
                    )
                )

                print(
                    "Kategori berhasil diupdate!"
                )
                return True

            pilih_merk -= 1

            if not (
                0 <= pilih_merk
                < len(daftar_merk)
            ):
                print(
                    "Pilihan merk tidak valid!"
                )
                continue

            merk_terpilih = daftar_merk[
                pilih_merk
            ]

            # =======================
            # MENU SERIES
            # =======================
            while True:
                daftar_series = buka_data[
                    kategori_terpilih
                ][merk_terpilih]

                print(
                    "\n=== UPDATE MERK / SERIES ==="
                )
                print(
                    "0. Update Nama Merk"
                )

                # tampilkan series
                daftar_series = (
                    daftar_series.to_list()
                )

                print(
                    "\nDaftar Series:"
                )
                for i in range(
                    len(daftar_series)
                ):
                    print(
                        f"{i+1}. {daftar_series[i]}"
                    )

                nomor_kembali = (
                    len(daftar_series) + 1
                )
                print(
                    f"{nomor_kembali}. Kembali"
                )

                try:
                    pilih_series = int(
                        input(
                            "Pilih series (0 = update merk): "
                        )
                    )
                except ValueError:
                    print(
                        "Input harus angka!"
                    )
                    continue

                # kembali ke merk
                if (
                    pilih_series
                    == nomor_kembali
                ):
                    break

                # update merk
                elif pilih_series == 0:
                    merk_baru = input(
                        "Masukkan nama merk baru: "
                    ).strip()

                    if merk_baru == "":
                        print(
                            "Nama merk tidak boleh kosong!"
                        )
                        continue

                    buka_data[
                        kategori_terpilih
                    ][merk_baru] = (
                        buka_data[
                            kategori_terpilih
                        ].pop(
                            merk_terpilih
                        )
                    )

                    print(
                        "Merk berhasil diupdate!"
                    )
                    return True

                pilih_series -= 1

                if not (
                    0
                    <= pilih_series
                    < len(
                        daftar_series
                    )
                ):
                    print(
                        "Pilihan series tidak valid!"
                    )
                    continue

                print("0. Batal")

                series_baru = input(
                    "Masukkan nama series baru: "
                ).strip()

                # batal update series
                if series_baru == "0":
                    print(
                        "Update series dibatalkan."
                    )
                    continue

                elif series_baru == "":
                    print(
                        "Nama series tidak boleh kosong!"
                    )
                    continue

                buka_data[
                    kategori_terpilih
                ][
                    merk_terpilih
                ].update_at_index(
                    pilih_series,
                    series_baru
                )

                print(
                    "Series berhasil diupdate!"
                )
                return True

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

                daftar_series = daftar_series.to_list()
                for i in range(len(daftar_series)):
                    print(f"{i+1}. {daftar_series[i]}")

                pilih_series = int(input("Pilih series: ")) - 1

                if 0 <= pilih_series < len(daftar_series):
                    series = daftar_series[pilih_series]

                    konfirmasi = input(f"Yakin hapus series '{series}'? (y/t): ").lower()
                    if konfirmasi == "y":
                        buka_data[kategori][merk].delete_at_index(pilih_series)
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

def tampil_next_prev(series_dcll):
    if series_dcll.head is None:
        print("Kosong")
        return

    current = series_dcll.head

    while True:
        print(f"\nSekarang: {current.data}")
        print(f"Prev: {current.prev.data}")
        print(f"Next: {current.next.data}")

        aksi = input("n=next, p=prev, q=keluar: ")

        if aksi == "n":
            current = current.next
        elif aksi == "p":
            current = current.prev
        elif aksi == "q":
            break
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
                print("2. Lihat Next/Prev Series")
                print("3. Kembali")

                sub_pilihan = input("Pilih submenu (1-3): ").strip()

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
                            for series in buka_data[kategori_terpilih][merk_terpilih].to_list():
                                print(f"• {series}")
                        else:
                            print("Pilihan merk tidak valid")
                    else:
                        print("Pilihan kategori tidak valid")
                elif sub_pilihan == "2":
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
                            tampil_next_prev(buka_data[kategori][merk])
                elif sub_pilihan == "3":
                    break

                else:
                    print("Pilihan submenu tidak valid")

        elif pilihan == "2":
            tambah_data(buka_data)
            simpan_data(nama_file, buka_data)
            print("\n=== DATA BERHASIL DI TAMBAHKAN ===")

        elif pilihan == "3":
            hasil_update = update_data(buka_data)
            if hasil_update:
                simpan_data(nama_file, buka_data)
                print("\n=== DATA BERHASIL DI UPDATE ===")
            else:
                print("\nTidak ada perubahan data")

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