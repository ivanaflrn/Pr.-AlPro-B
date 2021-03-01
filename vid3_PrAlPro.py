#Ivana Florencia Tanggara / 71200545
#Universitas Kristen Duta Wacana

"""
Ani mendapat tugas kuliah untuk membuat program perhitungan
mencari bilangan prima, bantu Ani untuk membuatnya!

https://www.pythonindo.com/mengecek-bilangan-prima-atau-tidak/
"""
"""
diketahui: mencari bilangan prima pada range tertentu

input: range dan sampai

proses : bilangan akan di modulo = 0 : bukan bilangan prima, else : bilangan prima

output: bilangan primanya.
"""

def prime(x):
    prim = True
    if x >= 2:
        for i in range(2,x):
            if x % i == 0:
                prim = False
    else:
        prim = False
    return prim

a =[]
x = int(input("Masukkan range: "))
y = int(input("to: "))
for i in range(x,y):
    if prime(i):
        a.append(i)
print("Bilangan prima dari range",x,"to",y,"adalah",a)

"""
1. range 2 to 10

2. range 10 to 100

3. range 0 to 1
"""
