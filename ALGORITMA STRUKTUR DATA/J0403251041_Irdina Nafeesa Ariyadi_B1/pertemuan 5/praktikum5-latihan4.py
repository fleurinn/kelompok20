#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================#
# Latihan 4: Kombinasi Huruf #
#============================#

def kombinasi(n, hasil=""):
    # base case
    if len(hasil) == n:
        print(hasil)
        return
    # recursive case
    kombinasi(n, hasil+"A")
    kombinasi(n, hasil+"B")
kombinasi(2)