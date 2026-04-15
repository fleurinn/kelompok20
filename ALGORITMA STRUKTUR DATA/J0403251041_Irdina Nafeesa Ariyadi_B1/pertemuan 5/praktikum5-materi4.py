#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#======================================#
# Materi Rekursif: Kombinasi Biner (n) #
#======================================#

def biner(n, hasil=""):
    # base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # choose + explore: tambah 0
    biner(n, hasil + "0")
    # choose + explore: tambah 1
    biner(n, hasil + "1")
biner(3)