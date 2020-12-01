#Bolunen sayıyı bulma
#1
def bolunenSayiBulma( min_sayi , max_sayi , bolunecek_sayi ):
    sayac = 0
    bolununler = []
    for i in range( min_sayi,max_sayi + 1 ):
        if i % bolunecek_sayi == 0:
            bolununler.append( i )
            sayac += 1
    return sayac,bolununler
print(bolunenSayiBulma(1,150,5))



