#Ivana Florencia Tanggara_71200545
#Universitas Kristen Duta Wacana
"""
Ani mendirikan toko kecil dengan pemesanan otomatis, 
melalui program yang akan dibuat akan dapat memasukan jenis barang,
jumlah barang, dan mengeluarkan harga total belanjaan yang akan dibayarkan pembeli.
Harga dan barang yang dijual dan ditampilkan adalah:
1. Mie goreng = 2500
2. mie rebus = 2200
3. gula 1 kg = 14000
4. minyak 1 lt = 15000
5. telur 1 kg = 20000
"""
"""
diketahui:
1. Mie goreng = 2500
2. mie rebus = 2200
3. gula 1 kg = 14000
4. minyak 1 lt = 15000
5. telur 1 kg = 20000
"""
"""
input : nama, jenis barang (kode), jumlah yang akan dibeli

proses : harga total belanja = harga barang * jumlah barang

output : harga total belanjaan yang harus dibayar

"""

print("------TOKO ANI-------")
nama = str(input("Masukkan nama anda : "))
print("Selamat datang",nama, "di toko Ani, selamat berbelanja")
mie_g = print("1. Mie Goreng = 2500")
mie_r = print("2. Mie Rebus = 2200")
gula = print("3. Gula (1kg) = 14000")
minyak = print("4. Minyak (1lt) = 15000")
telur = print("5.Telur (1kg) = 20000")

beli = int(input("Ingin membeli apa? (masukkan nomornya) : "))
if beli == 1:
    mie = int(input("Masukkan jumlah mie goreng yang ingin dibeli : "))
    harga = mie * 2500
    print("Total belanjaan yang harus dibayar adalah",harga,"Silahkan bayar dikasir")
    print("Terima kasih telah berbelanja")
elif beli == 2:
    mie = int(input("Masukkan jumlah mie rebus yang ingin dibeli: "))
    harga = mie * 2200
    print("Total belanjaan yang harus dibayar adalah",harga,"Silahkan bayar di kasir")
    print("Terima kasih telah berbelanja")
elif beli == 3:
    gula = int(input("Masukkan jumlah gula yang ingin dibeli : "))
    harga = gula * 14000
    print("Total belanjaan yang harus dibayar adalah",gula,"Silahkan bayar di kasir")
    print("Terima kasih telah berbelanja")
elif beli == 4:
    minyak = int(input("Masukkan jumlah minyak yang ingin dibeli : "))
    harga = minyak * 15000
    print("Total belanjaan yang harus dibayar adalah",minyak,"Silahkan bayar di kasir")
    print("Terima kasih telah berbelanja")
elif beli == 5:
    telur = int(input("Masukkan jumlah telur yang ingin dibeli : "))
    harga = telur * 20000
    print("Total belanjaan yang harus dibayar adalah",telur,"Silahkan bayar di kasir")
    print("Terima kasih telah berbelanja")
else:
    print("Kode barang tidak ditemukan")

"""
nama : lulu
beli mie goreng 5

nama : fani
beli dengan kode 7
"""
