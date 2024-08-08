

#1,2
"""
elon = {
    'ism' : 'elon',
    'famliliya' : 'musk',
    'tyil' : '1971',
    'tyer' : 'Pretoria, Transvaal, South Africa',
    'ochgan' : ['SpaceX', 'Tesla Inc', 'X (formerly Twitter)']
    }


bill = {
    'ism' : 'bill',
    'famliliya' : 'gates',
    'tyil' : '1955',
    'tyer' : 'Seattle, Washington, U.S',
    'ochgan' : ['Microsoft', 'IBM partnership', 'Windows']
    } 


albert = {
    'ism' : 'albert',
    'famliliya' : 'eintein',
    'tyil' : '1879',
    'tyer' : 'Ulm, Kingdom of Württemberg, German Empire',
    'ochgan' : ['On a Heuristic Viewpoint Concerning the Production and Transformation of Light', 'On the Motion of Small Particles Suspended in a Stationary Liquid, as Required by the Molecular Kinetic Theory of Heat']
    } 



thomas = {
    'ism' : 'thomas',
    'famliliya' : 'edison',
    'tyil' : '1847',
    'tyer' : 'Milan, Ohio, U.S.',
    'ochgan' : ['birinchi sperial lampa']
    }

taniqli_odamlar = [elon, bill, albert, thomas]


for odam in taniqli_odamlar:
    print(f"{odam['ism'].title()} familiyasi {odam['famliliya'].title()}, "
          f"tug'ilgan yili {odam['tyil']}, tug'ilgan yeri {odam['tyer']}, ",
          odam['ism'].title(), " ning hayoti davomida ochgan narsalari:", end=" ")
    for narsa in odam['ochgan']:
        print(narsa, end=" ")
    print("\n")
""" 
    
    
    
    
#3
"""
sevimli_kinolar = {
    'baqash' : ['Sevgi ortida', "Ko'z yoshlar qirolichasi", "Dokon yulduzi",],
    'sherlan' : ['Qog\'oz bino', "Halokat Patruli", "Chelbiylar"],
    'manas' : ["Temir odam", "O'rgimchak odam", "Chimoli odam"]
    }

for ism, kinolar in sevimli_kinolar.items():
    print(ism.title(), "ning sevimli kinolari quyidagicha: ", end='')
    for kino in kinolar:
        print(kino, end=', ')
    print("\n")
"""    
    
    
    
#4

davlatlar = {
    'aqsh' : {
        'poytaxt' : 'vashington',
        'viloyat soni' : "50 ta shtat turadi",
        'rasmiy tili' : "ingliz",
        'prezidenti' : 'joe biden',
        "maydoni" : "9 833 520 kvadrat km",
        "pul birligi" : "AQSh dollari"
        },
    
    "uzbekiston" : {
        'poytaxt' : 'tashkent',
        'viloyat soni' : 12,
        'rasmiy tili' : "uzbek",
        'prezidenti' : 'shavkat mirziyoyev',
        "maydoni" : "447,400 kvadrat km",
        "pul birligi" : "uzbek sum"
        },
    
    'kazakstan' : {
        'poytaxt' : 'nursultan',
        'viloyat soni' : 12,
        'rasmiy tili' : "kazak",
        'prezidenti' : 'kassym-jomart tokayev',
        "maydoni" : "2,724,900 kvadrat km",
        "pul birligi" : "tenge"
        }
    }



for davlat, info in davlatlar.items():
    if davlat.lower() == "aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
        
    poytaxt = info['poytaxt']
    viloyat = info["viloyat soni"]
    rasmiy_t = info["rasmiy tili"]
    prezident = info["prezidenti"]
    maydoni = info["maydoni"]
    pul_birligi = info["pul birligi"]
    
    
    #print(f"{davlat} davlatining poytaxti: {poytaxt.title()}, "
    #       f"rasmiy tili: {rasmiy_t.title()} tili, prezidenti: {prezident.title()}, "
    #       f"yer maydoni: {maydoni}, pul birligi: {pul_birligi.capitalize()} \n")






#5


kirtilgan = input("Bir davlat kiriting: ").lower()

malumot = davlatlar.get(kirtilgan)

if malumot == None:
    print("Bizda bu davlat haqida ma'lumot yo'q")
else:
    print(f"{kirtilgan.title()} ning poytaxti: {malumot['poytaxt'].title()}, "
          f"viloyat soni: {malumot['viloyat soni']}, tili: {malumot['rasmiy tili'].title()}, "
          f"prezidenti: {malumot['prezidenti'].title()}, yer maydoni: {malumot['maydoni']}, "
          f"pul birligi: {malumot['pul birligi']}")










