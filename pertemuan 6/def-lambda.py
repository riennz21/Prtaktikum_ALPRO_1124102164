import os
import webbrowser

# Fungsi untuk membuka media sesuai pilihan
def buka_media(pilihan):
    media = {
        1: lambda: webbrowser.open("https://open.spotify.com"),
        2: lambda: webbrowser.open("https://music.youtube.com"),
        3: lambda: webbrowser.open("https://soundcloud.com"),
        4: lambda: os.system("start wmplayer"),  # Buka Windows Media Player
        5: lambda: os.system("explorer C:\\Users\\Public\\Music"),  # Buka folder musik
        6: lambda: os.system("explorer C:\\Users\\Public\\Videos"),  # Buka folder video
    }
    aksi = media.get(pilihan)
    if aksi:
        aksi()
        return f"Pilihan {pilihan} dijalankan."
    elif pilihan == 0:
        print("Keluar dari program...")
        return
    else:
        return "Pilihan tidak valid. Masukkan angka 0–6."

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== Media Center ===")
    print("1. Buka Spotify (Web)")
    print("2. Buka YouTube Music")
    print("3. Buka SoundCloud")
    print("4. Buka Windows Media Player")
    print("5. Buka Folder Musik Lokal")
    print("6. Buka Folder Video Lokal")
    print("0. Keluar")

# Program utama
while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Masukkan pilihan (0–6): "))
        hasil = buka_media(pilihan)
        if hasil:
            print(hasil)
        if pilihan == 0:
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka antara 0–6.")
