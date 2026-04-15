#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#=============================#
# pertemuan 9:                #
# materi 2: membuat node tree #
#=============================#

# class node adalah unit dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left =  None # child kiri
        self.right = None # child kanan

# membuat root
root = Node("A")

# membuat child lvl 1
root.left = Node("B")
root.right = Node("C")

# membuat child lvl 2
root.left.left = Node("D")
root.left.right = Node("E")

# membuat child lvl 3
root.right.left = Node("F")
root.right.right = Node("G")

# menampilkan isi node
print("data pada root: ", root.data)
print("data pada child kiri root: ", root.left.data)
print("data pada child kanan root: ", root.right.data)
print("child kiri dari B: ", root.left.left.data)
print("child kanan dari B: ", root.left.right.data)
print("child kiri dari C: ", root.right.left.data)
print("child kanan dari C: ", root.right.right.data)

# penjelasan:
'''
pada program ini, tree dimulai dari root "A" sebagai node utama. lalu root memiliki child kiri "B" dan child kanan "C" sebagai level pertama.
selanjutnya, node B bercabang lagi menjadi "D" dan "E", sedangkan node C bercabang menjadi "F" dan "G". dari sini terlihat kalau setiap node bisa punya child kiri dan child kanan, sehingga tree terbentuk secara bertingkat dari atas ke bawah.
di akhir, program menampilkan isi tiap node supaya hubungan antara root, parent, dan child terlihat lebih jelas.
'''