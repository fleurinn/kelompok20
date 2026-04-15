# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Irdina Nafeesa Ariyadi
# NIM     : J0403251041
# Kelas   : TPL/B1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
nama_file = "buku.txt" # variabel untuk menyimpan nama file yang berisi data buku
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {} # inisialisasi dict untuk menyimpan data
    
    with open("buku.txt", "r", encoding="utf-8") as file: # buka file buku.txt dalam mode baca (R)
        for baris in file: 
            baris = baris.strip() # hilangkan karakter baris baru (\n)
            parts = baris.split(",") # pisahkan isi baris berdasarkan koma

            if len(parts) !=3: # menunjukkan data yang terdiri dari 3 bagian (kode_buku, judul, harga)
                continue
            kode_buku, judul, harga = parts
            harga_int = int(harga) # ubah str ke int
            database_buku[kode_buku]={"judul": judul, "harga": harga_int}
            kode_buku, judul, harga = baris.split(",") # pecah menjadi data satuan

            # simpan data buku ke directory dengan key kode_buku
            database_buku[kode_buku]={
                "judul": judul,
                "harga": int(harga)
            }
    return database_buku # mengembalikan dict yang berisi data buku

# memanggil fungsi muat_data_buku dan simpan hasilnya ke buka_data
buka_data = muat_data_buku(nama_file) 
print("Jumlah Data Terbaca: ", len(buka_data)) 

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul # menyimpan judul
        self.next = None # pointer ke node selanjutnya

class LinkedListPromosi:
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        node_baru = Node(judul)

        if self.head is None: # jika linked list kosong
            self.head = node_baru 
        else: # jika list sudah ada isinya
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru 

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        if self.head is None: # jika tidak ada data 
            print("Tidak ada buku promosi")
            return

        current = self.head
        print("Daftar Buku Promosi: ")
        while current:
            print("-", current.judul)
            current = current.next

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        self.antrean.append(nama_pelanggan)
        print(nama_pelanggan, "berhasil ditambah ke antrean.")

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if len(self.antrean) == 0:
            print("Tidak ada pelanggan dalam antrean.")
        else:
            pelanggan = self.antrean.pop(0)
            print("Pelanggan dilayani: ", pelanggan)


# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    for i in range(1, len(list_harga)):
        key = list_harga[i] # nilai yang akan dibandingkan
        j = i - 1 # indeks elemen sebelumnya

        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j] # geser elemen ke kanan
            j -= 1 # pindah ke elemen sebelumnya

        list_harga[j + 1] = key # menempatkan key di posisi yang benar
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':

            print("\n1. Tambah Antrean") 
            print("2. Layani Pelanggan")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama) # menambah pelanggan ke antrean
            elif pilihan == "2":
                antrean_toko.layani_pelanggan() # melayani pelanggan pertama (berurutan)
            else:
                print("Pilihan Tidak Valid!")

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()