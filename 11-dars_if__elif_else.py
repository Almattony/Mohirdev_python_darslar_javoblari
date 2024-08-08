

# #1

# juf_son = int(input("Juft son kiriting: "))

# if juf_son % 2 == 0:
#     print('Raxmat')
# elif juf_son% 2 == 1:
#     print("Bu son juft emas")
    
    
    
# #2

# yosh = int(input("Yoshingiz nechida? >>>"))
# summa = 0

# if yosh < 4 or yosh > 60:
#     print("Kirish bepul")
# elif yosh < 18:
#     summa += 10000
# elif yosh > 18:
#     summa += 20000

# if summa > 0:    
#     print("Sizga shuncha narh: ", summa)





#3
"""
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ekinchi sonni kiriting: "))

if son1 == son2:
    print("sonlar teng", son1, "=", son2)
elif son1 > son2:
    print("Birinchi son ekinchi sonnan katta ", son1, ">", son2)
else:
    print("Ekinchi son birinchi sonna katta ", son2, ">", son1)
 """   



#4, 5

# =============================================================================
# mahsulotlar = ['olma', 'banan', 'klubnika', 'pomidor', 'sabiz', 'olcha', 'onar', 'shaftoli', 'uzum', 'non']
# savat = []
# yangi_mahsulotlar = []
# yoq_mahsulotlar = []
# 
# for n in range(5):
#     savat.append(input(f"{n + 1} chi mahsulotni kiriting: "))
# 
# for narsa in savat:
#     if narsa in mahsulotlar:
#         yangi_mahsulotlar.append(narsa)
#     else:
#         yoq_mahsulotlar.append(narsa)
#        
# if yoq_mahsulotlar:
#     print("Quyidagi mahsulotlar do'konimizda yo'q: ", yoq_mahsulotlar)
# else:
#     print("Siz soragan mahsulatlarinig barchasi bor")
#     
# =============================================================================
        

        
  
#6
"""
foydalanuvchilar = []

for n in range(5):
    foydalanuvchilar.append(input(f"{n + 1} chi login kiriting: "))

foydalanuvchi = input("Yangi login kiriting: ")

if foydalanuvchi in foydalanuvchilar:
    print("Login band, yangi login tanlang!")

else:
    print("Xush kelibsiz!", foydalanuvchi)
"""    
    
    

#7

son = int(input("Biror bir butun son kiriting: "))



for n in range(2, 11):
    if son % n == 0:
        print(son, " bu ", n, " soniga qoldiqsiz bo'linadi")
    










