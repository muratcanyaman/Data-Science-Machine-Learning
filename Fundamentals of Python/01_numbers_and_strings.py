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
