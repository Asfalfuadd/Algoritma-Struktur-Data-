def Luas_Persegi_Panjang (panjang, lebar):
    return panjang*lebar


def  luas_lingkaran (jari_jari, phi = 3.14):
    return phi * jari_jari*jari_jari


def fungsi (x) :
    return 2 * (x**2) + (3 * x ) - 10


while True:
    print("\nPilihan fungsi:")
    print("1. hitung Luas Persegi Panjang")
    print("2. hitung Luas Lingkaran")
    print("3. hitung f(x)")
    print("4. Keluar")
    
    pilihan = int(input("Masukkan pilihan Anda 1, 2, 3, atau 4 : "))
    
    if pilihan == 1:
        p = int(input("Masukkan nilai panjang persegi panjang: "))
        l = int(input("Masukkan nilai lebar persegi panjang: "))
        hasil_luas = Luas_Persegi_Panjang(p, l)
        print("Luas persegi panjang adalah:", hasil_luas)
    
    elif pilihan == 2:
        r = int(input("Masukkan jari-jari lingkaran: "))
        hasil_luas_lingkaran = luas_lingkaran(r)
        print("Luas lingkaran adalah:", hasil_luas_lingkaran)
    
    elif pilihan == 3:
        x = int(input("Masukkan nilai x: "))
        hasil_fx = fungsi(x)
        print("Hasil dari f(x) adalah:", hasil_fx)
    
    elif pilihan == 4:
        print("Program selesai. Terima kasih!")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
