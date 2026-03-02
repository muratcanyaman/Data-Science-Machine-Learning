# SAYILAR VE STRINGLERE GIRIS
9
9.2
9+9
9*9

print('HELLO AI ERA')
"HELLO AI ERA"

type(9)
type(9.2)
type("HELLO AI ERA")

# STRINGLERE YAKINDAN BAKALIM

""
''

123
type(123)
"123"
type("123")

"a" + "b"
"a" " b"
"a" + "-b"

# "a" - "b"  # Hatalı, çıkarıldı

"a "*3
# "a"/3  # Hatalı, çıkarıldı

#STRING METOTLARI - len

gel_yaz = "gelecegi_yazanlar"
#del mvk
a = 9
b = 10

a*b

len(gel_yaz)
len("gelecegi_yazanlar")

#STRING METOTLARI - upper() & lower()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()

B.islower()
B.isupper()

#STRING METOTLARI - replace()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.replace("e", "a")
gel_yaz.replace("a", "i")

#STRING METOTLARI - strip()

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip()

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")

gel_yaz = "lgelecegi_yazanlarl"
gel_yaz.strip("l")

#METOTLARA GENEL BAKIS

gel_yaz = "gelecegi_yazanlar"

dir(gel_yaz)

gel_yaz.capitalize()
gel_yaz.title()

#SUBSTRINGLER

gel_yaz = "gelecegi_yazanlar"

gel_yaz[1]
# gel_yaz[20]  # Hatalı, çıkarıldı

gel_yaz[0:3]
gel_yaz[3:7]

#DEGISKENLER

a = 9
b = "ali_uzaya_git"
c = a*2
c

a/c
a*c
a*5

type(100)
type(100.2)
type(1+2j)

a = 100.2

#TIP_DONUSUMLERI

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki)

int(11.0)

12

float(12)

type(str(12))

#print()

print("HELLO AI ERA")

print("gelecegi", "yazanlar", sep = "-")

#VERI YAPILARI

#Listeler

# []
#list()

notlar = [90, 80, 70, 60, 50]
print(notlar)
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a", 19.3, 90, notlar]

print(list_genis)

len(list_genis)

list_genis[0]
list_genis[1]
list_genis[3]

type(list_genis[0])
type(list_genis[1])
type(list_genis[3])

tum_liste = [liste,list_genis]
print(tum_liste)

#del tum_liste

#Listeler - Eleman Islemleri

liste = [10,20,30,40,50]

liste[0]
liste[1]
# liste[6]  # Hatalı, çıkarıldı

liste[0:2]
liste[:2]
liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste

yeni_liste[2]
yeni_liste[0:2]
yeni_liste[2][1]

#Listeler - Eleman Degistirme

liste = ["ali", "veli", "berkcan","ayse"]
liste

liste[1] = "velinin_babasi"
liste

liste[0:3] = "alinin_babasi","velinin_babasi","berkcanin_babasi"
liste

liste = ["ali", "veli", "berkcan","ayse"]

liste = liste + ["kemal"]
liste

#del liste[2]
liste

#Listeler - Liste Metodları

liste = ["ali","veli","isik"]
dir(liste)

liste

#append & remove - listenin sonuna eleman ekler / listeden eleman siler

liste.append("berkcan")
liste

liste.remove("berkcan")
liste

#insert - index'e göre listeye eleman ekleyen metod.

liste = ["ali","veli","isik"]

liste
liste.insert(0,"ayse")
liste

liste.insert(2,"Mehmet")
liste

liste.insert(5,"berk")
liste

liste.insert(len(liste),"murat")
liste

#pop - index'e göre listeden eleman siler.

liste.pop(0)
liste
liste.pop(4)
liste

#count - listedeki herhangi bir eleman sayısını dönderir

liste = ["ali","veli","isik","ali","veli"]
liste.count("ali")
liste.count("veli")
liste.count("isik")

#copy - mevcut listenin ilk halini yedekler

liste_yedek = liste.copy()
liste_yedek

#extend - listeleri birleştirir

liste.extend(["a","b",10])
liste

#index - herhangi bir liste elemanının index bilgisini döndürür.

liste.index("ali")

#reverse - liste elemanlarını ters çevirir.
liste.reverse()
liste

#sort -  sıralama için kullanılan metod.Aslında bu metodu başka dillerde yazmak nispeten zordur.Keza sort metodu bildiğimiz sıralama algoritması ile çalışır.

liste = [10,40,5,90]
liste.sort()
liste

#clear - listeyi temizler

liste.clear()
liste

#Veri Yapıları - Tuple

#Tuple oluşturma

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t

t = "ali","veli",1,2,3.2,[1,2,3,4]
t

#tuple()

t = ("eleman",)
type(t)

#Tuple Eleman Islemleri

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t

t[1]
t[0:3]
# t[2] = 99  # Hatalı, çıkarıldı

#Veri Yapıları - Dictionary(Sözlük)

#Sozluk Oluşturma

sozluk = {"REG" : "Regresyon Modeli",
    "LOJ" : "Lojistik Regresyob",
    "CART" : "Classification and REG"}
sozluk
len(sozluk)

sozluk = {"REG" : 10,
    "LOJ" : 20,
    "CART" : 30}
sozluk

sozluk = {"REG" : ["RMSE",10,],
    "LOJ" : ["MSE",20,],
    "CART" : ["SSE",30]}
sozluk
len(sozluk)

#Sozluk Eleman Islemleri

sozluk = {"REG" : "Regresyon Modeli",
    "LOJ" : "Lojistik Regresyon",
    "CART" : "Classification and REG"}

sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG" : {"RMSE" :10,
            "MSE" : 20,
            "SSE" : 30,
            },

    "LOJ" : {"RMSE" :10,
            "MSE" : 20,
            "SSE" : 30,
            },

    "CART" : {"RMSE" :10,
            "MSE" : 20,
            "SSE" : 30,
            }}

sozluk["REG"]
sozluk
sozluk["REG"]["SSE"]

#Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG" : "Regresyon Modeli",
    "LOJ" : "Lojistik Regresyon",
    "CART" : "Classification and REG"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Çoklu Doğrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"
sozluk

l = [1]
l

# sozluk[l] = "yeni bir sey"  # Hatalı, çıkarıldı

t = (tuple,)
t

sozluk[t] = "yeni bir sey"
sozluk

#Veri Yapıları - Setler

#Set Olusturmak

s = set()
s

l = [1,"a","ali",123]
s = set(l)
s

t = ("a","ali")
s = set(t)
s

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s

l = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
l

s = set(l)
s

len(s)

l[0]
# s[0]  # Hatalı, çıkarıldı

#Eleman ekleme & cikarma

l = ["gelecegi", "yazanlar"]
s = set(l)
s

dir(s)

s.add("ile")
s

s.add("gelecege_git")
s

s.add("ile")
s

s.remove("ile")
s

s.add("ali")
s

s.remove("ali")
s

s.discard("ali")
s

#Setler - Klasik Kume Islemleri

""" # difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symetric_difference() ikisinde de olmayanlari. """

#difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1

#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2
kesisim

set1.union(set2)
set2.union(set1)

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1

#Set Sorgu Islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kümenin kesisiminin bos olup
#olmadiginin sorgulanmasi

set1.isdisjoint(set2)

#bir kumenin butun elemanlarinin baska bir kume
#icerisinde yer alip almadigi

set1.issubset(set2)

# bir kumenin diger kumeyi kapsayip kapsamadigi

set1.issuperset(set2)
set2.issuperset(set1)

liste = ["a","b","c"]
liste.extend(liste)
liste

#FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI

print("a","b",sep = "_")
print()

#Matematiksel Islemler
4*4
4/4
5-1
6+3
3**2

#Fonksiyon Nasil Yazilir?

def kare_al(x):
    print(x**2)

kare_al(5)

#Bilgi Notuyla Cikti Uretmek

def kare_al(x):
    print("Girilen Sayinin karesi: " + str(x**2) )

kare_al(5)

def kare_al(x):
    print("Girilen Sayi : "
    + str(x) +
    "," +
    "Girilen Sayinin Karesi : "
    + str(x**2) )

kare_al(5)

#Iki Argumanli Fonksiyon Tanımlamak

def kare_al(x):
    print(x**2)

def carpma_yap(x, y):
    print(x * y)

#On Tanimli Argumanlar

def carpma_yap(x, y = 1):
    print(x * y)

carpma_yap(3, 4)

print("HELLO AI ERA")

#Argumanlarin Sıralanmasi

def carpma_yap(x, y = 1):
    print(x * y)

carpma_yap(y = 2, x = 3)

# Ne Zaman Fonksiyon Yazilir?

#isi, nem, sarj

def direk_hesap(isi, nem, sarj):
    print((isi + nem) / sarj)

direk_hesap(25, 40, 70)

#Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi, nem, sarj):
    return (isi + nem) / sarj

cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)

direk_hesap(25,40,90) *9

#Local ve Global Degiskenler

#x = 10
#y = 20

def carpma_yap(x = 2, y = 1):
    return x*y

carpma_yap(2,3)

# Local Etki Alanindan Global Etki Alanini Degistirmek

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi.")

eleman_ekle(1)
x
eleman_ekle(10)
x
eleman_ekle("ali")
x

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
    
#NESNE YONELIMLI PROGRAMLAMA

#Sinif Nedir?


     

#Sinif Ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
#Siniflarin ozelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

#siniflarin ozelliklerini degistirmek
VeriBilimci.sql = "Hayir"
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql

veli.bildigi_diller

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller
ali.bolum

VeriBilimci.bolum
ali.bolum = "istatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum

#Ornek Metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)


ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

#Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
#veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
#mar1.


class Employee_yeni():
    def __init__(self, FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = Employee_yeni("a","b","c")
ali.FirstName




#Python'da Fonksiyonel Programlama

#Fonksiyonlar dilin bastacidir. 
#(Birinci sinif nesnelerdir)
#Yan etkisiz fonksiyonlar. (stateless, girdi-cikti)
#Yuksek seviye fonksiyonlar.
#Vektorel operasyonlar.


#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1:Bagimsizlik

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b


impure_sum(6)
pure_sum(3,4)

#Ornek2: Olumcul yan etkiler
#OOP
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
    
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)


lc = LineCounter('deneme.txt') 

print(lc.lines)
print(lc.count())

lc.read()
lc.count()

#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count


#Isimsiz Fonksiyonlar

def old_sum(a,b):
    return a + b

old_sum(4,5)


new_sum = lambda a,b : a + b
new_sum(4,6)


sirasiz_liste = [('b', 3), ('a', 8), ('d', 12), ('c', 1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x : x[1])


#Vektorel Operasyonlar
#OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0 , len(a))

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab

#FP

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b 


#Onemli !!! map & filter & reduce

liste = [1,2,3,4,5]


for i in liste:
    print(i + 10)

# map                                  
list(map(lambda x : x + 10, liste)) # verilen bir vektorun icerisinde belirli bir fonksiyonun
                                    # calismasina imkan verir.

#filter
liste = [1,2,3,4,5,6,7,8,9,10] 


list(filter(lambda x : x % 2 == 0, liste)) # burada kosul var dikkat et.

#reduce - indirgeme
from functools import reduce

liste = [1,2,3,4]

reduce(lambda a,b : a + b, liste)


#modul olusturmak
#belirli görevleri yerine getirmek icin olusturulan,birtakim fonksiyonlar barindiran yapilardir.


import modul
modul.kare_al(25)

import modul as m
m.kare_al(5)

from modul import topla
topla(45,30)


m.maaslar

#Hatalar / Istisnalar (exceptions)
#Programcı Hatalari
#Program Hatalari (bug)

#ZeroDivisionError hatasi
a = 10
b = 0

a/b 


try:
    print(a/b)
except ZeroDivisionError:
    print("Paydada sifir olmaz.")
    

#tip hatasi

a = 10
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayi ve string problemi.")
    

liste = [1,2,3,4]

A = []

for i in liste:
    A.append(i**2)
    
print(A)


list(map(lambda x : x**2, liste))


def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")
 
yap(1,2,0)

x = 1
y = 2
z = 0

x/y*z














