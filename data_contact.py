class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

class KsiazkaTeleadresowa:
    def __init__(self): 
        self.kontakty = []

    def dodaj_kontakt(self, kontakt):
        self.kontakty.append(kontakt)



k1 = Kontakt("Tomek", "Jajko",  "543654564", "tomekjajko@gmail.com")
k2 = Kontakt("Jacek", "Placek", "769474839", "placekjacek@gmail.com")
k3 = Kontakt("Bogdan", "Doniek", "203633768", "DoniekB@gmail.com")
k4 = Kontakt("Maciej", "Wozny", "948793675", "KoloMaciejow@gmail.com")
k5 = Kontakt("Romek", "Szybki", "846593645", "romekszybki@gmail.com")




Ksiazka = KsiazkaTeleadresowa() #ten obiekt uzylem w wyswietlaniu kontaktow
Ksiazka.kontakty = [k1, k2, k3, k4]

Ksiazka.dodaj_kontakt(k5)
