import pickle
import customtkinter as ctk
from customtkinter import *


def edit_contact():


    def confirm_and_edit():
        choose_contact_window.destroy()


        def save_data_close_window():
            #dodanie kontaktu do bazy 
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


        name_entry=CTkEntry(master=edit_contact_window, placeholder_text="Jacek", width=200, text_color="#FFCC70")
        name_entry.place(x=140, y=70)

        surname_entry=CTkEntry(master=edit_contact_window, placeholder_text="Duda", width=200, text_color="#FFCC70")
        surname_entry.place(x=140, y=130)

        phone_entry=CTkEntry(master=edit_contact_window, placeholder_text="657483465", width=200, text_color="#FFCC70")
        phone_entry.place(x=140, y=190)

        email_entry=CTkEntry(master=edit_contact_window, placeholder_text="jacekduda@op.pl", width=200, text_color="#FFCC70")
        email_entry.place(x=140, y=250)

        button_confirm=CTkButton(master=edit_contact_window, text="Zatwierdź", command=save_data_close_window, corner_radius=12)
        button_confirm.place(relx=0.98, rely=0.98, anchor="se")
        


    choose_contact_window=ctk.CTk()
    choose_contact_window.resizable(False, False)
    choose_contact_window.title("Edit contact")
    choose_contact_window.geometry("400x150")


    label_start = ctk.CTkLabel(choose_contact_window, text="Który kontakt chcesz edytować ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=choose_contact_window, values=["option 1", "option 2", "option 3"])
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=choose_contact_window, text="Zatwierdź", corner_radius=12, command=confirm_and_edit)
    button_confirm.place(relx=0.99, rely=0.96, anchor="se")