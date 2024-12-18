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



class ModifCabestan(Screen):
    """ 
    Classe du menu cabestan du BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu cabestan du BE
        """
        super(ModifCabestan, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout2 = GridLayout(cols=2, padding=20, spacing=20, size_hint=(1, 0.2))
        layout2.bind(minimum_height=layout2.setter('height'))

        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=2, padding=50, spacing=35, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))


        self.back_btn = Button(text="Retour", color=[1, 1, 1, 1], height=30)
        self.back_btn.bind(on_press=self.go_to_modif_choix_categorie)
        layout2.add_widget(self.back_btn)

        layout2.add_widget(Label(text="Cabestan", size_hint=(1, None), height=100, bold=True, font_size=40)) 

        layout.add_widget(Label(text="5T traction statique :"))
        self.Cb_5T_traction_statique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_traction_statique)

        layout.add_widget(Label(text="5T traction dynamique :"))
        self.Cb_5T_traction_dynamique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_traction_dynamique)

        layout.add_widget(Label(text="5T pression :"))
        self.Cb_5T_pression = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_pression)

        layout.add_widget(Label(text="5T vitesse rotation :"))
        self.Cb_5T_vitesse_rotation = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_vitesse_rotation)

        layout.add_widget(Label(text="5T debit :"))
        self.Cb_5T_debit = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_debit)

        layout.add_widget(Label(text="5T essai file vire :"))
        self.Cb_5T_essai_file_vire = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_essai_file_vire)

        layout.add_widget(Label(text="5T freinage :"))
        self.Cb_5T_freinage = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_5T_freinage)

        layout.add_widget(Label(text="3T traction statique :"))
        self.Cb_3T_traction_statique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_traction_statique)

        layout.add_widget(Label(text="3T traction dynamique :"))
        self.Cb_3T_traction_dynamique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_traction_dynamique)

        layout.add_widget(Label(text="3T pression :"))
        self.Cb_3T_pression = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_pression)

        layout.add_widget(Label(text="3T vitesse rotation :"))
        self.Cb_3T_vitesse_rotation = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_vitesse_rotation)

        layout.add_widget(Label(text="3T debit :"))
        self.Cb_3T_debit = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_debit)

        layout.add_widget(Label(text="3T essai file vire :"))
        self.Cb_3T_essai_file_vire = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_essai_file_vire)

        layout.add_widget(Label(text="3T freinage :"))
        self.Cb_3T_freinage = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.Cb_3T_freinage)

        top_layout.add_widget(layout2)
        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # Bouton Valider
        self.submit_btn = Button(text="Valider", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.submit_form)
        top_layout.add_widget(self.submit_btn)
        
        self.add_widget(top_layout)

    def update(self):
        """ 
        Affichage des données précédentes de l'affaire
        """
        app_data = AppData()
        self.Cb_5T_traction_statique.text = app_data.data["Cb_5T_traction_statique"]
        self.Cb_5T_traction_dynamique.text = app_data.data["Cb_5T_traction_dynamique"]
        self.Cb_5T_pression.text = app_data.data["Cb_5T_pression"]
        self.Cb_5T_vitesse_rotation.text = app_data.data["Cb_5T_vitesse_rotation"]
        self.Cb_5T_debit.text = app_data.data["Cb_5T_debit"]
        self.Cb_5T_essai_file_vire.text = app_data.data["Cb_5T_essai_file_vire"]
        self.Cb_5T_freinage.text = app_data.data["Cb_5T_freinage"]
        self.Cb_3T_traction_statique.text = app_data.data["Cb_3T_traction_statique"]
        self.Cb_3T_traction_dynamique.text = app_data.data["Cb_3T_traction_dynamique"]
        self.Cb_3T_pression.text = app_data.data["Cb_3T_pression"]
        self.Cb_3T_vitesse_rotation.text = app_data.data["Cb_3T_vitesse_rotation"]
        self.Cb_3T_debit.text = app_data.data["Cb_3T_debit"]
        self.Cb_3T_essai_file_vire.text = app_data.data["Cb_3T_debit"]
        self.Cb_3T_freinage.text = app_data.data["Cb_3T_freinage"]

        self.Cb_5T_traction_statique.hint_text = app_data.data["Cb_5T_traction_statique"]
        self.Cb_5T_traction_dynamique.hint_text = app_data.data["Cb_5T_traction_dynamique"]
        self.Cb_5T_pression.hint_text = app_data.data["Cb_5T_pression"]
        self.Cb_5T_vitesse_rotation.hint_text = app_data.data["Cb_5T_vitesse_rotation"]
        self.Cb_5T_debit.hint_text = app_data.data["Cb_5T_debit"]
        self.Cb_5T_essai_file_vire.hint_text = app_data.data["Cb_5T_essai_file_vire"]
        self.Cb_5T_freinage.hint_text = app_data.data["Cb_5T_freinage"]
        self.Cb_3T_traction_statique.hint_text = app_data.data["Cb_3T_traction_statique"]
        self.Cb_3T_traction_dynamique.hint_text = app_data.data["Cb_3T_traction_dynamique"]
        self.Cb_3T_pression.hint_text = app_data.data["Cb_3T_pression"]
        self.Cb_3T_vitesse_rotation.hint_text = app_data.data["Cb_3T_vitesse_rotation"]
        self.Cb_3T_debit.hint_text = app_data.data["Cb_3T_debit"]
        self.Cb_3T_essai_file_vire.hint_text = app_data.data["Cb_3T_debit"]
        self.Cb_3T_freinage.hint_text = app_data.data["Cb_3T_freinage"]

    def on_enter(self, *args):
        """
        Mise à jour des données à chaque entrée dans la page
        Args:
          *args: 

        Returns:

        """
        self.update()


    def link_data(self):
        """ 
        Met à jour les données de l'application avec les données entrées par l'utilisateur
        """
        app_data = AppData()
        self.case_number = app_data.case_number

        app_data.Cb_5T_traction_statique = self.Cb_5T_traction_statique.text
        app_data.Cb_5T_traction_dynamique = self.Cb_5T_traction_dynamique.text
        app_data.Cb_5T_pression = self.Cb_5T_pression.text
        app_data.Cb_5T_vitesse_rotation = self.Cb_5T_vitesse_rotation.text
        app_data.Cb_5T_debit = self.Cb_5T_debit.text
        app_data.Cb_5T_essai_file_vire = self.Cb_5T_essai_file_vire.text
        app_data.Cb_5T_freinage = self.Cb_5T_freinage.text
        app_data.Cb_3T_traction_statique = self.Cb_3T_traction_statique.text
        app_data.Cb_3T_traction_dynamique = self.Cb_3T_traction_dynamique.text
        app_data.Cb_3T_pression = self.Cb_3T_pression.text
        app_data.Cb_3T_vitesse_rotation = self.Cb_3T_vitesse_rotation.text
        app_data.Cb_3T_debit = self.Cb_3T_debit.text
        app_data.Cb_3T_essai_file_vire = self.Cb_3T_essai_file_vire.text
        app_data.Cb_3T_freinage = self.Cb_3T_freinage.text

    def submit_form(self, instance):
        """
        Enregistre les données entrées par l'utilisateur et passe à la page suivante
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_modif_cabestan()
        self.manager.current = 'modif_appareil_gouverne'

    def go_to_modif_choix_categorie(self, instance):
        """
        Retourne au menu précédent
        Args:
          instance: 

        Returns:

        """
        # app_data = AppData()
        # app_data.save_data_modif_cabestan()
        self.manager.current = 'modif_treuils'
