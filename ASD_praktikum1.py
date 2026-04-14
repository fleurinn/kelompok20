#==========================================================
# Praktikum 1: Konsep Abstract Data Type dan File Handling
# Latihan Dasar 1A : Membaca seluruh isi file
#==========================================================

#Membuat file dgn mode read
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dlm 1 string
print(isi_file)

print("=== hasil read ===")
print("tipe data:", type(isi_file))
print("jumlah karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#Membuka file perbaris
print("=== membaca file perbaris ===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #'.strip()' untuk menghilangkan garis dibwhnya (\n)
        print("baris ke- ", jumlah_baris)
        print("isinya: ", baris)

#==========================================================
# Praktikum 1: Konsep Abstract Data Type dan File Handling
# Latihan Dasar 2 : Parsing baris menjadi kolom data
#==========================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #pecah mnjd data satuan
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", int(nilai)) 

#==========================================================
# Praktikum 1: Konsep Abstract Data Type dan File Handling
# Latihan Dasar 3 : Membaca file dan menyimpan ke list
#==========================================================

data_list = [] #inisialisasi list untuk menampung data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)]) #menyimpan data ke list

print("=== data mahasiswa dalam list ===")
print(data_list)

print("=== jumlah record dlm list ===")
print("jumlah record", len(data_list))

print("=== menampilkan data record tertentu ===")
print("contoh record pertama: ", data_list[0]) #array dimulai dr 0

#===========================================================
# Praktikum 1: Konsep Abstract Data Type dan File Handling
# Latihan Dasar 4 : Membaca file dan menyimpan ke dictionary
#===========================================================

data_dict = {} #inisialisasi buat variabel utk dictionary

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan data mahasiswa ke dictionary dgn key 'NIM'
        data_dict[nim] = {          #key
            "nama": nama,           #value
            "nilai": int(nilai)     #value
        }

print("=== data mahasiswa dlm dictionary ===")
print(data_dict)