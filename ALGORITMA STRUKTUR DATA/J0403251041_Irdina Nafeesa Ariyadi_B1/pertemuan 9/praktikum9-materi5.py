#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#=======================================#
# pertemuan 9:                          #
# materi 5: membuat traversal postorder #
#=======================================#

# class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left =  None # child kiri
        self.right = None # child kanan

# membuat traversal postorder: left => right => root
def postorder(node):
    if node is not None:
        postorder(node.left) # left
        postorder(node.right) # right
        print(node.data, end=" ") # root

# membuat tree
# membuat sebuah node root
root = Node("A")

# membuat child lvl 1
root.left = Node("B")
root.right = Node("C")

# membuat child lvl 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal postorder
print("hasil traversal postorder: ")
postorder(root)

# penjelasan:
'''
program ini menunjukkan cara menelusuri tree menggunakan traversal postorder. pada postorder, urutan pembacaannya adalah child kiri dulu, lalu child kanan, dan root dibaca paling akhir.
tree dimulai dari root "A", lalu memiliki child kiri "B" dan child kanan "C". setelah itu, node "B" punya child kiri "D", sedangkan node "C" punya child kanan "E".
fungsi postorder() berjalan secara rekursif untuk membaca node sesuai urutan left => right => root. jadi hasil akhirnya akan tampil D B E C A, yang menunjukkan kalau semua cabang dibaca dulu sebelum kembali ke root utama.
'''