import customtkinter as ctk
from customtkinter import *
from data_contact import *


def edit_contact():


    
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




    def confirm_and_edit():
        choose_contact_window.destroy()


        def save_changes_and_close_window():
            #edycja kontaktu w bazie 
            edit_contact_window.destroy()
            
            




        

        edit_contact_window=ctk.CTk()
        edit_contact_window.resizable(False, False)
        edit_contact_window.title("Edit contact")
        edit_contact_window.geometry("400x400")


        label_start = ctk.CTkLabel(edit_contact_window, text="Podaj dane poniżej")
        label_start.pack()

        name_label = ctk.CTkLabel(edit_contact_window, text="Imię:")
        name_label.place(x=60, y=70)

        surname_label = ctk.CTkLabel(edit_contact_window, text="Nazwisko:")
        surname_label.place(x=60, y=130)

        phone_label = ctk.CTkLabel(edit_contact_window, text="Numer tel:")
        phone_label.place(x=60, y=190)

        email_label = ctk.CTkLabel(edit_contact_window, text="Email:")
        email_label.place(x=60, y=250)


        name_entry=CTkEntry(master=edit_contact_window, placeholder_text=obiekt.imie, width=200, text_color="#FFCC70")
        name_entry.place(x=140, y=70)

        surname_entry=CTkEntry(master=edit_contact_window, placeholder_text=obiekt.nazwisko, width=200, text_color="#FFCC70")
        surname_entry.place(x=140, y=130)

        phone_entry=CTkEntry(master=edit_contact_window, placeholder_text=obiekt.telefon, width=200, text_color="#FFCC70")
        phone_entry.place(x=140, y=190)

        email_entry=CTkEntry(master=edit_contact_window, placeholder_text=obiekt.email, width=200, text_color="#FFCC70")
        email_entry.place(x=140, y=250)

        button_confirm=CTkButton(master=edit_contact_window, text="Zatwierdź", command=save_changes_and_close_window, corner_radius=12)
        button_confirm.place(relx=0.98, rely=0.98, anchor="se")

        edit_contact_window.mainloop()
        


    choose_contact_window=ctk.CTk()
    choose_contact_window.resizable(False, False)
    choose_contact_window.title("Edit contact")
    choose_contact_window.geometry("400x150")


    label_start = ctk.CTkLabel(choose_contact_window, text="Który kontakt chcesz edytować ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=choose_contact_window, values=lista, command=set_value if niepusta else None)
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=choose_contact_window, text="Zatwierdź", corner_radius=12, command=confirm_and_edit)
    button_confirm.place(relx=0.99, rely=0.96, anchor="se")

    choose_contact_window.mainloop()