



#1

def sonlar_kopaytmasi(*sonlar):
    kopaytma_yigindisi = 1
    for son in sonlar:
        kopaytma_yigindisi *= son
    return kopaytma_yigindisi



print(sonlar_kopaytmasi(1,2,3,4,5))



#2

def talaba_info(ism, familya, **s_malumotlar):
    
    s_malumotlar['ism'] = ism.title()
    s_malumotlar["familya"] = familya.title()
    
    return s_malumotlar



print(talaba_info('almat', 'kabakbaev', yili = 2000, malumoti = 'oliy'))


























