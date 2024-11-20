from kalkulator import *


x = True

while x == True :

    awal = int(input("Masukkan nilai awal : "))
    akhir = int(input("Masukkan nilai awal : "))

    print("===================================================")
    print("||        MENU UNTUK KALKULATOR SEDERHANA        ||")
    print("===================================================")
    print("||   1 . Penjumlahan                             ||")
    print("||   2 . Pengurangan                             ||")
    print("||   3 . Perkalian                               ||")
    print("||   4 . Pembagian                               ||")
    print("===================================================")
    pilihan = int(input("Masukkan Pilihan\n=> "))
    
    if pilihan == 1 :
        print(tambah(awal, akhir))
        
    elif pilihan == 2 :
        print(pengurangan(awal, akhir))
        
    
    elif pilihan == 3 :
        print(perkalian(awal, akhir))
    
    elif pilihan == 4 :
    
        # if akhir == 0 : 
        #     print("Tidak bisa dibagi 0")
        # else :
        #     print(pembagian(awal, akhir))
    
        try :
            print(pembagian(awal, akhir))
        except :
            print("tidak bisa dibagi 0")


    opsi2 = str(input("Lagi????(y/n)\n=> "))

    if opsi2 is not "y" :
        x = False



    
    
    
