# ===========================================================
# Studi Kasus: Sistem Kategori Produk Toko Online (File .txt)
# Kelompok 20
# ===========================================================

# ===========================================================
# FILE HANDLING & DICTIONARY
# ===========================================================

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

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

    def __iter__(self):

        if self.head is None:
            return

        current = self.head

        while True:

            yield current.data
            current = current.next

            if current == self.head:
                break

    def __len__(self):

        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:

            count += 1
            current = current.next

            if current == self.head:
                break

        return count

    def __getitem__(self, index):

        node = self.get_node_at_index(index)

        if node is None:
            raise IndexError("Index out of range")

        return node.data

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

    def get_node_at_index(self, index):
        if self.head is None:
            return None
        current = self.head
        count = 0
        while True:
            if count == index:
                return current
            current = current.next
            count += 1
            if current == self.head:
                break
        return None
# ===========================================================
# WARNA TAMPILAN
# ===========================================================
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RED_BOLD = '\033[1;91m'
    GREEN_BOLD = '\033[1;92m'
    YELLOW_BOLD = '\033[1;93m'
    BLUE_BOLD = '\033[1;94m'
    CYAN_BOLD = '\033[1;96m'

# ===========================================================
# STACK RIWAYAT UPDATE
# ===========================================================

# Mengimpor modul datetime untuk mencatat waktu saat riwayat update disimpan
from datetime import datetime


# Class Stack digunakan untuk menyimpan riwayat perubahan data
# dengan konsep LIFO, yaitu data yang terakhir masuk akan menjadi data pertama yang keluar.
class Stack:

    # Constructor, dijalankan saat objek Stack dibuat. 
    # Membuat list kosong sebagai tempat penyimpanan data stack
    def __init__(self):
        self.items = []

    # Mengecek apakah stack kosong. Mengembalikan True jika kosong, False jika ada isi
    def is_empty(self):
        return len(self.items) == 0

    # Menambahkan data baru ke bagian paling atas stack
    def push(self, data):
        self.items.append(data)

    # Menghapus dan mengambil data paling atas stack. Jika stack kosong, mengembalikan None
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    # Melihat data paling atas stack tanpa menghapusnya. Jika stack kosong, mengembalikan None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # Mengambil seluruh isi stack, digunakan untuk menampilkan seluruh riwayat yang tersimpan
    def get_all(self):
        return self.items

'''
Membuat objek stack global bernama riwayat_update
objek ini digunakan untuk menyimpan seluruh riwayat 
update data selama program berjalan
'''
riwayat_update = Stack()

# ===========================================================
# SIMPAN RIWAYAT UPDATE KE STACK
# ===========================================================
# Fungsi untuk menyimpan data perubahan (update)
# ke dalam stack riwayat_update
def simpan_riwayat_update(
    kategori,
    merk,
    data_lama,
    data_baru
):

    # Mengambil tanggal dan waktu saat update dilakukan
    # Format: hari-bulan-tahun jam:menit:detik
    waktu_update = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    # Membuat dictionary yang berisi informasi riwayat update
    histori = {
        "tanggal": waktu_update,     # waktu terjadinya update
        "kategori": kategori,        # kategori produk
        "merk": merk,                # merk produk
        "data_lama": data_lama.copy(), # data sebelum diubah
        "data_baru": data_baru.copy()  # data setelah diubah
    }

    # Menyimpan data histori ke dalam stack
    # menggunakan metode push()
    riwayat_update.push(histori) 
# ===========================================================
# SIMPAN RIWAYAT KE FILE TXT
# ===========================================================
def simpan_riwayat_txt(
    nama_file="riwayat_update.txt"
):

    with open(
        nama_file,
        "a",   # ganti dari "w" ke "a"
        encoding="utf-8"
    ) as file:

        data = riwayat_update.peek()

        if data:

            file.write(
                "=" * 50 + "\n"
            )

            file.write(
                f"Tanggal Update : "
                f"{data['tanggal']}\n"
            )

            file.write(
                f"Kategori       : "
                f"{data['kategori']}\n"
            )

            file.write(
                f"Merk            : "
                f"{data['merk']}\n"
            )

            file.write("\n--- DATA LAMA ---\n")

            file.write(
                f"Series    : "
                f"{data['data_lama']['series']}\n"
            )

            file.write(
                f"Harga     : "
                f"{data['data_lama']['harga']}\n"
            )

            file.write(
                f"Deskripsi : "
                f"{data['data_lama']['deskripsi']}\n"
            )

            file.write(
                f"Stok      : "
                f"{data['data_lama'].get('stok', 0)}\n"
            )

            file.write("\n--- DATA BARU ---\n")

            file.write(
                f"Series    : "
                f"{data['data_baru']['series']}\n"
            )

            file.write(
                f"Harga     : "
                f"{data['data_baru']['harga']}\n"
            )

            file.write(
                f"Deskripsi : "
                f"{data['data_baru']['deskripsi']}\n"
            )

            file.write(
                f"Stok      : "
                f"{data['data_baru'].get('stok', 0)}\n"
            )

            file.write(
                "=" * 50 + "\n\n"
            )
# ==========================================================
# LIHAT SEMUA RIWAYAT UPDATE
# ==========================================================
def lihat_riwayat_update(
    nama_file="riwayat_update.txt"
):

    print("\n" + Colors.CYAN + "=" * 60 + Colors.RESET)
    print(Colors.CYAN_BOLD + "       📋 RIWAYAT UPDATE DATA          ".center(60) + Colors.RESET)
    print(Colors.CYAN + "=" * 60 + Colors.RESET)

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            isi = file.read()

            if isi.strip() == "":
                print(Colors.YELLOW + "Belum ada riwayat update." + Colors.RESET)

            else:
                print(isi)

    except FileNotFoundError:
        print(Colors.YELLOW + "Belum ada file riwayat update." + Colors.RESET)
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
                parts = baris.split(",", 5)
                if len(parts) < 6:
                    continue
                kategori = parts[0].strip()
                merk = parts[1].strip()
                series = parts[2].strip()
                harga = int(parts[3].strip())
                deskripsi = parts[4].strip()
                stok = int(parts[5].strip()) if parts[5].strip().isdigit() else 0

                if kategori not in database_kategori:
                    database_kategori[kategori] = {}
                if merk not in database_kategori[kategori]:
                    database_kategori[kategori][merk] = DoubleCircularLinkedList()
                database_kategori[kategori][merk].append({
                    "series": series,
                    "harga": harga,
                    "deskripsi": deskripsi,
                    "stok": stok
                })
    except FileNotFoundError:
        print(Colors.YELLOW + "File belum ada, akan dibuat saat penyimpanan" + Colors.RESET)

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
    
    print("\n" + "═" * 70)
    print("📦 KATALOG PRODUK TOKO ONLINE".center(70))
    print("═" * 70)
    
    total = 0
    
    for kategori, data_merk in buka_data.items():
        # HEADER KATEGORI
        print(f"\n[{kategori.upper()}]")
        
        for merk, produk_list in data_merk.items():
            # HEADER MERK
            print(f"  [{merk}]")
            
            for p in produk_list:
                series = p.get('series', '')
                harga = format_rupiah(p.get('harga', 0))
                desk = p.get('deskripsi', '')
                stok = p.get('stok', 0)
                
                # Label stok
                if stok <= 0:
                    st = Colors.RED + "🚫 HABIS" + Colors.RESET
                elif stok <= 5:
                    st = Colors.YELLOW + f"⚠️ {stok}" + Colors.RESET
                else:
                    st = Colors.GREEN + f"✅ {stok}" + Colors.RESET
                
                print(f"    📱 {Colors.BOLD}{series}{Colors.RESET}")
                print(f"       💰 {harga}   {st}")
                print(f"       📝 {desk}")
                print()
                
                total += 1
    
    print("─" * 70)
    print(f"Total Produk: {Colors.YELLOW}{total}{Colors.RESET}")
    print("─" * 70)
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

    print("\n" + Colors.CYAN + "═" * 50 + Colors.RESET)
    print(Colors.CYAN_BOLD + "         ➕ TAMBAH DATA BARU          ".center(50) + Colors.RESET)
    print(Colors.CYAN + "═" * 50 + Colors.RESET)

    kategori = input(Colors.WHITE + "\n"
    "Masukkan Kategori (HP/Laptop): " + Colors.RESET).strip()
    merk = input(Colors.WHITE + "Masukkan Merk                : " + Colors.RESET).strip()
    series = input(Colors.WHITE + "Masukkan Series              : " + Colors.RESET).strip()
    harga = input(Colors.WHITE + "Masukkan Harga (angka)       : " + Colors.RESET).strip()
    deskripsi = input(Colors.WHITE + "Masukkan Deskripsi Barang    : " + Colors.RESET).strip()
    stok = input(Colors.WHITE + "Masukkan Jumlah Stok (angka) : " + Colors.RESET).strip()

    # ======================================================
    # VALIDASI INPUT
    # ======================================================

    if kategori == "" or merk == "" or series == "" or harga == "" or deskripsi == "":
        print("\nSemua input wajib diisi!" + Colors.RESET)
        return

    if not harga.isdigit():
        print("\nHarga harus berupa angka!" + Colors.RESET)
        return

    harga = int(harga)
    stok = int(stok)

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

        buka_data[kategori_key][merk] = DoubleCircularLinkedList()
        merk_key = merk
        merk_baru = True

    # ======================================================
    # CEK DUPLIKASI SERIES
    # ======================================================

    for produk in buka_data[kategori_key][merk_key]:

        if produk['series'].lower() == series.lower():
            print(Colors.RED + "\nSeries sudah ada!" + Colors.RESET)
            return

    # ======================================================
    # TAMBAH DATA
    # ======================================================

    buka_data[kategori_key][merk_key].append({
        "series": series,
        "harga": harga,
        "deskripsi": deskripsi,
        "stok": stok
    })

    # ======================================================
    # OUTPUT
    # ======================================================

    print(Colors.GREEN + "\n" + "═" * 45 + Colors.RESET)
    print(Colors.GREEN_BOLD + "      ✅ DATA BERHASIL DITAMBAHKAN       ".center(45) + Colors.RESET)
    print(Colors.GREEN + "═" * 45 + Colors.RESET)
    
    print(f"\n{Colors.WHITE}Kategori  :{Colors.RESET} {kategori_key}")
    print(f"{Colors.WHITE}Merk       :{Colors.RESET} {merk_key}")
    print(f"{Colors.WHITE}Series     :{Colors.RESET} {series}")
    print(f"{Colors.WHITE}Harga      :{Colors.RESET} {format_rupiah(harga)}")
    print(f"{Colors.WHITE}Deskripsi  :{Colors.RESET} {deskripsi}")
    print(f"{Colors.WHITE}Stok      :{Colors.RESET} {stok} unit")

    if kategori_baru:
        print(Colors.CYAN + "Kategori baru berhasil dibuat!" + Colors.RESET)
    if merk_baru:
        print(Colors.CYAN + "Merk baru berhasil dibuat!" + Colors.RESET)
    
    print(Colors.GREEN + "═" * 45 + Colors.RESET)
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
                        f"{produk['deskripsi']},"
                        f"{produk['stok']}\n"
                )
# ===========================================================
# UPDATE DATA
# ===========================================================
def update_data(buka_data):

    # menampilkan header menu update data
    print("\n" + Colors.CYAN + "═" * 50 + Colors.RESET)
    print(Colors.CYAN_BOLD + "         🔄 UPDATE DATA          ".center(50) + Colors.RESET)
    print(Colors.CYAN + "═" * 50 + Colors.RESET)
    # mengambil seluruh kategori yang tersedia
    daftar_kategori = list(buka_data.keys())
    # menghentikan proses jika tidak ada data kategori
    if len(daftar_kategori) == 0:
        print("Data kosong!")
        return False
    # pilih kategori
    lebar_no = 3
    lebar_kategori = 46
    RED = "\033[91m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # KATEGORI
    # while true digunakan agar menu kategori terus ditampilkan sampai user memilih opsi kembali atau memasukkan pilihan yang valid
    while True:

        # mengambil semua nama kategori dari dictionary buka_data lalu mengubahnya menjadi list agar bisa ditampilkan satu per satu
        daftar_kategori = list(buka_data.keys())

        # menampilkan header tabel kategori
        print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}}{RESET}")
        print("─" * (lebar_no + lebar_kategori + 1))

        # menampilkan seluruh kategori beserta nomor urutnya
        for i in range(len(daftar_kategori)):
            print(f"{str(i+1) + '.':<{lebar_no}}{daftar_kategori[i]:<{lebar_kategori}}")

        # membuat nomor khusus untuk opsi kembali, jika ada 3 kategori maka nomor kembali menjadi 4
        nomor_kembali = len(daftar_kategori) + 1

        # menampilkan opsi kembali ke menu sebelumnya
        print("-" * (lebar_no + lebar_kategori + 1))
        print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")

        try:
            # meminta user memilih kategori berdasarkan nomor input dikonversi menjadi integer
            pilih_kategori = int(input("\nPilih kategori: "))
        except ValueError:
            # dijalankan jika user memasukkan selain angka contoh: user mengetik "abc" atau "makanan"
            print(f"{BOLD}{RED}Input harus angka!{RESET}")
            # kembali ke awal while dan menampilkan menu lagi
            continue

        # mengecek apakah user memilih menu kembali
        if (pilih_kategori == nomor_kembali):
            # keluar dari menu kategori dan kembali ke menu sebelumnya
            return False

        # mengubah nomor pilihan user menjadi indeks list
        # contoh: user pilih 1 -> indeks 0
        pilih_kategori -= 1

        # mengecek apakah nomor yang dipilih berada dalam rentang kategori yang tersedia
        if not (0 <= pilih_kategori < len(daftar_kategori)):
            # menampilkan pesan error jika pilihan tidak tersedia
            print(f"{RED}{BOLD}Pilihan kategori tidak valid.{RESET}")
            # kembali ke awal while dan menampilkan menu lagi
            continue

        # MERK
        # mengambil nama kategori yang sebelumnya dipilih user, contoh: user memilih kategori "hp"
        kategori_terpilih = (daftar_kategori[pilih_kategori])

        # while true digunakan agar menu merk terus ditampilkan sampai user memilih kembali atau berhasil mengubah kategori
        while True:

            # membuat judul menu berdasarkan kategori yang dipilih, contoh: "UPDATE NAMA HP:"
            teks = f"UPDATE NAMA {kategori_terpilih}:".upper()
            print(f"{GREEN}{BOLD}\n{teks}{RESET}")
            # opsi 0 digunakan untuk mengubah nama kategori
            print("0. Update")

            # mengambil seluruh merk yang ada di dalam kategori terpilih, contoh:Samsung, Iphone, Oppo, dsb
            daftar_merk = list(buka_data[kategori_terpilih].keys())

            # menentukan lebar masing-masing kolom tabel
            lebar_no = 3
            lebar_kategori = 10
            lebar_merk = 35
            # menampilkan header tabel
            print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}}{'KATEGORI':<{lebar_kategori}}{'MERK':<{lebar_merk}}{RESET}")
            print("─" * (lebar_no + lebar_kategori + lebar_merk + 2))
            # menampilkan seluruh merk dalam kategori yang dipilih
            for i in range(len(daftar_merk)):
                # nama kategori hanya ditampilkan pada baris pertama agar tabel lebih rapi
                kategori_tampil = (kategori_terpilih if i == 0 else "")
                print(f"{str(i+1)+'.':<{lebar_no}}{kategori_tampil:<{lebar_kategori}}{daftar_merk[i]:<{lebar_merk}}")

            # membuat nomor untuk opsi kembali, contoh: jika ada 3 merk maka nomor kembali = 4
            nomor_kembali = (len(daftar_merk) + 1)

            # menampilkan opsi kembali
            print("-" * (lebar_no + lebar_kategori + lebar_merk + 2))
            print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")
            
            try:
                # meminta user memilih merk atau kategori [0 = update kategori, 1,2,3,... = memilih merk]
                pilih_merk = int(input(f"\nPilih Merk atau Kategori: "))
            except ValueError:
                # dijalankan jika user memasukkan selain angka, contoh: "abc", "minuman", "@@@"
                print("Input harus angka!")
                # kembali ke awal while
                continue

            # mengecek apakah user memilih opsi kembali
            if (pilih_merk == nomor_kembali):
                # keluar dari menu merk dan kembali ke menu sebelumnya
                break

            # mengecek apakah user memilih opsi update kategori
            if pilih_merk == 0:
                # meminta nama kategori baru, strip() digunakan untuk menghapus spasi di awal dan akhir input
                kategori_baru = input("Masukkan nama kategori baru (Enter = tidak diubah): ").strip()
                # jika user langsung menekan enter tanpa mengisi nama kategori
                if kategori_baru == "":
                    # kategori tidak diubah
                    print(f"{BOLD}{RED}Kategori tidak diubah.{RESET}")
                    continue
                # mengecek apakah nama kategori baru berbeda dari kategori lama
                if (kategori_baru.lower() != kategori_terpilih.lower()):
                    # mencari apakah kategori dengan nama tersebut sudah ada
                    kategori_sudah_ada = (cari_key_case_insensitive(buka_data, kategori_baru))
                    # jika kategori ditemukan maka berarti duplikat
                    if (kategori_sudah_ada is not None):
                        # update dibatalkan karena nama kategori sudah digunakan
                        print(f"{BOLD}{RED}Kategori sudah ada!{RESET}")
                        continue

                # mengganti nama key kategori pada dictionary, data yang ada di dalam kategori tetap dipertahankan
                buka_data[kategori_baru] = buka_data.pop(kategori_terpilih)
                # memperbarui variabel kategori yang sedang dipilih
                kategori_terpilih = (kategori_baru)
                # menampilkan pesan berhasil
                print(f"{BOLD}{GREEN}Kategori berhasil diupdate!{RESET}")
                # mengakhiri fungsi dan mengembalikan nilai true
                return True

            # mengubah nomor pilihan user menjadi indeks list, contoh: user pilih 1 -> indeks 0
            pilih_merk -= 1

            # mengecek apakah nomor merk yang dipilih valid
            if not (0 <= pilih_merk < len(daftar_merk)):
                # menampilkan pesan error jika nomor merk tidak tersedia
                print("Pilihan merk tidak valid")
                # kembali ke awal while
                continue

            # SERIES
            # mengambil merk yang dipilih user dari daftar merk, contoh: user memilih "samsung"
            merk_terpilih = (daftar_merk[pilih_merk])

            # while true digunakan agar menu series terus ditampilkan,sampai user memilih kembali atau melakukan update
            while True:
                # mengambil seluruh data produk dari merk yang dipilih, lalu mengubah linked list menjadi list agar mudah ditampilkan
                daftar_produk = buka_data[kategori_terpilih][merk_terpilih]
                produk_list = daftar_produk.to_list()

                # mengecek apakah merk memiliki series atau tidak, jika kosong maka user tidak bisa melakukan update series
                if len(produk_list) == 0:
                    print(f"{BOLD}{RED}\nMerk ini tidak punya series.{RESET}")
                    break

                # menampilkan menu update series beserta daftar series yang tersedia
                teks = f"UPDATE SERIES {merk_terpilih}:".upper()
                print(f"{GREEN}{BOLD}\n{teks}{RESET}")
                print("0. Update")

                # menentukan ukuran kolom dan menampilkan tabel series
                lebar_no = 3
                lebar_kategori = 10
                lebar_merk = 10
                lebar_series = 24

                print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}} {'MERK':<{lebar_merk}} {'SERIES':<{lebar_series}}{RESET}")
                print("─" * (lebar_no + lebar_kategori + lebar_merk + lebar_series + 3))

                # menampilkan seluruh series yang dimiliki merk terpilih, kategori dan merk hanya ditampilkan pada baris pertama agar tabel lebih rapi
                for i in range(len(produk_list)):
                    kategori_tampil = (kategori_terpilih if i == 0 else "")
                    merk_tampil = (merk_terpilih if i == 0 else "")
                    print(f"{str(i+1)+'.':<{lebar_no}} {kategori_tampil:<{lebar_kategori}} {merk_tampil:<{lebar_merk}} {produk_list[i]['series']:<{lebar_series}}")

                # membuat nomor untuk opsi kembali
                nomor_kembali = (len(produk_list) + 1)
                print("-" * (lebar_no + lebar_kategori + lebar_merk + lebar_series + 3))
                print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")
                try:
                    # meminta user memilih series yang ingin diupdate
                    pilih_series = int(input(f"\nPilih Series: "))
                except ValueError:
                    # dijalankan jika user memasukkan selain angka
                    print(f"{BOLD}{RED}Input harus angka!{RESET}")
                    continue

                # jika user memilih opsi kembali maka keluar dari menu series
                if pilih_series == nomor_kembali:
                    break

                # ==========================================
                # UPDATE NAMA MERK
                # ==========================================
                # jika user memilih 0 maka program akan mengubah nama merk
                if pilih_series == 0:

                    # meminta nama merk baru, enter tanpa input berarti batal mengubah merk
                    merk_baru = input("Masukkan nama merk baru (Enter = tidak diubah): ").strip()
                    if merk_baru == "":
                        print(f"{BOLD}{RED}Merk tidak diubah.{RESET}")
                        continue

                    # mengecek apakah nama merk baru sudah ada dalam kategori yang sama, agar tidak terjadi duplikasi data merk
                    merk_sudah_ada = (
                        cari_key_case_insensitive(buka_data[kategori_terpilih], merk_baru))
                    if (merk_sudah_ada is not None and
                        merk_sudah_ada.lower() != merk_terpilih.lower()):
                        print(f"{BOLD}{RED}Merk sudah ada!{RESET}")
                        continue

                    # mengganti nama key merk pada dictionary, seluruh data produk di dalam merk tetap dipertahankan
                    buka_data[kategori_terpilih][merk_baru] = (
                        buka_data[kategori_terpilih].pop(merk_terpilih)
                    )
                    merk_terpilih = merk_baru
                    print(f"{BOLD}{GREEN}Merk berhasil diupdate!{RESET}")
                    # mengakhiri proses karena update berhasil
                    return True

                # mengubah nomor pilihan user menjadi indeks list
                pilih_series -= 1

                # memastikan nomor series yang dipilih berada dalam rentang yang valid
                if not (0 <= pilih_series < len(produk_list)):
                    print(f"{BOLD}{RED}Pilihan series tidak valid!{RESET}")
                    continue

                # mengambil node produk berdasarkan indeks series yang dipilih
                node_produk = daftar_produk.get_node_at_index(pilih_series)

                # memastikan node produk benar-benar ditemukan
                if node_produk is None:
                    print(f"{BOLD}{RED}Data tidak ditemukan!{RESET}")
                    continue

                # mengambil data produk dari node terpilih, lalu membuat salinan data lama sebagai backup sebelum proses update
                produk = node_produk.data
                data_lama = produk.copy()

                # ==========================================
                # DATA LAMA
                # ==========================================
                # menampilkan data produk lama sebagai referensi sebelum user melakukan perubahan
                print(f"\n{BOLD}{GREEN}=== DATA LAMA ==={RESET}")
                print(f"Series     : {produk['series']}")
                print(f"Harga      : {format_rupiah(produk['harga'])}")
                print(f"Deskripsi  : {produk['deskripsi']}")
                print(f"Stok       : {produk['stok']}")
                print("\nKosongkan input jika tidak ingin diubah")

                # ==========================================
                # INPUT DATA BARU
                # ==========================================
                # meminta data baru dari user, input yang dikosongkan akan tetap menggunakan data lama
                series_baru = input("Series baru        : ").strip()
                harga_baru = input("Harga baru(angka): Rp").strip()
                deskripsi_baru = input("Deskripsi baru     : ").strip()
                stok_baru = input("Stok baru          : ").strip()

                # ==========================================
                # VALIDASI DUPLIKAT SERIES
                # ==========================================
                # mengecek apakah nama series baru sudah digunakan oleh produk lain dalam merk yang sama
                if series_baru != "":
                    series_duplikat = False
                    for i in range(len(produk_list)):
                        if (i != pilih_series and produk_list[i]['series'].lower() == series_baru.lower()):
                            print(f"{BOLD}{RED}Series sudah ada!{RESET}")
                            series_duplikat = True
                            break
                    # membatalkan proses update jika ditemukan series yang sama
                        if series_duplikat:
                            continue
                    # mengubah nama series jika user memasukkan series baru
                        continue

                # ==========================================
                # UPDATE SERIES
                # ==========================================
                # mengubah nama series jika user memasukkan series baru
                if series_baru != "":
                    produk['series'] = series_baru

                # ==========================================
                # UPDATE HARGA
                # ==========================================
                # mengubah harga jika user memasukkan harga baru dan memastikan input berupa angka
                if harga_baru != "":
                    if harga_baru.isdigit():
                        produk['harga'] = int(harga_baru)
                    else:
                        print(f"{BOLD}{RED}Harga harus berupa angka!{RESET}")
                        continue

                # ==========================================
                # UPDATE DESKRIPSI
                # ==========================================
                # mengubah deskripsi produk jika user memasukkan deskripsi baru
                if deskripsi_baru != "":
                    produk['deskripsi'] = deskripsi_baru

                # ==========================================
                # UPDATE STOK
                # ==========================================
                # mengubah stok jika user memasukkan stok baru dan memastikan input berupa angka
                if stok_baru != "":
                    if stok_baru.isdigit():
                        produk['stok'] = int(stok_baru)
                    else:
                        print(f"{BOLD}{RED}Stok harus berupa angka!{RESET}")
                        continue
                # menyimpan data produk setelah update sebagai riwayat perubahan
                data_baru = produk.copy()
                # menyimpan riwayat update ke stack dan file txt agar dapat dilacak kembali
                simpan_riwayat_update(kategori_terpilih, merk_terpilih, data_lama, data_baru)
                simpan_riwayat_txt()
                # menampilkan pesan berhasil lalu mengakhiri proses update
                print(f"{BOLD}{GREEN}\nSeries berhasil diupdate!{RESET}")
                return True
# ===========================================================
# HAPUS DATA
# ===========================================================
def hapus_data(buka_data):

    RED = "\033[91m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print("\n" + CYAN + "═" * 50 + RESET)
    print(CYAN + BOLD + "         🗑️ HAPUS DATA          ".center(50) + RESET)
    print(CYAN + "═" * 50 + RESET)

    # menampilkan menu hapus data
    print(f"1. Hapus Kategori")
    print(f"2. Hapus Merk")
    print(f"3. Hapus Series")
    print(f"4. Hapus Riwayat Update")
    print(f"5. Kembali")

    pilihan = input("\nPilih jenis yang ingin dihapus (1-5): ").strip()
    
    if pilihan == "5":
        return False

    # ==========================================
    # HAPUS KATEGORI
    # ==========================================
    if pilihan == "1":

        # mengambil seluruh kategori yang tersedia
        daftar_kategori = list(buka_data.keys())

        # menghentikan proses jika tidak ada data kategori
        if len(daftar_kategori) == 0:
            print(f"{BOLD}{RED}Data kosong!{RESET}")
            return False

        # menentukan ukuran kolom lalu menampilkan daftar kategori
        lebar_no = 3
        lebar_kategori = 45
        print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}}{RESET}")
        print("─" * (lebar_no + lebar_kategori + 1))
        for i in range(len(daftar_kategori)):
            print(f"{str(i+1)+'.':<{lebar_no}} {daftar_kategori[i]:<{lebar_kategori}}")

        # membuat nomor untuk opsi kembali
        nomor_kembali = len(daftar_kategori) + 1
        print("-" * (lebar_no + lebar_kategori + 1))
        print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")

        try:
            # meminta user memilih kategori yang ingin dihapus
            pilih = int(input("\nPilih kategori: "))
        except ValueError:
            # dijalankan jika user memasukkan selain angka
            print(f"{BOLD}{RED}Input harus angka!{RESET}")
            return False

        # kembali ke menu sebelumnya jika user memilih opsi kembali
        if pilih == nomor_kembali:
            return False

        # mengubah nomor pilihan menjadi indeks list
        pilih -= 1

        # memastikan kategori yang dipilih valid
        if 0 <= pilih < len(daftar_kategori):
            kategori = daftar_kategori[pilih]
            # meminta konfirmasi sebelum data benar-benar dihapus
            while True:
                konfirmasi = input(f"\n{YELLOW}Yakin hapus kategori '{kategori}'? {GREEN}(y){RESET}/{RED}(t){RESET}: ").lower()
                # menghapus kategori jika user mengonfirmasi
                if konfirmasi == "y":
                    del buka_data[kategori]
                    print(f"{BOLD}{GREEN}Kategori berhasil dihapus!{RESET}")
                    return True
                # membatalkan proses penghapusan
                elif konfirmasi == "t":
                    print(f"{BOLD}{RED}Dibatalkan{RESET}")
                    return False
                # meminta user memasukkan pilihan yang benar
                else:
                    print(f"{BOLD}{RED}Masukkan y/t{RESET}")

        # dijalankan jika nomor kategori tidak tersedia
        else:
            print(f"{BOLD}{RED}Pilihan tidak valid{RESET}")
            return False
    # ==========================================
    # HAPUS MERK
    # ==========================================
    elif pilihan == "2":

        # mengambil seluruh kategori yang tersedia
        daftar_kategori = list(buka_data.keys())

        # menghentikan proses jika tidak ada data kategori
        if len(daftar_kategori) == 0:
            print(f"{BOLD}{RED}Data kosong!{RESET}")
            return False

        # menampilkan daftar kategori yang tersedia serta membuat nomor untuk opsi kembali
        lebar_no = 3
        lebar_kategori = 45
        print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}}{RESET}")
        print("─" * (lebar_no + lebar_kategori + 1))
        for i in range(len(daftar_kategori)):
            print(f"{str(i+1)+'.':<{lebar_no}} {daftar_kategori[i]:<{lebar_kategori}}")
        nomor_kembali = len(daftar_kategori) + 1
        print("-" * (lebar_no + lebar_kategori + 1))
        print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")

        try:
            # meminta user memilih kategori yang berisi merk yang akan dihapus
            pilih_kategori = int(input("\nPilih kategori: "))
        except ValueError:
            # dijalankan jika user memasukkan selain angka
            print(f"{BOLD}{RED}Input harus angka!{RESET}")
            return False

        # kembali ke menu sebelumnya jika user memilih opsi kembali
        if pilih_kategori == nomor_kembali:
            return False

        # mengubah nomor pilihan menjadi indeks list
        pilih_kategori -= 1

        # memastikan kategori yang dipilih valid
        if 0 <= pilih_kategori < len(daftar_kategori):
            kategori = daftar_kategori[pilih_kategori]
            daftar_merk = list(buka_data[kategori].keys())
            # menghentikan proses jika kategori tidak memiliki merk
            if len(daftar_merk) == 0:
                print(f"{BOLD}{RED}Merk tidak ada!{RESET}")
                return False
            # menampilkan daftar merk pada kategori yang dipilih
            lebar_no = 3
            lebar_kategori = 12
            lebar_merk = 32
            print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}} {'MERK':<{lebar_merk}}{RESET}")
            print("─" * (lebar_no + lebar_kategori + lebar_merk + 2))
            for i in range(len(daftar_merk)):
                kategori_tampil = kategori if i == 0 else ""
                print(f"{str(i+1)+'.':<{lebar_no}} {kategori_tampil:<{lebar_kategori}} {daftar_merk[i]:<{lebar_merk}}")
            # membuat nomor untuk opsi kembali
            nomor_kembali = len(daftar_merk) + 1
            print("-" * (lebar_no + lebar_kategori + lebar_merk + 2))
            print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")
            try:
                # meminta user memilih merk yang ingin dihapus
                pilih_merk = int(input("\nPilih merk: "))
            except ValueError:
                # dijalankan jika user memasukkan selain angka
                print(f"{BOLD}{RED}Input harus angka!{RESET}")
                return False
            # kembali ke menu sebelumnya jika user memilih opsi kembali
            if pilih_merk == nomor_kembali:
                return False

            # mengubah nomor pilihan menjadi indeks list
            pilih_merk -= 1

            # memastikan merk yang dipilih valid
            if 0 <= pilih_merk < len(daftar_merk):
                merk = daftar_merk[pilih_merk]
                # meminta konfirmasi sebelum data benar-benar dihapus
                while True:
                    konfirmasi = input(f"\n{YELLOW}Yakin hapus merk '{merk}'? {GREEN}(y){RESET}/{RED}(t){RESET}: ").lower()
                    # menghapus merk jika user mengonfirmasi
                    if konfirmasi == "y":
                        del buka_data[kategori][merk]
                        print(f"{BOLD}{GREEN}Merk berhasil dihapus!{RESET}")
                        return True
                    # membatalkan proses penghapusan
                    elif konfirmasi == "t":
                        print(f"{BOLD}{RED}Dibatalkan{RESET}")
                        return False
                    # meminta user memasukkan pilihan yang benar
                    else:
                        print(f"{BOLD}{RED}Masukkan y/t{RESET}")

            # dijalankan jika nomor merk tidak tersedia
            else:
                print(f"{BOLD}{RED}Pilihan merk tidak valid{RESET}")
                return False  
    # ==========================================
    # HAPUS SERIES
    # ==========================================
    elif pilihan == "3":

        # mengambil seluruh kategori yang tersedia
        daftar_kategori = list(buka_data.keys())

        # menghentikan proses jika tidak ada data kategori
        if len(daftar_kategori) == 0:
            print(f"{BOLD}{RED}Data kosong!{RESET}")
            return False

        # menampilkan daftar kategori yang tersedia
        lebar_no = 3
        lebar_kategori = 45

        print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}}{RESET}")
        print("─" * (lebar_no + lebar_kategori + 1))

        for i in range(len(daftar_kategori)):
            print(f"{str(i+1)+'.':<{lebar_no}} {daftar_kategori[i]:<{lebar_kategori}}")

        # membuat nomor untuk opsi kembali
        nomor_kembali = len(daftar_kategori) + 1

        print("-" * (lebar_no + lebar_kategori + 1))
        print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")

        try:
            # meminta user memilih kategori yang berisi series yang akan dihapus
            pilih_kategori = int(input("\nPilih kategori: "))
        except ValueError:
            # dijalankan jika user memasukkan selain angka
            print(f"{BOLD}{RED}Input harus angka!{RESET}")
            return False

        # kembali ke menu sebelumnya jika user memilih opsi kembali
        if pilih_kategori == nomor_kembali:
            return False

        # mengubah nomor pilihan menjadi indeks list
        pilih_kategori -= 1

        # memastikan kategori yang dipilih valid
        if 0 <= pilih_kategori < len(daftar_kategori):
            kategori = daftar_kategori[pilih_kategori]
            daftar_merk = list(buka_data[kategori].keys())

            # menghentikan proses jika kategori tidak memiliki merk
            if len(daftar_merk) == 0:
                print(f"{BOLD}{RED}Merk kosong!{RESET}")
                return False

            # menampilkan daftar merk pada kategori yang dipilih
            lebar_no = 3
            lebar_kategori = 12
            lebar_merk = 32

            print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}} {'MERK':<{lebar_merk}}{RESET}")
            print("─" * (lebar_no + lebar_kategori + lebar_merk + 2))

            for i in range(len(daftar_merk)):
                kategori_tampil = kategori if i == 0 else ""
                print(f"{str(i+1)+'.':<{lebar_no}} {kategori_tampil:<{lebar_kategori}} {daftar_merk[i]:<{lebar_merk}}")

            # membuat nomor untuk opsi kembali
            nomor_kembali = len(daftar_merk) + 1

            print("-" * (lebar_no + lebar_kategori + lebar_merk + 2))
            print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")

            try:
                # meminta user memilih merk yang berisi series yang akan dihapus
                pilih_merk = int(input("\nPilih merk: "))
            except ValueError:
                # dijalankan jika user memasukkan selain angka
                print(f"{BOLD}{RED}Input harus angka!{RESET}")
                return False

            # kembali ke menu sebelumnya jika user memilih opsi kembali
            if pilih_merk == nomor_kembali:
                return False

            # mengubah nomor pilihan menjadi indeks list
            pilih_merk -= 1

            # memastikan merk yang dipilih valid
            if 0 <= pilih_merk < len(daftar_merk):
                merk = daftar_merk[pilih_merk]
                daftar_produk = buka_data[kategori][merk]
                produk_list = daftar_produk.to_list()

                # menghentikan proses jika merk tidak memiliki series
                if len(produk_list) == 0:
                    print(f"{BOLD}{RED}Series kosong!{RESET}")
                    return False

                # menampilkan daftar series pada merk yang dipilih
                print(f"{GREEN}{BOLD}\nSERIES PADA {merk.upper()}:{RESET}")

                lebar_no = 3
                lebar_kategori = 10
                lebar_merk = 10
                lebar_series = 24

                print(f"\n{BOLD}{GREEN}{'NO':<{lebar_no}} {'KATEGORI':<{lebar_kategori}} {'MERK':<{lebar_merk}} {'SERIES':<{lebar_series}}{RESET}")
                print("─" * (lebar_no + lebar_kategori + lebar_merk + lebar_series + 3))

                for i in range(len(produk_list)):
                    kategori_tampil = kategori if i == 0 else ""
                    merk_tampil = merk if i == 0 else ""
                    print(f"{str(i+1)+'.':<{lebar_no}} {kategori_tampil:<{lebar_kategori}} {merk_tampil:<{lebar_merk}} {produk_list[i]['series']:<{lebar_series}}")

                # membuat nomor untuk opsi kembali
                nomor_kembali = len(produk_list) + 1

                print("-" * (lebar_no + lebar_kategori + lebar_merk + lebar_series + 3))
                print(f"{BOLD}{RED}{nomor_kembali}. Kembali{RESET}")

                try:
                    # meminta user memilih series yang ingin dihapus
                    pilih_series = int(input("\nPilih series: "))
                except ValueError:
                    # dijalankan jika user memasukkan selain angka
                    print(f"{BOLD}{RED}Input harus angka!{RESET}")
                    return False

                # kembali ke menu sebelumnya jika user memilih opsi kembali
                if pilih_series == nomor_kembali:
                    return False

                # mengubah nomor pilihan menjadi indeks list
                pilih_series -= 1

                # memastikan series yang dipilih valid
                if 0 <= pilih_series < len(produk_list):
                    series = produk_list[pilih_series]['series']
                    # meminta konfirmasi sebelum data benar-benar dihapus
                    while True:
                        konfirmasi = input(f"\n{YELLOW}Yakin hapus series '{series}'? {GREEN}(y){RESET}/{RED}(t){RESET}: ").lower()
                        # menghapus series jika user mengonfirmasi
                        if konfirmasi == "y":
                            daftar_produk.delete_at_index(pilih_series)
                            print(f"{BOLD}{GREEN}Series berhasil dihapus!{RESET}")
                            return True
                        # membatalkan proses penghapusan
                        elif konfirmasi == "t":

                            print(f"{BOLD}{RED}Dibatalkan{RESET}")
                            return False
                        # meminta user memasukkan pilihan yang benar
                        else:
                            print(f"{BOLD}{RED}Masukkan y/t{RESET}")

                # dijalankan jika nomor series tidak tersedia
                else:
                    print(f"{BOLD}{RED}Pilihan series tidak valid{RESET}")
                    return False
    # ==========================================
    # HAPUS RIWAYAT UPDATE
    # ==========================================
    elif pilihan == "4":

        # menampilkan menu penghapusan riwayat update
        print("\n" + CYAN + "═" * 50 + RESET)
        print(CYAN + BOLD + "     🗑️ HAPUS RIWAYAT UPDATE     ".center(50) + RESET)
        print(CYAN + "═" * 50 + RESET)

        print(f"{BOLD}{GREEN}1.{RESET} Hapus Riwayat Update Hari Ini")
        print(f"{BOLD}{GREEN}2.{RESET} Hapus Seluruh Riwayat Update")
        print(f"{BOLD}{RED}3. Kembali{RESET}")

        # meminta user memilih jenis riwayat yang ingin dihapus
        pilihan = input("\nPilih menu (1-3): ").strip()

        # kembali ke menu sebelumnya jika user memilih opsi kembali
        if pilihan == "3":
            return False

        # membaca isi file riwayat update
        try:
            with open("riwayat_update.txt", "r", encoding="utf-8") as file:
                isi = file.read()
        # menghentikan proses jika file belum tersedia
        except FileNotFoundError:
            print(f"{BOLD}{RED}File riwayat update belum ada!{RESET}")
            return False

        # menghentikan proses jika file masih kosong
        if isi.strip() == "":
            print(f"{BOLD}{RED}Belum ada riwayat update!{RESET}")
            return False

        # ==========================================
        # HAPUS RIWAYAT HARI INI
        # ==========================================
        if pilihan == "1":

            # mengambil tanggal hari ini untuk mencari riwayat yang sesuai
            hari_ini = datetime.now().strftime("%d-%m-%Y")

            blok_data = isi.split("=" * 50)
            hasil = []
            ditemukan = False

            # memisahkan data yang akan dihapus dan data yang akan dipertahankan
            for blok in blok_data:

                if f"Tanggal Update : {hari_ini}" in blok:
                    ditemukan = True

                else:
                    if blok.strip() != "":
                        hasil.append(blok)

            # menghentikan proses jika tidak ada riwayat update pada hari ini
            if not ditemukan:
                print(f"{BOLD}{RED}Tidak ada riwayat update hari ini!{RESET}")
                return False

            # meminta konfirmasi sebelum menghapus seluruh riwayat hari ini
            while True:

                konfirmasi = input(f"\n{YELLOW}Yakin hapus semua riwayat update hari ini? {GREEN}(y){RESET}/{RED}(n){RESET}: ").lower()

                # menghapus seluruh riwayat update pada tanggal hari ini
                if konfirmasi == "y":

                    with open("riwayat_update.txt", "w", encoding="utf-8") as file:

                        for data in hasil:
                            file.write("=" * 50 + data)

                    print(f"{BOLD}{GREEN}Riwayat update hari ini berhasil dihapus!{RESET}")
                    return True

                # membatalkan proses penghapusan
                elif konfirmasi == "n":

                    print(f"{BOLD}{RED}Penghapusan dibatalkan!{RESET}")
                    return False

                # meminta user memasukkan pilihan yang benar
                else:
                    print(f"{BOLD}{RED}Masukkan y/n!{RESET}")

        # ==========================================
        # HAPUS SELURUH RIWAYAT
        # ==========================================
        elif pilihan == "2":

            # meminta konfirmasi sebelum menghapus seluruh riwayat update
            while True:

                konfirmasi = input(f"\n{YELLOW}Yakin hapus SELURUH riwayat update? {GREEN}(y){RESET}/{RED}(n){RESET}: ").lower()

                # menghapus seluruh isi file riwayat update
                if konfirmasi == "y":

                    with open("riwayat_update.txt", "w", encoding="utf-8") as file:
                        file.write("")

                    print(f"{BOLD}{GREEN}Seluruh riwayat update berhasil dihapus!{RESET}")
                    return True

                # membatalkan proses penghapusan
                elif konfirmasi == "n":

                    print(f"{BOLD}{RED}Penghapusan dibatalkan!{RESET}")
                    return False

                # meminta user memasukkan pilihan yang benar
                else:
                    print(f"{BOLD}{RED}Masukkan y/n!{RESET}")

        # dijalankan jika menu yang dipilih tidak tersedia
        else:
            print(f"{BOLD}{RED}Pilihan tidak valid!{RESET}")
            return False
    # dijalankan jika user memilih menu utama yang tidak tersedia
    else:
        print(f"{BOLD}{RED}Pilihan tidak valid{RESET}")
        return False
# ===========================================================
# SEARCH DATA
# ===========================================================
def search_data(buka_data):

    print("\n=== SEARCH DATA ===")
    print("1. Cari Kategori")
    print("2. Cari Merk")
    print("3. Cari Series")
    print("4. Kembali")

    pilihan = input("Pilih pencarian (1-4): ").strip()

    # ======================================================
    # VALIDASI PILIHAN
    # ======================================================

    if pilihan == "4":
        return

    if pilihan not in ["1", "2", "3"]:
        print("\nPilihan harus angka 1-4!")
        return

    # ======================================================
    # INPUT KEYWORD
    # ======================================================

    keyword = input("Masukkan keyword: ").strip().lower()

    if keyword == "":
        print("\nKeyword tidak boleh kosong!")
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

                print(f"Kategori : {kategori}")
                print("Merk     :")

                for merk, daftar_produk in merk_dict.items():
                    print(f"          • {merk}")

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

                    print(f"Merk : {merk}")
                    print(f"Kategori : {kategori}")

                    for produk in daftar_produk:

                        print(f"• {produk['series']}")

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
                        print(f"Stok      : {produk['stok']} Unit")

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
    print("3. Kembali")

    pilihan = input("Pilih sorting (1-3): ").strip()

    # ======================================================
    # VALIDASI PILIHAN
    # ======================================================

    if pilihan == "3":
        return

    if pilihan not in ["1", "2"]:
        print("\nPilihan harus angka 1-3!")
        return

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
                    "deskripsi": produk['deskripsi'],
                    "stok": produk['stok']
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
            print(f"  Stok     : {produk['stok']} Unit")
            

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
            print(f"  Stok     : {produk['stok']} Unit")

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
        print("7. Lihat Riwayat Update")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ").strip()

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
                                print(f"  Stok : {produk['stok']}")

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

                                print("\n===================================================")
                                print(f"Series : {produk['series']}")
                                print(f"Harga  : {format_rupiah(produk['harga'])}")
                                print(f"Desk   : {produk['deskripsi']}")
                                print(f"Stok   : {produk['stok']}")
                                print("=====================================================")

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
        # TAMBAH DATA 
        # ==================================================
        elif pilihan == "2":

            tambah_data(buka_data)
            simpan_data(nama_file, buka_data)

        # ==================================================
        # UPDATE DATA
        # ==================================================
        elif pilihan == "3":
            hasil_update = update_data(
                buka_data
            )
            if hasil_update:
                simpan_data(
                    nama_file,
                    buka_data
                )
        # ==================================================
        # HAPUS DATA
        # ==================================================
        elif pilihan == "4":

            hasil_hapus = hapus_data(
                buka_data
            )

            if hasil_hapus:

                simpan_data(
                    nama_file,
                    buka_data
                )

            else:

                print(
                    f"{BOLD}{RED}\nTidak ada data yang dihapus.{RESET}"
                )

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
        # LIHAT RIWAYAT UPDATE
        # ==================================================
        elif pilihan == "7":

            lihat_riwayat_update()
        # ==================================================
        # KELUAR
        # ==================================================
        elif pilihan == "8":

            print("Program selesai!!")
            break

        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
