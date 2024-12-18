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


class MainMenu(Screen):
    """ 
    Classe du menu principal pour le BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu principal du BE
        """
        super(MainMenu, self).__init__(**kwargs)

        layout = FloatLayout(size=(1, 1))

        self.new_file_btn = Button(text="Créer une affaire", color=[1,1,1,1], size_hint=(0.3, 0.2), pos_hint={'x': 0.01, 'y': 0.55})
        self.new_file_btn.bind(on_press=self.go_to_carac_affaire)
        layout.add_widget(self.new_file_btn)

        self.new_file_modif = Button(text="Modifier une affaire", color=[1, 1, 1, 1], size_hint=(0.3, 0.2),
                                   pos_hint={'x': 0.35, 'y': 0.55})
        self.new_file_modif.bind(on_press=self.go_to_modif_affaire)
        layout.add_widget(self.new_file_modif)

        self.new_file_supp = Button(text="Supprimer une affaire", color=[1, 1, 1, 1], size_hint=(0.3, 0.2),
                                   pos_hint={'x': 0.69, 'y': 0.55})
        self.new_file_supp.bind(on_press=self.go_to_supp_affaire)
        layout.add_widget(self.new_file_supp)

        self.back_btn = Button(text="Retour", color=[1,1,1,1], size_hint=(0.3, 0.2), pos_hint={'x': 0.01, 'y': 0.01})
        self.back_btn.bind(on_press=self.go_to_connexion)
        layout.add_widget(self.back_btn)

        self.add_widget(layout)


    def go_to_carac_affaire(self, instance):
        """
        Passe au menu de caractérisation de l'affaire du BE
        Args:
          instance: agr de binding

        Returns:
          None
        """
        app_data = AppData()
        self.manager.current = 'carac_affaire'

    def go_to_modif_affaire(self, instance):
        """
        Passe au menu de modification d'affaire du BE
        Args:
          instance: arg de binding

        Returns:
          None
        """
        app_data = AppData()
        self.manager.current = 'modif_affaire'

    def go_to_supp_affaire(self, instance):
        """
        Passe au menu de suppression d'affaire du BE
        Args:
          instance: arg de binding

        Returns:
          None
        """
        app_data = AppData()
        self.manager.current = 'supp_affaire'

    def go_to_connexion(self, instance):
        """
        Retourne au menu de connexion de l'application
        Args:
          instance: 

        Returns:

        """
        self.manager.current='connexion'