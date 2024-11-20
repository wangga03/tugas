arr = input("Masukkan Kata\n=> ")
print(type(arr))
##Mengconvert string menjadi list
Arr2 = list(arr)  
print("Tipe data setelah di convert ",type(Arr2))

panjang = len(Arr2)
n = int((panjang-1) / 2)
print(f"Jumlah huruf adalah {panjang} dan 'n' adalah jumlah perulangan {n}")

x = panjang

a = 0


while a < panjang and n >= 0:

    # print(f"Index ke-{a} ditukar dengan undex ke-{x - a-1}")

    temp = Arr2[panjang - 1 - a]

    Arr2[panjang - 1 - a] = Arr2[a]

    Arr2[a] = temp

    a += 1

    n -= 1


for a in range(panjang):
    print(Arr2[a], end='')
arrConvert = list(arr)
cek = False
if arrConvert == Arr2 :
    cek = True
else :
    cek = False
    
print("\n",cek)