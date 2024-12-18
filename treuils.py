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



class Treuils(Screen):
    """ 
    Classe du menu treuil pour le BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu treuil
        """
        super(Treuils, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        scrollView = ScrollView(size_hint=(1, 1))

        layout = GridLayout(cols=2, padding=50, spacing=35, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))    

        self.back_btn = Button(text="Retour", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_choix_categorie)
        top_layout.add_widget(self.back_btn)

        layout.add_widget(Label(text="TPH125 0 traction premiere couche statique :"))
        self.TPH125_0_traction_premiere_couche_statique = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_traction_premiere_couche_statique)

        layout.add_widget(Label(text="TPH125 0 traction premiere couche dynamique :"))
        self.TPH125_0_traction_premiere_couche_dynamique = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_traction_premiere_couche_dynamique)

        layout.add_widget(Label(text="TPH125 0 pression :"))
        self.TPH125_0_pression = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_pression)

        layout.add_widget(Label(text="TPH125 0 vitesse rotation PV :"))
        self.TPH125_0_vitesse_rotation_PV = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_vitesse_rotation_PV)

        layout.add_widget(Label(text="TPH125 0 vitesse rotation GV :"))
        self.TPH125_0_vitesse_rotation_GV = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_vitesse_rotation_GV)

        layout.add_widget(Label(text="TPH125 0 debit :"))
        self.TPH125_0_debit = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_debit)

        layout.add_widget(Label(text="TPH125 0 essai file vire :"))
        self.TPH125_0_essai_file_vire = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_essai_file_vire)

        layout.add_widget(Label(text="TPH125 0 essai freinage :"))
        self.TPH125_0_essai_freinage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_essai_freinage)

        layout.add_widget(Label(text="TPH125 0 selection PV GV :"))
        self.TPH125_0_selection_PV_GV = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_selection_PV_GV)

        layout.add_widget(Label(text="TPH50 0 traction premiere couche statique :"))
        self.TPH50_0_traction_premiere_couche_statique = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_traction_premiere_couche_statique)

        layout.add_widget(Label(text="TPH50 0 traction premiere couche dynamique :"))
        self.TPH50_0_traction_premiere_couche_dynamique = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_traction_premiere_couche_dynamique)

        layout.add_widget(Label(text="TPH50 0 pression :"))
        self.TPH50_0_pression = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_pression)

        layout.add_widget(Label(text="TPH50 0 vitesse rotation PV :"))
        self.TPH50_0_vitesse_rotation_PV = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_vitesse_rotation_PV)

        layout.add_widget(Label(text="TPH50 0 vitesse rotation GV :"))
        self.TPH50_0_vitesse_rotation_GV = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_vitesse_rotation_GV)

        layout.add_widget(Label(text="TPH50 0 debit :"))
        self.TPH50_0_debit = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_debit)

        layout.add_widget(Label(text="TPH50 0 essai file vire :"))
        self.TPH50_0_essai_file_vire = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_essai_file_vire)

        layout.add_widget(Label(text="TPH50 0 essai freinage :"))
        self.TPH50_0_essai_freinage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_essai_freinage)

        layout.add_widget(Label(text="TPH50 0 selection PV GV :"))
        self.TPH50_0_selection_PV_GV = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_selection_PV_GV)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # Bouton Valider
        self.submit_btn = Button(text="Valider", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.submit_form)
        top_layout.add_widget(self.submit_btn)

        self.add_widget(top_layout)

    def link_data(self):
        """ 
        Met à jour les données de l'application avec les données entrées par l'utilisateur
        """
        app_data = AppData()
        self.case_number = app_data.case_number
        
        app_data.TPH125_0_traction_premiere_couche_statique = self.TPH125_0_traction_premiere_couche_statique.text
        app_data.TPH125_0_traction_premiere_couche_dynamique = self.TPH125_0_traction_premiere_couche_dynamique.text
        app_data.TPH125_0_pression = self.TPH125_0_pression.text
        app_data.TPH125_0_vitesse_rotation_PV = self.TPH125_0_vitesse_rotation_PV.text
        app_data.TPH125_0_vitesse_rotation_GV = self.TPH125_0_vitesse_rotation_GV.text
        app_data.TPH125_0_debit = self.TPH125_0_debit.text
        app_data.TPH125_0_essai_file_vire = self.TPH125_0_essai_file_vire.text
        app_data.TPH125_0_essai_freinage = self.TPH125_0_essai_freinage.text
        app_data.TPH125_0_selection_PV_GV = self.TPH125_0_selection_PV_GV.text
        app_data.TPH50_0_traction_premiere_couche_statique = self.TPH50_0_traction_premiere_couche_statique.text
        app_data.TPH50_0_traction_premiere_couche_dynamique = self.TPH50_0_traction_premiere_couche_dynamique.text
        app_data.TPH50_0_pression = self.TPH50_0_pression.text
        app_data.TPH50_0_vitesse_rotation_PV = self.TPH50_0_vitesse_rotation_PV.text
        app_data.TPH50_0_vitesse_rotation_GV = self.TPH50_0_vitesse_rotation_GV.text
        app_data.TPH50_0_debit = self.TPH50_0_debit.text
        app_data.TPH50_0_essai_file_vire = self.TPH50_0_essai_file_vire.text
        app_data.TPH50_0_essai_freinage = self.TPH50_0_essai_freinage.text
        app_data.TPH50_0_selection_PV_GV = self.TPH50_0_selection_PV_GV.text


    def submit_form(self, instance):
        """
        Enregistre les données entrées par l'utilisateur et passe à l'écran du choix de catégorie du BE
        Args:
          instance: arg de binding

        Returns:
          None
        """
        self.link_data()
        app_data = AppData()
        app_data.save_data()
        self.manager.current = 'choix_categorie'

    def go_to_choix_categorie(self, instance):
        """
        Retourne à l'écran du choix de catégorie du BE
        Args:
          instance: 

        Returns:

        """
        app_data = AppData()
        app_data.save_data()
        self.manager.current = 'choix_categorie'

