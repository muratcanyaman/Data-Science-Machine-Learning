# KARAR & KONTROL YAPILARI

#True - False Sorgulamalari

sinir = 5000

sinir == 4000

sinir == 5000

5 == 4

5 == 5

# if

sinir = 50000   
gelir = 35000

if gelir < sinir:
    print("Gelir sinirdan kucuk.")
    print(gelir*2)
    
if gelir > sinir:
    print("Gelir sinirdan buyuk.")
else:
    print("Gelir sinirdan buyuk olacak")    

#else

sinir = 70000   
gelir = 60000

if gelir > sinir:
    print("Gelir sinirdan buyuk.")
else:
    print("Gelir sinirdan kucuk ") 


#elif

sinir = 50000   
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000


if gelir1 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir1 < sinir:
    print("Uyari!")
else:
    print("Takibe devam ") 


if gelir3 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir3 < sinir:
    print("Uyari!")
else:
    print("Takibe devam ")
    

if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir2 < sinir:
    print("Uyari!")
else:
    print("Takibe devam ") 


#mini uygulama

sinir = 50000
magaza_adi = input("Magaza adi nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
    print("Tebrikler " + magaza_adi + " Promosyon kazandiniz!")
elif gelir < sinir:
    print("Uyarı! Cok dusuk gelir : " + str(gelir))
else:
    print("Takibe Devam")
