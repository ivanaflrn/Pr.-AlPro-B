"""
Ivana FLorencia / Universitas Kristen Duta Wacana

Ani adalah seorang murid SMP yang belum bisa menyelesaikan masalah bilangan berpangkat,
Ani meminta untuk dibuatkan program mencari bilangan berpangkat tersebut, mari kita bantu
"""
"""
input: user input bilangan yang ingin dicari(a,b)
proses: input-dipangkat
output: bilangan hasil pangkat 
"""
a = int(input("Masukkan angka: "))
b = int(input("Masukkan pangkatnya: "))

def pangkat(a,b):
    if b == 0:
        return 1
    else:
        return a * pangkat(a,b-1)

print(pangkat(a,b))