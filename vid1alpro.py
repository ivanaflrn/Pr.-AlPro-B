#Ivana Florencia Tanggara / 71200545
#Universitas Kristen Duta Wacana

"""
solusimatematika85.blogspot.com

soal:
kelas A, kelas B, dan kelas C memiliki bola dengan perbandingan 2 : 4 : 5.
Kelas A memiliki 20 bola, berapa bola yang dimilki kelas B dan C?
"""
"""
diketahui:
p_a = perbandingan bola kelas A
p_b = perbandingan bola kelas B
p_c = perbandingan bola kelas C
j_a = jumlah bola kelas A
j_b = jumlah bola kelas B
j_c = jumlah bola kelas C


input : j_a = 20; p_a = 2; p_b = 4; p_c = 5

proses :
jumlah bola = (perbandingan yg dicari / perbandingan yg diketahui)* jumlah bola diketahui
jumlah bola C = (perbandingan C / perbandingan A)* jumlah bola A
jumlah bola B = (perbandingan B / perbandingan A)* jumlah bola A

output : jumlah bola B dan jumlah bola C

"""

print("----Menghitung Jumlah Bola----")
p_a = int(input("Masukkan perbandingan bola kelas A : "))
p_b = int(input("Masukkan perbandingan bola kelas B : "))
p_c = int(input("Masukkan perbandingan bola kelas C : "))
j_a = int(input("Masukkan jumlah bola kelas A : "))

j_b = (p_b / p_a)* j_a
print("Jumlah bola milik kelas B adalah ",j_b)
j_c = (p_c / p_a)* j_a
print("Jumlah bola milik kelas C adalah ",j_c)


