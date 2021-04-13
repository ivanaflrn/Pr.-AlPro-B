#Ivana Florencia / 71200545
"""
Ani diminta oleh kepala sekolahnya untuk membuat sebuah program 
yang dapat mencetak data peserta didik baru dalam file txt.
Program tersebut akan meminta user yaitu wali peserta didik baru untuk
memasukan data peserta dan akan tercetak dalam file txt. 
"""
"""
input : yang akan di input oleh user - nama, tanggal lahir, jenis kelamin, umur
proses : setelah user menginputkan datanya, data akan di masukkan kedalam file txt
output: data akan tampil dalam file txt
"""

x = open("peserta.txt","w+")
print("===SELAMAT DATANG PESERTA DIDIK BARU===")
print("Silahkan mendaftarkan data diri")
nama = input("Masukkan nama peserta: ")
tgl = input("Masukkan tanggal lahir (dd-mm-yyyy): ")
jns = input("Masukkan jenis kelamin: ")
umur = input("Masukkan umur (th): ")
xx = ''
xx += "Nama:"+nama+"\n"+"Tanggal lahir:"+tgl+"\n"+"Jenis kelamin:"+jns+"\n"+"Umur:"+umur+"tahun"
x.write(xx)
x.close()

"""
Nama : Ivana
Tanggal lahir: 28-02-2002
Jenis kelamin: Perempuan
Umur: 19 tahun

Nama : Budi
Tanggal lahir : 10-05-2006
Jenis kelaminnya : Laki-laki
Umur: 15 
"""
