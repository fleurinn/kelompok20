#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# main: membuat fungsi load data        # 
#=======================================# 

nama_file = "stok_barang.txt" 
def r_stok_barang(nama_file): # fungsi untuk ambil data dari file txt
    data_dict = {} # dictionary kosong
    try: 
        with open(nama_file, "r", encoding="utf-8") as file: # buka file mode baca
            for baris in file: # cek isi file baris per baris
                baris = baris.strip() # hapus baris baru di akhir teks
                if not baris: continue # lewati baris kosong  
                
                parts = baris.split(",") # bagi teks jadi list pakai pemisah koma
                if len(parts) == 3: # pastikan data punya 3 bagian (kode,nama,stok)
                    kode, nama_brg, stok = parts # pecah list ke variabel masing-masing
                    data_dict[kode] = { 
                        "nama barang": nama_brg, 
                        "jumlah stok": int(stok) 
                    }
    except FileNotFoundError: 
        open(nama_file, "w").close() # buat file baru yang masih kosong
    return data_dict 

buka_data = r_stok_barang(nama_file) # jalankan fungsi baca data di awal
print("jumlah data terbaca: ", len(buka_data)) # tampilkan total barang yang ada

#=========================================# 
# tugas praktikum w2: tipe data koleksi   # 
# menu 1: membuat fungsi menampilkan data # 
#=========================================# 

def tampilkan_data(data_dict): # fungsi cetak semua isi stok
    if len(data_dict) == 0: # cek kalau tidak ada barang sama sekali
        print("data kosong")
        return 
    print("=== daftar stok barang ===") # header tabel
    print(f"{'kode': <8} | {'nama barang': <12} | {'jumlah stok': >5}") # judul kolom
    print("-" * 32) # garis pembatas tabel

    for kode in sorted(data_dict.keys()): # urutkan barang berdasarkan kode
        nama_brg = data_dict[kode]["nama barang"] 
        stok = data_dict[kode]["jumlah stok"] 
        print(f"{kode: <8} | {nama_brg: <12} | {stok: >5}") # cetak baris barang

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu 2: membuat fungsi mencari data   # 
#=======================================# 

def cari_data(data_dict): # fungsi cari barang pakai kode
    kode_cari = input("masukkan kode barang yang ingin dicari: ").strip() 

    if kode_cari in data_dict: 
        nama_brg = data_dict[kode_cari]["nama barang"] 
        stok = data_dict[kode_cari]["jumlah stok"] 
        print("data barang ditemukan") 
        print(f"kode: {kode_cari}") 
        print(f"nama barang: {nama_brg}") 
        print(f"jumlah stok: {stok}")
    else: 
        print("data barang tidak ditemukan") 

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu 3: membuat fungsi tambah barang  # 
#=======================================# 

def tambah_data(data_dict): # fungsi input barang baru
    kode = input("kode barang: ").strip() 
    if kode in data_dict: # cek biar tidak ada kode yang double
        print("kode sudah ada") 
        return 

    nama_brg = input("nama barang: ").strip() 
    stok = input("jumlah stok: ").strip() 
    
    if stok.isdigit(): # pastikan yang diketik user adalah angka
        data_dict[kode] = {"nama barang": nama_brg, "jumlah stok": int(stok)} # simpan ke dict
        print("data berhasil ditambahkan") 
    else: 
        print("stok harus berupa angka") 

#===========================================# 
# tugas praktikum w2: tipe data koleksi     # 
# menu 4: membuat fungsi update stok barang # 
#===========================================# 

def update_stok(data_dict): # fungsi ubah jumlah stok barang lama
    kode = input("masukkan kode barang yang ingin di update: ") 

    if kode not in data_dict: 
        print("kode tidak ditemukan, update dibatalkan") 
        return
    try: 
        jumlah_stok_baru = int(input("masukkan jumlah stok barang baru: ").strip()) 
    except ValueError: 
        print("stok harus berupa angka") 
        return 
        
    print("jumlah stok barang: ", jumlah_stok_baru) # konfirmasi input stok baru
    jumlah_stok_lama = data_dict[kode]["jumlah stok"] 
    data_dict[kode]["jumlah stok"] = jumlah_stok_baru 
    print(f"update berhasil, \nstok barang lama: {jumlah_stok_lama} \nstok barang baru: {jumlah_stok_baru}") # laporan

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu 5: membuat menyimpan data        # 
#=======================================# 

def simpan_data(nama_file, data_dict): # fungsi tulis data ke file txt
    with open (nama_file,"w", encoding ="utf-8")as file: 
        for kode in sorted(data_dict.keys()): 
            nama_brg = data_dict[kode]["nama barang"]
            stok = data_dict[kode]["jumlah stok"]  
            file.write(f"{kode},{nama_brg},{stok}\n") 

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu utama: main mode                 # 
#=======================================# 

def main(): # fungsi pusat kendali program
    buka_data = r_stok_barang(nama_file) # load data saat pertama kali buka

    while True: # looping sampai user pilih keluar
        print("\n=== menu data persediaan barang ===") # tampilan menu
        print("1. tampilkan semua data") # menu 1
        print("2. cari barang berdasarkan kode") # menu 2
        print("3. tambah data barang") # menu 3
        print("4. update stok barang") # menu 4
        print("5. simpan data") # menu 5
        print("0. keluar") # menu tutup program

        pilihan = input("pilihan menu: ").strip() # ambil input pilihan user

        if pilihan == "1": # logika menu 1
            tampilkan_data(buka_data) # panggil fungsi tampil
        elif pilihan == "2": # logika menu 2
            cari_data(buka_data) # panggil fungsi cari
        elif pilihan == "3": # logika menu 3
            tambah_data(buka_data) # panggil fungsi tambah
        elif pilihan == "4": # logika menu 4
            update_stok(buka_data) # panggil fungsi update
        elif pilihan == "5": # logika menu 5
            simpan_data(nama_file, buka_data) # panggil fungsi simpan
            print("data berhasil disimpan") 
        elif pilihan == "0": # logika keluar
            print("program selesai") 
            break # hentikan perulangan while
        else: # jika input selain 0-5
            print("pilihan tidak valid, coba lagi") 


if __name__ == "__main__": 
    main() # panggil fungsi main untuk mulai program