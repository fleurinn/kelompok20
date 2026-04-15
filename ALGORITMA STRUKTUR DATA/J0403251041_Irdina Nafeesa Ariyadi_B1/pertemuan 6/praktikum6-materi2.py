#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#===============================#
# Insertion Sort dengan Tracing #
#===============================#

def insertion_sort(data):
    # melihat data awal
    print("data awal: ", data)
    print("="*50)

    # loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        key = data[i] # simpan nilai yang di sisipkan
        j = i-1 # index elemen terakhir di bagian kiri
        print("iterasi ke- ", i)
        print("nilai key: ", key)
        print("bagian kiri (terurut): ", data[:1])
        print("bagian kanan (belum terurut: )", data[i:])
        # geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
        # sisipkan key ke posisi yang benar
        data[j+1] = key
        print("setelah disisipkan: ", data)
        print("-"*50)
    return data

angka = [7,8,5,2,4,6]
print("hasil sorting: ", insertion_sort(angka))