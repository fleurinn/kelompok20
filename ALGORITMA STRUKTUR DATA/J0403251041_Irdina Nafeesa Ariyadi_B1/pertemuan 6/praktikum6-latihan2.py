#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#======================================#
# Latihan 2 : Melengkapi Potongan Kode #
#======================================#

angka = [3,7,4,2,5,10]
print("Angka sebelum di Sorting: ",angka)

'''
Jawab:
1. Sorting Ascending
'''

def insertion_sort(data):
    # loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        key = data[i] # simpan niai yang disisipkan
        j = i-1 # index elemen terakhir di bagian kiri
        # geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # sisipkan key ke posisi yang benar
        data[j+1] = key
    return data 

print("Hasil Sorting Ascending: ", insertion_sort(angka))

'''
2. Sorting Descending
'''
def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        while j>=0 and data[j] < key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

print("Hasil Sorting Descending: ", insertion_sort_descending(angka))