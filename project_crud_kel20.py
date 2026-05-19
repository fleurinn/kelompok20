# ===========================================================
# Studi Kasus: Sistem Kategori Produk Toko Online (File .txt)
# Kelompok 20
# ===========================================================

# ===========================================================
# FILE HANDLING & DICTIONARY
# ===========================================================

nama_file = "kategori.txt"


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

                if current.next == current:
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


# ===========================================================
# LOAD DATA
# ===========================================================

def muat_data_kategori(nama_file):

    database_kategori = {}

    try:

        with open(nama_file, "r", encoding="utf-8") as file:

            for baris in file:

                baris = baris.strip()

                if not baris or baris.startswith("#"):
                    continue

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
                    "series": series,
                    "harga": harga,
                    "deskripsi": deskripsi
                })

    except FileNotFoundError:
        print("File belum ada, akan dibuat saat penyimpanan")

    return database_kategori


# ===========================================================
# FORMAT RUPIAH
# ===========================================================

def format_rupiah(angka):
    return f"Rp {angka:,}".replace(",", ".")


# ===========================================================
# TAMPILKAN DATA
# ===========================================================

def tampilkan_data(buka_data):

    print("\n" + "=" * 60)
    print("DATA KATEGORI PRODUK TOKO ONLINE")
    print("=" * 60)

    total_produk = 0

    for kategori, daftar_merk in buka_data.items():

        print(f"\n[{kategori.upper()}]")

        for merk, daftar_produk in daftar_merk.items():

            print(f"  [{merk}]")

            for produk in daftar_produk:

                print(f"    • {produk['series']}")
                print(f"      Harga     : {format_rupiah(produk['harga'])}")
                print(f"      Deskripsi : {produk['deskripsi']}")

                total_produk += 1

    print(f"\n[Total Produk: {total_produk}]")


# ===========================================================
# CASE INSENSITIVE
# ===========================================================

def cari_key_case_insensitive(data_dict, key_input):

    for key in data_dict.keys():

        if key.lower() == key_input.lower():
            return key

    return None


# ===========================================================
# TAMBAH DATA
# ===========================================================

def tambah_data(buka_data):

    print("\n=== TAMBAH DATA ===")

    kategori = input("Masukkan kategori : ").strip()
    merk = input("Masukkan merk      : ").strip()
    series = input("Masukkan series    : ").strip()
    harga = input("Masukkan harga     : ").strip()
    deskripsi = input("Masukkan deskripsi : ").strip()

    # ======================================================
    # VALIDASI INPUT
    # ======================================================

    if kategori == "" or merk == "" or series == "" or harga == "" or deskripsi == "":
        print("\nSemua input wajib diisi!")
        return

    if not harga.isdigit():
        print("\nHarga harus berupa angka!")
        return

    harga = int(harga)

    kategori_baru = False
    merk_baru = False

    # ======================================================
    # CEK KATEGORI
    # ======================================================

    kategori_key = cari_key_case_insensitive(
        buka_data,
        kategori
    )

    if kategori_key is None:

        buka_data[kategori] = {}
        kategori_key = kategori
        kategori_baru = True

    # ======================================================
    # CEK MERK
    # ======================================================

    merk_key = cari_key_case_insensitive(
        buka_data[kategori_key],
        merk
    )

    if merk_key is None:

        buka_data[kategori_key][merk] = []
        merk_key = merk
        merk_baru = True

    # ======================================================
    # CEK DUPLIKASI SERIES
    # ======================================================

    for produk in buka_data[kategori_key][merk_key]:

        if produk['series'].lower() == series.lower():
            print("\nSeries sudah ada!")
            return

    # ======================================================
    # TAMBAH DATA
    # ======================================================

    buka_data[kategori_key][merk_key].append({
        "series": series,
        "harga": harga,
        "deskripsi": deskripsi
    })

    # ======================================================
    # OUTPUT
    # ======================================================

    print("\n===================================")
    print("      DATA BERHASIL DITAMBAHKAN")
    print("===================================")

    print(f"Kategori  : {kategori_key}")
    print(f"Merk      : {merk_key}")
    print(f"Series    : {series}")
    print(f"Harga     : {format_rupiah(harga)}")
    print(f"Deskripsi : {deskripsi}")

    if kategori_baru:
        print("➜ Kategori baru berhasil dibuat")

    if merk_baru:
        print("➜ Merk baru berhasil dibuat")

    print("===================================")


# ===========================================================
# SIMPAN DATA
# ===========================================================

def simpan_data(nama_file, data):

    with open(nama_file, "w", encoding="utf-8") as file:

        for kategori, merk_dict in data.items():

            for merk, daftar_produk in merk_dict.items():

                for produk in daftar_produk:

                    file.write(
                        f"{kategori},"
                        f"{merk},"
                        f"{produk['series']},"
                        f"{produk['harga']},"
                        f"{produk['deskripsi']}\n"
                    )


# ===========================================================
# UPDATE DATA
# ===========================================================

def update_data(buka_data):

    print("\n=== UPDATE DATA ===")

    daftar_kategori = list(buka_data.keys())

    for i in range(len(daftar_kategori)):
        print(f"{i+1}. {daftar_kategori[i]}")

    try:
        pilih_kategori = int(input("Pilih kategori: ")) - 1

    except ValueError:
        print("Input harus angka!")
        return

    if 0 <= pilih_kategori < len(daftar_kategori):

        kategori = daftar_kategori[pilih_kategori]

        daftar_merk = list(buka_data[kategori].keys())

        for i in range(len(daftar_merk)):
            print(f"{i+1}. {daftar_merk[i]}")

        try:
            pilih_merk = int(input("Pilih merk: ")) - 1

        except ValueError:
            print("Input harus angka!")
            return

        if 0 <= pilih_merk < len(daftar_merk):

            merk = daftar_merk[pilih_merk]

            daftar_produk = buka_data[kategori][merk]

            for i in range(len(daftar_produk)):

                print(f"{i+1}. {daftar_produk[i]['series']}")

            try:
                pilih_series = int(input("Pilih series: ")) - 1

            except ValueError:
                print("Input harus angka!")
                return

            if 0 <= pilih_series < len(daftar_produk):

                series_baru = input("Masukkan series baru: ").strip()

                if series_baru == "":
                    print("Series tidak boleh kosong!")
                    return

                daftar_produk[pilih_series]['series'] = series_baru

                print("Data berhasil diupdate")

            else:
                print("Pilihan series tidak valid")

        else:
            print("Pilihan merk tidak valid")

    else:
        print("Pilihan kategori tidak valid")


# ===========================================================
# HAPUS DATA
# ===========================================================

def hapus_data(buka_data):

    print("\n=== HAPUS DATA ===")
    print("1. Hapus Kategori")
    print("2. Hapus Merk")
    print("3. Hapus Series")

    pilihan = input("Pilih jenis yang ingin dihapus (1-3): ").strip()

    # ======================================================
    # HAPUS KATEGORI
    # ======================================================

    if pilihan == "1":

        daftar_kategori = list(buka_data.keys())

        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        try:
            pilih = int(input("Pilih kategori: ")) - 1

        except ValueError:
            print("Input harus angka!")
            return

        if 0 <= pilih < len(daftar_kategori):

            kategori = daftar_kategori[pilih]

            konfirmasi = input(
                f"Yakin hapus kategori '{kategori}'? (y/t): "
            ).lower()

            if konfirmasi == "y":

                del buka_data[kategori]
                print("Kategori berhasil dihapus!")

            else:
                print("Dibatalkan")

        else:
            print("Pilihan tidak valid")

    # ======================================================
    # HAPUS MERK
    # ======================================================

    elif pilihan == "2":

        daftar_kategori = list(buka_data.keys())

        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        try:
            pilih_kategori = int(input("Pilih kategori: ")) - 1

        except ValueError:
            print("Input harus angka!")
            return

        if 0 <= pilih_kategori < len(daftar_kategori):

            kategori = daftar_kategori[pilih_kategori]

            daftar_merk = list(buka_data[kategori].keys())

            for i in range(len(daftar_merk)):
                print(f"{i+1}. {daftar_merk[i]}")

            try:
                pilih_merk = int(input("Pilih merk: ")) - 1

            except ValueError:
                print("Input harus angka!")
                return

            if 0 <= pilih_merk < len(daftar_merk):

                merk = daftar_merk[pilih_merk]

                konfirmasi = input(
                    f"Yakin hapus merk '{merk}'? (y/t): "
                ).lower()

                if konfirmasi == "y":

                    del buka_data[kategori][merk]
                    print("Merk berhasil dihapus!")

                else:
                    print("Dibatalkan")

            else:
                print("Pilihan merk tidak valid")

        else:
            print("Pilihan kategori tidak valid")

    # ======================================================
    # HAPUS SERIES
    # ======================================================

    elif pilihan == "3":

        daftar_kategori = list(buka_data.keys())

        for i in range(len(daftar_kategori)):
            print(f"{i+1}. {daftar_kategori[i]}")

        try:
            pilih_kategori = int(input("Pilih kategori: ")) - 1

        except ValueError:
            print("Input harus angka!")
            return

        if 0 <= pilih_kategori < len(daftar_kategori):

            kategori = daftar_kategori[pilih_kategori]

            daftar_merk = list(buka_data[kategori].keys())

            for i in range(len(daftar_merk)):
                print(f"{i+1}. {daftar_merk[i]}")

            try:
                pilih_merk = int(input("Pilih merk: ")) - 1

            except ValueError:
                print(" Input harus angka!")
                return

            if 0 <= pilih_merk < len(daftar_merk):

                merk = daftar_merk[pilih_merk]

                daftar_produk = buka_data[kategori][merk]

                for i in range(len(daftar_produk)):
                    print(f"{i+1}. {daftar_produk[i]['series']}")

                try:
                    pilih_series = int(input("Pilih series: ")) - 1

                except ValueError:
                    print(" Input harus angka!")
                    return

                if 0 <= pilih_series < len(daftar_produk):

                    series = daftar_produk[pilih_series]['series']

                    konfirmasi = input(
                        f"Yakin hapus series '{series}'? (y/t): "
                    ).lower()

                    if konfirmasi == "y":

                        del daftar_produk[pilih_series]

                        print(" Series berhasil dihapus!")

                    else:
                        print("Dibatalkan")

                else:
                    print(" Pilihan series tidak valid")

            else:
                print(" Pilihan merk tidak valid")

        else:
            print(" Pilihan kategori tidak valid")

    else:
        print(" Pilihan tidak valid")


# ===========================================================
# SEARCH DATA
# ===========================================================

def search_data(buka_data):

    print("\n=== SEARCH DATA ===")
    print("1. Cari Kategori")
    print("2. Cari Merk")
    print("3. Cari Series")

    pilihan = input("Pilih pencarian (1-3): ").strip()

    keyword = input("Masukkan keyword: ").strip().lower()

    if keyword == "":
        print("\n Keyword tidak boleh kosong!")
        return

    ditemukan = False

    # ======================================================
    # SEARCH KATEGORI
    # ======================================================

    if pilihan == "1":

        if len(keyword) < 2:
            print("\n Kategori minimal 2 huruf!")
            return

        for kategori, merk_dict in buka_data.items():

            if keyword in kategori.lower():

                print(f"\n Kategori : {kategori}")

                for merk, daftar_produk in merk_dict.items():

                    print(f"\nMerk : {merk}")

                    for produk in daftar_produk:

                        print(f"• {produk['series']}")
                        print(f"  Harga : {format_rupiah(produk['harga'])}")
                        print(f"  Desk  : {produk['deskripsi']}")

                ditemukan = True

    # ======================================================
    # SEARCH MERK
    # ======================================================

    elif pilihan == "2":

        if len(keyword) < 3:
            print("\n Merk minimal 3 huruf!")
            return

        for kategori, merk_dict in buka_data.items():

            for merk, daftar_produk in merk_dict.items():

                if keyword in merk.lower():

                    print(f"\n Merk : {merk}")
                    print(f"Kategori : {kategori}")

                    for produk in daftar_produk:

                        print(f"\n• {produk['series']}")
                        print(f"  Harga : {format_rupiah(produk['harga'])}")
                        print(f"  Desk  : {produk['deskripsi']}")

                    ditemukan = True

    # ======================================================
    # SEARCH SERIES
    # ======================================================

    elif pilihan == "3":

        if len(keyword) < 3:
            print("\n Series minimal 3 huruf!")
            return

        for kategori, merk_dict in buka_data.items():

            for merk, daftar_produk in merk_dict.items():

                for produk in daftar_produk:

                    if keyword in produk['series'].lower():

                        print("\n===================================")
                        print("SERIES DITEMUKAN")
                        print("===================================")

                        print(f"Kategori  : {kategori}")
                        print(f"Merk      : {merk}")
                        print(f"Series    : {produk['series']}")
                        print(f"Harga     : {format_rupiah(produk['harga'])}")
                        print(f"Deskripsi : {produk['deskripsi']}")

                        ditemukan = True

    else:
        print("\n Pilihan tidak valid!")
        return

    if not ditemukan:
        print("\n Data tidak ditemukan")


# ==========================================================
# SORT DATA
# ==========================================================

def sort_data(buka_data):

    print("\n=== SORT DATA ===")
    print("1. Sort Harga Termurah")
    print("2. Sort Harga Termahal")

    pilihan = input("Pilih sorting (1-2): ").strip()

    semua_produk = []

    # ======================================================
    # GABUNGKAN SEMUA PRODUK
    # ======================================================

    for kategori, merk_dict in buka_data.items():

        for merk, daftar_produk in merk_dict.items():

            for produk in daftar_produk:

                semua_produk.append({
                    "kategori": kategori,
                    "merk": merk,
                    "series": produk['series'],
                    "harga": produk['harga'],
                    "deskripsi": produk['deskripsi']
                })

    # ======================================================
    # SORT HARGA TERMURAH
    # ======================================================

    if pilihan == "1":

        harga_sorted = sorted(
            semua_produk,
            key=lambda x: x['harga']
        )

        print("\n=== SORT HARGA TERMURAH ===")

        for produk in harga_sorted:

            print(f"\n• {produk['series']}")
            print(f"  Kategori : {produk['kategori']}")
            print(f"  Merk     : {produk['merk']}")
            print(f"  Harga    : {format_rupiah(produk['harga'])}")
            print(f"  Desk     : {produk['deskripsi']}")

    # ======================================================
    # SORT HARGA TERMAHAL
    # ======================================================

    elif pilihan == "2":

        harga_sorted = sorted(
            semua_produk,
            key=lambda x: x['harga'],
            reverse=True
        )

        print("\n=== SORT HARGA TERMAHAL ===")

        for produk in harga_sorted:

            print(f"\n• {produk['series']}")
            print(f"  Kategori : {produk['kategori']}")
            print(f"  Merk     : {produk['merk']}")
            print(f"  Harga    : {format_rupiah(produk['harga'])}")
            print(f"  Desk     : {produk['deskripsi']}")

    else:
        print(" Pilihan sorting tidak valid")


# ==========================================================
# MAIN PROGRAM
# ==========================================================
def main():

    # load data dari file
    buka_data = muat_data_kategori(nama_file)

    # tampilkan data awal
    tampilkan_data(buka_data)

    print("\nJumlah Kategori Terbaca:", len(buka_data))

    while True:

        print("\n=== MENU KATEGORI TOKO ONLINE ===")
        print("1. Lihat Kategori Produk")
        print("2. Tambah Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Search Data")
        print("6. Sort Data")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ").strip()

        # ==================================================
        # MENU LIHAT DATA
        # ==================================================
        if pilihan == "1":

            while True:

                print("\n--- SUB MENU KATEGORI ---")
                print("1. Pilih Kategori")
                print("2. Lihat Next/Prev Series")
                print("3. Kembali")

                sub_pilihan = input("Pilih submenu (1-3): ").strip()

                # ==========================================
                # PILIH KATEGORI
                # ==========================================
                if sub_pilihan == "1":

                    daftar_kategori = list(buka_data.keys())

                    print("\nDaftar Kategori:")

                    for i in range(len(daftar_kategori)):
                        print(f"{i+1}. {daftar_kategori[i]}")

                    try:
                        pilih_kategori = int(
                            input("Pilih kategori (input dalam angka): ")
                        ) - 1

                    except ValueError:
                        print("Input harus angka!")
                        continue

                    if 0 <= pilih_kategori < len(daftar_kategori):

                        kategori_terpilih = daftar_kategori[pilih_kategori]

                        daftar_merk = list(
                            buka_data[kategori_terpilih].keys()
                        )

                        print(f"\nMerk untuk {kategori_terpilih}:")

                        for i in range(len(daftar_merk)):
                            print(f"{i+1}. {daftar_merk[i]}")

                        try:
                            pilih_merk = int(
                                input("Pilih merk (input dalam angka): ")
                            ) - 1

                        except ValueError:
                            print("Input harus angka!")
                            continue

                        if 0 <= pilih_merk < len(daftar_merk):

                            merk_terpilih = daftar_merk[pilih_merk]

                            print(f"\nSeries {merk_terpilih}:")

                            daftar_produk = buka_data[
                                kategori_terpilih
                            ][merk_terpilih]

                            for produk in daftar_produk:

                                print(f"\n• {produk['series']}")
                                print(f"  Harga : {format_rupiah(produk['harga'])}")
                                print(f"  Desk  : {produk['deskripsi']}")

                        else:
                            print("Pilihan merk tidak valid")

                    else:
                        print("Pilihan kategori tidak valid")

                # ==========================================
                # NEXT PREV
                # ==========================================
                elif sub_pilihan == "2":

                    daftar_kategori = list(buka_data.keys())

                    print("\nDaftar Kategori:")

                    for i in range(len(daftar_kategori)):
                        print(f"{i+1}. {daftar_kategori[i]}")

                    try:
                        pilih_kategori = int(
                            input("Pilih kategori (input dalam angka): ")
                        ) - 1

                    except ValueError:
                        print("Input harus angka!")
                        continue

                    if 0 <= pilih_kategori < len(daftar_kategori):

                        kategori = daftar_kategori[pilih_kategori]

                        daftar_merk = list(
                            buka_data[kategori].keys()
                        )

                        print(f"\nMerk untuk {kategori}:")

                        for i in range(len(daftar_merk)):
                            print(f"{i+1}. {daftar_merk[i]}")

                        try:
                            pilih_merk = int(
                                input("Pilih merk (input dalam angka): ")
                            ) - 1

                        except ValueError:
                            print("Input harus angka!")
                            continue

                        if 0 <= pilih_merk < len(daftar_merk):

                            merk = daftar_merk[pilih_merk]

                            daftar_produk = buka_data[kategori][merk]

                            index = 0

                            while True:

                                produk = daftar_produk[index]

                                print("\n===================================")
                                print(f"Series : {produk['series']}")
                                print(f"Harga  : {format_rupiah(produk['harga'])}")
                                print(f"Desk   : {produk['deskripsi']}")
                                print("===================================")

                                print("\n[n] Next")
                                print("[p] Prev")
                                print("[q] Keluar")

                                aksi = input(
                                    "Pilih aksi (n/p/q): "
                                ).lower()

                                if aksi == "n":
                                    index = (
                                        index + 1
                                    ) % len(daftar_produk)

                                elif aksi == "p":
                                    index = (
                                        index - 1
                                    ) % len(daftar_produk)

                                elif aksi == "q":
                                    break

                                else:
                                    print("Pilihan tidak valid")

                        else:
                            print("Pilihan merk tidak valid")

                    else:
                        print("Pilihan kategori tidak valid")

                # ==========================================
                # KEMBALI
                # ==========================================
                elif sub_pilihan == "3":
                    break

                else:
                    print("Pilihan submenu tidak valid")

        # ==================================================
        # TAMBAH DATA (PUNYA KAMU)
        # ==================================================
        elif pilihan == "2":

            tambah_data(buka_data)
            simpan_data(nama_file, buka_data)

        # ==================================================
        # UPDATE DATA
        # ==================================================
        elif pilihan == "3":

            update_data(buka_data)
            simpan_data(nama_file, buka_data)

            print("\n=== DATA BERHASIL DI UPDATE ===")

        # ==================================================
        # HAPUS DATA
        # ==================================================
        elif pilihan == "4":

            hapus_data(buka_data)
            simpan_data(nama_file, buka_data)

            print("\n=== DATA BERHASIL DIHAPUS ===")

        # ==================================================
        # SEARCH DATA (PUNYA KAMU)
        # ==================================================
        elif pilihan == "5":

            search_data(buka_data)

        # ==================================================
        # SORT DATA (PUNYA KAMU)
        # ==================================================
        elif pilihan == "6":

            sort_data(buka_data)

        # ==================================================
        # KELUAR
        # ==================================================
        elif pilihan == "7":

            print("Program selesai!!")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()