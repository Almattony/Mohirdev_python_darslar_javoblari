
#1
"""
ismlar = []
ismlar.append("Asad")
ismlar.append("Baxash")
ismlar.append("Aybat")

print(ismlar)
"""

#2

ismlar = []
ismlar.append("Asad")
ismlar.append("Baxash")
ismlar.append("Aybat")

print(f"""Salom {ismlar[0]}, bugun choyxona bormi?
{ismlar[1]}, choyxonaga boramizmi?
{ismlar[2]} san borasangmi?""")


#3
"""
sonlar = [12, 15, -50, 40.2, 100]
print(sonlar)


#4

print(f"{sonlar[0]} + {sonlar[1]}  = ", sonlar[0] + sonlar[1],"\n"
      f"{sonlar[2]} * {sonlar[3]} = ", sonlar[2] * sonlar[3], "\n"
      f"{sonlar[2]} / {sonlar[0]} = ", sonlar[2] / sonlar[0])

del sonlar[4]
print(sonlar)

sonlar.append(200)
print(sonlar)

sonlar.insert(4, 100)
print(sonlar)
"""


#5
"""
t_shaxslar = []
z_shaxslar = []

t_shaxslar.append("Albert Enshtein")
t_shaxslar.append("Nikolay Tesla")

z_shaxslar.append('Bill Gates')
z_shaxslar.append("Elon Mask")

print(t_shaxslar)
print(z_shaxslar)
"""

#6
"""
shaxs = t_shaxslar.pop(0)
shaxs2 = z_shaxslar.pop(1)

print("Men tarixiy shaxslardan ", shaxs, " bilan zamonaviy shaxslardan esa ", shaxs2, " bilan suhbat qilishni istar edim\n")
 
print(t_shaxslar, "\n")
print(z_shaxslar)
"""


#7

friends = []
friends.append("Nurg'azi")
friends.append("Berik")
friends.append("Ismag'ul")
friends.append("Asad")
friends.append("Janibek")

print(friends)

#8

friends.remove("Asad")
print(friends)
del friends[3]
print(friends)



#9

friends.insert(0, "Ruslan")
friends.insert(2, "Razzaq")
friends.insert(-1, "Erlan")
print(friends)


#10

yangi_mehmonlar = []
yangi_mehmonlar.append(friends.pop(1))
yangi_mehmonlar.append(friends.pop(-1))
yangi_mehmonlar.append(friends.pop(0))

print("Kelgan mehmonlar: ", yangi_mehmonlar)





















