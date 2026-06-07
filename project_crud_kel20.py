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
from datetime import datetime

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def get_all(self):
        return self.items

# buat stack global
riwayat_update = Stack()
# ===========================================================
# SIMPAN RIWAYAT UPDATE KE STACK
# ===========================================================
def simpan_riwayat_update(
    kategori,
    merk,
    data_lama,
    data_baru
):

    waktu_update = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    histori = {
        "tanggal": waktu_update,
        "kategori": kategori,
        "merk": merk,
        "data_lama": data_lama.copy(),
        "data_baru": data_baru.copy()
    }

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

    kategori = input(Colors.WHITE + "\n Masukkan Kategori (HP/Laptop): " + Colors.RESET).strip()
    merk = input(Colors.WHITE + "Masukkan Merk           : " + Colors.RESET).strip()
    series = input(Colors.WHITE + "Masukkan Series         : " + Colors.RESET).strip()
    harga = input(Colors.WHITE + "TMasukkan Harga (angka)   : " + Colors.RESET).strip()
    deskripsi = input(Colors.WHITE + "Masukkan Deskripsi Barang      : " + Colors.RESET).strip()
    stok = input(Colors.WHITE + "Masukkan Jumlah Stok (angka)   : " + Colors.RESET).strip()

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
    
    print(f"\n{Colors.WHITE}📁 Kategori  :{Colors.RESET} {kategori_key}")
    print(f"{Colors.WHITE}🏷️  Merk       :{Colors.RESET} {merk_key}")
    print(f"{Colors.WHITE}📱 Series     :{Colors.RESET} {series}")
    print(f"{Colors.WHITE}💰 Harga      :{Colors.RESET} {format_rupiah(harga)}")
    print(f"{Colors.WHITE}📝 Deskripsi  :{Colors.RESET} {deskripsi}")
    print(f"{Colors.WHITE}📦 Stok      :{Colors.RESET} {stok} unit")

    if kategori_baru:
        print(Colors.CYAN + "✨ Kategori baru berhasil dibuat!" + Colors.RESET)
    if merk_baru:
        print(Colors.CYAN + "✨ Merk baru berhasil dibuat!" + Colors.RESET)
    
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
                        f"{produk['deskripsi']}\n"
                        f"{produk['stok']}\n"
                    )
# ===========================================================
# UPDATE DATA
# ===========================================================
def update_data(buka_data):

    print("\n" + Colors.CYAN + "═" * 50 + Colors.RESET)
    print(Colors.CYAN_BOLD + "         🔄 UPDATE DATA          ".center(50) + Colors.RESET)
    print(Colors.CYAN + "═" * 50 + Colors.RESET)

    daftar_kategori = list(buka_data.keys())

    if len(daftar_kategori) == 0:
        print("Data kosong!")
        return False

    # ======================================================
    # PILIH KATEGORI
    # ======================================================
    for i in range(
        len(daftar_kategori)
    ):
        print(
            f"{i+1}. "
            f"{daftar_kategori[i]}"
        )

    nomor_kembali = (
        len(daftar_kategori)
        + 1
    )

    print(
        f"\n{nomor_kembali}. "
        "Kembali"
    )

    try:
        pilih_kategori = int(
            input(
                "Pilih kategori: "
            )
        )

    except ValueError:
        print(
            "Input harus angka!"
        )
        return False

    # ==========================================
    # KEMBALI
    # ==========================================
    if (
        pilih_kategori
        == nomor_kembali
    ):
        return False

    pilih_kategori -= 1

    # ==========================================
    # VALIDASI PILIHAN
    # ==========================================
    if not (
        0 <= pilih_kategori
        < len(daftar_kategori)
    ):
        print(
            "Pilihan kategori "
            "tidak valid"
        )
        return False

    kategori_terpilih = (
        daftar_kategori[
            pilih_kategori
        ]
    )

    while True:

        # ==================================================
        # TAMPILKAN MERK
        # ==================================================
        print(f"\nUPDATE NAMA {kategori_terpilih}:")
        print("0. Update")

        print(f"\nDAFTAR MERK {kategori_terpilih}:")
        daftar_merk = list(
            buka_data[
                kategori_terpilih
            ].keys()
        )
        for i in range(len(daftar_merk)):
            print(
                f"{i+1}. "
                f"{daftar_merk[i]}"
            )
        nomor_kembali = (
            len(daftar_merk) + 1
        )
        print(
            f"\n{nomor_kembali}. "
            "Kembali"
        )
        try:
            pilih_merk = int(
                input(
                    "Pilih Merk/Kategori (kembali untuk batal) : "
                )
            )
        except ValueError:
            print("Input harus angka!")
            continue

        # ==================================================
        # KEMBALI
        # ==================================================
        if pilih_merk == nomor_kembali:
            break

        # ==================================================
        # UPDATE KATEGORI
        # ==================================================
        if pilih_merk == 0:

            kategori_baru = input(
                "Masukkan nama kategori baru (Enter = tidak diubah): "
            ).strip()

            if kategori_baru == "":
                print(
                    "Kategori tidak diubah"
                )
                continue

            # VALIDASI DUPLIKAT
            if (
                kategori_baru.lower()
                != kategori_terpilih.lower()
            ):

                kategori_sudah_ada = (
                    cari_key_case_insensitive(
                        buka_data,
                        kategori_baru
                    )
                )

                if (
                    kategori_sudah_ada
                    is not None
                ):
                    print(
                        "Kategori sudah ada!"
                    )
                    continue

            buka_data[
                kategori_baru
            ] = buka_data.pop(
                kategori_terpilih
            )

            kategori_terpilih = (
                kategori_baru
            )

            print(
                "Kategori berhasil diupdate!"
            )

            return True

        pilih_merk -= 1

        # ==================================================
        # VALIDASI MERK
        # ==================================================
        if not (
            0 <= pilih_merk
            < len(daftar_merk)
        ):
            print(
                "Pilihan merk tidak valid"
            )
            continue

        merk_terpilih = (
            daftar_merk[
                pilih_merk
            ]
        )

        while True:

            daftar_produk = buka_data[
                kategori_terpilih
            ][merk_terpilih]

            produk_list = (
                daftar_produk
                .to_list()
            )

            # ==========================================
            # CEK PRODUK KOSONG
            # ==========================================
            if len(produk_list) == 0:

                print(
                    "\nMerk ini "
                    "tidak punya "
                    "series."
                )

                break

            # ==========================================
            # TAMPILKAN SERIES
            # ==========================================
            print(f"\nUPDATE NAMA {merk_terpilih}:")
            print("0. Update")

            for i in range(
                len(produk_list)
            ):
                print(f"DAFTAR SERIES {produk_list}")
                print(
                    f"{i+1}. "
                    f"{produk_list[i]['series']}"
                )

            nomor_kembali = (
                len(produk_list)
                + 1
            )

            print(
                f"\n{nomor_kembali}. "
                "Kembali"
            )

            try:
                pilih_series = int(
                    input(
                        "Pilih series/merk (kembali tuk batal): "
                    )
                )

            except ValueError:
                print(
                    "Input harus angka!"
                )
                continue

            # ==========================================
            # KEMBALI
            # ==========================================
            if (
                pilih_series
                == nomor_kembali
            ):
                break

            # ==========================================
            # UPDATE MERK
            # ==========================================
            if pilih_series == 0:

                merk_baru = input(
                    "Masukkan nama merk baru (Enter = tidak diubah): "
                ).strip()

                if merk_baru == "":
                    print(
                        "Merk tidak diubah"
                    )
                    continue

                # VALIDASI DUPLIKAT
                if (
                    merk_baru.lower()
                    != merk_terpilih.lower()
                ):

                    merk_sudah_ada = (
                        cari_key_case_insensitive(
                            buka_data[
                                kategori_terpilih
                            ],
                            merk_baru
                        )
                    )

                    if (
                        merk_sudah_ada
                        is not None
                    ):
                        print(
                            "Merk sudah ada!"
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

                merk_terpilih = (
                    merk_baru
                )

                print(
                    "Merk berhasil diupdate!"
                )

                return True

            pilih_series -= 1

            # ==========================================
            # VALIDASI SERIES
            # ==========================================
            if not (
                0 <= pilih_series
                < len(produk_list)
            ):
                print(
                    "Pilihan series tidak valid"
                )
                continue

            node_produk = daftar_produk.get_node_at_index(
                pilih_series
            )

            if node_produk is None:
                print("Data tidak ditemukan!")
                continue

            produk = node_produk.data
            data_lama = produk.copy()

            print(
                "\n=== DATA LAMA ==="
            )

            print(
                f"Series            : "
                f"{produk['series']}"
            )

            print(
                f"Harga(tanpa titik): Rp"
                f"{format_rupiah(produk['harga'])}"
            )

            print(
                f"Deskripsi         : "
                f"{produk['deskripsi']}"
            )

            print(
                "\nKosongkan input jika tidak ingin diubah"
            )

            # ======================================
            # INPUT DATA BARU
            # ======================================
            series_baru = input(
                "Series baru        : "
            ).strip()

            harga_baru = input(
                "Harga baru(tanpa .): Rp"
            ).strip()

            deskripsi_baru = input(
                "Deskripsi baru     : "
            ).strip()

            # ======================================
            # VALIDASI DUPLIKAT SERIES
            # ======================================
            if series_baru != "":

                for i in range(
                    len(produk_list)
                ):

                    if (
                        i
                        != pilih_series
                        and
                        produk_list[i][
                            'series'
                        ].lower()
                        ==
                        series_baru.lower()
                    ):

                        print(
                            "Series sudah ada!"
                        )

                        return False

            # ======================================
            # UPDATE SERIES
            # ======================================
            if series_baru != "":

                produk[
                    'series'
                ] = (
                    series_baru
                )

            # ======================================
            # UPDATE HARGA
            # ======================================
            if harga_baru != "":

                if (
                    harga_baru
                    .isdigit()
                ):

                    produk[
                        'harga'
                    ] = int(
                        harga_baru
                    )

                else:

                    print(
                        "Harga harus berupa angka!"
                    )

                    continue

            # ======================================
            # UPDATE DESKRIPSI
            # ======================================
            if (
                deskripsi_baru
                != ""
            ):

                produk[
                    'deskripsi'
                ] = (
                    deskripsi_baru
                )
            # data baru setelah update
            data_baru = produk.copy()

            # simpan ke stack
            simpan_riwayat_update(
                kategori_terpilih,
                merk_terpilih,
                data_lama,
                data_baru       
            )

            # simpan ke txt
            simpan_riwayat_txt()
            return True

    return False

# ===========================================================
# HAPUS DATA
# ===========================================================
def hapus_data(buka_data):

    print("\n=== HAPUS DATA ===")
    print("1. Hapus Kategori")
    print("2. Hapus Merk")
    print("3. Hapus Series")
    print("4. Kembali")

    pilihan = input(
        "Pilih jenis yang ingin dihapus (1-4): "
    ).strip()

    if pilihan == "4":
        return False

    # ======================================================
    # HAPUS KATEGORI
    # ======================================================
    if pilihan == "1":

        daftar_kategori = list(
            buka_data.keys()
        )

        if len(daftar_kategori) == 0:
            print("Data kosong!")
            return False

        for i in range(
            len(daftar_kategori)
        ):
            print(
                f"{i+1}. "
                f"{daftar_kategori[i]}"
            )

        nomor_kembali = (
            len(daftar_kategori)
            + 1
        )

        print(
            f"\n{nomor_kembali}. "
            "Kembali"
        )

        try:
            pilih = int(
                input(
                    "Pilih kategori: "
                )
            )

        except ValueError:
            print(
                "Input harus angka!"
            )
            return False

        if pilih == nomor_kembali:
            return False

        pilih -= 1

        if 0 <= pilih < len(
            daftar_kategori
        ):

            kategori = (
                daftar_kategori[pilih]
            )

            while True:

                konfirmasi = input(
                    f"Yakin hapus kategori "
                    f"'{kategori}'? "
                    f"(y/t/kembali): "
                ).lower()

                if konfirmasi == "y":

                    del buka_data[
                        kategori
                    ]

                    print(
                        "Kategori berhasil "
                        "dihapus!"
                    )

                    return True

                elif konfirmasi == "t":
                    print("Dibatalkan")
                    return False

                elif (
                    konfirmasi
                    == "kembali"
                ):
                    return False

                else:
                    print(
                        "Masukkan "
                        "y/t/kembali"
                    )

        else:
            print(
                "Pilihan tidak valid"
            )
            return False

    # ======================================================
    # HAPUS MERK
    # ======================================================
    elif pilihan == "2":

        daftar_kategori = list(
            buka_data.keys()
        )

        if len(daftar_kategori) == 0:
            print("Data kosong!")
            return False

        for i in range(
            len(daftar_kategori)
        ):
            print(
                f"{i+1}. "
                f"{daftar_kategori[i]}"
            )

        nomor_kembali = (
            len(daftar_kategori)
            + 1
        )

        print(
            f"\n{nomor_kembali}. "
            "Kembali"
        )

        try:
            pilih_kategori = int(
                input(
                    "Pilih kategori: "
                )
            )

        except ValueError:
            print(
                "Input harus angka!"
            )
            return False

        if (
            pilih_kategori
            == nomor_kembali
        ):
            return False

        pilih_kategori -= 1

        if (
            0 <= pilih_kategori
            < len(daftar_kategori)
        ):

            kategori = (
                daftar_kategori[
                    pilih_kategori
                ]
            )

            daftar_merk = list(
                buka_data[
                    kategori
                ].keys()
            )

            if len(daftar_merk) == 0:
                print(
                    "Merk tidak ada!"
                )
                return False

            for i in range(
                len(daftar_merk)
            ):
                print(
                    f"{i+1}. "
                    f"{daftar_merk[i]}"
                )

            nomor_kembali = (
                len(daftar_merk)
                + 1
            )

            print(
                f"\n{nomor_kembali}. "
                "Kembali"
            )

            try:
                pilih_merk = int(
                    input(
                        "Pilih merk: "
                    )
                )

            except ValueError:
                print(
                    "Input harus angka!"
                )
                return False

            if (
                pilih_merk
                == nomor_kembali
            ):
                return False

            pilih_merk -= 1

            if (
                0 <= pilih_merk
                < len(daftar_merk)
            ):

                merk = daftar_merk[
                    pilih_merk
                ]

                while True:
                    konfirmasi = input(
                        f"Yakin hapus "
                        f"merk '{merk}'? "
                        f"(y/t/kembali): "
                    ).lower()
                    if konfirmasi == "y":
                        del buka_data[
                            kategori
                        ][merk]
                        print(
                            "Merk berhasil "
                            "dihapus!"
                        )
                        return True
                    elif konfirmasi == "t":
                        print("Dibatalkan")
                        return False
                    elif (
                        konfirmasi
                        == "kembali"
                    ):
                        return False
                    else:
                        print(
                            "Masukkan "
                            "y/t/kembali"
                        )
            else:
                print(
                    "Pilihan merk "
                    "tidak valid"
                )
                return False

    # ======================================================
    # HAPUS SERIES
    # ======================================================
    elif pilihan == "3":

        daftar_kategori = list(
            buka_data.keys()
        )

        if len(daftar_kategori) == 0:
            print("Data kosong!")
            return False

        for i in range(
            len(daftar_kategori)
        ):
            print(
                f"{i+1}. "
                f"{daftar_kategori[i]}"
            )

        nomor_kembali = (
            len(daftar_kategori)
            + 1
        )

        print(
            f"\n{nomor_kembali}. "
            "Kembali"
        )

        try:
            pilih_kategori = int(
                input(
                    "Pilih kategori: "
                )
            )

        except ValueError:
            print(
                "Input harus angka!"
            )
            return False

        if (
            pilih_kategori
            == nomor_kembali
        ):
            return False

        pilih_kategori -= 1

        if (
            0 <= pilih_kategori
            < len(daftar_kategori)
        ):

            kategori = (
                daftar_kategori[
                    pilih_kategori
                ]
            )

            daftar_merk = list(
                buka_data[
                    kategori
                ].keys()
            )

            if len(daftar_merk) == 0:
                print("Merk kosong!")
                return False

            for i in range(
                len(daftar_merk)
            ):
                print(
                    f"{i+1}. "
                    f"{daftar_merk[i]}"
                )

            nomor_kembali = (
                len(daftar_merk)
                + 1
            )

            print(
                f"\n{nomor_kembali}. "
                "Kembali"
            )

            try:
                pilih_merk = int(
                    input(
                        "Pilih merk: "
                    )
                )

            except ValueError:
                print(
                    "Input harus angka!"
                )
                return False

            if (
                pilih_merk
                == nomor_kembali
            ):
                return False

            pilih_merk -= 1

            if (
                0 <= pilih_merk
                < len(daftar_merk)
            ):

                merk = daftar_merk[
                    pilih_merk
                ]

                daftar_produk = (
                    buka_data[
                        kategori
                    ][merk]
                )

                produk_list = (
                    daftar_produk
                    .to_list()
                )

                if len(produk_list) == 0:
                    print(
                        "Series kosong!"
                    )
                    return False

                print(
                    f"\nSeries pada "
                    f"{merk}:"
                )

                for i in range(
                    len(produk_list)
                ):
                    print(
                        f"{i+1}. "
                        f"{produk_list[i]['series']}"
                    )

                nomor_kembali = (
                    len(produk_list)
                    + 1
                )

                print(
                    f"\n{nomor_kembali}. "
                    "Kembali"
                )

                try:
                    pilih_series = int(
                        input(
                            "Pilih series: "
                        )
                    )

                except ValueError:
                    print(
                        "Input harus angka!"
                    )
                    return False

                if (
                    pilih_series
                    == nomor_kembali
                ):
                    return False

                pilih_series -= 1

                if (
                    0 <= pilih_series
                    < len(produk_list)
                ):

                    series = (
                        produk_list[
                            pilih_series
                        ]['series']
                    )

                    while True:

                        konfirmasi = input(
                            f"Yakin hapus "
                            f"series "
                            f"'{series}'? "
                            f"(y/t/kembali): "
                        ).lower()

                        if konfirmasi == "y":

                            daftar_produk.delete_at_index(
                                pilih_series
                            )

                            print(
                                "Series berhasil "
                                "dihapus!"
                            )

                            return True

                        elif konfirmasi == "t":
                            print("Dibatalkan")
                            return False

                        elif (
                            konfirmasi
                            == "kembali"
                        ):
                            return False

                        else:
                            print(
                                "Masukkan "
                                "y/t/kembali"
                            )

                else:
                    print(
                        "Pilihan series "
                        "tidak valid"
                    )
                    return False

    else:
        print(
            "Pilihan tidak valid"
        )
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
                print(
                    "\n=== DATA BERHASIL DI UPDATE ==="
                )
            else:
                print(
                    "\nTidak ada data yang diubah"
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

                print(
                    "\n=== DATA BERHASIL DIHAPUS ==="
                )

            else:

                print(
                    "\nTidak ada data yang dihapus"
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
