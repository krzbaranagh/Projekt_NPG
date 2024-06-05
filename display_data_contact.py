import pickle
import customtkinter as ctk
from customtkinter import *


def display_contact():
    print("Przycisk 2 został naciśnięty")
    display_contact_window=ctk.CTk()
    display_contact_window.title("Display contact")
    display_contact_window.geometry("400x150")


    label_start = ctk.CTkLabel(display_contact_window, text="Kogo dane chcesz zobaczyć ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=display_contact_window, values=["option 1", "option 2", "option 3"])
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=display_contact_window, text="Zatwierdź", corner_radius=12)
    button_confirm.place(relx=0.99, rely=0.96, anchor="se")


    display_contact_window.mainloop()