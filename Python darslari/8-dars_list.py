
#1

mamlakatlar = ['AQSH', "Japoniya", "UC", "Koreya", "Singapure", "Mekke"]
print(mamlakatlar)



#2
"""
print(len(mamlakatlar))


#3

print(sorted(mamlakatlar))



#4

print(sorted(mamlakatlar, reverse=True))



#5

print(mamlakatlar)



#6

mamlakatlar.reverse()
print(mamlakatlar)
"""


#7

mamlakatlar.sort()
print(mamlakatlar)
mamlakatlar.sort(reverse=True)
print(mamlakatlar)


#8

juft_sonlar = list(range(120, 1200, 2))
print(juft_sonlar)


#9

print(sum(juft_sonlar))


#10

min = min(juft_sonlar)
max = max(juft_sonlar)
ayirma = max - min
print(ayirma)



#11

print("sonlar uzunligi: ", len(juft_sonlar))



#12

print("Royxatning boshi: ", juft_sonlar[:20])

print("Royxatning ortasi: ", juft_sonlar[(len(juft_sonlar)//2):((len(juft_sonlar)//2)+20)])

print("Royxatning oxiri: ", juft_sonlar[-20:])





#13

taomlar = []
taomlar.append("Manti")
taomlar.append("Palaw")
taomlar.append("Somsa")
taomlar.append("Bo'rek")
taomlar.insert(-1, "Et asiw")




#14

nonushta = taomlar[:]
del nonushta[0]
nonushta.remove("Palaw")
nonushta.append("Perashka")






#15


print(taomlar)
print(nonushta)



#16

nonushta = tuple(nonushta)
print(type(nonushta))
































