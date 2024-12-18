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

from app_data import AppData

class SupprimerAffaire(Screen):
    """ 
    Classe du menu de suppression d'une affaire pour le BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu de suppression d'une affaire
        """
        super(SupprimerAffaire, self).__init__(**kwargs)
        self.path = ""

        # Liste les fichiers du dossier "./data"
        liste_affaires = [f for f in os.listdir("./data") if os.path.isfile(os.path.join("./data", f))]

        app_data = AppData()

        layout = FloatLayout(size=(1, 1))

        # Bouton "Retour"
        self.back_btn = Button(text="Retour", color=[1, 1, 1, 1], pos_hint={'x': 0.01, 'y': .75}, size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_main_menu)
        layout.add_widget(self.back_btn)

        # Spinner pour sélectionner un fichier
        self.intervention_type = Spinner(
            text="Sélectionnez l'affaire à supprimer", color=[1, 1, 1, 1], pos_hint={'x': 0.5, 'y': 0.75}, size_hint=(0.49, 0.2),
            values=tuple(liste_affaires))
        layout.add_widget(self.intervention_type)
        self.intervention_type.bind(text=self.on_spinner_select)

        # Bouton "Valider"
        self.submit_btn = Button(text="Valider", color=(1, 1, 1, 1), pos_hint={'x': 0.01, 'y': 0.01}, size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.supp)
        layout.add_widget(self.submit_btn)

        self.add_widget(layout)

    def go_to_main_menu(self, instance):
        """
        Passe à l'écran du menu principal
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.manager.current = 'main_menu'

    def on_spinner_select(self, spinner, text):
        """
        Enregistre la valeur sélectionnée dans le menu déroulant
        Args:
          spinner: 
          text: 

        Returns:
          None
        """
        # Stocke le chemin complet du fichier sélectionné
        self.path = os.path.join("./data", text)

    def supp(self, instance):
        """
        Supprime l'affaire sélectionnée
        Args:
          instance: argument lié au binding (non utilisé ici)

        Returns:
          None
        """
        if self.path and os.path.exists(self.path):
            os.remove(self.path)
            # print(f"Fichier supprimé : {self.path}")
        else:
            # print("Erreur : aucun fichier sélectionné ou le fichier n'existe pas.")
            pass
        self.intervention_type._update_dropdown()
        # Retourne au menu principal après la suppression
        self.go_to_main_menu(instance)
