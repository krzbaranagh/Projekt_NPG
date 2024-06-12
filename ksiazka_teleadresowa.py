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

main_window = ctk.CTk()
main_window.title("Phonebook")
main_window.geometry("650x430")
main_window.resizable(False, False)


def close_main_window():
    Ksiazka.data_save()
    main_window.destroy()


def close_window_and_confirm_data():
    print("ok")

def toggle_dalton_mode():
    if dalton_switch.get() == 1:
        # Włączenie trybu dla daltonistów
        main_window.configure(bg='#2C2C2C')
        button_close.configure(fg_color="#FF4500")
        add_contact_button.configure(fg_color="#FF4500", hover_color="#FF6347")
        display_contact_button.configure(fg_color="#FF4500", hover_color="#FF6347")
        edit_contact_button.configure(fg_color="#FF4500", hover_color="#FF6347")
        delete_contact_button.configure(fg_color="#FF4500", hover_color="#FF6347")
        save_contacts_to_file_button.configure(fg_color="#FF4500", hover_color="#FF6347")
        load_contacts_to_file_button.configure(fg_color="#FF4500", hover_color="#FF6347")
    else:
        # Wyłączenie trybu dla daltonistów, powrót do domyślnych kolorów
        main_window.configure(bg='#FFFFFF')
        button_close.configure(fg_color="#a51b0b")
        add_contact_button.configure(fg_color="#1f6aa5", hover_color="#144870")
        display_contact_button.configure(fg_color="#1f6aa5", hover_color="#144870")
        edit_contact_button.configure(fg_color="#1f6aa5", hover_color="#144870")
        delete_contact_button.configure(fg_color="#1f6aa5", hover_color="#144870")
        save_contacts_to_file_button.configure(fg_color="#1f6aa5", hover_color="#144870")
        load_contacts_to_file_button.configure(fg_color="#1f6aa5", hover_color="#144870")


    
button_close = ctk.CTkButton(master=main_window, text="Zamknij", command=close_main_window, corner_radius=12, fg_color="#a51b0b")
button_close.place(relx=0.98, rely=0.02, anchor="ne")

add_contact_button = ctk.CTkButton(master=main_window, text="Dodaj kontakt", command=add_cont_funk.add_contact, width=200, height=50, corner_radius=12)
add_contact_button.pack(pady=10)

display_contact_button = ctk.CTkButton(master=main_window, text="Wyświetl dane kontaktu", command=display_data_contact.display_contact, width=200, height=50, corner_radius=12)
display_contact_button.pack(pady=10)

edit_contact_button = ctk.CTkButton(master=main_window, text="Edytuj kontakt", command=edit_contact_funk.edit_contact, width=200, height=50, corner_radius=12)
edit_contact_button.pack(pady=10)

delete_contact_button = ctk.CTkButton(master=main_window, text="Usuń kontakt", command=delete_cont_funk.delete_contact, width=200, height=50, corner_radius=12)
delete_contact_button.pack(pady=10)

save_contacts_to_file_button = ctk.CTkButton(master=main_window, text="Zapisz dane do pliku", command=save_contacts_to_file.save_contacts_to_txt, width=200, height=50, corner_radius=12)
save_contacts_to_file_button.pack(pady=10)

load_contacts_to_file_button = ctk.CTkButton(master=main_window, text="Odczytaj dane z pliku", command=load_contacts_from_file.load_contacts_from_txt, width=200, height=50, corner_radius=12)
load_contacts_to_file_button.pack(pady=10)

dalton_switch=CTkSwitch(master=main_window, text="Tryb dla daltonistów", command=toggle_dalton_mode)
dalton_switch.place(relx=0.98, rely=0.98, anchor="se")


    


main_window.mainloop()
