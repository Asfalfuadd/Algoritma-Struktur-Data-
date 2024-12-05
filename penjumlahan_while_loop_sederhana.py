total = 0  # Inisialisasi variabel total
angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    total = sum([total, angka])  # Menambahkan angka ke total menggunakan sum
    angka = int(input("Masukkan angka lagi (0 untuk berhenti): "))

print(f"Total jumlah angka yang dimasukkan adalah: {total}")
