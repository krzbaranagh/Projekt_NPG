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
        for kontakt in self.kontakty:
            if kontakt.imie == imie and kontakt.nazwisko == nazwisko:
                self.kontakty.remove(kontakt)
                print("Kontakt usunięty pomyślnie.")
                return
        print("Nie znaleziono kontaktu o podanych danych.")

    def funkcja_wyszukaj_kontakt(self, imie, nazwisko) -> None:
        for kontakt in self.kontakty:
            if kontakt.imie == imie and kontakt.nazwisko == nazwisko:
                print(f"Imię i Nazwisko: {kontakt.imie} {kontakt.nazwisko}")
                print(f"Telefon: {kontakt.telefon}")
                print(f"Email: {kontakt.email}")    #robimy type hinting czy nie?
                return None
            else:
                print("Znie znalezniono dopasowania.")
                return None
