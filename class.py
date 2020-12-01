class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []
    def kisi_bilgileri(self):
        return f' Ad: { self.ad }, Soyad: { self.soyad },Yas: { self.yas },Ulke:{ self.ulke },Sehir:{ self.sehir }'
    def yetenek_ekle(self,yetenek):
        self.yetenekler.append(yetenek)

yeni_insan = Insan("Abdülkadir", "karakus", "24", "Tr", "Antep")
yeni_insan.yetenek_ekle('Bisiklete binmek.')
yeni_insan.yetenek_ekle('yemek yemek.')
print(yeni_insan.kisi_bilgileri())
print(yeni_insan.yetenekler)
