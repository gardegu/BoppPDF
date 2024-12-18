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
import os

from app_data import AppData
# from make_pdf import pdfMaker
from writePDF import pdfWriter



class Closure(Screen):
    """ 
    Classe du menu de validation du BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu de validation du BE
        """
        super(Closure, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=3, padding=20, spacing=20, size_hint=(1,1))

        self.back_btn = Button(text="Retour", size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_choix_categorie)
        layout.add_widget(self.back_btn)

        self.pdf_btn = Button(text="Générer le PDF de l'affaire", size_hint=(0.3, 0.2))
        self.pdf_btn.bind(on_press=self.go_to_make_pdf)
        layout.add_widget(self.pdf_btn)

        self.exit_btn = Button(text="Quitter", size_hint=(0.3, 0.2))
        self.exit_btn.bind(on_press=self.go_to_exit)
        layout.add_widget(self.exit_btn)

        self.menu_btn = Button(text="Retour au menu principal", size_hint=(0.3, 0.2))
        self.menu_btn.bind(on_press=self.go_to_main_menu)
        layout.add_widget(self.menu_btn)

        scrollView.add_widget(layout)

        top_layout.add_widget(scrollView)

        # self.file_view = FileChooserIconView(rootpath=os.getcwd())
        # top_layout.add_widget(self.file_view)

        self.add_widget(top_layout)

    def go_to_choix_categorie(self, instance):
        """
        Passer à l'écran de choix de catégorie
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        app_data = AppData()
        app_data.save_data()
        self.manager.current = 'choix_categorie'

    def go_to_make_pdf(self, instance):
        """
        Sauvegarde les données et génère le PDF
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        app_data = AppData()
        app_data.save_data()
        # pdf_maker = pdfMaker()
        # pdf_maker.execute()
        pdf_writer = pdfWriter()
        pdf_writer.execute()
        # self.file_view._update_files()
        # if os.path.exists('./media'):
        #     try:
        #         shutil.rmtree('./media')
        #     except Exception as e:
        #         self.show_popup(f"Erreur lors de la suppression des photos : {e}")
        #     os.makedirs('./media', exist_ok=True)

    def go_to_exit(self, instance):
        """
        Passe à l'écran de connexion
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        app_data = AppData()
        app_data.save_data()
        self.manager.current = 'connexion'

    def go_to_main_menu(self, instance):
        """
        Passe au menu principal
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
          None
        """
        app_data = AppData()
        app_data.save_data()
        self.manager.current = 'main_menu'