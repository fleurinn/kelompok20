#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#===========================================#
# Implementasi Dasar: Node pada Linked List #
#===========================================#

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai /data
        self.next = None # pointer ke note berikutnya (awal = none)
# langkah ke-1: membuat node satu persatu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
# langkah ke-2: menghubungkan node; A -> B -> C -> none
nodeA.next = nodeB
nodeB.next = nodeC
# langkah ke-3: menentukan node pertama (head)
head = nodeA
# langkah ke-4: menelusuri dari head sampe none
current = head
while current is not None:
    print(current.data) # menampilkan data pada node saat ini
    current = current.next # pindah ke node berikutnya

#===============================================#
# Implementasi Dasar: Linked List + Insert Awal #
#===============================================#

class LinkedList: # class implementasi stack
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self, data): # push dalam stack
        # 1) buat node baru
        nodebaru = Node(data) # panggil class node
        # 2) node baru menunjuk ke head lama
        nodebaru.next = self.head
        # 3) head pindah ke node baru
        self.head = nodebaru

    def hapus_awal(self): # pop dlm stack
        data_terhapus = self.head.data # peek dlm stack
        # menggeser head ke node berikutnya
        self.head = self.head.next
        print("node yg dihapus adalah: ", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
print("=== list baru ===")
ll = LinkedList() # instantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()

