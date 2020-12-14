class Ogrenci:
    def __init__(self, ogrenciadi, ogrencisoyadi, ogrencisinifi):
        self.ogrenciadi = ogrenciadi
        self.ogrencisoyadi = ogrencisoyadi
        self.ogrencisinifi = ogrencisinifi

    def goster(self):
        print("Adı ", "Soyadi :" ,self.ogrenciadi, self.ogrencisoyadi,"sınıfı:",self.ogrencisinifi)

class Soru:
    def __init__(self):
        self.dogruSayisi = int(input("Öğrenci doğru sayısı :"))
        self.yanlisSayisi = int(input("Öğrenci yanlış sayısı :"))


    def netsayisi(self):
        toplamSoru = self.dogruSayisi + self.yanlisSayisi
        if toplamSoru > 50:
            print("Toplam soru sayısı 50'den fazla olamaz.")
            quit()

        dogru_net = self.yanlisSayisi / 4
        net_sayisi = self.dogruSayisi - dogru_net
        return net_sayisi

    def hesapla(self, net_sayisi):
        ogrenciPuan = net_sayisi * 1
        if ogrenciPuan < 0:
            ogrenciPuan = 0
        return ogrenciPuan

ogrenci1 = Ogrenci("Kral ", "Hoca", "5")
Soru1 = Soru()
ogrenci1.goster()
print(Soru1.hesapla(Soru1.netsayisi()))