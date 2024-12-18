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


class MainMenuDev(Screen):
    """ 
    Classe de debug pour les développeurs, menu intermédiaire
    """
    def __init__(self, **kwargs):
        super(MainMenuDev, self).__init__(**kwargs)

        layout = FloatLayout(size=(1, 1))

        layout.add_widget(Label(text="Choisissez le menu vers lequel vous souhaitez vous déplacer :", pos_hint={'x': 0, 'y': 0.3}))

        self.new_file_btn = Button(text="Partie BE", color=[1,1,1,1], size_hint=(0.3, 0.2), pos_hint={'x': 0.10, 'y': 0.50})
        self.new_file_btn.bind(on_press=self.go_to_BE)
        layout.add_widget(self.new_file_btn)

        self.new_file_modif = Button(text="Partie intervenant", color=[1, 1, 1, 1], size_hint=(0.3, 0.2),
                                   pos_hint={'x': 0.60, 'y': 0.50})
        self.new_file_modif.bind(on_press=self.go_to_modif_affaire)
        layout.add_widget(self.new_file_modif)

        self.add_widget(layout)


    def go_to_BE(self, instance):
        """

        Args:
          instance: 

        Returns:

        """
        app_data = AppData()
        self.manager.current = 'main_menu'

    def go_to_modif_affaire(self, instance):
        """

        Args:
          instance: 

        Returns:

        """
        app_data = AppData()
        self.manager.current = 'main_menu_int'