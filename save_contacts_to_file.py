import pickle
import os
import customtkinter as ctk
from customtkinter import *

import data_contact

def save_contacts_to_file(ksiazka):
    current_dir = os.path.dirname(os.path.abspath(__file__)) #ustalanie bieżącego katalogu
    file_path = os.path.join(current_dir, 'kontakty.txt') #znajdowanie pliku do którego będą zapisywane kontakty
