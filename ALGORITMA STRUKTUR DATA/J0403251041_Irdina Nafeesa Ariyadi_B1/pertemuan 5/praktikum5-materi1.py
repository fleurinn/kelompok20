#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================#
# Materi Rekursif: Faktorial #
# Recursive Case: 3! = 3x2x1 #
# Base Case: 0, berhenti     #
#============================#

def faktorial(n):
    # base case
    if n == 0:
        return 1
    #recursive case
    return n*faktorial(n-1) # (n-1)*(n-2)*(n-3)*...(n-n)
print("=== Program Faktorial ===")
print("hasil faktorial: ", faktorial(3))