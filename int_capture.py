from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
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
import os
import time
from jnius import autoclass

from app_data import AppData

Context = autoclass('android.content.Context')
Environment = autoclass('android.os.Environment')
current_activity = autoclass('org.kivy.android.PythonActivity').mActivity
app_storage_path = current_activity.getExternalFilesDir(None).getAbsolutePath()


class IntCapture(Screen):
    """ 
    Classe du menu de prise de photo des intervenants
    """
    def __init__(self, **kwargs):
        """
        Visuel de la page de prise de photo des intervenants
        """
        super(IntCapture, self).__init__(**kwargs)

        self.media_path = os.path.join(app_storage_path, 'media')
        os.makedirs(self.media_path, exist_ok=True)

        self.top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.back_button = Button(text='Retour', size_hint=(0.3, None), height=100)
        self.back_button.bind(on_press=self.go_to_choix_categorie)
        self.top_layout.add_widget(self.back_button)

        self.media_grid = GridLayout(cols=2, spacing=20, size_hint=(1, 1))
        self.camera = Camera(resolution=(640, 480), size_hint=(1, 1), play=False)
        self.media_grid.add_widget(self.camera)

        self.file_view = FileChooserIconView(rootpath=self.media_path)
        self.media_grid.add_widget(self.file_view)

        self.top_layout.add_widget(self.media_grid)

        self.legend = TextInput(hint_text='Légende (à remplir avant capture)', size_hint=(1, None), height=100, multiline=False)
        self.top_layout.add_widget(self.legend)

        self.bottom_layout = GridLayout(cols=2, spacing=20, size_hint=(1, 1))
        self.capture_button = Button(text='Capturer', size_hint=(1, None), height=200) #, pos_hint={'center_x':0.5})
        self.capture_button.bind(on_press=self.take_picture)
        self.bottom_layout.add_widget(self.capture_button)

        self.submit_button = Button(text='Valider', size_hint=(1, None), height=200)
        self.submit_button.bind(on_press=self.submit_form)
        self.bottom_layout.add_widget(self.submit_button)

        self.top_layout.add_widget(self.bottom_layout)

        self.add_widget(self.top_layout)

    def take_picture(self, instance):
        """
        Enregistre le contenu du widget Camera dans un fichier PNG avec une légende
        Args:
          instance: arg de binding

        Returns:
          None
        """
        try:
            timestamp = str(int(time.time())) 
            img_name = f"{self.legend.text}-{timestamp}.png"
            file_name = os.path.join(self.media_path, f"{img_name}")
            # file_name = os.path.join("/media", f"{img_name}")
            self.camera.export_to_png(file_name)
            self.file_view.rootpath = self.media_path
            # self.file_view.rootpath = "/media"
            self.file_view._update_files()
            # app_data = AppData()
        except Exception as e:
            self.show_popup(f"Impossible d'enregistrer la photo : {e}")

    def link_data(self):
        """ 
        Met à jour la galerie de l'application
        """
        app_data = AppData()
        app_data.picture.clear()
        os.makedirs('./media/', exist_ok=True)
        # for file_name in os.listdir('./media'):
        for file_name in os.listdir(self.media_path):
        # for file_name in os.listdir('/media'):
            if file_name.endswith('.png'):
                app_data.picture.append(file_name)
        
        if len(app_data.picture) != 0: 
            app_data.is_galerie = True

    def submit_form(self, instance):
        """ 
        Valide la saisie utilisateur, sauvegarde et passe à l'écran suivant 
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.link_data()
        # app_data = AppData()
        # app_data.save_data()
        self.manager.current = 'int_recap_intervention'

    def on_enter(self, *args):
        """
        Allume la caméra à l'entrée de l'écran
        Args:
          *args: arg de binding

        Returns:

        """
        self.camera.play = True

    def on_leave(self, *args):
        """
        Etein la caméra à la sortie de l'écran
        Args:
          *args: arg de binding

        Returns:
          None
        """
        self.camera.play = False

    def go_to_choix_categorie(self, instance):
        """
        Eteint la caméra et passe à l'écran de recapitulatif d'intervention
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.camera.play = False
        self.manager.current = 'int_recap_intervention'

    def show_popup(self, message):
        """
        Permets d'afficher un message
        Args:
          message: message à afficher

        Returns:
          None
        """
        layout = BoxLayout(orientation='vertical')
        label = Label(text=message)
        dismiss_button = Button(text='Fermer')
        layout.add_widget(label)
        layout.add_widget(dismiss_button)

        popup = Popup(title='Information', content=layout, size_hint=(0.8, 0.4))
        dismiss_button.bind(on_press=popup.dismiss)
        popup.open()