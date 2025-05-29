# IF ELSE, ELIF, NESTED IF
def cek_suhu_ruangan():
    # Input
    suhu = float(input("Masukkan suhu ruangan saat ini (dalam °C): "))
    print("1. Di dalam rumah")
    print("2. Di luar rumah")
    lokasi = input("Di mana Anda berada? Pilih angka 1 atau 2: ")

    # IF ELSE & ELIF
    if lokasi == "1":
        if suhu < 18:
            print("Suhu terlalu dingin untuk di dalam rumah.")
            print("Disarankan untuk menyalakan pemanas ruangan.")
        elif suhu <= 25:
            print("Suhu nyaman untuk di dalam rumah.")
        else:
            print("Suhu terlalu panas untuk di dalam rumah.")
            print("Disarankan untuk menyalakan AC atau kipas angin.")

    elif lokasi == "2":
        if suhu < 20:
            print("Suhu cukup dingin di luar. Gunakan jaket jika perlu.")
        elif suhu <= 30:
            print("Suhu luar cukup nyaman.")
        else:
            # Nested IF
            print("Suhu di luar cukup panas.")
            aktivitas = input("Apakah Anda ingin berolahraga di luar? (y/n): ").lower()
            if aktivitas == "y":
                print("Disarankan untuk membawa air minum dan menghindari paparan langsung matahari.")
            else:
                print("Lebih baik tetap di tempat teduh atau di dalam ruangan.")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

cek_suhu_ruangan()
