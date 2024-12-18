import glob
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.spinner import Spinner
from kivy.graphics import *
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.core.window import Window
from PIL import Image as PilImage  # Pillow pour le traitement d'images (si nécessaire)
from kivy.lang import Builder
import shutil
import json
from kivy.properties import StringProperty
import int_recap_intervention

from modif_carac_affaire import *
from app_data import AppData

nom_etude = ""
num_affaire = ""
nom_client = ""
nom_bateau = ""
nb = ""
nom_chantier = ""
type_intervention = ""
direc = ""


class MainMenuInt(Screen):
    """ 
    Classe du menu principal des intervenants
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu principal des intervenants
        """
        super(MainMenuInt, self).__init__(**kwargs)

        layout = FloatLayout(size=(1, 1))

        os.makedirs("./data", exist_ok=True)
        files_names = [f for f in os.listdir("./data")]
        liste_affaires = []
        for x in files_names:
            liste_affaires.append(x[4:len(x) - 5])

        app_data = AppData()

        layout = FloatLayout(size=(1, 1))

        # self.back_btn = Button(text="Retour", color=[1, 1, 1, 1], pos_hint={'x': 0.01, 'y': .75}, size_hint=(0.3, 0.2))
        # self.back_btn.bind(on_press=self.go_to_main_menu)
        # layout.add_widget(self.back_btn)

        # Type d'intervention (liste déroulante)
        self.intervention_type = Spinner(
            text="Sélectionnez l'affaire à modifier", color=[1, 1, 1, 1], pos_hint={'x': 0.5, 'y': 0.75},
            size_hint=(0.49, 0.2),
            values=(f'{x}' for x in liste_affaires))
        layout.add_widget(self.intervention_type)
        self.intervention_type.bind(text=self.on_spinner_select)
        self.spinnerSelection = Label(text="Selected value in spinner is: %s" % self.intervention_type.text)

        self.submit_btn = Button(text="Valider", color=(1, 1, 1, 1), pos_hint={'x': 0.01, 'y': 0.01},
                                 size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.go_to_int_carac)
        layout.add_widget(self.submit_btn)

        self.add_widget(layout)

    # def go_to_main_menu(self, instance):
    #     app_data = AppData()
    #     app_data.save_data()
    #     self.manager.current = 'main_menu_int'

    def go_to_int_carac(self, instance):
        """
        Passe au menu de caractérisation de l'affaire choisie par l'intervenant
        Args:
          instance: arg de binding

        Returns:
            None
        """
        app_data = AppData()
        self.manager.current = 'int_carac_affaire'

    def on_spinner_select(self, spinner, text):
        """
        Permet de choisir un affaire depuis un menu déroulant
        Args:
          spinner: widget spinner
          text: 

        Returns:

        """
        self.spinnerSelection.text = "Selected value in spinner is: %s" % self.intervention_type.text
        self.etude = str(self.intervention_type.text)
        direc = "./data/data" + self.etude + ".json"
        int_recap_intervention.directory = direc
        app_data = AppData()
        app_data.update(direc)