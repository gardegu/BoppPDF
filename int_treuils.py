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



class IntTreuils(Screen):
    """ 
    Classe du menu treuils pour les intervenants
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu treuils pour les intervenants
        """
        super(IntTreuils, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout2 = GridLayout(cols=2, padding=20, spacing=20, size_hint=(1, 0.2))
        layout2.bind(minimum_height=layout2.setter('height'))

        scrollView = ScrollView(size_hint=(1, 1))

        layout = GridLayout(cols=3, padding=50, spacing=35, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        self.back_btn = Button(text="Retour", color=[1, 1, 1, 1], height=30)
        self.back_btn.bind(on_press=self.go_to_modif_choix_categorie)
        layout2.add_widget(self.back_btn)

        layout2.add_widget(Label(text="Treuils", size_hint=(1, None), height=100, bold=True, font_size=40)) 

        layout.add_widget(Label(text="Dénomination :"))
        layout.add_widget(Label(text="Valeur BE :"))
        layout.add_widget(Label(text="Valeur Intervenant :"))

        layout.add_widget(Label(text="TPH125 0 traction premiere couche statique :"))
        self.TPH125_0_traction_premiere_couche_statique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_traction_premiere_couche_statique = TextInput(hint_text="",
                                                                    size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_traction_premiere_couche_statique)
        layout.add_widget(self.int_TPH125_0_traction_premiere_couche_statique)

        layout.add_widget(Label(text="TPH125 0 traction premiere couche dynamique :"))
        self.TPH125_0_traction_premiere_couche_dynamique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_traction_premiere_couche_dynamique = TextInput(hint_text="",
                                                                     size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH125_0_traction_premiere_couche_dynamique)
        layout.add_widget(self.int_TPH125_0_traction_premiere_couche_dynamique)

        layout.add_widget(Label(text="TPH125 0 pression :"))
        self.TPH125_0_pression = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_pression = TextInput(hint_text="", size_hint=(1, None), height=100,
                                           multiline=False)
        layout.add_widget(self.TPH125_0_pression)
        layout.add_widget(self.int_TPH125_0_pression)

        layout.add_widget(Label(text="TPH125 0 vitesse rotation PV :"))
        self.TPH125_0_vitesse_rotation_PV = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_vitesse_rotation_PV = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                      multiline=False)
        layout.add_widget(self.TPH125_0_vitesse_rotation_PV)
        layout.add_widget(self.int_TPH125_0_vitesse_rotation_PV)

        layout.add_widget(Label(text="TPH125 0 vitesse rotation GV :"))
        self.TPH125_0_vitesse_rotation_GV = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_vitesse_rotation_GV = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                      multiline=False)
        layout.add_widget(self.TPH125_0_vitesse_rotation_GV)
        layout.add_widget(self.int_TPH125_0_vitesse_rotation_GV)

        layout.add_widget(Label(text="TPH125 0 debit :"))
        self.TPH125_0_debit = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_debit = TextInput(hint_text="", size_hint=(1, None), height=100,
                                        multiline=False)
        layout.add_widget(self.TPH125_0_debit)
        layout.add_widget(self.int_TPH125_0_debit)

        layout.add_widget(Label(text="TPH125 0 essai file vire :"))
        self.TPH125_0_essai_file_vire = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_essai_file_vire = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                  multiline=False)
        layout.add_widget(self.TPH125_0_essai_file_vire)
        layout.add_widget(self.int_TPH125_0_essai_file_vire)

        layout.add_widget(Label(text="TPH125 0 essai freinage :"))
        self.TPH125_0_essai_freinage = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_essai_freinage = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                 multiline=False)
        layout.add_widget(self.TPH125_0_essai_freinage)
        layout.add_widget(self.int_TPH125_0_essai_freinage)

        layout.add_widget(Label(text="TPH125 0 selection PV GV :"))
        self.TPH125_0_selection_PV_GV = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH125_0_selection_PV_GV = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                  multiline=False)
        layout.add_widget(self.TPH125_0_selection_PV_GV)
        layout.add_widget(self.int_TPH125_0_selection_PV_GV)

        layout.add_widget(Label(text="TPH50 0 traction premiere couche statique :"))
        self.TPH50_0_traction_premiere_couche_statique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_traction_premiere_couche_statique = TextInput(hint_text="",
                                                                   size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_traction_premiere_couche_statique)
        layout.add_widget(self.int_TPH50_0_traction_premiere_couche_statique)

        layout.add_widget(Label(text="TPH50 0 traction premiere couche dynamique :"))
        self.TPH50_0_traction_premiere_couche_dynamique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_traction_premiere_couche_dynamique = TextInput(hint_text="",
                                                                    size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.TPH50_0_traction_premiere_couche_dynamique)
        layout.add_widget(self.int_TPH50_0_traction_premiere_couche_dynamique)

        layout.add_widget(Label(text="TPH50 0 pression :"))
        self.TPH50_0_pression = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_pression = TextInput(hint_text="", size_hint=(1, None), height=100,
                                          multiline=False)
        layout.add_widget(self.TPH50_0_pression)
        layout.add_widget(self.int_TPH50_0_pression)

        layout.add_widget(Label(text="TPH50 0 vitesse rotation PV :"))
        self.TPH50_0_vitesse_rotation_PV = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_vitesse_rotation_PV = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                     multiline=False)
        layout.add_widget(self.TPH50_0_vitesse_rotation_PV)
        layout.add_widget(self.int_TPH50_0_vitesse_rotation_PV)

        layout.add_widget(Label(text="TPH50 0 vitesse rotation GV :"))
        self.TPH50_0_vitesse_rotation_GV = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_vitesse_rotation_GV = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                     multiline=False)
        layout.add_widget(self.TPH50_0_vitesse_rotation_GV)
        layout.add_widget(self.int_TPH50_0_vitesse_rotation_GV)

        layout.add_widget(Label(text="TPH50 0 debit :"))
        self.TPH50_0_debit = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_debit = TextInput(hint_text="", size_hint=(1, None), height=100,
                                       multiline=False)
        layout.add_widget(self.TPH50_0_debit)
        layout.add_widget(self.int_TPH50_0_debit)

        layout.add_widget(Label(text="TPH50 0 essai file vire :"))
        self.TPH50_0_essai_file_vire = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_essai_file_vire = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                 multiline=False)
        layout.add_widget(self.TPH50_0_essai_file_vire)
        layout.add_widget(self.int_TPH50_0_essai_file_vire)

        layout.add_widget(Label(text="TPH50 0 essai freinage :"))
        self.TPH50_0_essai_freinage = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_essai_freinage = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                multiline=False)
        layout.add_widget(self.TPH50_0_essai_freinage)
        layout.add_widget(self.int_TPH50_0_essai_freinage)

        layout.add_widget(Label(text="TPH50 0 selection PV GV :"))
        self.TPH50_0_selection_PV_GV = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_TPH50_0_selection_PV_GV = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                 multiline=False)
        layout.add_widget(self.TPH50_0_selection_PV_GV)
        layout.add_widget(self.int_TPH50_0_selection_PV_GV)

        top_layout.add_widget(layout2)
        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # Bouton Valider
        self.submit_btn = Button(text="Valider", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.submit_form)
        top_layout.add_widget(self.submit_btn)

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
        self.TPH125_0_traction_premiere_couche_statique.text = app_data.data["TPH125_0_traction_premiere_couche_statique"]
        self.TPH125_0_traction_premiere_couche_dynamique.text = app_data.data["TPH125_0_traction_premiere_couche_dynamique"]
        self.TPH125_0_pression.text = app_data.data["TPH125_0_pression"]
        self.TPH125_0_vitesse_rotation_PV.text = app_data.data["TPH125_0_vitesse_rotation_PV"]
        self.TPH125_0_vitesse_rotation_GV.text = app_data.data["TPH125_0_vitesse_rotation_GV"]
        self.TPH125_0_debit.text = app_data.data["TPH125_0_debit"]
        self.TPH125_0_essai_file_vire.text = app_data.data["TPH125_0_essai_file_vire"]
        self.TPH125_0_essai_freinage.text = app_data.data["TPH125_0_essai_freinage"]
        self.TPH125_0_selection_PV_GV.text = app_data.data["TPH125_0_selection_PV_GV"]
        self.TPH50_0_traction_premiere_couche_statique.text = app_data.data["TPH50_0_traction_premiere_couche_statique"]
        self.TPH50_0_traction_premiere_couche_dynamique.text = app_data.data["TPH50_0_traction_premiere_couche_dynamique"]
        self.TPH50_0_pression.text = app_data.data["TPH50_0_pression"]
        self.TPH50_0_vitesse_rotation_PV.text = app_data.data["TPH50_0_vitesse_rotation_PV"]
        self.TPH50_0_vitesse_rotation_GV.text = app_data.data["TPH50_0_vitesse_rotation_GV"]
        self.TPH50_0_debit.text = app_data.data["TPH50_0_debit"]
        self.TPH50_0_essai_file_vire.text = app_data.data["TPH50_0_essai_file_vire"]
        self.TPH50_0_essai_freinage.text = app_data.data["TPH50_0_essai_freinage"]
        self.TPH50_0_selection_PV_GV.text = app_data.data["TPH50_0_selection_PV_GV"]

        self.int_TPH125_0_traction_premiere_couche_statique.text = app_data.data["int_TPH125_0_traction_premiere_couche_statique"]
        self.int_TPH125_0_traction_premiere_couche_dynamique.text = app_data.data["int_TPH125_0_traction_premiere_couche_dynamique"]
        self.int_TPH125_0_pression.text = app_data.data["int_TPH125_0_pression"]
        self.int_TPH125_0_vitesse_rotation_PV.text = app_data.data["int_TPH125_0_vitesse_rotation_PV"]
        self.int_TPH125_0_vitesse_rotation_GV.text = app_data.data["int_TPH125_0_vitesse_rotation_GV"]
        self.int_TPH125_0_debit.text = app_data.data["int_TPH125_0_debit"]
        self.int_TPH125_0_essai_file_vire.text = app_data.data["int_TPH125_0_essai_file_vire"]
        self.int_TPH125_0_essai_freinage.text = app_data.data["int_TPH125_0_essai_freinage"]
        self.int_TPH125_0_selection_PV_GV.text = app_data.data["int_TPH125_0_selection_PV_GV"]
        self.int_TPH50_0_traction_premiere_couche_statique.text = app_data.data["int_TPH50_0_traction_premiere_couche_statique"]
        self.int_TPH50_0_traction_premiere_couche_dynamique.text = app_data.data["int_TPH50_0_traction_premiere_couche_dynamique"]
        self.int_TPH50_0_pression.text = app_data.data["int_TPH50_0_pression"]
        self.int_TPH50_0_vitesse_rotation_PV.text = app_data.data["int_TPH50_0_vitesse_rotation_PV"]
        self.int_TPH50_0_vitesse_rotation_GV.text = app_data.data["int_TPH50_0_vitesse_rotation_GV"]
        self.int_TPH50_0_debit.text = app_data.data["int_TPH50_0_debit"]
        self.int_TPH50_0_essai_file_vire.text = app_data.data["int_TPH50_0_essai_file_vire"]
        self.int_TPH50_0_essai_freinage.text = app_data.data["int_TPH50_0_essai_freinage"]
        self.int_TPH50_0_selection_PV_GV.text = app_data.data["int_TPH50_0_selection_PV_GV"]

        self.int_TPH125_0_traction_premiere_couche_statique.hint_text = app_data.data["int_TPH125_0_traction_premiere_couche_statique"]
        self.int_TPH125_0_traction_premiere_couche_dynamique.hint_text = app_data.data["int_TPH125_0_traction_premiere_couche_dynamique"]
        self.int_TPH125_0_pression.hint_text = app_data.data["int_TPH125_0_pression"]
        self.int_TPH125_0_vitesse_rotation_PV.hint_text = app_data.data["int_TPH125_0_vitesse_rotation_PV"]
        self.int_TPH125_0_vitesse_rotation_GV.hint_text = app_data.data["int_TPH125_0_vitesse_rotation_GV"]
        self.int_TPH125_0_debit.hint_text = app_data.data["int_TPH125_0_debit"]
        self.int_TPH125_0_essai_file_vire.hint_text = app_data.data["int_TPH125_0_essai_file_vire"]
        self.int_TPH125_0_essai_freinage.hint_text = app_data.data["int_TPH125_0_essai_freinage"]
        self.int_TPH125_0_selection_PV_GV.hint_text = app_data.data["int_TPH125_0_selection_PV_GV"]
        self.int_TPH50_0_traction_premiere_couche_statique.hint_text = app_data.data["int_TPH50_0_traction_premiere_couche_statique"]
        self.int_TPH50_0_traction_premiere_couche_dynamique.hint_text = app_data.data["int_TPH50_0_traction_premiere_couche_dynamique"]
        self.int_TPH50_0_pression.hint_text = app_data.data["int_TPH50_0_pression"]
        self.int_TPH50_0_vitesse_rotation_PV.hint_text = app_data.data["int_TPH50_0_vitesse_rotation_PV"]
        self.int_TPH50_0_vitesse_rotation_GV.hint_text = app_data.data["int_TPH50_0_vitesse_rotation_GV"]
        self.int_TPH50_0_debit.hint_text = app_data.data["int_TPH50_0_debit"]
        self.int_TPH50_0_essai_file_vire.hint_text = app_data.data["int_TPH50_0_essai_file_vire"]
        self.int_TPH50_0_essai_freinage.hint_text = app_data.data["int_TPH50_0_essai_freinage"]
        self.int_TPH50_0_selection_PV_GV.hint_text = app_data.data["int_TPH50_0_selection_PV_GV"]

    def link_data(self):
        """ 
        Met à jour les données de l'application avec les données rentrées par l'utilisateur
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

        app_data.int_TPH125_0_traction_premiere_couche_statique = self.int_TPH125_0_traction_premiere_couche_statique.text
        app_data.int_TPH125_0_traction_premiere_couche_dynamique = self.int_TPH125_0_traction_premiere_couche_dynamique.text
        app_data.int_TPH125_0_pression = self.int_TPH125_0_pression.text
        app_data.int_TPH125_0_vitesse_rotation_PV = self.int_TPH125_0_vitesse_rotation_PV.text
        app_data.int_TPH125_0_vitesse_rotation_GV = self.int_TPH125_0_vitesse_rotation_GV.text
        app_data.int_TPH125_0_debit = self.int_TPH125_0_debit.text
        app_data.int_TPH125_0_essai_file_vire = self.int_TPH125_0_essai_file_vire.text
        app_data.int_TPH125_0_essai_freinage = self.int_TPH125_0_essai_freinage.text
        app_data.int_TPH125_0_selection_PV_GV = self.int_TPH125_0_selection_PV_GV.text
        app_data.int_TPH50_0_traction_premiere_couche_statique = self.int_TPH50_0_traction_premiere_couche_statique.text
        app_data.int_TPH50_0_traction_premiere_couche_dynamique = self.int_TPH50_0_traction_premiere_couche_dynamique.text
        app_data.int_TPH50_0_pression = self.int_TPH50_0_pression.text
        app_data.int_TPH50_0_vitesse_rotation_PV = self.int_TPH50_0_vitesse_rotation_PV.text
        app_data.int_TPH50_0_vitesse_rotation_GV = self.int_TPH50_0_vitesse_rotation_GV.text
        app_data.int_TPH50_0_debit = self.int_TPH50_0_debit.text
        app_data.int_TPH50_0_essai_file_vire = self.int_TPH50_0_essai_file_vire.text
        app_data.int_TPH50_0_essai_freinage = self.int_TPH50_0_essai_freinage.text
        app_data.int_TPH50_0_selection_PV_GV = self.int_TPH50_0_selection_PV_GV.text


    def submit_form(self, instance):
        """
        Enregistre les données entrées par l'utilisateur et passe à l'écran suivant
        Args:
          instance: 

        Returns:

        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_int_treuil()
        self.manager.current = 'int_cabestan'
        # print(app_data.data)

    def go_to_modif_choix_categorie(self, instance):
        """
        Reviens à l'écran précédent
        Args:
          instance: 

        Returns:

        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_int_treuil()
        self.manager.current = 'int_local_machine'

