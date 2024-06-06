class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

class KsiazkaTeleadresowa:
    def __init__(self): 
        self.kontakty = []


janek = Kontakt("Jan", "Kowalski", "123456789", "jan.kowalski@example.com")
maciek = Kontakt("Maciek", "Zuczek", "564957341", "maciekzuczek@wp.pl")


import pickle
import customtkinter as ctk
from customtkinter import *

import add_cont_funk
import display_data_contact
import delete_cont_funk

main_window = ctk.CTk()
main_window.title("Phonebook")
main_window.geometry("650x430")
main_window.resizable(False, False)





def edit_contact():
    print("Przycisk 3 został naciśnięty")
    main_window3=ctk.CTk()
    main_window3.title("Edit contact")
    main_window3.geometry("400x400")



def save_to_file():
    print("ok")


def load_from_file():
    print("ok")


def close_main_window():
    main_window.destroy()


def close_window_and_confirm_data():
    print("ok")



    
button_close = ctk.CTkButton(master=main_window, text="Zamknij", command=close_main_window, corner_radius=12, fg_color="#a51b0b")
button_close.place(relx=0.98, rely=0.02, anchor="ne")

add_contact_button = ctk.CTkButton(master=main_window, text="Dodaj kontakt", command=add_cont_funk.add_contact, width=200, height=50, corner_radius=12)
add_contact_button.pack(pady=10)

display_contact_button = ctk.CTkButton(master=main_window, text="Wyświetl dane kontaktu", command=display_data_contact.display_contact, width=200, height=50, corner_radius=12)
display_contact_button.pack(pady=10)

edit_contact_button = ctk.CTkButton(master=main_window, text="Edytuj kontakt", command=edit_contact, width=200, height=50, corner_radius=12)
edit_contact_button.pack(pady=10)

delete_contact_button = ctk.CTkButton(master=main_window, text="Usuń kontakt", command=delete_cont_funk.delete_contact, width=200, height=50, corner_radius=12)
delete_contact_button.pack(pady=10)

save_contacts_to_file_button = ctk.CTkButton(master=main_window, text="Zapisz dane do pliku", command=save_to_file, width=200, height=50, corner_radius=12)
save_contacts_to_file_button.pack(pady=10)

load_contacts_to_file_button = ctk.CTkButton(master=main_window, text="Odczytaj dane z pliku", command=load_from_file, width=200, height=50, corner_radius=12)
load_contacts_to_file_button.pack(pady=10)

dalton_switch=CTkSwitch(master=main_window, text="Tryb dla daltonistów")
dalton_switch.place(relx=0.98, rely=0.98, anchor="se")


    


main_window.mainloop()