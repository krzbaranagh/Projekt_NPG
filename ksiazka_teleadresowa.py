import pickle
import customtkinter as ctk
from customtkinter import *

import add_cont_funk
import display_data_contact
import delete_cont_funk
import edit_contact_funk
from data_contact import *
import save_contacts_to_file
import load_contacts_from_file
import data_variable
import add_edit_add_to_groups

main_window = ctk.CTk()
main_window.title("Phonebook")
main_window.geometry("650x550")
main_window.resizable(False, False)

def close_main_window() -> None:
    Ksiazka.data_save()
    main_window.destroy()

def set_colors() -> None:
    for button in buttons:
        button.configure(fg_color="#FF4500",hover_color="#FF6347")

def set_dalton_colors() -> None:
    for button in buttons:
        button.configure(fg_color="#1f6aa5", hover_color="#144870")

data_variable.DaltonMode = 1

def toggle_dalton_mode() -> None:
    if dalton_switch.get() == 1: 
        data_variable.DaltonMode = 0
        set_colors()
    else: 
        data_variable.DaltonMode = 1
        set_dalton_colors()
        
button_close = ctk.CTkButton(master = main_window, text = "Zamknij", command = close_main_window, corner_radius = 12, fg_color = "#a51b0b")
button_close.place(relx = 0.98, rely = 0.02, anchor = "ne")

add_contact_button = ctk.CTkButton(master = main_window, text = "Dodaj kontakt", command = add_cont_funk.add_contact, width = 200, height = 50, corner_radius = 12)
add_contact_button.pack(pady = 10)

display_contact_button = ctk.CTkButton(master = main_window, text = "Wyświetl dane kontaktu", command = display_data_contact.display_contact, width = 200, height = 50, corner_radius = 12)
display_contact_button.pack(pady = 10)

edit_contact_button = ctk.CTkButton(master = main_window, text = "Edytuj kontakt", command = edit_contact_funk.edit_contact, width = 200, height = 50, corner_radius = 12)
edit_contact_button.pack(pady = 10)

delete_contact_button = ctk.CTkButton(master = main_window, text = "Usuń kontakt", command = delete_cont_funk.delete_contact, width = 200, height = 50, corner_radius = 12)
delete_contact_button.pack(pady = 10)

save_contacts_to_file_button = ctk.CTkButton(master = main_window, text = "Zapisz dane do pliku", command = save_contacts_to_file.save_contacts_to_txt, width = 200, height = 50, corner_radius = 12)
save_contacts_to_file_button.pack(pady = 10)

load_contacts_to_file_button = ctk.CTkButton(master = main_window, text = "Odczytaj dane z pliku", command = load_contacts_from_file.load_contacts_from_txt, width = 200, height = 50, corner_radius = 12)
load_contacts_to_file_button.pack(pady = 10)

add_edit_add_to_groups_button = ctk.CTkButton(master = main_window, text = "Dodaj i edytuj grupę kontaków", command = add_edit_add_to_groups.add_edit_add_to_groups, width = 200, height = 50, corner_radius = 12)
add_edit_add_to_groups_button.pack(pady = 10)

dalton_switch=CTkSwitch(master = main_window, text="Tryb dla daltonistów", command=toggle_dalton_mode, fg_color="#FF4500")
dalton_switch.place(relx=0.98, rely=0.98, anchor="se")

buttons= [button_close, add_contact_button, display_contact_button, edit_contact_button, delete_contact_button, save_contacts_to_file_button, load_contacts_to_file_button, add_edit_add_to_groups_button]

main_window.mainloop()
