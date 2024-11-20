from login import *
from dataBase import *
from bankMenu import menuBank
import random
# from bankMenu import menuBank


def inputLogin(x, y, kesempatan):
    for x in range(3) :
        print("===================================")
        print("||             LOGIN             ||")
        print("===================================")

        index = 0
        uname = str(input("Masukkan Username : "))
        pasw = str(input("Masukkan Password : "))

        # print(username1.index(uname))
        y = login(uname, pasw)

        if y == True :

            menuBank(index, uname)
            main()
            break
        elif kesempatan == 0 :
            print("==========================================")
            print("||        KESEMPATAN SUDAH HABIS        ||")
            print("==========================================")

            input("Tekan sembarang tombol untuk lanjut..............")
            main()
        else :

            print("=============================================")
            print("-          Kesempatan anda tinggal", kesempatan, "       -")
            print("=============================================")
            
                
            kesempatan = kesempatan -1
            

def main():
    print("==============================================")
    print("||                                          ||")
    print("||             - BANK WANGGA -              ||")
    print("||                                          ||")
    print("==============================================")
    print("   ||             1. Login               ||")
    print("   ||            2. Sign in              ||")
    print("   ||          0. Program Off            ||")
    print("   ========================================")

    opsi = int(input("Masukkan Pilihan : "))


    x = 0
    kesempatan = 2
    y = False



    if opsi == 1 :
        inputLogin(x, y, kesempatan)
    elif opsi == 2 :

        user = str(input("Username : "))
        pw = str(input("Password : "))
        addPin = int(input("PIN : "))
        noRek = random.randint(10000000, 99999999)

        # Proses menambah pada list
        username1.append(user)
        pasword1.append(pw)
        pinDataBase.append(addPin)
        noRekDataBase.append(noRek)
        saldo.append(0)

        print("=============================================")
        print("||            - AKUN ANDA -                ||")
        print("=============================================")
        print("USER NAME\t: ", user)
        print("PIN ANDA\t: ", addPin)
        print("NO REKENING\t: ", noRek)

        input("Tekan Sembarang Tombol untuk Lanjut................................")
        # inputLogin(x,y, kesempatan)
        main()
    elif opsi == 0 :
        print("============================================================")
        print("-          TERIMAKASIH TELAH PERCAYA KEPADA KAMI           -")
        print("============================================================")
        print(len(pasword1))
    else :
        print("Pilihan tidak ada")


main()


