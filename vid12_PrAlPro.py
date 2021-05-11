"""
Ivana Florencia Tanggara / 71200545

Kelas A  akan mengadakan perjalanan ke kebun binatang dan ke kebun bunga.
Murid kelas A diminta untuk memilih akan ikut ke perjalanan mana saja.
Setiap murid diperbolehkan untuk memilih satu atau kedua perjalanan. Diperoleh data sbb:
kebun bunga : Ani, Runi, Rina, Ina, Lova, Indi.
kebun binatang : Runi, Anggi, Bimo, Ani, Kiki, Fari, Indi.
Bantu wali kelas A untuk mengelompokkan siswa yang ikut ke kebun binatang,
ikut ke kebun bunga, dan ikut keduanya.
"""
"""
input = input nomor pengecekan 
proses = memilih menu pengecekan lalu proses data siswa
output = data siswa yang mengikuti masing-masing perjalanan
"""
while True:
    print("======MENU=====")
    print("1. Data siswa yang ikut ke kebun binatang")
    print("2. Data siswa yang ikut ke kebun bunga")
    print("3. Data siswa yang ikut kedua perjalanan wisata")
    print("4. Data siswa yang ikut perjalanan wisata")
    print("5. Selesai")
    pil = int(input("Masukkan nomor menu yang akan ditampilkan datanya: "))
    kebun_bunga = ["Ani", "Runi", "Rina", "Ina", "Lova", "Indi"]
    kebun_binatang = ["Runi", "Anggi", "Bimo", "Ani", "Kiki", "Fari", "Indi"]
    a = set(kebun_binatang)
    b = set(kebun_bunga)

    if pil == 1:
        print("Siswa yang ikut ke kebun binatang ada",len(a),"siswa, yaitu",a)
    elif pil == 2:
        print("Siswa yang ikut ke kebun bunga ada",len(b),"siswa, yaitu",b)
    elif pil == 3:
        keduanya = a & b
        print("Siswa yang ikut kedua perjalanan ada",len(keduanya),"siswa, yaitu",keduanya)
    elif pil == 4:
        semua = a | b
        print("Jumlah siswa yang ikut perjalanan wisata adalah",len(semua),"siswa, yaitu",semua)
    elif pil == 5:
        print("Pengecekan telah selesai")
        break
    else:
        print("Menu tidak ada, silahkan pilih yang terdapat di menu")