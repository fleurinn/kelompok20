#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==============================================#
# Tugas Hands-On: Sistem Antrian Bengkel Motor #
#==============================================#

class Node:
    def __init__(self,no,nama,servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def EnQueue(self):
        # tambahkan data ke antrian
        pass

    def DeQueue(self):
        # layani pelanggan terdepan
        pass

    def tampilkan(self):
        # tampilkan seluruh antrian
        pass

def main():
    q = QueueBengkel()

    while True:
        print("=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih Menu: ")

        if pilih == "1":
            no = input("Nomor Antrian   : ")
            nama = input("Nama  : ")
            servis = input("Servis  : ")
            q.EnQueue(no,nama,servis)
        elif pilih == "2":
            q.DeQueue()
        elif pilih == "3":
            q.tampilkan()
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()