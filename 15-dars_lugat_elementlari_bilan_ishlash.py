

#1

sozlar = {
    'apple' : "o'lma",
    'banana' : 'banan',
    'car' : 'mashina',
    'home' : 'uy',
    'air' : 'havo',
    'fresh' : 'svejey',
    'morning' : "to'ng",
    'noon' : 'tush',
    'afternoon' : 'tushdan keyin',
    'airport' : 'ayroport'
    }

for k, v in sorted(sozlar.items()):
    print(f"{k.title()} : {v.capitalize()}")
    
    
    
    
    
    
#2
"""
davlatlar = {
    'usa' : "vashington",
    'uk' : 'london',
    'kazakstan' : 'nursultan',
    'uzbekiston' : 'tashkent',
    'kirgiziston' : 'beyshkek',
    'rossiya' : 'moskva',
    'braziliya' : 'braziliya',
    'yaponiya' : 'tokyo'
    }
print("Dunyo davlatlari:")
for davlat in sorted(davlatlar.keys()):
    if davlat == "usa":
        print(davlat.upper())
    elif davlat == "uk":
        print(davlat.upper())
    else:
        print(davlat.title())
    
print('\nDavlatlarning poytaxtlari')    
for davlat in sorted(davlatlar.values()):
    print(davlat.title())
"""  
    
    
    
    
    
    
#3

"""
davlat_input = input("Istalgan bir davlat kiriting: ").lower()

davlatlar = {
    'usa' : "vashington",
    'uk' : 'london',
    'kazakstan' : 'nursultan',
    'uzbekiston' : 'tashkent',
    'kirgiziston' : 'beyshkek',
    'rossiya' : 'moskva',
    'braziliya' : 'braziliya',
    'yaponiya' : 'tokyo'
    }

if davlat_input in davlatlar:
    print(davlatlar[davlat_input])
    
else:
    print("Bizda bunday malumot yo'q")
        

temp = davlatlar.get(davlat_input)

if temp == None:
    print("Kechirasiz bizda bunday malumot yo'q")
else:
    print(davlat_input.title(), "ning poytaxti ", temp.title())
"""




#4

menular = {
    'somsa' : 5000,
    'manti' : 10000,
    'palaw' : 10000,
    'shashlik' : 8000,
    'ayran' : 4000,
    'oliviye salat' : 15000,
    'tort' : 15000,
    'kompot' : 4000,
    'frukti salat' : 20000,
    'chay' : 4000
    }

zakazlar = []

for n in range(3):
    zakazlar.append(input(f"{n + 1} chi taomni kiriting: ").lower())
    
for zakaz in zakazlar:
    if zakaz in menular:
        print(f"Siz so'ragan {zakaz.title()} taominig narhi: {menular[zakaz]}")
    else:
        print("Bizda bunday ", zakaz, " taom yo'q")
        








