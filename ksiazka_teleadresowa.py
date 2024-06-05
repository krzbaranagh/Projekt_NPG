


# class Kontakt:
#     def __init__(self, imie, nazwisko, telefon, email):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.telefon = telefon
#         self.email = email

# class KsiazkaTeleadresowa:
#     def __init__(self): #konstruktor klasy KsiazkaTeleadresowa #Tworzy listę pustą z późniejszą możliwością edycji
#         self.kontakty = []



import pickle
import customtkinter as ctk
from customtkinter import *

app = ctk.CTk()

app.title("Phonebook")
app.geometry("650x430")


def add_contact():


    def close_new_window1():
        new_window1.destroy()

    new_window1=ctk.CTk()
    new_window1.title("Dodaj kontakt")
    new_window1.geometry("400x400")

    label_start = ctk.CTkLabel(new_window1, text="Podaj dane poniżej")
    label_start.pack()

    label1 = ctk.CTkLabel(new_window1, text="Imię:")
    label1.place(x=60, y=70)

    label2 = ctk.CTkLabel(new_window1, text="Nazwisko:")
    label2.place(x=60, y=130)

    label3 = ctk.CTkLabel(new_window1, text="Numer tel:")
    label3.place(x=60, y=190)

    label4 = ctk.CTkLabel(new_window1, text="Email:")
    label4.place(x=60, y=250)


    entry1=CTkEntry(master=new_window1, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    entry1.place(x=130, y=70)

    entry2=CTkEntry(master=new_window1, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    entry2.place(x=130, y=130)

    entry3=CTkEntry(master=new_window1, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    entry3.place(x=130, y=190)

    entry4=CTkEntry(master=new_window1, placeholder_text="Start typing...", width=200, text_color="#FFCC70")
    entry4.place(x=130, y=250)

    button_confirm=CTkButton(master=new_window1, text="Zatwierdź", command=close_window_and_confirm_data, corner_radius=12)
    button_confirm.place(relx=0.98, rely=0.98, anchor="se")
    

    button_cancel=CTkButton(master=new_window1, text="Anuluj", command=close_new_window1, corner_radius=12)
    button_cancel.place(relx=0.02, rely=0.98, anchor="sw")

    new_window1.mainloop()

    

#button_close.place(relx=1, rely=0, anchor="ne")    


def display_contact():
    print("Przycisk 2 został naciśnięty")
    app2=ctk.CTk()
    app2.title("Display contact")
    app2.geometry("400x400")

def edit_contact():
    print("Przycisk 3 został naciśnięty")
    app3=ctk.CTk()
    app3.title("Edit contact")
    app3.geometry("400x400")

def delete_contact():
    print("Przycisk 4 został naciśnięty")
    app4=ctk.CTk()
    app4.title("Delete contact")
    app4.geometry("400x400")

def save_to_file():
    print("ok")

def load_from_file():
    print("ok")


def close_app():
    app.destroy()






def close_window_and_confirm_data():
    print("ok")



    
button_close = ctk.CTkButton(master=app, text="Zamknij", command=close_app, corner_radius=12, fg_color="#a51b0b")
button_close.place(relx=1, rely=0, anchor="ne")

button1 = ctk.CTkButton(master=app, text="Dodaj kontakt", command=add_contact, width=200, height=50, corner_radius=12)
button1.pack(pady=10)

button2 = ctk.CTkButton(master=app, text="Wyświetl dane kontaktu", command=display_contact, width=200, height=50, corner_radius=12)
button2.pack(pady=10)

button3 = ctk.CTkButton(master=app, text="Edytuj kontakt", command=edit_contact, width=200, height=50, corner_radius=12)
button3.pack(pady=10)

button4 = ctk.CTkButton(master=app, text="Usuń kontakt", command=delete_contact, width=200, height=50, corner_radius=12)
button4.pack(pady=10)

button5 = ctk.CTkButton(master=app, text="Zapisz dane do pliku", command=save_to_file, width=200, height=50, corner_radius=12)
button5.pack(pady=10)

button6 = ctk.CTkButton(master=app, text="Odczytaj dane z pliku", command=load_from_file, width=200, height=50, corner_radius=12)
button6.pack(pady=10)

switch1=CTkSwitch(master=app, text="Tryb dla daltonistów")
switch1.place(relx=0.98, rely=0.98, anchor="se")


    


app.mainloop()