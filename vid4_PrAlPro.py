"""
Ani ingin membuat program untuk mengetahui pola file teman-temannya.
bantu Ani untuk membuat program yang dapat mengetahui setiap pola dalam file 
dan memisahkan menjadi informasi yang berguna untuk Ani.
Contoh = Tugas-Ina-A-MaDis
menjadi =
Jenis file : Tugas
Nama : Ina
Kelas : A
Mata kuliah : MaDis

https://ichi.pro/id/split-vs-partition-di-python-strings-163852204420949
"""
"""
diketahui : tipe nama file

input : user akan menginput menu pengecekan dan input nama file

proses : nama file di split lalu penginputan akan dilakukan secara berulang sampai keluar
 2 menu : 1. Pengecekan dan 2. Keluar

output : penaman dari setiap unsur nama file
"""

while True:
    print("Menu:")
    print("1. Pengecekan")
    print("2. Keluar")
    pilih = int(input("Pilih menu (1/2): "))
    if pilih == 1:
        file = str(input("Masukkan nama file : "))
        x = file.split("-")
        jenis = x[0]
        nama = x[1]
        kelas = x[2]
        matkul = x[3]

        print("Jenis file :",jenis)
        print("Nama mahasiswa :",nama)
        print("Kelas yang diikuti :",kelas)
        print("Mata kuliah :",matkul)
    elif pilih == 2:
        print("Selesai, Anda keluar")
        break
    else:
        print("Menu tidak ada didaftar, silahkan masukkan 1 atau 2")
