from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
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

class ModifCaracAffaire(Screen):
    """ 
    Classe du menu de caractérisation de l'affaire pour le BE
    """
    def __init__(self,  **kwargs):
        """
        Visuel du menu
        """
        super(ModifCaracAffaire, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        scrollView = ScrollView(size_hint=(1, 1))

        layout = GridLayout(cols=2, padding=50, spacing=35, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        self.back_btn = Button(text="Retour", color=[1, 1, 1, 1], size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_main_menu)
        layout.add_widget(self.back_btn)

        layout.add_widget(Label(text="Caractérisation affaire", size_hint=(1, None), height=30, bold=True, font_size=40))

        # Numéro d'affaire ou d'appel
        layout.add_widget(Label(text="Numéro d'affaire ou d'appel :"))
        self.case_number = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.case_number)

        # Nom du client
        layout.add_widget(Label(text="Nom du client :"))
        self.client_name = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.client_name)

        # Nom du bateau
        layout.add_widget(Label(text="Nom du bateau :"))
        self.boat_name = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.boat_name)

        # NB
        layout.add_widget(Label(text="NB :"))
        self.nb_field = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.nb_field)

        # Nom du chantier
        layout.add_widget(Label(text="Nom du chantier :"))
        self.site_name = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.site_name)

        # Armement
        layout.add_widget(Label(text="Armement :"))
        self.armement = TextInput(hint_text="Entrez l'armement", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.armement)

        # Bopp name
        layout.add_widget(Label(text="BOPP name :"))
        self.bopp_name = TextInput(hint_text="BOPP name", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.bopp_name)

        #Bopp date
        layout.add_widget(Label(text="BOPP date :"))
        self.bopp_date = TextInput(hint_text="BOPP date", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.bopp_date)

        #Bopp visa
        layout.add_widget(Label(text="BOPP visa :"))
        self.bopp_visa = TextInput(hint_text="BOPP visa", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.bopp_visa)

        # Chantier name
        layout.add_widget(Label(text="Chantier name :"))
        self.chantier_name = TextInput(hint_text="Chantier name", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.chantier_name)

        # Chantier date
        layout.add_widget(Label(text="Chantier date :"))
        self.chantier_date = TextInput(hint_text="Chantier date", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.chantier_date)

        # Chantier visa
        layout.add_widget(Label(text="Chantier visa :"))
        self.chantier_visa = TextInput(hint_text="Chantier visa", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.chantier_visa)

        # Armement name
        layout.add_widget(Label(text="Armement name :"))
        self.armement_name = TextInput(hint_text="Armement name", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.armement_name)

        # Armement date
        layout.add_widget(Label(text="Armement date :"))
        self.armement_date = TextInput(hint_text="Armement date", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.armement_date)

        # Armement visa
        layout.add_widget(Label(text="Armement visa :"))
        self.armement_visa = TextInput(hint_text="Armement visa", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.armement_visa)

        # Type d'intervention (liste déroulante)
        layout.add_widget(Label(text="Type d'intervention :"))
        self.intervention_type = Spinner(
            text="", color=[1, 1, 1, 1],
            values=("Mise en service", "Garantie", "SAV"),
            size_hint=(1, None), 
            height=100)
        layout.add_widget(self.intervention_type)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # Bouton Valider
        self.submit_btn = Button(text="Valider", color=[1, 1, 1, 1], size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.submit_form)
        top_layout.add_widget(self.submit_btn)

        self.add_widget(top_layout)

    def update(self):
        """ 
        Récupération des anciennes données de l'affaire
        """
        app_data = AppData()
        self.case_number.text = app_data.data["case_number"]
        self.case_number.hint_text = app_data.data["case_number"]
        self.client_name.text = app_data.data["client_name"]
        self.client_name.hint_text = app_data.data["client_name"]
        self.boat_name.text = app_data.data["boat_name"]
        self.boat_name.hint_text = app_data.data["boat_name"]
        self.nb_field.text = app_data.data["nb_field"]
        self.nb_field.hint_text = app_data.data["nb_field"]
        self.site_name.text = app_data.data["site_name"]
        self.site_name.hint_text = app_data.data["site_name"]
        self.armement.text = app_data.data["armement"]
        self.armement.hint_text = app_data.data["armement"]
        self.bopp_name.text = app_data.data["BOPP_name"]
        self.bopp_name.hint_text = app_data.data["BOPP_name"]
        self.bopp_date.text = app_data.data["BOPP_date"]
        self.bopp_date.hint_text = app_data.data["BOPP_date"]
        self.bopp_visa.text = app_data.data["BOPP_visa"]
        self.bopp_visa.hint_text = app_data.data["BOPP_visa"]
        self.chantier_name.text = app_data.data["chantier_name"]
        self.chantier_name.hint_text = app_data.data["chantier_name"]
        self.chantier_date.text = app_data.data["chantier_date"]
        self.chantier_date.hint_text = app_data.data["chantier_date"]
        self.chantier_visa.text = app_data.data["chantier_visa"]
        self.chantier_visa.hint_text = app_data.data["chantier_visa"]
        self.armement_name.text = app_data.data["armement_name"]
        self.armement_name.hint_text = app_data.data["armement_name"]
        self.armement_date.text = app_data.data["armement_date"]
        self.armement_date.hint_text = app_data.data["armement_date"]
        self.armement_visa.text = app_data.data["armement_visa"]
        self.armement_visa.hint_text = app_data.data["armement_visa"]
        self.intervention_type.text = app_data.data["intervention_type"]
        self.intervention_type.hint_text = app_data.data["intervention_type"]

    def on_enter(self, *args):
        """
        Mise à jour des données à chaque entrée dans l'écran
        Args:
          *args:

        Returns:
            None
        """
        self.update()

    def link_data(self):
        """ 
        Mise à jour des données de l'application avec les données rentrées par l'utilisateur
        """
        app_data = AppData()
        app_data.case_number = self.case_number.text    
        app_data.client_name = self.client_name.text
        app_data.boat_name = self.boat_name.text
        app_data.nb_field = self.nb_field.text
        app_data.site_name = self.site_name.text
        app_data.armement = self.armement.text
        app_data.BOPP_name = self.bopp_name.text
        app_data.BOPP_date = self.bopp_date.text
        app_data.BOPP_visa = self.bopp_visa.text
        app_data.chantier_name = self.chantier_name.text
        app_data.chantier_date = self.chantier_date.text
        app_data.chantier_visa = self.chantier_visa.text
        app_data.armement_name = self.armement_name.text
        app_data.armement_date = self.armement_date.text
        app_data.armement_visa = self.armement_visa.text

        app_data.intervention_type = self.intervention_type.text

    def submit_form(self, instance):
        """
        Enregistrement des données rentrées par l'utilisateur et passage à l'écran suivant
        Args:
          instance: arg de binding

        Returns:
            None
        """
        # print("Formulaire validé avec les données suivantes :")
        # print(f"Numéro d'affaire : {self.case_number.text}")
        # print(f"Nom du client : {self.client_name.text}")
        # print(f"Nom du bateau : {self.boat_name.text}")
        # print(f"NB : {self.nb_field.text}")
        # print(f"Nom du chantier : {self.site_name.text}")
        # print(f"Type d'intervention : {self.intervention_type.text}")
        self.link_data()
        app_data = AppData()
        app_data.save_data_modif_carac()
        # self.manager.current = 'modif_choix_categorie'
        self.manager.current = 'modif_local_machine'

    def go_to_main_menu(self, instance):
        """
        Retour au menu principal
        Args:
          instance: arg de binding

        Returns:
            None
        """
        # app_data = AppData()
        # app_data.save_data()
        self.manager.current = 'main_menu'