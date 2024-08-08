
from math import sqrt
import random as r

# =============================================================================
# lambda "nomsiz funksiya"
# 
# def daraja(n):
#     return lambda x: x**n
# 
# kvadrat = daraja(2)
# kub = daraja(3)
# 
# print(f"5 saninin' kvadrati {kvadrat(5)} ge ten'\n"
#       f"5 saninin' kubi {kub(5)} ge ten'")
# 
# 
# =============================================================================




#map() funksiyasi

# =============================================================================
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# 
# print(sonlar)
# print(ildizlar)
#  
# =============================================================================




# ============================================================================= 
#sonlar = list(range(11))
# 
# def daraja2(x):
#     return x*x
# 
# print(sonlar)
# print(list(map(daraja2, sonlar)))
# =============================================================================



# =============================================================================
# sonlar = list(range(11))
# kvadratlar = list(map(lambda x: x*x, sonlar))
# print(kvadratlar)
# 
# =============================================================================



# =============================================================================
# a = [5, 4 , 3 ,2]
# b = [1, 2, 3, 4]
# 
# a_plus_b= list(map(lambda x, y: x+y, a, b))
# 
# print(a_plus_b)
# =============================================================================


# =============================================================================
# ismlar = ['almat', 'asad', 'baxash', 'berik']
# print(list(map(lambda matn: matn.upper(), ismlar)))
# =============================================================================







#filter() funksiyasi

# =============================================================================
# sonlar = r.sample(range(100), 10)
# 
# def juftmi(x):
#     return x % 2  == 0
# 
# juft_sonlar = list(filter(juftmi, sonlar))
# 
# print(sonlar)
# print(juft_sonlar)
# 
# =============================================================================



# =============================================================================
# sonlar = r.sample(range(100), 10)
# 
# 
# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# 
# print(sonlar)
# print(juft_sonlar)
# =============================================================================




# =============================================================================
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'tarvuz', 'qovun', 'banan']
# 
# mevalar_b = list(filter(lambda meva: meva.startswith('b'), mevalar))
# 
# print(mevalar_b)
# =============================================================================


# =============================================================================
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'tarvuz', 'qovun', 'banan']
# 
# mevalar2 = list(filter(lambda meva: len(meva) <= 4, mevalar))
# 
# print(mevalar2)
# =============================================================================



# =============================================================================
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'tarvuz', 'qovun', 'banan']
# mevalar3 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
# 
# print(mevalar3)
# 
# =============================================================================

















