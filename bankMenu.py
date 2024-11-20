# from bangMain import *
from dataBase import *
from login import *
import time

def menuBank(saldoNow, uname) :

    saldoNow = username1.index(uname)

    # Nabung
    # Tarik Tunai
    # Transfer
    print("=============================")
    print("||        MENU BANK        ||")
    print("=============================")
    print(" Saldo Anda : Rp", saldo[saldoNow])
    print("=============================")
    print("1. Isi Saldo")
    print("2. Tarik Tunai")
    print("3. Tranfer")
    print("4. Info Akun")
    print("0. Keluar")

    x = int(input("Pilihan anda : "))


    if x==1 :
        print("=========================================")
        print("||              ISI SALDO              ||")
        print("=========================================")
        isiSaldo(saldoNow)
        menuBank(saldoNow, uname)
    elif x == 2 :

        n = 0
        kesempatan = 2 

        for n in range(3) :
        
            pin = int(input("PIN : "))

            cek = loginPin(pin, uname)

            if cek == True :
                tarikTunai(saldoNow, uname)
                menuBank(saldoNow, uname)
                break
            elif kesempatan == 0 :
                print("==========================================")
                print("||        KESEMPATAN SUDAH HABIS        ||")
                print("==========================================")
                menuBank(saldoNow, uname)
                    
            
            else :
                    print("============================================")
                    print("||      PIN YANG ANDA MASUKKAN SALAH      ||")
                    print("============================================")
                    print("         Kesempatan tinggal", kesempatan, "kali")
                
                
                    
                    kesempatan = kesempatan - 1
            
    elif x == 3 :
        bankName = str(input("Masukkan Nama Bank\n=> "))
        noRekening = int(input("Masukkan No. Rekeneing Tujuan (8 Digit)\n=>"))

        i = 0
        
    # ### MENCARI INDEX PENERIMA
    #     while i < len(noRekDataBase) and noRekening is not noRekDataBase[i] :
            
    #         i = i + 1

        cek = CariNoRek(noRekening, uname)
        indexPengirim = username1.index(uname)

        # print("Cek Index penerima ", noRekDataBase.index(noRekening))
        # print("Cek Index Pengirim",saldoNow)

        if cek == True :
            print("==================================================")
            print("||             SILAHKAN TRANSFER :)             ||")
            print("==================================================")
         
            nominal = int(input("Nominal Transfer\n=>"))
            if nominal > saldo[saldoNow] : 
                print("Saldo anda tidak mencukupi untuk melakukan transfer")
            else : 
                saldo[noRekDataBase.index(noRekening)] = saldo[noRekDataBase.index(noRekening)] + nominal
                saldo[indexPengirim] = saldo[indexPengirim] - nominal

            menuBank(saldoNow, uname)

        else :
            print("NO REKENING TIDAK DITEMUKAN!!!!!!!!!!")
            menuBank(saldoNow, uname)

        
        # cekNoRek = noRekDataBase.index(noRekening)

        # if noRekening == noRekDataBase[cekNoRek] :

        #     print("SILAHKAN TRANSFER :)")
             
        #     nominal = int(input("Nominal Transfer\n=>"))

        #     if nominal > saldo[saldoNow] : 
        #         print("Saldo anda tidak mencukupi untuk melakukan transfer")

        #     else : 

        #         saldo[cekNoRek]= saldo[cekNoRek] + nominal
        #         saldo[saldoNow] = saldo[saldoNow] - nominal
        # else :
        #     print("NO REKENING TIDAK DITEMUKAN!!!!!!!!!!")

    elif x == 4 :
        print("=============================================")
        print("||            - AKUN ANDA -                ||")
        print("=============================================")
        print("USERNAME\t: ", username1[saldoNow])
        print("PIN ANDA\t: ", pinDataBase[saldoNow])
        print("NO REKENING\t: ", noRekDataBase[saldoNow])

        input("\n\nTEKAN ENTER UNTUK LANJUT...........................")
        menuBank(saldoNow, uname)

    elif x ==  0:

        print("ANDA KELUAR DALAM WAKTU 1 DETIK")
        time.sleep(1)
        
    else :
        print("Pilihan Tidak Ada")
    
        menuBank(saldoNow, uname)

def isiSaldo(saldoNow) :
    print("Saldo : ", saldo[saldoNow])
    isi = int(input("Isi Berapa ??\n=> "))

    saldo[saldoNow] = saldo[saldoNow] + isi

def tarikTunai(saldoNow, uname) :

        print("SALDO ANDA", saldo[saldoNow])

        tarik = int(input("NOMINAL YANG INGIN ANDA TARIK\n=> Rp "))

        if tarik > saldo[saldoNow] :
             print("==================================================")
             print("||          SALDO ANDA TIDAK MENCUKUPI          ||")
             print("==================================================")
             input("Tekan sembarang tombol untuk lanjut..............")
            
        else :
             saldo[saldoNow] = saldo[saldoNow]-tarik



