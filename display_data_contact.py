import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *


def display_contact(): 
    
    obiekt : Kontakt
    niepusta : bool = len(Ksiazka.kontakty) != 0

    if niepusta: 
        obiekt = Ksiazka.kontakty[0]
        slownik = {(adres.imie + " " + adres.nazwisko) :adres for adres in Ksiazka.kontakty}
        lista = [adres.imie + " " + adres.nazwisko for adres in Ksiazka.kontakty]
    else:
        lista = ["Brak kontaktów"]


    def set_value(wybor): 
        nonlocal obiekt
        obiekt = slownik[wybor]

    def close_display_contact_window():
        choose_contact_window.destroy()



    def display():   #funkcja którą zatwierdza się wybrany kontakt z checklisty. zamyka to okno i otwiera nowe z wypisanymi danymi
        choose_contact_window.destroy()

        display_contact_window=ctk.CTk()
        display_contact_window.resizable(False, False)
        display_contact_window.title("Dane kontaktu")
        display_contact_window.geometry("320x295")

        name_label = ctk.CTkLabel(display_contact_window, text="Imie: ")
        name_label.place(x=60, y=20)

        surname_label = ctk.CTkLabel(display_contact_window, text="Nazwisko: ")
        surname_label.place(x=60, y=80)

        phone_label = ctk.CTkLabel(display_contact_window, text="Telefon: ")
        phone_label.place(x=60, y=140)

        email_label = ctk.CTkLabel(display_contact_window, text="Email: ")
        email_label.place(x=60, y=200)


        value_name_label = ctk.CTkLabel(display_contact_window, text=obiekt.imie)
        value_name_label.place(x=130, y=20)

        value_surname_label = ctk.CTkLabel(display_contact_window, text=obiekt.nazwisko)
        value_surname_label.place(x=130, y=80)

        value_phone_label = ctk.CTkLabel(display_contact_window, text=obiekt.telefon)
        value_phone_label.place(x=130, y=140)

        value_email_label = ctk.CTkLabel(display_contact_window, text=obiekt.email)
        value_email_label.place(x=130, y=200)


        button_close=CTkButton(master=display_contact_window, text="Zamknij", corner_radius=12, command=display_contact_window.destroy)
        button_close.place(relx=0.99, rely=0.96, anchor="se")


        display_contact_window.mainloop()

    choose_contact_window=ctk.CTk()
    choose_contact_window.resizable(False, False)
    choose_contact_window.title("Display contact")
    choose_contact_window.geometry("400x150")
    choose_contact_window.resizable(False, False)

    label_start = ctk.CTkLabel(choose_contact_window, text="Kogo dane chcesz zobaczyć ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=choose_contact_window, values=lista ,command= set_value if niepusta else None)
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=choose_contact_window, text="Zatwierdź", corner_radius=12, command= display if niepusta else close_display_contact_window)
    button_confirm.place(relx=0.98, rely=0.96, anchor="se")

    button_cancel=CTkButton(master=choose_contact_window, text="Anuluj", command=close_display_contact_window, corner_radius=12)
    button_cancel.place(relx=0.02, rely=0.96, anchor="sw")

    choose_contact_window.mainloop()
