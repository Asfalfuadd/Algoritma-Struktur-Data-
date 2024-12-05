def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Mencari titik tengah
        L = arr[:mid]        # Membagi elemen ke dalam list kiri
        R = arr[mid:]        # Membagi elemen ke dalam list kanan

        merge_sort(L)        # Mengurutkan list kiri
        merge_sort(R)        # Mengurutkan list kanan

        i = j = k = 0

        # Salin data ke list sementara L dan R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Memeriksa apakah ada elemen yang tersisa di L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Memeriksa apakah ada elemen yang tersisa di R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Daftar angka yang ingin diurutkan
angka = [2, 7, 10, 9, 5, 3, 6, 11, 20, 19]

# Memanggil fungsi merge_sort
merge_sort(angka)

# Menampilkan hasil
print("Daftar yang diurutkan:", angka)
