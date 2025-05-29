# Function: Tampilkan Menu & Minta Pilihan
def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Lihat Daftar")
    print("3. Hapus Barang")
    print("4. Keluar")
    return input("Pilih opsi (1-4): ")

# Function: Tambah barang ke daftar
def tambah_barang(nama):
    daftar.append(nama)
    print(f"'{nama}' telah ditambahkan.")

# Function: Lihat isi daftar
def lihat_daftar():
    if daftar:
        print("Isi Daftar:")
        for i, item in enumerate(daftar, start=1):
            print(f"{i}. {item}")
    else:
        print("Daftar masih kosong.")

# Function: Hapus barang
def hapus_barang(nama):
    if nama in daftar:
        daftar.remove(nama)
        print(f"'{nama}' telah dihapus.")
    else:
        print(f"'{nama}' tidak ditemukan di daftar.")

# Daftar utama
daftar = []

# Program utama
jalan = True
while jalan:
    pilihan = tampilkan_menu()
    
    if pilihan == "1":
        nama = input("Masukkan nama barang: ")
        tambah_barang(nama)
    elif pilihan == "2":
        lihat_daftar()
    elif pilihan == "3":
        nama = input("Nama barang yang ingin dihapus: ")
        hapus_barang(nama)
    elif pilihan == "4":
        print("Program selesai.")
        jalan = False
    else:
        print("Pilihan tidak valid. Coba lagi.")
