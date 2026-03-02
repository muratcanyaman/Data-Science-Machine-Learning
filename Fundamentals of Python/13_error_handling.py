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
