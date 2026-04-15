#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#========================#
# pertemuan 9:           #
# materi 1: membuat node #
#========================#

# class node digunakan untuk dasar dari  tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left =  None # child kiri
        self.right = None # child kanan

# membuat root
root = Node("A")

# menampilkan isi node
print("data pada root: ", root.data)
print("child kiri root: ", root.left)
print("child kanan root: ", root.right)

# penjelasan: 
'''
program ini menjelaskan dasar struktur data tree, yaitu membuat sebuah node. pertama, dibuat class Node sebagai template yang punya tiga atribut: data untuk menyimpan nilai, serta left dan right untuk child kiri dan kanan.
setelah itu dibuat root "A" sebagai node pertama. karena root baru dibuat dan belum terhubung ke node lain, maka child kiri dan kanannya masih bernilai None.
di akhir, program menampilkan isi root beserta child kiri dan kanan untuk menunjukkan kalau tree selalu dimulai dari root, dan pada awalnya child masih kosong.
'''