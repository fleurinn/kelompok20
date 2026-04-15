#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#=================================#
# Materi Rekursif: Call Stack     #
# Tracing Bilangan (masuk-keluar) #
# co/: input = 3                  #
# 3-2-1 | 1-2-3                   #
#=================================#

def hitung(n):
    # base case
    if n == 0:
        print("selesai")
        return
    print("masuk: ", n)
    hitung(n-1) # recursive case
    print("keluar: ", n)
print("=== Tracing ===")
hitung(3)