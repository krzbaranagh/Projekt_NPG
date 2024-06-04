import pickle
import customtkinter as ctk
from customtkinter import *


class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

class KsiazkaTeleadresowa:
    def __init__(self): #konstruktor klasy KsiazkaTeleadresowa #Tworzy listę pustą z późniejszą możliwością edycji
        self.kontakty = []





# Inicjalizacja aplikacji
app = ctk.CTk()

# Ustawienia okna
app.title("Phonebook")
app.geometry("800x600")

# Funkcje przycisków
def add_contact():
    print("Przycisk 1 został naciśnięty")

def display_contact():
    print("Przycisk 2 został naciśnięty")

def edit_contact():
    print("Przycisk 3 został naciśnięty")

def delete_contact():
    print("Przycisk 4 został naciśnięty")

# Tworzenie przycisków
button1 = ctk.CTkButton(master=app, text="Przycisk 1", command=add_contact, width=150, height=50)
button1.pack(pady=10)

button2 = ctk.CTkButton(master=app, text="Przycisk 2", command=display_contact)
button2.pack(pady=10)

button3 = ctk.CTkButton(master=app, text="Przycisk 3", command=edit_contact)
button3.pack(pady=10)

button4 = ctk.CTkButton(master=app, text="Przycisk 4", command=delete_contact)
button4.pack(pady=10)

# Uruchomienie aplikacji
app.mainloop()