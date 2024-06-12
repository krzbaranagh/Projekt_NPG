import pickle
import os

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.telefon}, {self.email}"

class KsiazkaTeleadresowa:
    def __init__(self): 
        self.kontakty = []

    def data_save(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'data_contact.txt')
        with open(file_path, 'w') as plik:
            for kontakt in Ksiazka.kontakty:
                plik.write(f"{kontakt.imie} {kontakt.nazwisko} {kontakt.telefon} {kontakt.email}\n")

    def data_load(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'data_contact.txt')
        if os.path.exists(file_path):
                with open(file_path, 'r') as plik:
                    for linia in plik:
                        imie, nazwisko, telefon, email = linia.strip().split(' ')
                        kontakt = Kontakt(imie, nazwisko, telefon, email)
                        Ksiazka.kontakty.append(kontakt)
        else:
            self.kontakty = []

k1 = Kontakt("Tomek", "Jajko",  "543654564", "tomekjajko@gmail.com")
k2 = Kontakt("Jacek", "Placek", "769474839", "placekjacek@gmail.com")
k3 = Kontakt("Bogdan", "Doniek", "203633768", "DoniekB@gmail.com")
k4 = Kontakt("Maciej", "Wozny", "948793675", "KoloMaciejow@gmail.com")
k5 = Kontakt("Romek", "Szybki", "846593645", "romekszybki@gmail.com")

Ksiazka = KsiazkaTeleadresowa() #ten obiekt uzylem w wyswietlaniu kontaktow
Ksiazka.data_load()
