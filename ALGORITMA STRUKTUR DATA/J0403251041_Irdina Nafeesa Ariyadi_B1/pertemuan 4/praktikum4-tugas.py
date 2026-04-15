#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==============================================#
# Tugas Hands-On: Sistem Antrian Bengkel Motor #
#==============================================#

class Node:
    def __init__(self, no, nama, servis):
        self.no = no # menyimpan nomor antrian
        self.nama = nama # menyimpan nama pelanggan
        self.servis = servis # menyimpan data servis
        self.next = None # pointer ke node selanjutnya

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # ketika Queue kosong maka front = rear = None
        return self.front is None
    # menambahkan data antrian (dari belakang)
    def EnQueue(self, no, nama, servis):
        nodebaru = Node(no, nama, servis)
        # jika data baru msk dari Queue yg kosong, maka data baru = front = rear
        if self.is_empty:
            self.front = nodebaru
            self.rear = nodebaru
            return
        # jika Queue tidak kosong, maka data baru diletakkan setelah rear
        self.rear.next = nodebaru
        self.rear = nodebaru
    # menghapus data (dari belakang)
    def DeQueue(self):
        if self.is_empty():
            print("antrian kosong, tidak ada pelanggan yang dilayani")
            return main()
        # layani pelanggan terdepan
        # jika data di front, simpan di variabel data yg akan dihapus (dilayani)
        node_dilayani = self.front
        # geser pointer ke next front
        self.front = self.front.next
        # jika front = None (data akhir yang dilayani) maka front = rear = None
        if self.front is None:
            self.rear = None
            return node_dilayani
    def tampilkan(self):
        # jika antrian kosong, maka akan kembali ke main
        if self.front is None:
            print("tidak ada data antrian")
            return
        # tampilkan seluruh antrian
        # jika ada antrian maka lakukan perulangan 
        # mendefinisikan current sebagai data terdepan
        current = self.front
        no = 1
        print("=== Daftar Antrian ===")
        # melakukan looping ketika current tidak kosong (ada data)
        while current is not None:
            print(f"{no}, {current.no} - {current.nama} - {current.servis}")
            # geser pointer ke current next
            current = current.next
            no += 1

# program utama
def main():
    q = QueueBengkel()
    # melakukan looping ketika nilai True
    while True:
        print("=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih Menu (1-4): ").strip()
        # opsi "1" = tambah pelanggan (menambahkan data ke belakang (fungsi EnQueue))
        if pilih == "1":
            no = input("Nomor Antrian: ").strip() 
            nama = input("Nama: ").strip() 
            servis = input("Servis: ").strip() 
            q.EnQueue(no, nama, servis)
            print("Pelanggan berhasil ditambahkan ke antrian")
        # opsi "2" = layani pelanggan (melayani/menghapus data terdepan (fungsi DeQueue))
        elif pilih == "2":
            dilayani = q.DeQueue()
            print(f"Pelanggan dilayani: {dilayani.no} - {dilayani.nama} - {dilayani.servis}")
        # opsi "3" = menampilkan semua antrian
        elif pilih == "3":
            q.tampilkan()
        # opsi "4" = keluar dari program
        elif pilih == "4":
            print("Program selesai, terima kasih")
            break
        # jika pilihan menu tidak valid
        else:
            print("Pilihan tidak valid, pilih menu (1-4): ")
            
# eksekusi program utama
if __name__ == "__main__":
    main()