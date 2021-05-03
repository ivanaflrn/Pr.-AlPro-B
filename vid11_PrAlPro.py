"""
Ivana Florencia / 71200545

Ani meminta dibuatkan sebuah program menghitung banyak buah yang ada dalam sebuah tuple, 
Ia ingin mengurutkan banyak buah yang ada dalam tuplenya. Bantu Ani membuatnya

Contoh: 
buah = (mangga, apel, nanas, mangga, pisang, apel, apel, nanas, mangga, apel)
mangga = 3
apel = 4
nanas = 2
pisang = 1
"""
"""
input : buah
proses : tuple(buah) -> list -> dict 
output : jumlah dari masing masing buah
"""
buah = ("mangga","apel","nanas","mangga","pisang","apel","apel","nanas","mangga","apel")
ubah_list = list(buah)
ubah_list.sort()
x = []
for i in range(len(ubah_list)):
    if ubah_list[i-1] != ubah_list[i]:
        x.append(ubah_list[i])

dict_ksg = {}
for value in x:
    tampung = []
    for j in ubah_list :
        if value == j:
            tampung.append(j)
        dict_ksg[value]=len(tampung)

for key,value in dict_ksg.items():
    print(key,"=",value)
