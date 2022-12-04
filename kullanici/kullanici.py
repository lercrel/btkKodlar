# input, tkinter veya doğrudan kodla alınan bilgiler ile Kullanici class'ında yeni obje
# oluşturulup json'a kaydedilir ve çekildiğinde pandas dataframei olarak ekrana yazdırılır.

from datetime import datetime
import pandas as pd
x = pd.DataFrame(
    {
        "Ad": ["John", "Jane"],
        "Soyad": ["Doe","Doe"],
        "Yaş": [10,20],
        "Doğum tarihi": [2022, 2010]
     })
class Kullanici:
    def __init__(self, ad, soyad, yas, dogumtarihi):
        print("Yeni kullanıcı başarıyla kaydedildi!")


