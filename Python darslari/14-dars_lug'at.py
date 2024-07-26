

#1

otam = {
    'ism' : 'maxset',
    'familiya' : 'doshmuratov',
    'yili' : 1960    
    }

onam = {
    'ism' : 'madina',
    'familiya' : 'sadiykova',
    'yili' : 1960    
    }

akam = {
    'ism' : 'danil',
    'familiya' : 'doshmuratov',
    'yili' : 1985    
    }

opam = {
    'ism' : 'lazzat',
    'familiya' : 'doshmuratov',
    'yili' : 1983    
    }


print(f"Otamning ismi {otam['ism']}, familiyasi esa {otam['familiya']}, tug'ilgan yili: {otam['yili']}")






#2

sevimli_taomlar = {
    "maxset" : 'manti',
    'madina' : 'kurtik',
    'danil' : 'palaw',
    'ayapa' : 'borek',
    'men' : 'somsa'
    }

print(f"Maxsettin' sevimli taomi {sevimli_taomlar['maxset']}")

print(f"Madinanin' sevimli taomi {sevimli_taomlar['madina']}")

print(f"Danildin' sevimli taomi {sevimli_taomlar['danil']}")






#3-4-5


sozlar = {
    'for' : 'cikl operatori',
    'if' : 'agar',
    'else' : 'boshqa xolda',
    'int' : 'butun son qabul qiladi',
    'float' : "o'nlik son qabul qiladi",
    'string' : 'matn qabul qiladi',
    'boolean' : 'logikalik operator',
    'list' : 'royxat',
    'tuple' : "o'zgarmas royxat"
    }



soz = input("Biror bir so'z kiriting: ").lower()

#print(sozlar.get(soz, "Bunday so'z mavjud emas"))



# if soz in sozlar:
#     print(f"{soz} bu so'znin tarjimasi {sozlar[soz]}")
# else:
#     print("Bunday so'z mavjud emas")


qiymat = sozlar.get(soz)

if qiymat == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"Siz kiritgan {soz} tarjimasi {qiymat}")






















