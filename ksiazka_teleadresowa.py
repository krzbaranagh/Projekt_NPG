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


    def dodaj_kontakt(self, kontakt): # <--- tutaj było wcięcie zle zrobione
        self.kontakty.append(kontakt) # i tu tez chyba 
    
    def usun_kontakt(self, imie, nazwisko):
        for kontakt in self.kontakty:
            if kontakt.imie == imie and kontakt.nazwisko == nazwisko:
                self.kontakty.remove(kontakt)
                print("Kontakt usunięty pomyślnie.")
                return
        print("Nie znaleziono kontaktu o podanych danych.")

    def wypisz(self):
        print("Lista kontaktów: ")
        for kontakt in self.kontakty:
            naz = kontakt.nazwisko
            im = kontakt.imie
            em = kontakt.email
            tel = kontakt.telefon
    
            space1 = " "*(15 - len(naz))
            space2 = " "*(15 - len(im))
            space3 = " "*(30 - len(em))
            space4 = " "*(9 - len(tel))

            print("-> | Nazwisko: " + naz + space1 + " | Imie: " + im + space2 + " | Email: " + em + space3 +" | Telefon: " + tel + space4 + " |")
