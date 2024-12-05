
def antrian():
        queue = ()
        while True:
                print("\nTest Program Antrian")
                print("1. Tambahkan pelanggan ke antrian")
                print("2. Layani pelanggan")
                print("3. Tampilkan antrian")
                print("4. Exit")
                pilihan = input("Pilih Menu : ")
                
                if pilihan == "1":
                        nama = input("Masukkan Nama : ")
                        queue += (nama,)
                        print(nama, "Berhasil Ditambahkan ke antrian")
                elif pilihan == "2":
                        if queue == ():
                                print("Antrian Kosong")
                        else:
                                dilayani, queue = queue[0], queue[1:]
                                print(dilayani, "Sedang di layani")
                elif pilihan == "3":
                        if queue == ():
                                print("Antrian Kosong")
                        else:
                                print("Antrian Saat Ini : ", queue)
                elif pilihan == "4":
                        print("Terima Kasih")
                        break
                else:
                        print("Pilihan Tidak Tersedia")

antrian()
