#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#===================================#
# Latihan 3: Mencari Nilai Maksimum #
#===================================#

def cari_max(data, index=0):
    # base case
    if index == len(data)-1:
        return data[index]
    # recursive case
    max_sisa = cari_max(data, index+1)
    if data[index] > max_sisa:
        return data[index]
    else:
        return max_sisa
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum: ", cari_max(angka))