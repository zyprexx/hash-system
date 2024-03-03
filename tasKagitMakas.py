import random

def bilgisayar_secimi_uret():
    n = random.randint(1,3)
    if n == 1:
        return "taş"
    elif n == 2:
        return "kağıt"
    else:
        return "makas"
    
skor_kullanici = 0
skor_bilgisayar = 0

while True:

    kullanici_secimi = input("Taş? Kağıt? Makas?")
    bilgisayar_secimi = bilgisayar_secimi_uret()

    print("Bilgisayar :", bilgisayar_secimi)

    if bilgisayar_secimi == kullanici_secimi:
        print("BERABERE")
    elif bilgisayar_secimi == "taş" and kullanici_secimi == "kağıt":
        skor_kullanici += 1
    elif bilgisayar_secimi == "kağıt" and kullanici_secimi == "makas":
        skor_kullanici += 1
    elif bilgisayar_secimi == "makas" and kullanici_secimi == "taş":
        skor_kullanici += 1
    else:
        skor_bilgisayar +=1

    print("Siz :",skor_kullanici, "VS Bilgisayar :", skor_bilgisayar)

    if skor_bilgisayar == 3 or skor_kullanici == 3:
        break



if skor_bilgisayar > skor_kullanici:
    print("KAYBETTİNİZ")
else:
    print("KAZANDINIZ")



