# =============================================================================
# 
# def avto_info_ber(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto_info = {
#         "kompaniya" : kompaniya,
#         'model' : model,
#         'rangi' : rangi,
#         'korobka' : korobka,
#         'yili' : yili,
#         'narhi' : narhi
#     }
#        
#     return avto_info
# 
# 
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='\n')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
# 
#     avtolar.append(avto_info_ber(kompaniya, model, rangi, korobka, yili, narhi))
# 
# 
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
#     
#     
# print("Salonimizdagi avtolar: \n")
# 
# for avto in avtolar:
#     if avto['narhi']:
#         narhi = avto['narhi']
#     else:
#         narhi = 'Nomalum'
#     print(f"{avto['rangi'].title()} {avto['model'].title()}, {avto['korobka']} korobka. Narhi: {narhi}")
# 
# =============================================================================





#1-2


# def lugat_tuz(ism, familya, t_yil, t_joy, e_mail = '', telefon = None):
#     """ Lug'at qilib tuzib beradigan funksiya """
#     malumotlari = {
#         'ismi' : ism,
#         'familya' : familya,
#         'yoshi' : 2024 - t_yil,
#         't_yili' : t_yil,
#         't_joyi' : t_joy,
#         'e-mail' : e_mail,
#         'telefoni' : telefon
#         }
#     return malumotlari

    

# print("Assalomu alykum! Bir qator malumotlaringizni kiritib o'tsangiz")

# malumotlar = []
# while True:
#     ism = input("Ismingizni kiriting: ")
#     familya = input("Familyangizni kiriting: ")
#     t_yil = input("Tug'ilgan yilingizni kiriting: ")
#     t_joy = input("Tug'ilgan joyingizni kiriting: ")
#     e_mail = input("E-mail manzilingizni kiriting: ")
#     telefon =input("Telefon raqamingizni kiriting: ")
    
#     malumotlar.append(lugat_tuz(ism, familya, t_yil, t_joy, e_mail, telefon))
    
#     javob = input("Yana malumotlar kiritasizmi? (yes/no) ")
#     if javob == "no":
#         break
    


# print("Malumotlar quydagicha:")

# for malumot in malumotlar:
    
#     if malumot['telefoni']:
#         telefon = malumot['telefoni']
#     else:
#         telefon = "Nomalum"
        
#     if malumot['e-mail']:
#         e_maili = malumot['e-mail']
#     else:
#         e_maili = "Nomalum"
    
#     print(f"{malumot['ismi'].title()} {malumot['familya'].title()},"
#           f" yoshi: {malumot['yoshi']}, tug'ilgan yili: {malumot['t_yili']} ,"
#           f"tug'ilgan joyi: {malumot['t_joyi'].title()}, e-maili: {e_maili}"
#           f" telefoni: {telefon}")
  
    
    


#3



# =============================================================================
# def kattasin_qaytar(son1, son2, son3):
#     """ Sonlarning eng kattasini beruvchi funksiya """
#     
#     katta_son = 0
#     
#     if son1 > son2:
#         katta_son = son1
#     if son3 > katta_son:
#         katta_son = son3
#     if son2 > katta_son:
#         katta_son = son2
#     
#             
#     return katta_son
# 
# 
# 
# print("Uchta son kiriting:")
# 
# son1 = float(input("1-chi son: "))
# son2 = float(input("2-chi son: "))
# son3 = float(input("3-chi son: "))
# 
# son = kattasin_qaytar(son1, son2, son3)
# 
# print(son)
# 
# =============================================================================



#4
"""
def aylana_radiusini_xisobla(r, pi = 3.14159):
    
    diametr = r * 2
    uzunlig = 2 * r * pi
    yuz = pi * (r ** 2)
    
    aylana_info = {
        'radiusi' : r,
        'diametri' : diametr,
        "uzunligi" : uzunlig,
        'yuzi' : yuz
        }
    
    return aylana_info





info = aylana_radiusini_xisobla(5)

print(f"Radiusi: {info['radiusi']} \n"
      f"diametri: {info['diametri']} \n"
      f"uzunligi: {info['uzunligi']} \n"
      f"yuzi: {info['yuzi']}")






#5

def tup_sonlar_tuz(min, max):
            
    sonlar = list(range(min,max+1))
    tub_sonlar = []
    
    for son in sonlar:
        i = 0
        if son == 1:
            continue
        
        for n in range(2, son):
            if son == 2:
                tub_sonlar.append(son)
            elif son % n == 0:
                i += 1
            
            
        
        if i == 0:
            tub_sonlar.append(son)
            
    return tub_sonlar


print(tup_sonlar_tuz(1, 10))

"""





#6,1

"""
son = 55
sonlar = []
fibonachchi_sonlar = []

for n in range(1, son+1):
    sonlar.append(n)\


i = 0
a = 1
while i < son:
    if sonlar[i] == 1:
        fibonachchi_sonlar.append(sonlar[i])
    if sonlar[i] + 1 == 2:
        fibonachchi_sonlar.append(sonlar[i])
    elif sonlar[i] == (fibonachchi_sonlar[a-1] + fibonachchi_sonlar[a]):
        fibonachchi_sonlar.append(sonlar[i])
        a+=1
        
    i+=1
    
        
print(fibonachchi_sonlar)

"""


#6,2

def f_sonlar_tuz(son):
    
    fibo_sonlar = [] # 1,1/ 1,1,2/ 1,1,2,3
    for n in range(son):
        if n == 0 or n == 1:
            fibo_sonlar.append(1)
        else:
            fibo_sonlar.append(fibo_sonlar[n-1] + fibo_sonlar[n-2])
    
    return fibo_sonlar







print(f_sonlar_tuz(10))





        
    



















