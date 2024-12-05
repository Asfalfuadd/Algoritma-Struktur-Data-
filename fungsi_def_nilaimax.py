# fungsi mencari nilai maximal dan  minimal
def max (angka1, angka2, angka3) :
    if ((angka1 > angka2) and (angka1 > angka3)) :
        return angka1
    elif ((angka2 > angka1) and (angka2 > angka3)) :
        return angka2
    else :
        return angka3

a= int(input("masukan angka 1: "))
b= int(input("masukan angka 2: "))
c= int(input("masukan angka 3: "))

cek_max= max(a,b,c)
print ("nilai maximal dari ",a,",",b,",",c,"adalah ",cek_max)
print ("nilai maximal adalah ", cek_max)

cek_min= min(a,b,c)
print ("nilai manimal dari ",a,",",b,",",c,"adalah ",cek_min)
print ("nilai minimal adalah ", cek_min)

a = [12, 14, 50, 60, 88]
