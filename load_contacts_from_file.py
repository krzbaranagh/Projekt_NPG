import pickle
import os
import customtkinter as ctk
from customtkinter import *

from data_contact import *

def show_confirmation_window():

    confirmation_window = ctk.CTk()
    confirmation_window.geometry("300x100")
    confirmation_window.title("Potwierdzenie")

    label = ctk.CTkLabel(confirmation_window, text="Pomyślnie zapisano kontakty do pliku")
    label.pack(pady=10)

    def close_window():
        confirmation_window.destroy()

    ok_button = ctk.CTkButton(confirmation_window, text="OK", command=close_window)
    ok_button.pack(pady=10)

    confirmation_window.mainloop()

def show_error_window():
        
    error_window = ctk.CTk()
    error_window.geometry("300x100")
    error_window.title("Odmowa")

    label = ctk.CTkLabel(error_window, text="Brak odpowiedniego pliku to zapisu kontaktów")
    label.pack(pady=10)

    def close_window():
        error_window.destroy()

    ok_button = ctk.CTkButton(error_window, text="OK", command=close_window)
    ok_button.pack(pady=10)

    error_window.mainloop()

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
