class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

class KsiazkaTeleadresowa:
    def __init__(self): 
        self.kontakty = []



import pickle
import customtkinter as ctk
from customtkinter import *

import add_cont_funk

main_window = ctk.CTk()

main_window.title("Phonebook")
main_window.geometry("650x430")



    


def display_contact():
    print("Przycisk 2 został naciśnięty")
    main_window2=ctk.CTk()
    main_window2.title("Display contact")
    main_window2.geometry("600x400")
    


def edit_contact():
    print("Przycisk 3 został naciśnięty")
    main_window3=ctk.CTk()
    main_window3.title("Edit contact")
    main_window3.geometry("600x400")

def delete_contact():
    print("Przycisk 4 został naciśnięty")
    main_window4=ctk.CTk()
    main_window4.title("Delete contact")
    main_window4.geometry("600x400")

def save_to_file():
    print("ok")

def load_from_file():
    print("ok")


def close_main_window():
    main_window.destroy()



def close_window_and_confirm_data():
    print("ok")



    
button_close = ctk.CTkButton(master=main_window, text="Zamknij", command=close_main_window, corner_radius=12, fg_color="#a51b0b")
button_close.place(relx=1, rely=0, anchor="ne")

button1 = ctk.CTkButton(master=main_window, text="Dodaj kontakt", command=add_cont_funk.add_contact, width=200, height=50, corner_radius=12)
button1.pack(pady=10)

button2 = ctk.CTkButton(master=main_window, text="Wyświetl dane kontaktu", command=display_contact, width=200, height=50, corner_radius=12)
button2.pack(pady=10)

button3 = ctk.CTkButton(master=main_window, text="Edytuj kontakt", command=edit_contact, width=200, height=50, corner_radius=12)
button3.pack(pady=10)

button4 = ctk.CTkButton(master=main_window, text="Usuń kontakt", command=delete_contact, width=200, height=50, corner_radius=12)
button4.pack(pady=10)

button5 = ctk.CTkButton(master=main_window, text="Zapisz dane do pliku", command=save_to_file, width=200, height=50, corner_radius=12)
button5.pack(pady=10)

button6 = ctk.CTkButton(master=main_window, text="Odczytaj dane z pliku", command=load_from_file, width=200, height=50, corner_radius=12)
button6.pack(pady=10)

switch1=CTkSwitch(master=main_window, text="Tryb dla daltonistów")
switch1.place(relx=0.98, rely=0.98, anchor="se")


    


main_window.mainloop()