from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
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
from PIL import Image as PilImage  # Pillow pour le traitement d'images (si nécessaire)
from kivy.lang import Builder
import shutil
import json

from app_data import AppData

directory = ""

class IntRecapInter(Screen):
    """ 
    Classe du menu de récapitulatif d'intervention pour les intervenants
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu de récapitulatif d'intervention pour les intervenants
        """
        super(IntRecapInter, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=2, padding=20, spacing=20, size_hint=(1,1))
        layout2 = GridLayout(cols=1, padding=20, spacing=20, size_hint=(1,1))

        self.back_btn = Button(text="Retour", color=[1,1,1,1], height=30)
        self.back_btn.bind(on_press=self.go_to_int_choix_categorie)
        layout.add_widget(self.back_btn)

        layout.add_widget(Label(text="Récapitulatif d'intervention", size_hint=(1, None), height=30, bold=True, font_size=40)) 

        layout.add_widget(Label(text="Pièces changées :"))
        self.pieces_changees = TextInput(hint_text="Entrer les pièces changées", multiline=False)
        layout.add_widget(self.pieces_changees)

        layout.add_widget(Label(text="Pièces cassées :"))
        self.pieces_cassees = TextInput(hint_text="Entrer les pièces cassées", multiline=False)
        layout.add_widget(self.pieces_cassees)

        layout.add_widget(Label(text="Temps passé :"))
        self.temps_passe = TextInput(hint_text="Entrer le temps passé", multiline=False)
        layout.add_widget(self.temps_passe)

        layout.add_widget(Label(text="Temps mort :"))
        self.temps_mort = TextInput(hint_text="Entrer le temps mort", multiline=False)
        layout.add_widget(self.temps_mort)

        layout.add_widget(Label(text="Commentaires :"))
        self.commentaires = TextInput(hint_text="Entrer les commentaires", multiline=False)
        layout.add_widget(self.commentaires)

        self.capture_btn = Button(text="Prendre une photo", color=[1,1,1,1], size_hint=(0.3,0.2))
        self.capture_btn.bind(on_press=self.go_to_capture)
        layout2.add_widget(self.capture_btn)
        layout.add_widget(layout2)

        self.closure_btn = Button(text="Sauvegarder l'affaire", color=[1, 1, 1, 1])
        self.closure_btn.bind(on_press=self.go_to_save)
        layout.add_widget(self.closure_btn)

        self.closure_btn = Button(text="Valider affaire", color=[1, 1, 1, 1])
        self.closure_btn.bind(on_press=self.go_to_finish)
        layout.add_widget(self.closure_btn)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        self.add_widget(top_layout)

    def on_enter(self, *args):
        """
        Récupère et affiche les données précédemment enregistrées
        Args:
          *args: arg de binding

        Returns:
          None
        """
        self.update()

    def update(self):
        """ 
        Affiche les données précédemment enregistrées
        """
        app_data = AppData()
        self.pieces_changees.text = app_data.data["int_pieces_changees"]
        self.pieces_changees.hint_text = app_data.data["int_pieces_changees"]
        self.pieces_cassees.text = app_data.data["int_pieces_cassees"]
        self.pieces_cassees.hint_text = app_data.data["int_pieces_cassees"]
        self.temps_mort.text = app_data.data["int_temps_mort"]
        self.temps_mort.hint_text = app_data.data["int_temps_mort"]
        self.temps_passe.text = app_data.data["int_temps_passe"]
        self.temps_passe.hint_text = app_data.data["int_temps_passe"]
        self.commentaires.text = app_data.data["int_commentaires"]
        self.commentaires.hint_text = app_data.data["int_commentaires"]

    def link_data(self):
        """ 
        Enregistre les données entrées par l'utilisateur
        """
        app_data = AppData()

        app_data.int_pieces_changees = self.pieces_changees.text
        app_data.int_pieces_cassees = self.pieces_cassees.text
        app_data.int_temps_passe = self.temps_passe.text
        app_data.int_temps_mort = self.temps_mort.text
        app_data.int_commentaires = self.commentaires.text

    def go_to_int_choix_categorie(self, instance):
        """
        Passe au menu de choix de catégorie pour les intervenants
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.manager.current = 'int_appareil_gouverne'

    def go_to_save(self, instance):
        """
        Enregistre les données et passe au menu de choix de l'affaire pour les intervenants
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_int_recap()
        app_data.int_finale(directory)
        self.manager.current = 'main_menu_int'

    def go_to_finish(self, instance):
        """
        Enregistre les données et passe au menu de validation pour les intervenants
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_int_recap()
        app_data.int_finale(directory)
        self.manager.current = 'int_sauvegarder'

    def go_to_capture(self, instance):
        """   
        Passe au menu de prise de photo pour les intervenants
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.manager.current = 'int_capture'