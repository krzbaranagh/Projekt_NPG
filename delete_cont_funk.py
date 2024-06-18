import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *
import data_variable

def delete_contact() -> None:
    obiekt : Kontakt

    if len(Ksiazka.kontakty): 
        lista = [adres.imie + " " + adres.nazwisko for adres in Ksiazka.kontakty]
        obiekt=Ksiazka.kontakty[0]
    else:
        lista = ["Brak kontaktów"]

    def wybor_kontaktu(wybor) -> None:
        nonlocal obiekt
        for x in Ksiazka.kontakty:
            if x.imie + " " + x.nazwisko == wybor:
                obiekt = x
                print("wykonalo")

    def delete_and_close_window() -> None:
        if obiekt in Ksiazka.kontakty:
            print("jest")

            index = Ksiazka.kontakty.index(obiekt)
            for grupa in Rejestr:
                grupa.binarna_lista.remove(index)
            Ksiazka.kontakty.remove(obiekt)

        delete_contact_window.destroy()
        
    delete_contact_window = ctk.CTk()
    delete_contact_window.resizable(False, False)
    delete_contact_window.title("Delete contact")
    delete_contact_window.geometry("400x150")
    
    label_start = ctk.CTkLabel(delete_contact_window, text="Który kontakt chcesz usunąć ?")
    label_start.pack(pady=10)

    contact_choice = CTkComboBox(master = delete_contact_window, values = lista, command = wybor_kontaktu, width = 150)
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master = delete_contact_window, text = "Zatwierdź", corner_radius = 12, command = delete_and_close_window)
    button_confirm.place(relx = 0.99, rely = 0.96, anchor = "se")

    button_cancel=CTkButton(master = delete_contact_window, text = "Anuluj", command = delete_contact_window.destroy, corner_radius = 12)
    button_cancel.place(relx = 0.02, rely = 0.98, anchor = "sw")

    if data_variable.DaltonMode: 
        button_confirm.configure(fg_color = "#1f6aa5", hover_color = "#144870")
        button_cancel.configure(fg_color = "#1f6aa5", hover_color = "#144870")

    else: 
        button_confirm.configure(fg_color = "#FF4500", hover_color = "#FF6347")
        button_cancel.configure(fg_color = "#FF4500", hover_color = "#FF6347")

    delete_contact_window.mainloop()