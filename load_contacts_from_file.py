import pickle
import os
import customtkinter as ctk
from customtkinter import *

import data_contact

def load_contacts_from_txt(ksiazka):
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(current_dir, 'kontakty.txt')
