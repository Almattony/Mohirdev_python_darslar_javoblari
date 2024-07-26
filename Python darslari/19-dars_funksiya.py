

#1
"""
def yoshni_hisobla():
    ism = input("Ismingiz nima: ")
    t_yil = input("Yilingizni kiriting: ")
    
    print(ism.title(), "sizning yoshingiz : ", 2024-int(t_yil))
    
    
yoshni_hisobla()
"""



#2
"""
def matematik_amal_bajar(son):
    print(son, "ning kvadrati: ", son**2, "\n"
          "kubi esa: ", son**3)

matematik_amal_bajar(-2)
"""




#3
"""
def juft_toq_aniqla(son):
    if son % 2 == 0:
        print("Son juft ekan")
    else:
        print("Son toq ekan")
        
        
        
juft_toq_aniqla(1118)
juft_toq_aniqla(1111)
"""


#4
"""
def kattasi(son1, son2):
    if son1 > son2:
        print(son1, " > ", son2," da kattasi ekan") 
    elif son1 < son2:
        print(son2," > ", son1, " da soni katta ekan")
    else:
        print(son1, " = ", son2, "ekan")

kattasi(5, 10)
kattasi(500, 100)
kattasi(100, 100)
kattasi(500, 10*100)
kattasi(-500, 100)

"""



#5-6

"""
def darajaga_kotarish(x, y=2):
    
    print(x, " ning ", y, " darajasi: ", x**y)
    
    

darajaga_kotarish(2)
darajaga_kotarish(2, 3)
darajaga_kotarish(2, -1)
"""


#7

def qoldiqsiz_bolinishlar(x):
    
    for son in range(2, 11):
        if not x % son:
            print(f"{x} {son} ga qoldiqsiz bo'linadi")


qoldiqsiz_bolinishlar(50)
qoldiqsiz_bolinishlar(-100)
qoldiqsiz_bolinishlar(55)    
qoldiqsiz_bolinishlar(37)
    






















