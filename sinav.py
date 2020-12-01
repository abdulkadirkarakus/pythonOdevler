#
def check_not():
    vize1 = int(input("Vize 1 notunu giriniz :"))
    vize2 = int(input("Vize 2 notunu giriniz :"))
    final = int(input("Final notunu giriniz :"))
    if 0 > vize1 or vize1 > 100 or 0 > vize2 or vize2 > 100 or 0 > final or final > 100:
        print("0 ile 100 arasıda sayı giriniz :")
        check_not()
    else:
        return not_hesapla(vize1, vize2, final)
def not_hesapla(vize1, vize2, final):
    a = (float(vize1) * 0.30) + (float(vize2) * 0.30) + (float(final) * 0.40)
    return harf_notu(a)
def harf_notu(not_hesapla):
    if not_hesapla >= 90:
        print("AA")
    elif not_hesapla >= 85:
        print("BA")
    elif not_hesapla >= 80:
        print("BB")
    elif not_hesapla >= 75:
        print("CB")
    elif not_hesapla >= 70:
        print("CC")
    elif not_hesapla >= 65:
        print("DC")
    elif not_hesapla >= 60:
        print("DD")
    elif not_hesapla >= 55:
        print("FD")
    else:
        print("FF")
print(check_not())