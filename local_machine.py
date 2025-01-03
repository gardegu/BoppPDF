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



class LocalMachine(Screen):
    """ 
    Classe du menu local machine pour le BE
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu local machine pour le BE
        """
        super(LocalMachine, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=2, padding=50, spacing=35, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        self.back_btn = Button(text="Retour", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_choix_categorie)
        top_layout.add_widget(self.back_btn)

        layout.add_widget(Label(text="Schema synoptique :"))
        self.schema_synoptique = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.schema_synoptique)

        layout.add_widget(Label(text="Schema electrique :"))
        self.schema_electrique = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.schema_electrique)

        layout.add_widget(Label(text="Schema de bornier :"))
        self.schema_bornier = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.schema_bornier)

        layout.add_widget(Label(text="Schema de cablage :"))
        self.schema_cablage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.schema_cablage)

        layout.add_widget(Label(text="Relevés de rinçages des circuits :"))
        self.releves_rincages_circuits = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.releves_rincages_circuits)

        layout.add_widget(Label(text="AS Niveau Bas NB1 :"))
        self.as_niveau_bas_NB1 = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.as_niveau_bas_NB1)

        layout.add_widget(Label(text="AS Temperature Haute TH1 :"))
        self.as_temperature_haute_TH1 = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.as_temperature_haute_TH1)

        layout.add_widget(Label(text="AS Controle ARU :"))
        self.as_controle_ARU = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.as_controle_ARU)

        layout.add_widget(Label(text="AS Alarme Hydraulique Voyant Defaut :"))
        self.as_alarme_hydraulique_voyant_defaut = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.as_alarme_hydraulique_voyant_defaut)

        layout.add_widget(Label(text="Pompe Principale 45/100 - Verif plein huile :"))
        self.pompe_principale_45_100_verif_plein_huile = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_45_100_verif_plein_huile)

        layout.add_widget(Label(text="Pompe Principale 45/100 - Sens rotation :"))
        self.pompe_principale_45_100_sens_rotation = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_45_100_sens_rotation)

        layout.add_widget(Label(text="Pompe Principale 45/100 - Embrayage pompe :"))
        self.pompe_principale_45_100_embrayage_pompe = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_45_100_embrayage_pompe)

        layout.add_widget(Label(text="Pompe Principale 45/100 - Pression HP :"))
        self.pompe_principale_45_100_pression_HP = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_45_100_pression_HP)

        layout.add_widget(Label(text="Pompe Principale 45/100 - Stand-by :"))
        self.pompe_principale_45_100_stand_by = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_45_100_stand_by)

        layout.add_widget(Label(text="Pompe Principale HPR165/38 - Verif plein huile :"))
        self.pompe_principale_HPR165_38_verif_plein_huile = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_HPR165_38_verif_plein_huile)

        layout.add_widget(Label(text="Pompe Principale HPR165/38 - Sens rotation :"))
        self.pompe_principale_HPR165_38_sens_rotation = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_HPR165_38_sens_rotation)

        layout.add_widget(Label(text="Pompe Principale HPR165/38 - Embrayage pompe :"))
        self.pompe_principale_HPR165_38_embrayage_pompe = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_HPR165_38_embrayage_pompe)

        layout.add_widget(Label(text="Pompe Principale HPR165/38 - Pression HP :"))
        self.pompe_principale_HPR165_38_pression_HP = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_HPR165_38_pression_HP)

        layout.add_widget(Label(text="Pompe Principale HPR165/38 - Stand-by :"))
        self.pompe_principale_HPR165_38_stand_by = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.pompe_principale_HPR165_38_stand_by)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Sens rotation :"))
        self.groupe_secours_pompe_45_sens_rotation = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_sens_rotation)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Calage :"))
        self.groupe_secours_pompe_45_calage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_calage)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Serrage :"))
        self.groupe_secours_pompe_45_serrage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_serrage)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Verif plein huile :"))
        self.groupe_secours_pompe_45_verif_plein_huile = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_verif_plein_huile)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Marche arret moteur :"))
        self.groupe_secours_pompe_45_marche_arret_moteur = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_marche_arret_moteur)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Pression HP :"))
        self.groupe_secours_pompe_45_pression_HP = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_pression_HP)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Stand-by :"))
        self.groupe_secours_pompe_45_stand_by = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_stand_by)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Courant demarrage :"))
        self.groupe_secours_pompe_45_courant_demarrage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_courant_demarrage)

        layout.add_widget(Label(text="Groupe Secours Pompe 45 - Courant service :"))
        self.groupe_secours_pompe_45_courant_service = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.groupe_secours_pompe_45_courant_service)

        layout.add_widget(Label(text="Réglage Limiteur Pression REP10 :"))
        self.reglage_limiteur_pression_REP10 = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.reglage_limiteur_pression_REP10)

        layout.add_widget(Label(text="Réglage Pressostat Retour :"))
        self.reglage_pressostat_retour = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.reglage_pressostat_retour)

        layout.add_widget(Label(text="Réglage Réducteur Pression REP13 :"))
        self.reglage_reducteur_pression_REP13 = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.reglage_reducteur_pression_REP13)

        layout.add_widget(Label(text="Réglage Réducteur Pression Grue REP16 :"))
        self.reglage_reducteur_pression_grue_REP16 = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.reglage_reducteur_pression_grue_REP16)

        layout.add_widget(Label(text="Fonctionnement Sys Refrigeration Embrayage :"))
        self.fonctionnement_sys_refrigeration_embrayage = TextInput(hint_text="Entrer la valeur", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.fonctionnement_sys_refrigeration_embrayage)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # Bouton Valider
        self.submit_btn = Button(text="Valider", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.submit_btn.bind(on_press=self.submit_form)
        top_layout.add_widget(self.submit_btn)

        
        self.add_widget(top_layout)

    def link_data(self):
        """ 
        Met à jours les données de l'application avec les données rentrées par l'utilisateur
        """
        app_data = AppData()
        self.case_number = app_data.case_number

        app_data.Lm_schema_synoptique = self.schema_synoptique.text 
        app_data.Lm_schema_electrique = self.schema_electrique.text 
        app_data.Lm_schema_bornier = self.schema_bornier.text 
        app_data.Lm_schema_cablage = self.schema_cablage.text 
        app_data.Lm_releves_rincages_circuits = self.releves_rincages_circuits.text 
        app_data.Lm_as_niveau_bas_NB1 = self.as_niveau_bas_NB1.text 
        app_data.Lm_as_temperature_haute_TH1 = self.as_temperature_haute_TH1.text 
        app_data.Lm_as_controle_ARU = self.as_controle_ARU.text 
        app_data.Lm_as_alarme_hydraulique_voyant_defaut = self.as_alarme_hydraulique_voyant_defaut.text 
        app_data.Lm_pompe_principale_45_100_verif_plein_huile = self.pompe_principale_45_100_verif_plein_huile.text 
        app_data.Lm_pompe_principale_45_100_sens_rotation = self.pompe_principale_45_100_sens_rotation.text 
        app_data.Lm_pompe_principale_45_100_embrayage_pompe = self.pompe_principale_45_100_embrayage_pompe.text 
        app_data.Lm_pompe_principale_45_100_pression_HP = self.pompe_principale_45_100_pression_HP.text 
        app_data.Lm_pompe_principale_45_100_stand_by = self.pompe_principale_45_100_stand_by.text 
        app_data.Lm_pompe_principale_HPR165_38_verif_plein_huile = self.pompe_principale_HPR165_38_verif_plein_huile.text 
        app_data.Lm_pompe_principale_HPR165_38_sens_rotation = self.pompe_principale_HPR165_38_sens_rotation.text 
        app_data.Lm_pompe_principale_HPR165_38_embrayage_pompe = self.pompe_principale_HPR165_38_embrayage_pompe.text 
        app_data.Lm_pompe_principale_HPR165_38_pression_HP = self.pompe_principale_HPR165_38_pression_HP.text 
        app_data.Lm_pompe_principale_HPR165_38_stand_by = self.pompe_principale_HPR165_38_stand_by.text 
        app_data.Lm_groupe_secours_pompe_45_sens_rotation = self.groupe_secours_pompe_45_sens_rotation.text 
        app_data.Lm_groupe_secours_pompe_45_calage = self.groupe_secours_pompe_45_calage.text 
        app_data.Lm_groupe_secours_pompe_45_serrage = self.groupe_secours_pompe_45_serrage.text 
        app_data.Lm_groupe_secours_pompe_45_verif_plein_huile = self.groupe_secours_pompe_45_verif_plein_huile.text 
        app_data.Lm_groupe_secours_pompe_45_marche_arret_moteur = self.groupe_secours_pompe_45_marche_arret_moteur.text 
        app_data.Lm_groupe_secours_pompe_45_pression_HP = self.groupe_secours_pompe_45_pression_HP.text 
        app_data.Lm_groupe_secours_pompe_45_stand_by = self.groupe_secours_pompe_45_stand_by.text 
        app_data.Lm_groupe_secours_pompe_45_courant_demarrage = self.groupe_secours_pompe_45_courant_demarrage.text 
        app_data.Lm_groupe_secours_pompe_45_courant_service = self.groupe_secours_pompe_45_courant_service.text 
        app_data.Lm_reglage_limiteur_pression_REP10 = self.reglage_limiteur_pression_REP10.text 
        app_data.Lm_reglage_pressostat_retour = self.reglage_pressostat_retour.text 
        app_data.Lm_reglage_reducteur_pression_REP13 = self.reglage_reducteur_pression_REP13.text 
        app_data.Lm_reglage_reducteur_pression_grue_REP16 = self.reglage_reducteur_pression_grue_REP16.text 
        app_data.Lm_fonctionnement_sys_refrigeration_embrayage = self.fonctionnement_sys_refrigeration_embrayage.text

    def submit_form(self, instance):   
        """
        Enregistre les données et retourne au menu du choix de la catégorie pour le BE
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
        Enregistre les données et retourne au menu du choix de la catégorie pour le BE
        Args:
          instance: 

        Returns:

        """
        app_data = AppData()
        app_data.save_data()
        self.manager.current = 'choix_categorie'
        