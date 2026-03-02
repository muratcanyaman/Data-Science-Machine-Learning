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
