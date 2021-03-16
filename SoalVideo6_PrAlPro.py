"""
Membuat pola persegi dengan 2 karakter yang posisinya selalu bergantian
contoh:
*%*%*%
*%*%*%
*%*%*%
*%*%*%
*%*%*%
*%*%*%
"""
"""
input: jumlah baris dan jumlah kolom (n)

proses: perulangan i = baris 
perulangan j = kolom
j -> percabangan (modulo)

output: pola persegi 
"""
n = int(input("n = "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2 != 0:
            print("*",end='')
        else:
            print("%",end='')
    print()