#DONGULER - for

ogrenci = ["ali","veli","isik","berk"]
ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci:
    print(i)
    

# for - devam

maaslar = [1000,2000,3000,4000,5000]
maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]


for maas in maaslar:
    print(maas)

# dongu ve fonksiyonları birlikte kullanmak


def kare_al(x):
    print(x**2)
    
kare_al(5)

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
    

# maaslara yuzde 20 zam yapilacak gerekli kodlari
#yaziniz.


#dongu yazilacak
#fonksiyon yazilacak

def yeni_maas(x):
    print((x*20)/100 + x)
    

for i in maaslar:
    yeni_maas(i)

#mini uygulama
#if, for ve fonksiyonları birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print((x*10)/100 +x)

def maas_alt(x):
    print((x*20)/100 +x)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)

# break & continue

maaslar = [8000, 5000, 2000, 1000, 3000, 7000, 1000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
    

for i in maaslar:
    if i == 3000:
        continue
    print(i)
    

#while

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)
