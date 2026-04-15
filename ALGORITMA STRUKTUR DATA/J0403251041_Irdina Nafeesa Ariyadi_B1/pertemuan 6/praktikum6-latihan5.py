#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#====================================#
# Latihan 5: Melengkapi Fungsi Merge #
#====================================#

def merge(left, right):
    result = []
    i = 0
    j = 0 

    # membandingkan elemen kiri dan kanan selama keduanya masih ada isi
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # ambil nilai yang lebih kecil (ascending)
            result.append(left[i]) # masukkan ke result
            i += 1 # geser pointer ke kiri
        else:
            result.append(right[j]) # masukkan ke result 
            j += 1 # geser pointer ke kanan

    # jika masih ada sisa elemen di kiri, tambahkan semua
    result.extend(left[i:])

    # jika masih ada sisa elemen di kanan, tambahkan semua
    result.extend(right[j:])

    return result 

#=================#
# Panggil Program #
#=================#

left = [9, 17, 3]
right = [2, 7, 1, 13, 22]
hasil = merge(left, right)
print("hasil sorting: ", hasil)


"""
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend()!

Jawab:
1. (diatas)
2. fungsi result.extend() berfungsi untuk menambahkan sisa elemen yang belum diproses 
ke dalam list result. hal ini dilakukan agar semua elemen tetap masuk ke hasil akhir setelah proses
perbandingan selesai.
"""