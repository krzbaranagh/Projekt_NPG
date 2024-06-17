import pickle
import customtkinter as ctk
from customtkinter import *
from data_contact import *
import data_variable

def add_contacts_group() -> None:
    
    def close_add_contacts_group_window() -> None:
        add_contacts_group_window.destroy()

    def save_and_close_window() -> None:

        name = name_entry.get()
