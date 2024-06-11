import pickle
import os
import customtkinter as ctk
from customtkinter import *

import data_contact

def save_contacts_to_txt():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'saved_contacts.txt')

    if not os.path.exists(file_path):
        show_error_window() 
        return

    with open(file_path, 'w') as plik:
        for kontakt in Ksiazka.kontakty:
            plik.write(f"{kontakt.imie} {kontakt.nazwisko} {kontakt.telefon} {kontakt.email}\n")

    show_confirmation_window()
