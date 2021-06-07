"""
Ivana Florencia Tanggara / Univ Kristen Duta Wacana

Ani ingin memainkan teka-teki rahasia bersama temannya. Teman nya akan mengirimkan kalimat yang 
didalamnya akan ada angka-angka rahasia. Karna Ani kebingungan, akan dibuatkan sebuah program untuk mencari 
angka tersebut.
test case = badh7ndaki9bakjd2++$7ndjka8bakj4nkdandajei
"""
"""
input= kalimat 
proses= dalam kalimat akan dicari angka-angka 
output= angka-angka 
"""
import re
kalimat = input("Masukkan kalimatnya = ")
cari = [int(x) for x in re.findall(r"\d+",kalimat)]
print("Kode rahasianya adalah",end=" ")
for i in cari:
    print(i,end="")
