"""
Ani merupakan karyawan baru di sebuah toko buah anggur
terdapat 5 jenis buah anggur yang memiliki kode yang unik.
Karena Ani adalah karyawan baru, Ani belum mengerti kode dari anggur yang dijual.
Ani meminta bantuan untuk dibuatkan sebuah program yang dapat mengecek
kode yang ada.

jenis anggur :
- anggur merah(AM) China (CN)
- anggur merah(AM) Amerika Serikat (AS)
- anggur hijau(AH) China (CN)
- anggur hijau(AH) Amerika Serikat(AS)
- anggur hitam(AT) Amerika Serikat(AS)
untuk kode barang dengan format : jenis anggur-harga-negara asal
contoh :
1. AM-145-CN yang berarti
   jenis anggur :Anggur Merah; harga :145000; negara asal : China
2. AT-200-AS yang berarti
   jenis anggur :Anggur Hitam; harga :200000; negara asal : Amerika Serikat
"""
"""
diketahui : format anggur -> jenis anggur-harga-negara asal

input: format kode (anggur)
proses : kode -> split (for)
output : penjelasan dari kode barang

"""
kode = str(input("Masukkan kode:"))
brg = kode.split("-")
jns = brg[0]
hrg = brg[1]
ngr = brg[2]
v = ["AM-Anggur Merah","AH-Anggur Hijau","AT-Anggur Hitam"]
for i in v:
   j = i.split("-")
   if jns == j[0]:
      var = j[1]

n = ["CN-China","AS-Amerika Serikat"]
for i in n:
   k = i.split("-")
   if ngr == k[0]:
      neg = k[1]

print("Jenis anggur adalah ",var)
print("Harga anggur adalah ",hrg+"000")
print("Anggur berasal dari negara ",neg)

