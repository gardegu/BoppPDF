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


class ChoixCategorie(Screen):
    """ 
    Classe du menu Choix de la catégorie du BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu Choix de la catégorie
        """
        super(ChoixCategorie, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=4, padding=20, spacing=20, size_hint=(1,1))

        self.back_btn = Button(text="Retour", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_carac_affaire)
        top_layout.add_widget(self.back_btn)

        self.local_machine_btn = Button(text="Local Machine", color=[1,1,1,1], size_hint=(0.5, 0.2))
        self.local_machine_btn.bind(on_press=self.go_to_local_machine)
        layout.add_widget(self.local_machine_btn)

        self.treuils_btn = Button(text="Treuils", color=[1,1,1,1], size_hint=(0.5, 0.2))
        self.treuils_btn.bind(on_press=self.go_to_treuils)
        layout.add_widget(self.treuils_btn)

        self.cabestan_btn = Button(text="Cabestan", color=[1,1,1,1], size_hint=(0.5, 0.2))
        self.cabestan_btn.bind(on_press=self.go_to_cabestan)
        layout.add_widget(self.cabestan_btn)

        self.appareil_gouverne_btn = Button(text="Appareil à Gouverner", color=[1,1,1,1], size_hint=(0.5, 0.2))
        self.appareil_gouverne_btn.bind(on_press=self.go_to_appareil_gouverne)
        layout.add_widget(self.appareil_gouverne_btn)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # self.capture_and_submit_layout = GridLayout(cols=2, padding=20, spacing=20, size_hint=(1,0.2))
        # self.capture_btn = Button(text="Prendre une photo", color=[1,1,1,1], size_hint=(0.3,0.2))
        # self.capture_btn.bind(on_press=self.go_to_capture)
        # self.capture_and_submit_layout.add_widget(self.capture_btn)
        # self.closure_btn = Button(text="Valider affaire", color=[1,1,1,1], size_hint=(0.3,0.2))
        # self.closure_btn.bind(on_press=self.go_to_closure)
        # self.capture_and_submit_layout.add_widget(self.closure_btn)

        # top_layout.add_widget(self.capture_and_submit_layout)

        self.closure_btn = Button(text="Valider affaire", color=[1,1,1,1], size_hint=(0.3,0.2), pos_hint={'center_x': 0.5})
        self.closure_btn.bind(on_press=self.go_to_closure)
        top_layout.add_widget(self.closure_btn)
        
        self.add_widget(top_layout)

    def go_to_local_machine(self, instance):
        """
        Passe à l'écran Local Machine
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        self.manager.current = 'local_machine'
    
    def go_to_treuils(self, instance):
        """ 
        Passe à l'écran Treuils
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        self.manager.current = 'treuils'

    def go_to_cabestan(self, instance):
        """
        Passe à l'écran Cabestan
        Args:
          instance: argument nécessaire pour le binding de la fonction  

        Returns:
          None
        """
        self.manager.current = 'cabestan'

    def go_to_appareil_gouverne(self, instance):
        """
        Passe à l'écran Appareil à Gouverner
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        self.manager.current = 'appareil_gouverne'

    def go_to_carac_affaire(self, instance):
        """
        Passe à l'écran Caractéristiques de l'affaire
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        self.manager.current = 'carac_affaire'

    def go_to_closure(self, instance):
        """
        Passe à l'écran validation
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        self.manager.current = 'closure'

    def go_to_capture(self, instance):
        """
        Passe à l'écran prise de photo (plus possible pour le BE)
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        # self.manager.current = 'capture'
        pass
