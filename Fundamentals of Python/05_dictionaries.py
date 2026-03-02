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
