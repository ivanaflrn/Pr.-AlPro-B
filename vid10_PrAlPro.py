""" Ivana Florencia /71200545
Ani akan mencatat sisa uang saku yang diterimanya setiap hari, bantu Ani untuk membuat program
pencatatan kasnya!"""
"""
input : hari dan nominal uang 
proses : while, data akan disimpan dalam dict
output : hasil pencatatan input uang dalam kas ani
"""
kas = {}
repeat = True
while repeat == True:
    print("===Pencatatan Kas Ani===")
    print("1. Tambah catatan kas")
    print("2. Daftar catatan kas")
    print("3. Hapus catatan kas")
    print("4. Keluar")
    pil = int(input("Masukkan pilihan: "))
    if pil == 1:
        hari = input("Masuukkan hari: ")
        jmlh = int(input("Masukkan jumlah uang: "))
        if hari in kas: 
            kas[hari]+=jmlh
        else:
            kas[hari]=jmlh
    elif pil == 2:
        print("Hasil pencatatan kas:")
        for key in kas:
            print("Hari",key,"=",kas[key])
    elif pil == 3:
        hapus = input("Masukkan hari yang akan dihapus: ")
        if hapus in kas:
            kas.pop(hapus)
            print("Berhasil dihapus")
        else:
            print("Hari tidak ada")
    elif pil == 4:
        repeat = False
        print("Pencatatan selesai")