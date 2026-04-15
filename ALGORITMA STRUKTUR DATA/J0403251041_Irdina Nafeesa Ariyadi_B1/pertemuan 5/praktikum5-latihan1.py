#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================#
# Latihan 1: Rekursi Pangkat #
#============================#

def pangkat(a, n):
    # base case
    if n == 0:
        return 1
    # recursive case
    return a*pangkat(a, n-1)
print(pangkat(2,4))