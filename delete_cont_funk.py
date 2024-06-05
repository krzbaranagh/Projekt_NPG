import pickle
import customtkinter as ctk
from customtkinter import *


def delete_contact():

    def delete_and_close_window():
        #wyjebanie kontaktu
        delete_contact_window.destroy()



    delete_contact_window=ctk.CTk()
    delete_contact_window.title("Display contact")
    delete_contact_window.geometry("400x150")


    label_start = ctk.CTkLabel(delete_contact_window, text="Kogo dane chcesz zobaczyć ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=delete_contact_window, values=["option 1", "option 2", "option 3"])
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=delete_contact_window, text="Zatwierdź", corner_radius=12, command=delete_and_close_window)
    button_confirm.place(relx=0.99, rely=0.96, anchor="se")





    delete_contact_window.mainloop()