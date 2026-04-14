#=======================================================================
# Praktikum 2: Konsep Abstract Data Type dan File Handling (STUDI KASUS)
# Latihan 1: Membuat fungsi load data
#=======================================================================

nama_file = "data_mahasiswa.txt" #variabel buat nyimpen nama file yang isinya data mahasiswa

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {} #inialisasi data dictionary kosong buat nyimpen data mahasiswa

    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file: #buka file data_mahasiswa.txt dalam mode baca (R)
        for baris in file: #looping tiap baris
            baris = baris.strip() #hilangkan karakter baris baru (\n) diakhir baris
            parts = baris.split(",") #pisahin isi baris berdasarkan koma, hasilnya list

            if len(parts) !=3: #menunjukkan datanya terdiri dr 3 bag (nim, nama, nilai)
                continue
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str) #ubah str ke int
            data_dict[nim]={"nama": nama, "nilai": nilai_int}
            nim, nama, nilai = baris.split(",") #pecah menjadi data satuan

            # simpan data mahasiswa ke directory dengan key nim
            data_dict[nim]={
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict #manggil/balikin dict yg isinya data mahasiswa

#memanggil fungsi baca_data_mahasiswa dan simpan hasilnya ke buka_data
buka_data = baca_data_mahasiswa(nama_file) 
print("Jumlah Data Terbaca: ", len(buka_data)) 

#=======================================================================
# Praktikum 2: Konsep Abstract Data Type dan File Handling (STUDI KASUS)
# Latihan 2: Membuat fungsi menampilkan data
#=======================================================================

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("data kosong")
        return
    #membuat header tabel
    print("=== daftar mahasiswa ===")
    print(f"{'nim': <10} | {'nama': <12} | {'nilai': >5}")
    print("-"*32)

    '''
        untuk tampilan data yg rapi, atur f-string formating
        {'nim': <10} artinya:
        tampilkan nim <= rata kiri dgn lebar 10 karakter
        {'nama': <12} artinya:
        tampilkan nama rata kiri dgn lebar 12 karakter
        {'nilai': >5} artinya:
        tampilkan NIM >= rata kanan dgn lebar 5 karakter
    '''

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

#memanggil fungsi menampilkan data
tampilkan_data(buka_data)

#=======================================================================
# Praktikum 2: Konsep Abstract Data Type dan File Handling (STUDI KASUS)
# Latihan 3: Membuat fungsi menampilkan data
#=======================================================================

def cari_data(data_dict):
    #mencari data mahasiswa dgn NIM
    nim_cari = input("masukkan NIM yg ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("data mahasiswa ditemukan")
        print(f"NIM: {nim_cari}")
        print(f"nama: {nama}")
        print(f"nilai: {nilai}")
    else:
        print("data mahasiswa tdk ditemukan")

cari_data(buka_data)

#=======================================================================
# Praktikum 2: Konsep Abstract Data Type dan File Handling (STUDI KASUS)
# Latihan 4: Membuat fungsi update nilai
#=======================================================================

def update_nilai(data_dict):
    #asukkan nim mahasiswa yg ingin diupdate nilainya
    nim = input("masukkan NIM yg akan diupdate nilainya: ")

    if nim not in data_dict:
        print("NIM tdk ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("masukkan nilai br (0-100): ").strip())
    except ValueError:
        print("nilai hrs berupa angka")
        return
    if nilai_baru <0 or nilai_baru >100:
        print("nilai hrs 0-100")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"update berhasil, nilai {nim} berubah dari {nilai_lama} ke {nilai_baru}")

update_nilai(buka_data)

#=======================================================================
# Praktikum 2: Konsep Abstract Data Type dan File Handling (STUDI KASUS)
# Latihan 5: Membuat fungsi menyimpan data
#=======================================================================

def simpan_data(nama_file, data_dict):
    with open (nama_file,"w", encoding ="utf-8")as file:
        for nim in sorted(data_dict.keys()):
            nama= data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

simpan_data(nama_file, buka_data)
print("data berhasil disimpan")

#=======================================================================
# Praktikum 2: Konsep Abstract Data Type dan File Handling (STUDI KASUS)
# Latihan 6: Membuat fungsi menyimpan data
#=======================================================================

def main():
    #menjlnkan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("=== menu data mahasiswa ===")
    print("1. tampilkan semua data")
    print("2. update data mahasiswa")
    print("3. update nilai mahasiswa")
    print("4. simpan nilai ke data")
    print("0. keluar")

    pilihan = input("pilihan menu: ".strip())

    if pilihan == "1":
        tampilkan_data(buka_data)
    elif pilihan == "2":
        cari_data(buka_data)
    elif pilihan == "3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
        print("data berhasil disimpan")
    elif pilihan == "0":
        print("program selesai")
        break
    else:
        print("pilihan tdk valid, coba lg")

if __name__ == "__main__":
    main()