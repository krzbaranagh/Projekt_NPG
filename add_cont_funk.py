import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *
import data_variable

#główna funkcja
def add_contact():


    def close_add_contact_window():
        add_contact_window.destroy()

    def save_data_close_window():


        name=name_entry.get()
        surname=surname_entry.get()
        phone=phone_entry.get()
        email=email_entry.get()

        if len(name)!=0 and len(surname)!=0 and len(phone)==9 and len(email)!=0 and '@' in email:
            
            nowy_kontakt=Kontakt(name, surname, phone, email)
            Ksiazka.kontakty.append(nowy_kontakt)
            add_contact_window.destroy()

        else:
            
            if len(name)==0 or len(surname)==0 or len(phone)==0 or len(email)==0:
                statement1="Wszystkie pola muszą zostać wypełnione"
                statement2=""

            elif len(phone)!=9 and '@' not in email:
                statement1="Numer powinien składa się z 9 cyfr"
                statement2="Email musi zawierać @"

            elif len(phone)!=9 :
                statement1="Numer składa się z 9 cyfr"
                statement2=""

            elif '@' not in email:
                statement1="Email musi zawierać @"
                statement2=""
                



            error_window=ctk.CTk()
            error_window.resizable(False, False)
            error_window.title("Błąd")
            error_window.geometry("300x110")
        

            label_error1 = ctk.CTkLabel(error_window, text=statement1)
            label_error1.place(relx=0.5, rely=0.1, anchor="n")

            label_error2 = ctk.CTkLabel(error_window, text=statement2)
            label_error2.place(relx=0.5, rely=0.3, anchor="n")

            button_confirm=CTkButton(master=error_window, text="Zatwierdź", command=error_window.destroy, corner_radius=12)
            button_confirm.place(relx=0.97, rely=0.93, anchor="se")

            if data_variable.DaltonMode: 
                button_confirm.configure(fg_color="#1f6aa5", hover_color="#144870")
            else: 
                button_confirm.configure(fg_color="#FF4500",hover_color="#FF6347")

            error_window.mainloop()

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

    if data_variable.DaltonMode: 
        button_cancel.configure(fg_color="#1f6aa5", hover_color="#144870")
        button_confirm.configure(fg_color="#1f6aa5", hover_color="#144870")
    else: 
        button_cancel.configure(fg_color="#FF4500",hover_color="#FF6347")
        button_confirm.configure(fg_color="#FF4500",hover_color="#FF6347")
        

    add_contact_window.mainloop()
