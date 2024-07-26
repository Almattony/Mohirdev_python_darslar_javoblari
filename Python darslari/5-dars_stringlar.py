#1
"""
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyat")
"""

#2
"""
kocha = input("ko'changizni kiriting : ")
mahalla = input("mahalangizni kiriting : ")
tuman = input("tumaningizni kiriting : ")
viloyat = input("viloyatingizni kiriting : ")

print(f"{kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallasi, {tuman.capitalize()} tumani, {viloyat.capitalize()} viloyat")
"""

#3
"""
kocha = input("ko'changizni kiriting : ")
mahalla = input("mahalangizni kiriting : ")
tuman = input("tumaningizni kiriting : ")
viloyat = input("viloyatingizni kiriting : ")

print(f"{kocha.capitalize()} ko'chasi,\n{mahalla.capitalize()} mahallasi,\n{tuman.capitalize()} tumani,\n{viloyat.capitalize()} viloyat")
"""

#4

kocha = input("ko'changizni kiriting : ")
mahalla = input("mahalangizni kiriting : ")
tuman = input("tumaningizni kiriting : ")
viloyat = input("viloyatingizni kiriting : ")
manzil = f"{kocha.capitalize()} ko'chasi,\n{mahalla.title()} mahallasi,\n{tuman.lower()} tumani,\n{viloyat.upper()} viloyat"

print(manzil)