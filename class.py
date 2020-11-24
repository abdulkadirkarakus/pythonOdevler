class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return 'f Ad: {self.ad}, self.soyad,self.yas,self.ulke,self.sehir'

    def yetenek_ekle(self):
        self.yetenekler.append(self.yetenekler)
        return self.yetenekler

insan1 = Insan("Abdülkadir", )
insan1.yetenekler("")
print(insan1.kisi_bilgileri())
