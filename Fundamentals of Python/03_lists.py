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
