import random

def bahis_oyna():

    bakiye = 100
    print("Mevcut bakiyeniz: " + str(bakiye) + " TL")

    while bakiye > 0:
        bahis_miktari = int(input("Bahis miktarınızı girin: "))

        if bahis_miktari == 0:
            break

        if bahis_miktari > bakiye:
            print("Yetersiz bakiye!")
            continue

        tahmin = input("Tek mi çift mi? (t/ç): ")

        if tahmin not in ("t", "ç"):
            print("Geçersiz tahmin!")
            continue

        rastgele_sayi = random.randint(1, 10)
        print("Rastgele sayı: " + str(rastgele_sayi))

        if (rastgele_sayi % 2 == 0 and tahmin == "ç") or (rastgele_sayi % 2 != 0 and tahmin == "t"):
            bakiye += bahis_miktari
            print("Kazandınız!")
        else:
            bakiye -= bahis_miktari
            print("Kaybettiniz!")

        print("Mevcut bakiyeniz: " + str(bakiye) + " TL")

    print("Oyun bitti!")
    print("Kalan bakiyeniz: " + str(bakiye) + " TL")