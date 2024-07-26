

#1
"""
savol = "Yaxshi korgan kitoblaringizni kiriting: "
savol += "(dasturni toxtatish uchun 'stop' ni yozing) "

flag = ''

while flag != "stop":
    flag = input(savol)
"""    


    
#2 flag usuli
"""
savol = "Yoshingiz nechida? "
savol += "(dasturni toxtatish uchun 'exit' yoki 'quit' deb yozing) "

flag = True


while flag:
    qiymat = input(savol)
    qiymat = str(qiymat)
    
    if qiymat == 'exit' or qiymat == 'quit':
        flag = False
    else:
        qiymat = int(qiymat)
        if qiymat <= 7:
            print('Chipta narhi 2000')
        elif 7 <= qiymat <= 18:
            print('Chipta narhi 3000')
        elif 18 <= qiymat <= 65:
            print('Chipta narhi 10000')
        else:
            print('Chipta narhi bepul')
"""    
    
    


#3 shart tekshirish ululi

"""
savol = "Yoshingiz nechida? "
savol += "(dasturni toxtatish uchun 'exit' yoki 'quit' deb yozing) "

qiymat = ''

while qiymat != 'exit' and qiymat != 'quit':
    
    qiymat = input(savol)
    
    
    if qiymat != 'exit' and qiymat != 'quit':
        qiymat = int(qiymat)
        
        if qiymat <= 7:
            print('Chipta narhi 2000')
        elif 7 <= qiymat <= 18:
            print('Chipta narhi 3000')
        elif 18 <= qiymat <= 65:
            print('Chipta narhi 10000')
        else:
            print('Chipta narhi bepul')

"""   




#4   break usuli bilan toxtatish
"""
savol = "Yoshingizni kiriting: "
savol += "(dasturni toxtatish uchun 'exit' yoki 'quit' ni yozing) >>> "

qiymat = ''

while True:
    
    qiymat = input(savol)
    
    if qiymat == 'exit' or qiymat == 'quit':
        break
    else:
        qiymat = int(qiymat)
         
        if qiymat <= 7:
            print('Chipta narhi 2000')
        elif 7 <= qiymat <= 18:
            print('Chipta narhi 3000')
        elif 18 <= qiymat <= 65:
            print('Chipta narhi 10000')
        else:
            print('Chipta narhi bepul')

"""


#5

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if str(qiymat) == 'exit':
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
        














        









