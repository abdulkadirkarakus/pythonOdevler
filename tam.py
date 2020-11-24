def tambolenleri(sayi):
    tam_bolenler=[]
    for i in range(2,sayi):
        if (sayi % i == 0 ):
            tam_bolenler.append(i)
    return tam_bolenler
while True:
    sayi =int(input("sayi:"))
    if (sayi=="q"):
        print("program sonlandırıldı")
    else:
        print("Tam bölenler:",tambolenleri(sayi))
