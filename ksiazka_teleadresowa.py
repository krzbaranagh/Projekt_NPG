


# class Kontakt:
#     def __init__(self, imie, nazwisko, telefon, email):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.telefon = telefon
#         self.email = email

# class KsiazkaTeleadresowa:
#     def __init__(self): #konstruktor klasy KsiazkaTeleadresowa #Tworzy listę pustą z późniejszą możliwością edycji
#         self.kontakty = []



import pickle
import customtkinter as ctk
from customtkinter import *

main_window = ctk.CTk()

main_window.title("Phonebook")
main_window.geometry("650x430")


def add_contact():


    def close_add_contact_window():
        add_contact_window.destroy()

    add_contact_window=ctk.CTk()
    add_contact_window.title("Dodaj kontakt")
    add_contact_window.geometry("400x400")

    label_start = ctk.CTkLabel(add_contact_window, text="Podaj dane poniżej")
    label_start.pack()

    name_label = ctk.CTkLabel(add_contact_window, text="Imię:")
    name_label.place(x=60, y=70)

    surname_label = ctk.CTkLabel(add_contact_window, text="Nazwisko:")
    surname_label.place(x=60, y=130)

    phone_label = ctk.CTkLabel(add_contact_window, text="Numer tel:")
    phone_label.place(x=60, y=190)

    email_label = ctk.CTkLabel(add_contact_window, text="Email:")
    email_label.place(x=60, y=250)


    name_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    name_entry.place(x=130, y=70)

    surname_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    surname_entry.place(x=130, y=130)

    phone_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    phone_entry.place(x=130, y=190)

    email_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    email_entry.place(x=130, y=250)

    button_confirm=CTkButton(master=add_contact_window, text="Zatwierdź", command=close_window_and_confirm_data, corner_radius=12)
    button_confirm.place(relx=0.98, rely=0.98, anchor="se")
    

    button_cancel=CTkButton(master=add_contact_window, text="Anuluj", command=close_add_contact_window, corner_radius=12)
    button_cancel.place(relx=0.02, rely=0.98, anchor="sw")

    add_contact_window.mainloop()

    

#button_close.place(relx=1, rely=0, anchor="ne")    


def display_contact():
    print("Przycisk 2 został naciśnięty")
    main_window2=ctk.CTk()
    main_window2.title("Display contact")
    main_window2.geometry("600x400")
    #main_window2.mainloop()


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

button1 = ctk.CTkButton(master=main_window, text="Dodaj kontakt", command=add_contact, width=200, height=50, corner_radius=12)
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