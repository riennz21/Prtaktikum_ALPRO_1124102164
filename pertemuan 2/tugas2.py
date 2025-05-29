# Assignment
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
harga_per_barang = int(input("Masukkan harga per barang: Rp "))
punya_kupon = input("Apakah memiliki kupon diskon? (y/n): ").lower() == 'y'

# Assignment
total_harga = jumlah_barang * harga_per_barang  # Aritmatika
diskon = 0

# Comparison & Logical Operators
if total_harga > 1000000 and punya_kupon:  # Logical AND
    diskon = 0.20  # 20% diskon
elif total_harga > 750000:  # Comparison
    diskon = 0.10  # 10% diskon
elif total_harga >= 500000 or punya_kupon:  # Logical OR
    diskon = 0.05  # 5% diskon

# Aritmatika: Hitung total bayar setelah diskon
total_bayar = total_harga - (total_harga * diskon)

# Assignment
poin_reward = 0
if total_bayar > 300000:
    poin_reward = int(total_bayar // 20000)  # Aritmatika

# Output
print(f"\nJumlah Barang: {jumlah_barang}")
print(f"Harga per Barang: Rp {harga_per_barang:,.2f}")
print(f"Total Harga: Rp {total_harga:,.2f}")
print(f"Diskon: {diskon*100:.0f}%")
print(f"Total Bayar Setelah Diskon: Rp {total_bayar:,.2f}")
print(f"Poin Reward yang Didapat: {poin_reward}")

# Bonus tambahan
if poin_reward > 30 and total_bayar >= 600000:
    print("\nSelamat! Anda mendapatkan voucher belanja Rp 25.000!")
