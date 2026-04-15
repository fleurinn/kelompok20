#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#===============================================#
# Latihan 4: Memahami Kode Program (Merge Sort) #
#===============================================#

def merge_sort(data):
    # base case
    if len(data) <= 1: 
        return data 

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge_sort(left_sorted, right_sorted)

'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?

Jawab:
1. base case adalah kondisi penghenti pada fungsi rekursif, tanpa base case fungsi akan terus memanggil dirinya sendiri tanpa henti. di kode ini base case nya adalah:
    if len(data) <= 1:
        return data
    dimana jika ukuran data sudah tersisa 1 elemen maka akan dianggap sudah terurut, fungsi akan berhenti memecah data dan langsung mengembalikan data
2. fungsi memanggil dirinya sendiri karena menggunakan konsep rekursi, di kode ini recursive call nya adalah:
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
   fungsi terus memanggil dirinya sendiri agar proses sorting bisa dilakukan secara bertahap hingga mencapai base case.
3. tujuan fungsi merge() adalah untuk menggabungkan 2 daftar yang sudah terurut menjadi satu daftar yang terurut kembali.
'''