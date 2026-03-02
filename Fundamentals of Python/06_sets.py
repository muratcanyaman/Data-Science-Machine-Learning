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
