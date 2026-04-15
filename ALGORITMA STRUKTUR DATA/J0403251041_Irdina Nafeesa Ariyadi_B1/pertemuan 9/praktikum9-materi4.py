#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#======================================#
# pertemuan 9:                         #
# materi 4: membuat traversal inorder  #
#======================================#

# class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left =  None # child kiri
        self.right = None # child kanan

# membuat traversal inorder: left => root => right
def inorder(node):
    if node is not None:
        inorder(node.left) # left
        print(node.data, end=" ") # root
        inorder(node.right) # right

# membuat tree
# membuat sebuah node root
root = Node("A")

# membuat child lvl 1
root.left = Node("B")
root.right = Node("C")

# membuat child lvl 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal inorder
print("hasil traversal inorder: ")
inorder(root)

# penjelasan:
'''
program ini menunjukkan cara menelusuri tree menggunakan traversal inorder. pada inorder, urutan pembacaannya adalah child kiri dulu, lalu root, kemudian child kanan.
tree dimulai dari root "A", lalu memiliki child kiri "B" dan child kanan "C". setelah itu, node "B" punya child kiri "D", sedangkan node "C" punya child kanan "E".
fungsi inorder() berjalan secara rekursif untuk membaca node sesuai urutan left => root => right. jadi hasil akhirnya akan tampil D B A C E, yang menunjukkan kalau cabang kiri selalu dibaca lebih dulu sebelum kembali ke root dan lanjut ke kanan.
'''