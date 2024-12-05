angka = [2,7,10,9,5,3,6,11,20,19]

banyak_angka = len(angka)
for i in range(banyak_angka - 1):
        if angka [i] > angka[i+1]:
                temp = angka[i]
                angka[i] = angka[i+1]
                angka[i+1] = temp
                for j in range(banyak_angka - 1):
                        if angka[j] > angka[j+1]:
                                temp = angka[j]
                                angka[j] = angka[j+1]
                                angka[j+1] = temp
                                for k in range(banyak_angka - 1):
                                        if angka[k] > angka[k+1]:
                                                temp = angka[k]
                                                angka[k] = angka[k+1]
                                                angka[k+1] = temp
                                                print(angka)
