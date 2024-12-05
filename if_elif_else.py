# Meminta pengguna untuk memasukkan angka
angka = int(input("Masukkan sebuah angka: "))

# Memeriksa apakah angka adalah nol
if angka == 0:
    print("Angka tersebut adalah nol.")
# Memeriksa apakah angka genap
elif angka % 2 == 0:
    print(f"Angka {angka} adalah bilangan genap.")
# Memeriksa kondisi jika angka ganjil
else:
    print(f"Angka {angka} adalah bilangan ganjil.")
