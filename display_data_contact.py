import pickle
import customtkinter as ctk
from customtkinter import *




def display_contact():


    def confirm():   #funkcja która zatwierdza się wybrany kontakt z checklisty. zamyka to okno i otwiera nowe z wypisanymi danymi
        print("ok") 
        choose_contact_window.destroy()

        display_contact_window=ctk.CTk()
        display_contact_window.resizable(False, False)
        display_contact_window.title("Dane kontaktu")
        display_contact_window.geometry("320x295")
        



        name_label = ctk.CTkLabel(display_contact_window, text="Imię:")
        name_label.place(x=60, y=20)

        surname_label = ctk.CTkLabel(display_contact_window, text="Nazwisko:")
        surname_label.place(x=60, y=80)

        phone_label = ctk.CTkLabel(display_contact_window, text="Numer tel:")
        phone_label.place(x=60, y=140)

        email_label = ctk.CTkLabel(display_contact_window, text="Email:")
        email_label.place(x=60, y=200)


        value_name_label = ctk.CTkLabel(display_contact_window, text="Trza zaimp")
        value_name_label.place(x=130, y=20)

        value_surname_label = ctk.CTkLabel(display_contact_window, text="Trza zaimp")
        value_surname_label.place(x=130, y=80)

        value_phone_label = ctk.CTkLabel(display_contact_window, text="Trza zaimp")
        value_phone_label.place(x=130, y=140)

        value_email_label = ctk.CTkLabel(display_contact_window, text="Trza zaimp")
        value_email_label.place(x=130, y=200)


        button_close=CTkButton(master=display_contact_window, text="Zamknij", corner_radius=12, command=display_contact_window.destroy)
        button_close.place(relx=0.99, rely=0.96, anchor="se")


        display_contact_window.mainloop()

    
    choose_contact_window=ctk.CTk()
    choose_contact_window.resizable(False, False)
    choose_contact_window.title("Display contact")
    choose_contact_window.geometry("400x150")
    choose_contact_window.resizable(False, False)

    label_start = ctk.CTkLabel(choose_contact_window, text="Kogo dane chcesz zobaczyć ?")
    label_start.pack(pady=10)

    contact_choice=CTkComboBox(master=choose_contact_window, values=["option 1", "option 2", "option 3"])
    contact_choice.pack(pady=10)

    button_confirm=CTkButton(master=choose_contact_window, text="Zatwierdź", corner_radius=12, command=confirm)
    button_confirm.place(relx=0.99, rely=0.96, anchor="se")





    choose_contact_window.mainloop()