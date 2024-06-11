import pickle
import os
import customtkinter as ctk
from customtkinter import *

import data_contact

def save_contacts_to_file(ksiazka):
    current_dir = os.path.dirname(os.path.abspath(__file__)) #ustalanie bieżącego katalogu
    file_path = os.path.join(current_dir, 'contacts_to_save.txt') #znajdowanie pliku do którego będą zapisywane kontakty

    if not os.path.exists(file_path):
        print(f"Plik {file_path} nie istnieje.")
        return
        
    with open(file_path, 'w') as plik:
        for kontakt in ksiazka.kontakty:
            plik.write(f"{kontakt.imie}, {kontakt.nazwisko}, {kontakt.telefon}, {kontakt.email}\n")
    
    print(f"Kontakty zapisane do pliku {file_path}")
