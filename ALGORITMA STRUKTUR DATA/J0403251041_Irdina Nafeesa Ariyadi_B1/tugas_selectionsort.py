# fungsi untuk melakukan pengurutan 
# menggunakan algoritma Selection Sort
def selection_sort(data):

    n = len(data)  # menyimpan jumlah elemen dalam list

    # perulangan pertama untuk menentukan 
    # posisi yang akan diisi
    for i in range(n):

        min_index = i  # menganggap elemen pertama 
                       # sebagai nilai terkecil sementara

        # perulangan kedua untuk mencari 
        # nilai terkecil pada sisa data
        for j in range(i + 1, n):

            # membandingkan apakah elemen sekarang 
            # lebih kecil dari nilai minimum
            if data[j] < data[min_index]:
                min_index = j  # jika lebih kecil, 
                               # update posisi nilai minimum

        # menukar posisi elemen terkecil dengan 
        # elemen pada posisi awal
        data[i], data[min_index] = data[min_index], data[i]

    return data  # mengembalikan data yang sudah terurut


# contoh data yang akan diurutkan
angka = [29, 10, 14, 37, 13]

# memanggil fungsi selection_sort untuk mengurutkan data
hasil = selection_sort(angka)

# menampilkan hasil setelah diurutkan
print("Data setelah diurutkan:", hasil)