#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==========================================#
# pertemuan 9: STUDI KASUS                 #
# materi 6: struktur organisasi perusahaan #
#==========================================#

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
root = Node("Direktur")

# membuat child lvl 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# membuat child lvl 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.right = Node("Staff 3")

# menjalankan traversal postorder
print("struktur organisasi (preorder) : ")
preorder(root)

# penjelasan:
'''
program ini menerapkan struktur data tree pada studi kasus struktur organisasi perusahaan. tree dimulai dari root "Direktur" sebagai posisi tertinggi, lalu memiliki child kiri "Manajer A" dan child kanan "Manajer B".
selanjutnya, "Manajer A" memiliki dua staff yaitu "Staff 1" dan "Staff 2", sedangkan "Manajer B" memiliki "Staff 3". dari sini terlihat hubungan hierarki perusahaan dari jabatan tertinggi ke bawahan secara bertingkat.
fungsi preorder() digunakan untuk menampilkan struktur organisasi dengan urutan root => left => right, sehingga hasilnya akan dimulai dari Direktur, lalu cabang Manajer A beserta staff-nya, kemudian lanjut ke Manajer B dan staff-nya.
'''