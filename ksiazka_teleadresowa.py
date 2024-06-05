import pickle

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
if imie=0:
print "imie =0"
class KsiazkaTeleadresowa:
    def __init__(self):
        self.kontakty = []
def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(self.kontakty, plik)
        print("Kontakty zostały zapisane do pliku.")
 def wczytaj_z_pliku(self, nazwa_pliku):
        try:
            with open(nazwa_pliku, 'rb') as plik:
                self.kontakty = pickle.load(plik)
            print("Kontakty zostały wczytane z pliku.")
        except FileNotFoundError:
            print("Plik nie istnieje.")
