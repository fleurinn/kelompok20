#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================#
# Latihan 2: Tracing Rekursi #
#============================#

def countdown(n):
    # base case
    if n == 0:
        print("selesai")
        return
    # recursive case
    print("masuk: ", n)
    countdown(n-1)
    print("keluar: ", n)
countdown(3)