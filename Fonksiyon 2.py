
birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
sayi = int(input("Sayı:"))

def atama(sayi):
    if  10 <= sayi  or  sayi >= 99:
       print("İki basamaklı sayi giriniz ")


    return okunus(sayi)


def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10


    return onlar[ikinci] + " " + birler[birinci]
#sayi = int(input("Sayı:"))

print(okunus(sayi))