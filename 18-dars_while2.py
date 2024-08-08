


#1
"""

yangi_royxat = []

while True:
    kiritilgan = input("Mahsulotni kiriting: ")
    yangi_royxat.append(kiritilgan)
    kiritilgan_2 = input("Yana mahsulot kiritasizmi (ha/yo'q)? ")
    if kiritilgan_2 != "ha":
        break
"""    



#2
"""
mahsulotlar = {}

ishora = True

while ishora:
    nomi = input(f"Mahsulot nomini kiriting: ")
    narhi = input(f"{nomi.title()} ning narhini kiriting: ")
    mahsulotlar[nomi] = narhi
    tekser = input("Boshqa malumot kirtasizmi? (ha/yo'q) ")
    if tekser != "ha":
        ishora = False
        
        
"""      
        

        
#3

mahsulotlar = ['olma', 'banan', 'olcha', "orik", 'qulpinay']


e_bozor = {
    'olma' : 12000,
    'olcha' : 14000,
    'shaftoli' : 20000,
    'banan' : 25000,
    'chiya' : 15000,
    "orik" : 16000
    }


while mahsulotlar:
    mahsulot = mahsulotlar.pop()
    if mahsulot in e_bozor.keys():
        print(f"{mahsulot.title()} ning narhi: {e_bozor[mahsulot]}")
    else:
        print(f"Bizda {mahsulot.title()} mahsuloti yo'q")

    





























