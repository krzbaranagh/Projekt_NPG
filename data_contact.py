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

    def __eq__(self, other):
        if isinstance(other, Kontakt):
            return (self.imie == other.imie and
                    self.nazwisko == other.nazwisko and
                    self.telefon == other.telefon and
                    self.email == other.email)
        return False
    
    def __hash__(self):
        return hash((self.imie, self.nazwisko, self.telefon, self.email))


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



Ksiazka = KsiazkaTeleadresowa() 
Ksiazka.data_load()
