# 1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55,

def fibonachi (n):
        if n == 1 or n == 2:
                return 1
        else:
                return fibonachi(n - 1) + fibonachi(n - 2)

print ("Hasilnya adalah : ", fibonachi(2))
