#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#================================================#
# Implementasi Dasar: Queue Berbasis Linked List #
#================================================#

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai /data
        self.next = None # pointer ke note berikutnya (awal = none)
# Queue dgn 2 pointer: front dan rear
class Queuell:
    def __init__(self):
        self.front = None # node paling dpn
        self.rear = None # node paling blkg

    def is_empty(self):
        # mengembalikan true jika font adalah none ()
        return self.front is None

    def Enqueue(self, data):
        # menambah data di blkg (rear)
        nodebaru = Node(data)
        # jika queue kosong
        nodebaru = Node(data) # menambah data di  (rear)
        if self.is_empty():
            self.front = nodebaru
            self.rear = nodebaru
            return
        else:
        # jika queue tidak kosong
        # rear lama menunjuk node baru
            self.rear.next = nodebaru
        # rear pindah ke node baru
            self.rear = nodebaru

    def Dequeue(self):
        # menghapus data dr dpn
        # 1) ambil data yg plg dpn
        data_terhapus = self.front.data
        # 2) geser front ke node berikutnya
        self.front = self.front.next 
        # 3) jika setelah geser front menjadi none, maka queue kosong
        if self.front is None:
            self.rear = None
        return data_terhapus
    
    def tampilkan(self):
        current = self.front
        print("front ->", end=" -> ")
        while current is not None :
            print(current.data, end=" -> ")
            current= current.next
        print("node-rear di node terakhir")

# instantiasi objek class QueueLL
q = Queuell()
q.Enqueue("A")
q.Enqueue("B")
q.Enqueue("C")
q.tampilkan()
q.Dequeue()
q.tampilkan()