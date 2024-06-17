import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *
import data_variable

def add_contacts_group() -> None:
    def save_group_close_window() -> None:
        name = name_entry.get()

        Test_Lista = [grupa.nazwa for grupa in Rejestr]
        
        if name not in Test_Lista:
            nowa_grupa = GrupaKontaktów(name, "0"*len(Ksiazka.kontakty))
            Rejestr.append(nowa_grupa)
            add_contacts_group_window.destroy()
        else:
            error_window=ctk.CTk()
            error_window.resizable(False, False)
            error_window.title("Błąd")
            error_window.geometry("200x55")
        
            label_error = ctk.CTkLabel(error_window, text = "Istnieje grupa o podanej nazwie")
            label_error.place(relx = 0.5, rely = 0.1, anchor = "n")

            button_confirm = CTkButton(master = error_window, text = "Zatwierdź", command = error_window.destroy, corner_radius=12)
            button_confirm.place(relx = 0.97, rely = 0.93, anchor = "se")

            if data_variable.DaltonMode: 
                button_confirm.configure(fg_color = "#1f6aa5", hover_color = "#144870")
            else: 
                button_confirm.configure(fg_color = "#FF4500", hover_color = "#FF6347")

            error_window.mainloop()

    def close_add_contacts_group() -> None:
        add_contacts_group_window.destroy()
    
    add_contacts_group_window=ctk.CTk()
    add_contacts_group_window(False, False)
    add_contacts_group_window("Dodaj grupę kontaktów")
    add_contacts_group_window("250x250")

    label_start = ctk.CTkLabel(add_contacts_group_window, text="Podaj dane poniżej")
    label_start.pack()

    name_label = ctk.CTkLabel(add_contacts_group_window, text="Nazwa:")
    name_label.place(x = 60, y = 70)

    name_entry=CTkEntry(master=add_contacts_group_window, placeholder_text = "Start typing...", width = 200, text_color = "#FFCC70")
    name_entry.place(x = 140, y = 70)

    button_confirm=CTkButton(master = add_contacts_group_window, text = "Zatwierdź", command = save_group_close_window, corner_radius = 12)
    button_confirm.place(relx = 0.98, rely = 0.98, anchor = "se")
    
    button_cancel=CTkButton(master = add_contacts_group_window, text = "Anuluj", command = close_add_contacts_group, corner_radius = 12)
    button_cancel.place(relx = 0.02, rely = 0.98, anchor = "sw")

    if data_variable.DaltonMode: 
        button_cancel.configure(fg_color = "#1f6aa5", hover_color = "#144870")
        button_confirm.configure(fg_color = "#1f6aa5", hover_color = "#144870")
    else: 
        button_cancel.configure(fg_color = "#FF4500", hover_color = "#FF6347")
        button_confirm.configure(fg_color = "#FF4500", hover_color = "#FF6347")

    add_contacts_group_window.mainloop()

def remove_contacts_group() -> None:
    klasa: GrupaKontaktów

    if len(Rejestr):
        lista = [grupa.nazwa for grupa in Rejestr]
        klasa = Rejestr[0]
    else:
        lista = ["Brak grupy kontaktów"]

    def wybor_grupy(wybor) -> None:
        nonlocal klasa
        for grupa in Rejestr:
            if grupa.nazwa == wybor:
                klasa = grupa
                print("wykonało")

    def delete_contacts_group_and_close() -> None:
        if klasa in Rejestr:
            print("jest")
            Rejestr.remove(klasa)
        remove_contacts_group_window.destroy()

    remove_contacts_group_window=ctk.CTk()
    remove_contacts_group_window.resizable(False, False)
    remove_contacts_group_window.title("Delete contact")
    remove_contacts_group_window.geometry("400x150")
    
    label_start = ctk.CTkLabel(remove_contacts_group_window, text = "Którą grupę chcesz usunąć?")
    label_start.pack(pady=10)

    group_choice = CTkComboBox(master = remove_contacts_group_window, values = lista, command = wybor_grupy, width = 150)
    group_choice.pack(pady = 10)

    button_confirm  =CTkButton(master = remove_contacts_group_window, text = "Zatwierdź", corner_radius = 12, command = delete_contacts_group_and_close)
    button_confirm.place(relx = 0.99, rely = 0.96, anchor = "se")

    button_cancel = CTkButton(master = delete_contact_window, text  = "Anuluj", command = remove_contacts_group_window.destroy, corner_radius = 12)
    button_cancel.place(relx = 0.02, rely = 0.98, anchor = "sw")

    if data_variable.DaltonMode: 
        button_confirm.configure(fg_color="#1f6aa5", hover_color="#144870")
        button_cancel.configure(fg_color="#1f6aa5", hover_color="#144870")

    else: 
        button_confirm.configure(fg_color="#FF4500",hover_color="#FF6347")
        button_cancel.configure(fg_color="#FF4500",hover_color="#FF6347")

    remove_contacts_group_window.mainloop()

def add_edit_add_to_groups() -> None:
    add_edit_add_to_groups_window=ctk.CTk()
    add_edit_add_to_groups_window.resizable(False, False)
    add_edit_add_to_groups_window.title("Delete contact")
    add_edit_add_to_groups_window.geometry("400x350")

    button_close=CTkButton(master = add_edit_add_to_groups_window, text = "Zamknij", command = add_edit_add_to_groups_window.destroy, corner_radius = 12)
    button_close.place(relx = 0.02, rely = 0.98, anchor = "se")

    button_add_contacts_group = ctk.CTkButton(master = add_edit_add_to_groups_window, text = "Dodaj grupę kontaktów", command = add_contacts_group, corner_radius = 12, fg_color = "#a51b0b")
    button_add_contacts_group.pack(pady = 10)

    button_remove_contacts_group = ctk.CTkButton(master = add_edit_add_to_groups_window, text = "Usuń grupę kontaktów", command = remove_contacts_group, corner_radius = 12, fg_color = "#a51b0b")
    button_remove_contacts_group.pack(pady = 10)

    if data_variable.DaltonMode: 
        button_close.configure(fg_color = "#1f6aa5", hover_color = "#144870")
        button_remove_contacts_group.configure(fg_color = "#1f6aa5", hover_color = "#144870")
        button_add_contacts_group.configure(fg_color = "#1f6aa5", hover_color = "#144870")
    else: 
        button_close.configure(fg_color = "#FF4500", hover_color = "#FF6347")
        button_remove_contacts_group.configure(fg_color = "#FF4500", hover_color = "#FF6347")
        button_add_contacts_group.configure(fg_color = "#FF4500", hover_color = "#FF6347")

    add_edit_add_to_groups_window.mainloop()