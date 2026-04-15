#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#======================================================================#
# Studi Kasus: Sistem Antrian Layanan Akademik                         #
# Implementasi Queu:                                                   #
# Stack: data masuk dari depan (front -> C -> B -> A -> None)          #
# Queue: data masuk dari belakang (front -> A -> B -> C -> rear)       #
# EnQueue: memindahkan pointer rear (menambah data baru dari belakang) #
# DeQueue: memindahkan pointer head/front (menghapus data dari depan)  #
#======================================================================#

# 1) mendefinisikan Node (unit dari linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim # menyimpan NIM mahasiswa
        self.nama = nama # menyimpan nama mahasiswa
        self.next = None # pointer ke next Node
# 2) mendefinisikan Queue, terdiri dari front dan rear
class QueueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # ketika Queue kosong maka front = rear = None
        return self.front is None
    # menambahkan data baru ke belakang (rear) -> menambahkan antrian yg akan mengajukan layanan akademik
    def EnQueue(self,nim,nama):
        nodebaru = Node(nim,nama)
        # jika data baru msk dari Queue yg kosong, maka data baru = front = rear
        if self.is_empty:
            self.front = nodebaru
            self.rear = nodebaru
            return
        # jika Queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodebaru
        self.rear = nodebaru 
    # menghapus data paling belakang
    def DeQueue(self):
        if self.is_empty():
            print("antrian kosong, tidak ada mahasiswa yang dilayani")
        # jika data di front, simpan di variabel data yg akan dihapus (dilayani)
        node_dilayani = self.front
        # geser pointer front ke next front
        self.front = self.front.next
        # jika front menjadi None (data antrian terakhir yg dilayani maka front = rear = None)
        if self.front is None:
            self.rear = None
        return node_dilayani 
    
    def tampilkan(self):
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}, {current.nim} - {current.nama}")
            current = current.next
            no += 1
# program utama
def main():
    #intantiasi queue
    q = QueueAkademik()
    while True:
        print("=== Sistem Antrian Akademik ===")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilihan = input("Pilih Menu (1-4): ").strip()
        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            q.EnQueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahankan ke Antrian")
        elif pilihan == "2":
            dilayani = q.DeQueue()
            print(f"Mahasiswa Dilayani: {dilayani.nim} - {dilayani.nama}")
        elif pilihan == "3":
            q.tampilkan()
        elif pilihan == "4":
            print("Program Selesai. terima Kasih")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")
# penanda eksekusi program utama
if __name__ == "__main__":
    main()