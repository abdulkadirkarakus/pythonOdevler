vize1=int(input("Vize 1 notunuz girsene : "))
vize2=int(input("Vize 2 notunu girer misin :"))
final=int(input("Final notunu giriniz :"))
toplam_not=vize1*0.30+vize2*0.30+final*0.40
if toplam_not >=90:
    print("AA")
elif toplam_not >=85:
    print("BA")
elif toplam_not >=80:
    print("BB")
elif toplam_not >=75:
    print("CB")
elif toplam_not >=70:
    print("CC")
elif toplam_not >=65:
    print("DC")
elif toplam_not >=60:
    print("DD")
elif toplam_not >=55:
    print("FD")
else:
    print("FF")

