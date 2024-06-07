import pickle
import customtkinter as ctk
from customtkinter import *


def edit_contact():


    def confirm_and_edit():
        choose_contact_window.destroy()

        edit_contact_window=ctk.CTk()
        edit_contact_window.resizable(False, False)
        edit_contact_window.title("Edit contact")
        edit_contact_window.geometry("320x295")



        name_label = ctk.CTkLabel(edit_contact_window, text="Imię:")
        name_label.place(x=60, y=20)

        surname_label = ctk.CTkLabel(edit_contact_window, text="Nazwisko:")
        surname_label.place(x=60, y=80)

        phone_label = ctk.CTkLabel(edit_contact_window, text="Numer tel:")
        phone_label.place(x=60, y=140)

        email_label = ctk.CTkLabel(edit_contact_window, text="Email:")
        email_label.place(x=60, y=200)

        


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