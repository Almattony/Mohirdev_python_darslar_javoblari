
import datetime as dt
import re

# =============================================================================
# #1 Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani
# #  konsolga chiqaring
# 
# 
# bugun = dt.datetime.now()
# kecha = dt.date(2024, 8, 2)
# kecha = dt.date(2024, 8, 2)
# 
# 
# print(bugun.date())
# print(kecha)
# 
# =============================================================================


# =============================================================================
# 
# #3
# 
# tugilgan_kunim = dt.date(2000, 2, 21)
# bugun = dt.date.today()
# 
# yil = bugun.year - tugilgan_kunim.year
# oy = bugun.month - tugilgan_kunim.month
# kun = abs(bugun.day - tugilgan_kunim.day)
# 
# print(bugun)
# print(tugilgan_kunim)
# print(f"Bugun tug'ilgan kunimgacha chunsha vaqt o'tkan ekan {yil}, {oy}, {kun}")
# 
# =============================================================================



# =============================================================================
# #4
# 
# tel_kiriting = input("Telefon raqamingizni kiriting \n>>> ")
# 
# andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# 
# if re.match(andoza, tel_kiriting):
#     print("Sizning telefon raqamingiz qabul qilindi")
# else:
#     print("Siz noto'g'ri raqam kiritdingiz")
# 
# =============================================================================


#5

matn = "https://this-shouldn't.match@example.com"


andoza = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"

bet = re.findall(andoza, matn)

print(bet)


















