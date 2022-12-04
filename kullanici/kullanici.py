# input, tkinter veya doğrudan kodla alınan bilgiler ile Kullanici class'ında yeni obje
# oluşturulup json'a kaydedilir ve çekildiğinde pandas dataframei olarak ekrana yazdırılır.
"""
from datetime import datetime
import pandas as pd

x = pd.DataFrame(
    {
        "Ad": ["John", "Jane"],
        "Soyad": ["Doe","Doe"],
        "Yaş": [10,20],
        "Doğum tarihi": [2022, 2010]
     })
"""


class User:
    def __init__(self, ad):
        self.ad = ad
    def init(self, dogumtarihi, sifre, kadi=None, tad=None, soyad=None):
        self.dogumtarihi = dogumtarihi
        self.sifre = sifre
        self.kadi = self.ad if kadi is None else kadi
        self.tad = self.ad if tad is None else tad
        self.soyad = self.ad if soyad is None else soyad
        print(f"Created user {self.ad}")
    def signin(self, sifre):
        if sifre == self.sifre:
            print(f"Authenticated for {self.ad}")
        def createproject(name):
            print("hey")
            

#ad = input
#dogumtarihi = input()


