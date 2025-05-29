# List: Daftar buku yang tersedia
daftar_buku = ["Python Dasar", "Algoritma", "Basis Data", "Jaringan", "Kalkulus"]
print("\nDaftar Buku (List):", daftar_buku)

# Tambah buku baru
daftar_buku.append("Kecerdasan Buatan")
print("Setelah ditambah Kecerdasan Buatan:", daftar_buku)

# Urutkan daftar buku
daftar_buku.sort()
print("Daftar Buku Terurut:", daftar_buku)

# Tuple: Daftar kategori buku
kategori = ("Teknik", "Bisnis", "Sains", "Sastra")
print("\nDaftar Kategori (Tuple):", kategori)
print("Kategori pertama:", kategori[0])

# Set: Daftar topik populer (menghindari duplikat)
topik_populer = {"AI", "Big Data", "Cybersecurity", "AI"}  # "AI" duplikat
print("\nTopik Populer (Set):", topik_populer)

# Tambah dan hapus topik
topik_populer.add("Cloud Computing")
print("Setelah ditambah Cloud Computing:", topik_populer)

topik_populer.discard("Cybersecurity")
print("Setelah dihapus Cybersecurity:", topik_populer)

print("\n=== Sistem Manajemen Data Buku Perpustakaan ===")

# List of tuple (nested data): Data buku
data_buku = [
    ("Python Dasar", "Teknik", {"Pemrograman", "Algoritma"}),
    ("Manajemen Keuangan", "Bisnis", {"Keuangan", "Manajemen"}),
    ("Fisika Modern", "Sains", {"Energi", "Mekanika"})
]

# Loop untuk menampilkan detail
for judul, kat, topik in data_buku:
    print(f"\nJudul Buku: {judul}")
    print(f"Kategori: {kat}")
    print(f"Topik Bahasan: {topik}")
    if "Pemrograman" in topik:
        print(f"'{judul}' membahas topik Pemrograman")
