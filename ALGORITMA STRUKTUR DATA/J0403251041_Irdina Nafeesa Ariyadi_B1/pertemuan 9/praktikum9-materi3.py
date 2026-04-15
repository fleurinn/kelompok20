#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#======================================#
# pertemuan 9:                         #
# materi 3: membuat traversal preorder #
#======================================#

# class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left =  None # child kiri
        self.right = None # child kanan

# membuat traversal preorder: root => left => right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") # root
        preorder(node.left) # left
        preorder(node.right) # right

# membuat tree
# membuat sebuah node root
root = Node("A")

# membuat child lvl 1
root.left = Node("B")
root.right = Node("C")

# membuat child lvl 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal preorder
print("hasil traversal preorder: ")
preorder(root)

# penjelasan:
'''
program ini menunjukkan cara menelusuri tree menggunakan traversal preorder. pada preorder, urutan pembacaannya adalah root dulu, lalu child kiri, kemudian child kanan.
tree dimulai dari root "A", lalu punya child kiri "B" dan child kanan "C". setelah itu, node "B" punya child kiri "D", sedangkan node "C" punya child kanan "E"
fungsi preorder() berjalan secara rekursif untuk membaca setiap node sesuai urutan root => left => right. jadi hasil akhirnya akan tampil A B D C E, yang menunjukkan alur pembacaan dari atas ke bawah mengikuti cabang kiri lalu kanan.
'''