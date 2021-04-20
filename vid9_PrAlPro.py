#Ivana Florencia / 71200545
#Universitas Kristen Duta Wacana
"""
Bu Ani meminta tolong untuk dibuatkan program menghitung nilai rata-rata, terendah, dan tertinggi
nilai siswanya. Bantulah bu Ani untuk membuat program tersebut.
"""
"""
input : banyak nilai yang akan dihitung, nilai siswa
proses : nilai dimasukkan sebanyak input an banyak nilai, nilai akan dicari rata-rata,
nilai terendah, dan nilai tertinggi.
output : nilai rata-rata, nilai terendah, dan nilai tertinggi
"""
print("=====Program Menghitung Nilai======")
x =[]
banyak = int(input("Berapa banyak nilai yang akan dihitung: "))
for i in range(banyak):
    nilai = int(input("Masukkan nilai: "))
    x.append(nilai)

print("Dari nilai",x,"data yang diperoleh adalah:")
nil_r = min(x)
print("Nilai terendah adalah",nil_r)
nil_t = max(x)
print("Nilai tertinggi adalah",nil_t)
rata = sum(x)/len(x)
print("Rata-rata nilai adalah",rata)
print("Perhitungan selesai.")