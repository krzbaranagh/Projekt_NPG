import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *



def add_contact():


    def close_add_contact_window():
        add_contact_window.destroy()

    def save_data_close_window():


        name=name_entry.get()
        surname=surname_entry.get()
        phone=phone_entry.get()
        email=email_entry.get()

        if len(name)!=0 and len(surname)!=0 and len(phone)==9 and '@' in email:
            nowy_kontakt=Kontakt(name, surname, phone, email)
            Ksiazka.dodaj_kontakt(nowy_kontakt)
            add_contact_window.destroy()

        else:
            error_window=ctk.CTk()
            error_window.resizable(False, False)
            error_window.title("Błąd")
            error_window.geometry("225x85")
            label_error = ctk.CTkLabel(error_window, text="Wpisz poprawnie dane")
            label_error.place(relx=0.5, rely=0.1, anchor="n")

            button_confirm=CTkButton(master=error_window, text="Zatwierdź", command=error_window.destroy, corner_radius=12)
            button_confirm.place(relx=0.97, rely=0.93, anchor="se")

        
            
    
    
    
    add_contact_window=ctk.CTk()
    add_contact_window.resizable(False, False)
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
    name_entry.place(x=140, y=70)

    surname_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    surname_entry.place(x=140, y=130)

    phone_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    phone_entry.place(x=140, y=190)

    email_entry=CTkEntry(master=add_contact_window, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    email_entry.place(x=140, y=250)

    button_confirm=CTkButton(master=add_contact_window, text="Zatwierdź", command=save_data_close_window, corner_radius=12)
    button_confirm.place(relx=0.98, rely=0.98, anchor="se")
    

    button_cancel=CTkButton(master=add_contact_window, text="Anuluj", command=close_add_contact_window, corner_radius=12)
    button_cancel.place(relx=0.02, rely=0.98, anchor="sw")

    add_contact_window.mainloop()