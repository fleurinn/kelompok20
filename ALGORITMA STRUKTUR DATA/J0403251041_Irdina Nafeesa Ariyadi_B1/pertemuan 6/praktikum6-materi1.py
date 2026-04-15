#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================#
# Insertion Sort (Ascending) #
#============================#

def insertion_sort(data):
    # loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] # simpan nilai yang disisipkan
        j = i-1 # index elemen terakhir di bagian kiri

        # geser 
        while j>=0 and data[j] > key:
            data [j+1] = data[j]
            j -= 1
            # disisipkan key ke posisi yang benar
            data[j+1] = key
    return data
    
angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))