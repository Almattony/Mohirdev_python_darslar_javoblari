


#1

# =============================================================================
# # yosh = input("Yoshingizni kiriting: ")
# # yosh = int(yosh)
# # print(f"Siz {2024-yosh} yilda tug'ilgansiz")
# 
# # Yoshingizni kiriting: 36.5
# # ValueError: invalid literal for int() with base 10: '36.5'
# 
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritishingiz kerak")
# else:
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")
# 
# 
# =============================================================================





# =============================================================================
# #2 ValueError
# 
# yosh = input("Yoshingizni kiriting: ")
# 
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")
# 
# =============================================================================





# =============================================================================
# #3 ZeroDivisionError
# 
# x, y = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
#     
# =============================================================================



# =============================================================================
# #4 IndexError
# mevalar = ['olma','anor','anjir','uzum']
# 
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Royxatda {len(mevalar)} ta meva bor xolos")
# 
# =============================================================================




# =============================================================================
# #5 KeyError
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}
# 
# key = "tel"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")
# 
# =============================================================================



# =============================================================================
# #6 FileNotFoundError
# 
# filename = "data.txt"
# try:    
#     with open(filename) as f:
#         text = f.read()
# except:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Boshqa fayl tanlang.")
# 
# 
# =============================================================================


# =============================================================================
# 
# #7 BIR NECHTA XATOLARNI USHLASH
# 
# n = input("Butun son kiriting: ")
# 
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f" x = {x}")
# 
# =============================================================================




# =============================================================================
# #8 XATOLARNI KO'RSATMAY O'TISH
# 
# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])
#         # fayl ustida turli amallar 
# 
# 
# # Pass hech qanday malumot bermasdan keyingi amalga otkazib yuborish
# 
# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         pass
#     else:
#         print(talaba['ism'])
#     
# =============================================================================




#9 XATOLARNING OLDINI OLISH

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
print(f"Siz {2024-yosh} yilda tug'ilgansiz")











