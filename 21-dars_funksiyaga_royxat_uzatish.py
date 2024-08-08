
#1
"""

def katta_harf_qil(matnlar):
    
    # while matnlar:
    #     matn = matnlar.pop()
    #     matnlar2.append(matn.title())
    
    for n in range(len(matnlar)):
        matnlar[n] = matnlar[n].title()
        
        




matn_royxatlar = ['asadtin\' qizig\'iwi ol mashindar',
                  'baqashtin\' qizig\'iwi ol moda kiyimder']

katta_harf_qil(matn_royxatlar)

print(matn_royxatlar)

"""




#2

"""
def katta_harf_qil(matnlar):
    
    # while matnlar:
    #     matn = matnlar.pop()
    #     matnlar2.append(matn.title())
    
    for n in range(len(matnlar)):
        matnlar[n] = matnlar[n].title()
    
    return matnlar
        




matn_royxatlar = ['asadtin\' qizig\'iwi ol mashindar',
                  'baqashtin\' qizig\'iwi ol moda kiyimder']

matnlar = katta_harf_qil(matn_royxatlar[:])
print(matnlar)
print(matn_royxatlar)

"""




#3

def bahola(ismlar):
    baholar = {}
    # i = 0
    # while i < len(ismlar):
    #     ism = ismlar[i]
    #     baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
    #     baholar[ism]=baho
    #     i+=1
    for ism in ismlar:
        baho = input(f"{ism.title()} ning bahosi: ")
        baholar[ism] = baho
    
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)




























