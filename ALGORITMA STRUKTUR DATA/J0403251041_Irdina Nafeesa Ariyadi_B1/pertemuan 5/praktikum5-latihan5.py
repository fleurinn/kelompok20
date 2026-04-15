#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================#
# Studi Kasus: Generator PIN #
#============================#

def buat_pin(panjang, hasil=""):
    # base case
    if len(hasil) == panjang:
        print("PIN: ", hasil)
        return
    # recursive case
    # melakukan looping untuk list ("0","1","2")
    for angka in ["0","1","2"]:
        buat_pin(panjang, hasil + angka)
buat_pin(3)