class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return 'f Ad: {self.ad}, Soyad: {self.soyad},Yas: {self.yas},Ulke:{self.ulke},Sehir:{self.sehir}'

    def yetenek_ekle(self):
        self.yetenekler.append(self.yetenekler)
        return self.yetenekler

insan1 = Insan("Abdülkadir","karakus","24","Tr","Antep" )
insan1.yetenekler.append('Yazılımcı')
insan1.kisi_bilgileri()

print("AdSoyad :",insan1.ad,insan1.soyad)
print("Yaşı",insan1.yas)
print("Ülke:",insan1.ulke,"Şehir:",insan1.sehir)
print("Yetenekleri: ",insan1.yetenekler)
