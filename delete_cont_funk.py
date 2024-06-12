import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *

def delete_contact():
    obiekt : Kontakt
    niepusta : bool = len(Ksiazka.kontakty) != 0

    if niepusta: 
        
        lista = [adres.imie + " " + adres.nazwisko for adres in Ksiazka.kontakty]
    else:
        lista = ["Brak kontaktów"]
    def wybor_kontaktu(wybor):
        nonlocal obiekt
        for x in Ksiazka.kontakty:
            if x.imie + " " + x.nazwisko == wybor:
                obiekt = x
                print("wykonalo")
    def delete_and_close_window():
        #wyjebanie kontaktu
        if obiekt in Ksiazka.kontakty:
            print("jest")
            Ksiazka.kontakty.remove(obiekt)
        delete_contact_window.destroy()
        
    delete_contact_window=ctk.CTk()
    delete_contact_window.resizable(False, False)
    delete_contact_window.title("Delete contact")
    delete_contact_window.geometry("400x150")
    


    label_start = ctk.CTkLabel(delete_contact_window, text="Kogo dane chcesz zobaczyć ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=delete_contact_window, values=lista, command = wybor_kontaktu)
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=delete_contact_window, text="Zatwierdź", corner_radius=12, command=delete_and_close_window)
    button_confirm.place(relx=0.99, rely=0.96, anchor="se")



#d

    delete_contact_window.mainloop()