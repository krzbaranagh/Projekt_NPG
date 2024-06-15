import pickle
import os
import customtkinter as ctk
from customtkinter import *
import data_variable

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

    if data_variable.DaltonMode:
        ok_button.configure(fg_color="#1f6aa5", hover_color="#144870")
    else:
        ok_button.configure(fg_color="#FF4500",hover_color="#FF6347")

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

    if data_variable.DaltonMode:
        ok_button.configure(fg_color="#1f6aa5", hover_color="#144870")
    else:
        ok_button.configure(fg_color="#FF4500",hover_color="#FF6347")

    error_window.mainloop()

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