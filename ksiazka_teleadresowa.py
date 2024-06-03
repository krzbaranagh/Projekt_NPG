import pickle

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

class KsiazkaTeleadresowa:
    def __init__(self): #konstruktor klasy KsiazkaTeleadresowa #Tworzy listę pustą z późniejszą możliwością edycji
        self.kontakty = []


     def dodaj_kontakt(self, kontakt):
         self.kontakty.append(kontakt)
    
    def usun_kontakt(self, imie, nazwisko):
