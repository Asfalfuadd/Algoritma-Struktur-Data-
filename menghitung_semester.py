# Inisiasi
tahun_masuk = int(input("Masukkan tahun masuk mahasiswa: "))
tahun_sekarang = int(input("Masukkan tahun sekarang: "))

# Hitung selisih tahun
selisih_tahun = tahun_sekarang - tahun_masuk

# Hitung selisih semester
if selisih_tahun % 2 == 0:
        # Selisih tahun genap
        semester = selisih_tahun * 2
else:
        # Selisih tahun ganjil
        semester = selisih_tahun * 2 + 1

# Output
print("Jumlah semester mahasiswa saat ini adalah:", semester)
