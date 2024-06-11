import pickle
import os
import customtkinter as ctk
from customtkinter import *

import data_contact

def load_contacts_from_txt(ksiazka):
    current_dir = os.path.dirname(os.path.abspath(__file__)) #ustalanie bieżącego katalogu
    file_path = os.path.join(current_dir, 'contacts_to_load.txt')    #znajdowanie pliku z kontaktami

    if not os.path.exists(file_path):
        print(f"Plik {file_path} nie istnieje.")
        return

    with open(file_path, 'r') as plik:
        for linia in plik:
            imie, nazwisko, telefon, email = linia.strip().split(', ')
            kontakt = data_contact.Kontakt(imie, nazwisko, telefon, email)
            ksiazka.kontakty.append(kontakt)
    
    print(f"Kontakty zostały wczytane z pliku {file_path}")
