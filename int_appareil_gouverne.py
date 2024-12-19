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



class IntAppareilGouverne(Screen):
    """ 
    Classe du menu appareil gouverne des intervenants
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu appareil gouverne
        """
        super(IntAppareilGouverne, self).__init__(**kwargs)

        app_data = AppData()

        top_layout = BoxLayout(orientation='vertical', padding = 10, spacing=10)
        layout2 = GridLayout(cols=2, padding=20, spacing=20, size_hint=(1, 0.2))
        layout2.bind(minimum_height=layout2.setter('height'))

        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=3, padding=10, spacing=35, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        self.back_btn = Button(text="Retour", color=[1,1,1,1], height=30)
        self.back_btn.bind(on_press=self.go_to_modif_choix_categorie)
        layout2.add_widget(self.back_btn)

        layout2.add_widget(Label(text="Appareil à gouverner", size_hint=(1, None), height=100, bold=True, font_size=40)) 

        layout.add_widget(Label(text="Dénomination :"))
        layout.add_widget(Label(text="Valeur BE :"))
        layout.add_widget(Label(text="Valeur Intervenant :"))

        layout.add_widget(Label(text="Schema synoptique :"))
        self.AAG_schema_synoptique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_schema_synoptique = TextInput(hint_text="", size_hint=(1, None), height=100,
                                               multiline=False)
        layout.add_widget(self.AAG_schema_synoptique)
        layout.add_widget(self.int_AAG_schema_synoptique)

        layout.add_widget(Label(text="Schema electrique :"))
        self.AAG_schema_electrique = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_schema_electrique = TextInput(hint_text="", size_hint=(1, None), height=100,
                                               multiline=False)
        layout.add_widget(self.AAG_schema_electrique)
        layout.add_widget(self.int_AAG_schema_electrique)

        layout.add_widget(Label(text="Schema de bornier :"))
        self.AAG_schema_bornier = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_schema_bornier = TextInput(hint_text="", size_hint=(1, None), height=100,
                                            multiline=False)
        layout.add_widget(self.AAG_schema_bornier)
        layout.add_widget(self.int_AAG_schema_bornier)

        layout.add_widget(Label(text="Schema de cablage :"))
        self.AAG_schema_cablage = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_schema_cablage = TextInput(hint_text="", size_hint=(1, None), height=100,
                                            multiline=False)
        layout.add_widget(self.AAG_schema_cablage)
        layout.add_widget(self.int_AAG_schema_cablage)

        layout.add_widget(Label(text="Relevés de rinçages des circuits :"))
        self.AAG_releves_rincages_circuits = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_releves_rincages_circuits = TextInput(hint_text="", size_hint=(1, None),
                                                       height=100, multiline=False)
        layout.add_widget(self.AAG_releves_rincages_circuits)
        layout.add_widget(self.int_AAG_releves_rincages_circuits)

        layout.add_widget(Label(text="AS Niveau Bas NB1 :"))
        self.AAG_as_niveau_bas_NB1 = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_niveau_bas_NB1 = TextInput(hint_text="", size_hint=(1, None), height=100,
                                               multiline=False)
        layout.add_widget(self.AAG_as_niveau_bas_NB1)
        layout.add_widget(self.int_AAG_as_niveau_bas_NB1)

        layout.add_widget(Label(text="AS Controle ARU :"))
        self.AAG_as_controle_ARU = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_controle_ARU = TextInput(hint_text="", size_hint=(1, None), height=100,
                                             multiline=False)
        layout.add_widget(self.AAG_as_controle_ARU)
        layout.add_widget(self.int_AAG_as_controle_ARU)

        layout.add_widget(Label(text="AS Alarme Hydraulique Voyant Defaut :"))
        self.AAG_as_alarme_hydraulique_voyant_defaut = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_alarme_hydraulique_voyant_defaut = TextInput(hint_text="", size_hint=(1, None),
                                                                 height=100, multiline=False)
        layout.add_widget(self.AAG_as_alarme_hydraulique_voyant_defaut)
        layout.add_widget(self.int_AAG_as_alarme_hydraulique_voyant_defaut)

        layout.add_widget(Label(text="Verif zero mecanique safran :"))
        self.AAG_verif_zero_mecanique_safran = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_verif_zero_mecanique_safran = TextInput(hint_text="", size_hint=(1, None),
                                                         height=100, multiline=False)
        layout.add_widget(self.AAG_verif_zero_mecanique_safran)
        layout.add_widget(self.int_AAG_verif_zero_mecanique_safran)

        layout.add_widget(Label(text="Verif zero mecanique recepteur :"))
        self.AAG_verif_zero_mecanique_recepteur = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_verif_zero_mecanique_recepteur = TextInput(hint_text="", size_hint=(1, None),
                                                            height=100, multiline=False)
        layout.add_widget(self.AAG_verif_zero_mecanique_recepteur)
        layout.add_widget(self.int_AAG_verif_zero_mecanique_recepteur)

        layout.add_widget(Label(text="Verif positionnement transmetteur BOPP :"))
        self.AAG_verif_positionnement_transmetteur_BOPP = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_verif_positionnement_transmetteur_BOPP = TextInput(hint_text="",
                                                                    size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_verif_positionnement_transmetteur_BOPP)
        layout.add_widget(self.int_AAG_verif_positionnement_transmetteur_BOPP)

        layout.add_widget(Label(text="Controle puissance :"))
        self.AAG_controle_puissance = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_controle_puissance = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                multiline=False)
        layout.add_widget(self.AAG_controle_puissance)
        layout.add_widget(self.int_AAG_controle_puissance)

        layout.add_widget(Label(text="Controle frequence :"))
        self.AAG_controle_frequence = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_controle_frequence = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                multiline=False)
        layout.add_widget(self.AAG_controle_frequence)
        layout.add_widget(self.int_AAG_controle_frequence)

        layout.add_widget(Label(text="Controle commande :"))
        self.AAG_controle_commande = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_controle_commande = TextInput(hint_text="", size_hint=(1, None), height=100,
                                               multiline=False)
        layout.add_widget(self.AAG_controle_commande)
        layout.add_widget(self.int_AAG_controle_commande)

        layout.add_widget(Label(text="Controle presence 24VDC :"))
        self.AAG_controle_presence_24VDC = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_controle_presence_24VDC = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                     multiline=False)
        layout.add_widget(self.AAG_controle_presence_24VDC)
        layout.add_widget(self.int_AAG_controle_presence_24VDC)

        layout.add_widget(Label(text="AS Defauts puissance :"))
        self.AAG_as_defauts_puissance = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_defauts_puissance = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                  multiline=False)
        layout.add_widget(self.AAG_as_defauts_puissance)
        layout.add_widget(self.int_AAG_as_defauts_puissance)

        layout.add_widget(Label(text="AS Defauts moteur :"))
        self.AAG_as_defauts_moteur = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_defauts_moteur = TextInput(hint_text="", size_hint=(1, None), height=100,
                                               multiline=False)
        layout.add_widget(self.AAG_as_defauts_moteur)
        layout.add_widget(self.int_AAG_as_defauts_moteur)

        layout.add_widget(Label(text="AS Defauts commande :"))
        self.AAG_as_defauts_commande = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_defauts_commande = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                 multiline=False)
        layout.add_widget(self.AAG_as_defauts_commande)
        layout.add_widget(self.int_AAG_as_defauts_commande)

        layout.add_widget(Label(text="AS Niveau Bas :"))
        self.AAG_as_niveau_bas = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_niveau_bas = TextInput(hint_text="", size_hint=(1, None), height=100,
                                           multiline=False)
        layout.add_widget(self.AAG_as_niveau_bas)
        layout.add_widget(self.int_AAG_as_niveau_bas)

        layout.add_widget(Label(text="AS Test lampes :"))
        self.AAG_as_test_lampes = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_test_lampes = TextInput(hint_text="", size_hint=(1, None), height=100,
                                            multiline=False)
        layout.add_widget(self.AAG_as_test_lampes)
        layout.add_widget(self.int_AAG_as_test_lampes)

        layout.add_widget(Label(text="AS Controle ARU2 :"))
        self.AAG_as_controle_ARU2 = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_as_controle_ARU2 = TextInput(hint_text="", size_hint=(1, None), height=100,
                                              multiline=False)
        layout.add_widget(self.AAG_as_controle_ARU2)
        layout.add_widget(self.int_AAG_as_controle_ARU2)

        layout.add_widget(Label(text="Signalisation defauts :"))
        self.AAG_signalisation_defauts = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_signalisation_defauts = TextInput(hint_text="", size_hint=(1, None), height=100,
                                                   multiline=False)
        layout.add_widget(self.AAG_signalisation_defauts)
        layout.add_widget(self.int_AAG_signalisation_defauts)

        layout.add_widget(Label(text="APG Pompe double sens rotation :"))
        self.AAG_APG_pompe_double_sens_rotation = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_APG_pompe_double_sens_rotation = TextInput(hint_text="", size_hint=(1, None),
                                                            height=100, multiline=False)
        layout.add_widget(self.AAG_APG_pompe_double_sens_rotation)
        layout.add_widget(self.int_AAG_APG_pompe_double_sens_rotation)

        layout.add_widget(Label(text="APG Pompe double marche arret moteur :"))
        self.AAG_APG_pompe_double_marche_arret_moteur = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_APG_pompe_double_marche_arret_moteur = TextInput(hint_text="",
                                                                  size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_APG_pompe_double_marche_arret_moteur)
        layout.add_widget(self.int_AAG_APG_pompe_double_marche_arret_moteur)

        layout.add_widget(Label(text="APG Pompe double courant demarrage :"))
        self.AAG_APG_pompe_double_courant_demarrage = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_APG_pompe_double_courant_demarrage = TextInput(hint_text="", size_hint=(1, None),
                                                                height=100, multiline=False)
        layout.add_widget(self.AAG_APG_pompe_double_courant_demarrage)
        layout.add_widget(self.int_AAG_APG_pompe_double_courant_demarrage)

        layout.add_widget(Label(text="APG Pompe double courant service :"))
        self.AAG_APG_pompe_double_courant_service = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_APG_pompe_double_courant_service = TextInput(hint_text="", size_hint=(1, None),
                                                              height=100, multiline=False)
        layout.add_widget(self.AAG_APG_pompe_double_courant_service)
        layout.add_widget(self.int_AAG_APG_pompe_double_courant_service)

        layout.add_widget(Label(text="RTRIB Reglage limiteur pression centrale :"))
        self.AAG_RTRIB_reglage_limiteur_pression_centrale = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_reglage_limiteur_pression_centrale = TextInput(hint_text="",
                                                                      size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_reglage_limiteur_pression_centrale)
        layout.add_widget(self.int_AAG_RTRIB_reglage_limiteur_pression_centrale)

        layout.add_widget(Label(text="RTRIB Reglage limiteur pression double en ligne :"))
        self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne = TextInput(hint_text="",
                                                                             size_hint=(1, None), height=100,
                                                                             multiline=False)
        layout.add_widget(self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne)
        layout.add_widget(self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne)

        layout.add_widget(Label(text="RTRIB Controle vitesses recepteur moteur :"))
        self.AAG_RTRIB_controle_vitesses_recepteur_moteur = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur = TextInput(hint_text="",
                                                                      size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_vitesses_recepteur_moteur)
        layout.add_widget(self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur)

        layout.add_widget(Label(text="RTRIB Controle vitesses recepteur pompe :"))
        self.AAG_RTRIB_controle_vitesses_recepteur_pompe = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe = TextInput(hint_text="",
                                                                     size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_vitesses_recepteur_pompe)
        layout.add_widget(self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe)

        layout.add_widget(Label(text="RTRIB Controle vitesses recepteur reglage Pmax :"))
        self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax = TextInput(hint_text="",
                                                                            size_hint=(1, None), height=100,
                                                                            multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax)
        layout.add_widget(self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax)

        layout.add_widget(Label(text="RTRIB Controle fin course electrique arret electros :"))
        self.AAG_RTRIB_controle_fin_course_electrique_arret_electros = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros = TextInput(hint_text="",
                                                                                 size_hint=(1, None), height=100,
                                                                                 multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_fin_course_electrique_arret_electros)
        layout.add_widget(self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros)

        layout.add_widget(Label(text="RTRIB Controle fin course electrique PX1 :"))
        self.AAG_RTRIB_controle_fin_course_electrique_PX1 = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_fin_course_electrique_PX1 = TextInput(hint_text="",
                                                                      size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_fin_course_electrique_PX1)
        layout.add_widget(self.int_AAG_RTRIB_controle_fin_course_electrique_PX1)

        layout.add_widget(Label(text="RTRIB Controle fin course electrique PX2 :"))
        self.AAG_RTRIB_controle_fin_course_electrique_PX2 = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_fin_course_electrique_PX2 = TextInput(hint_text="",
                                                                      size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_fin_course_electrique_PX2)
        layout.add_widget(self.int_AAG_RTRIB_controle_fin_course_electrique_PX2)

        layout.add_widget(Label(text="RTRIB Controle fonctionnement indicateurs angle passerelle :"))
        self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle = TextInput(
            hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle)
        layout.add_widget(self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle)

        layout.add_widget(Label(text="RTRIB Controle fonctionnement indicateurs angle local barre :"))
        self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre = TextInput(
            hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre)
        layout.add_widget(self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre)

        layout.add_widget(Label(text="RBAB Reglage limiteur pression centrale :"))
        self.AAG_RBAB_reglage_limiteur_pression_centrale = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_reglage_limiteur_pression_centrale = TextInput(hint_text="",
                                                                     size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_reglage_limiteur_pression_centrale)
        layout.add_widget(self.int_AAG_RBAB_reglage_limiteur_pression_centrale)

        layout.add_widget(Label(text="RBAB Reglage limiteur pression double en ligne :"))
        self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne = TextInput(hint_text="",
                                                                            size_hint=(1, None), height=100,
                                                                            multiline=False)
        layout.add_widget(self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne)
        layout.add_widget(self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne)

        layout.add_widget(Label(text="RBAB Controle vitesses recepteur moteur :"))
        self.AAG_RBAB_controle_vitesses_recepteur_moteur = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_vitesses_recepteur_moteur = TextInput(hint_text="",
                                                                     size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_vitesses_recepteur_moteur)
        layout.add_widget(self.int_AAG_RBAB_controle_vitesses_recepteur_moteur)

        layout.add_widget(Label(text="RBAB Controle vitesses recepteur pompe :"))
        self.AAG_RBAB_controle_vitesses_recepteur_pompe = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_vitesses_recepteur_pompe = TextInput(hint_text="",
                                                                    size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_vitesses_recepteur_pompe)
        layout.add_widget(self.int_AAG_RBAB_controle_vitesses_recepteur_pompe)

        layout.add_widget(Label(text="RBAB Controle vitesses recepteur reglage Pmax :"))
        self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax = TextInput(hint_text="",
                                                                           size_hint=(1, None), height=100,
                                                                           multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax)
        layout.add_widget(self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax)

        layout.add_widget(Label(text="RBAB Controle fin course electrique arret electros :"))
        self.AAG_RBAB_controle_fin_course_electrique_arret_electros = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros = TextInput(hint_text="",
                                                                                size_hint=(1, None), height=100,
                                                                                multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_fin_course_electrique_arret_electros)
        layout.add_widget(self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros)

        layout.add_widget(Label(text="RBAB Controle fin course electrique PX1 :"))
        self.AAG_RBAB_controle_fin_course_electrique_PX1 = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_fin_course_electrique_PX1 = TextInput(hint_text="",
                                                                     size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_fin_course_electrique_PX1)
        layout.add_widget(self.int_AAG_RBAB_controle_fin_course_electrique_PX1)

        layout.add_widget(Label(text="RBAB Controle fin course electrique PX2 :"))
        self.AAG_RBAB_controle_fin_course_electrique_PX2 = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_fin_course_electrique_PX2 = TextInput(hint_text="",
                                                                     size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_fin_course_electrique_PX2)
        layout.add_widget(self.int_AAG_RBAB_controle_fin_course_electrique_PX2)

        layout.add_widget(Label(text="RBAB Controle fonctionnement indicateurs angle passerelle :"))
        self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle = TextInput(
            hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle)
        layout.add_widget(self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle)

        layout.add_widget(Label(text="RBAB Controle fonctionnement indicateurs angle local barre :"))
        self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre = TextInput(hint_text="", size_hint=(1, None), height=100, multiline=False, readonly=True)
        self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre = TextInput(
            hint_text="", size_hint=(1, None), height=100, multiline=False)
        layout.add_widget(self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre)
        layout.add_widget(self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre)

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
        Met à jour les champs de texte avec les données précédemment enregistrées à l'ouverture de la page
        Args:
          *args: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        self.update()

    def update(self):
        """ 
        Met à jour les champs de texte avec les données précédemment enregistrées
        """
        app_data = AppData()
        self.AAG_schema_synoptique.text = app_data.data["AAG_schema_synoptique"]
        self.AAG_schema_electrique.text = app_data.data["AAG_schema_electrique"]
        self.AAG_schema_bornier.text = app_data.data["AAG_schema_bornier"]
        self.AAG_schema_cablage.text = app_data.data["AAG_schema_cablage"]
        self.AAG_releves_rincages_circuits.text = app_data.data["AAG_releves_rincages_circuits"]
        self.AAG_as_niveau_bas_NB1.text = app_data.data["AAG_as_niveau_bas_NB1"]
        self.AAG_as_controle_ARU.text = app_data.data["AAG_as_controle_ARU"]
        self.AAG_as_alarme_hydraulique_voyant_defaut.text = app_data.data["AAG_as_alarme_hydraulique_voyant_defaut"]
        self.AAG_verif_zero_mecanique_safran.text = app_data.data["AAG_verif_zero_mecanique_safran"]
        self.AAG_verif_zero_mecanique_recepteur.text = app_data.data["AAG_verif_zero_mecanique_recepteur"]
        self.AAG_verif_positionnement_transmetteur_BOPP.text = app_data.data[
            "AAG_verif_positionnement_transmetteur_BOPP"]
        self.AAG_controle_puissance.text = app_data.data["AAG_controle_puissance"]
        self.AAG_controle_frequence.text = app_data.data["AAG_controle_frequence"]
        self.AAG_controle_commande.text = app_data.data["AAG_controle_commande"]
        self.AAG_controle_presence_24VDC.text = app_data.data["AAG_controle_presence_24VDC"]
        self.AAG_as_defauts_puissance.text = app_data.data["AAG_as_defauts_puissance"]
        self.AAG_as_defauts_moteur.text = app_data.data["AAG_as_defauts_moteur"]
        self.AAG_as_defauts_commande.text = app_data.data["AAG_as_defauts_commande"]
        self.AAG_as_niveau_bas.text = app_data.data["AAG_as_niveau_bas"]
        self.AAG_as_test_lampes.text = app_data.data["AAG_as_test_lampes"]
        self.AAG_as_controle_ARU2.text = app_data.data["AAG_as_controle_ARU2"]
        self.AAG_signalisation_defauts.text = app_data.data["AAG_signalisation_defauts"]
        self.AAG_APG_pompe_double_sens_rotation.text = app_data.data["AAG_APG_pompe_double_sens_rotation"]
        self.AAG_APG_pompe_double_marche_arret_moteur.text = app_data.data["AAG_APG_pompe_double_marche_arret_moteur"]
        self.AAG_APG_pompe_double_courant_demarrage.text = app_data.data["AAG_APG_pompe_double_courant_demarrage"]
        self.AAG_APG_pompe_double_courant_service.text = app_data.data["AAG_APG_pompe_double_courant_service"]
        self.AAG_RTRIB_reglage_limiteur_pression_centrale.text = app_data.data[
            "AAG_RTRIB_reglage_limiteur_pression_centrale"]
        self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne.text = app_data.data[
            "AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"]
        self.AAG_RTRIB_controle_vitesses_recepteur_moteur.text = app_data.data[
            "AAG_RTRIB_controle_vitesses_recepteur_moteur"]
        self.AAG_RTRIB_controle_vitesses_recepteur_pompe.text = app_data.data[
            "AAG_RTRIB_controle_vitesses_recepteur_pompe"]
        self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax.text = app_data.data[
            "AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"]
        self.AAG_RTRIB_controle_fin_course_electrique_arret_electros.text = app_data.data[
            "AAG_RTRIB_controle_fin_course_electrique_arret_electros"]
        self.AAG_RTRIB_controle_fin_course_electrique_PX1.text = app_data.data[
            "AAG_RTRIB_controle_fin_course_electrique_PX1"]
        self.AAG_RTRIB_controle_fin_course_electrique_PX2.text = app_data.data[
            "AAG_RTRIB_controle_fin_course_electrique_PX2"]
        self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle.text = app_data.data[
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"]
        self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre.text = app_data.data[
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"]
        self.AAG_RBAB_reglage_limiteur_pression_centrale.text = app_data.data[
            "AAG_RBAB_reglage_limiteur_pression_centrale"]
        self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne.text = app_data.data[
            "AAG_RBAB_reglage_limiteur_pression_double_en_ligne"]
        self.AAG_RBAB_controle_vitesses_recepteur_moteur.text = app_data.data[
            "AAG_RBAB_controle_vitesses_recepteur_moteur"]
        self.AAG_RBAB_controle_vitesses_recepteur_pompe.text = app_data.data[
            "AAG_RBAB_controle_vitesses_recepteur_pompe"]
        self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax.text = app_data.data[
            "AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"]
        self.AAG_RBAB_controle_fin_course_electrique_arret_electros.text = app_data.data[
            "AAG_RBAB_controle_fin_course_electrique_arret_electros"]
        self.AAG_RBAB_controle_fin_course_electrique_PX1.text = app_data.data[
            "AAG_RBAB_controle_fin_course_electrique_PX1"]
        self.AAG_RBAB_controle_fin_course_electrique_PX2.text = app_data.data[
            "AAG_RBAB_controle_fin_course_electrique_PX2"]
        self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle.text = app_data.data[
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"]
        self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre.text = app_data.data[
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"]

        self.int_AAG_schema_synoptique.text = app_data.data[
            "int_AAG_schema_synoptique"]
        self.int_AAG_schema_electrique.text = app_data.data[
            "int_AAG_schema_electrique"]
        self.int_AAG_schema_bornier.text = app_data.data[
            "int_AAG_schema_bornier"]
        self.int_AAG_schema_cablage.text = app_data.data[
            "int_AAG_schema_cablage"]
        self.int_AAG_releves_rincages_circuits.text = app_data.data[
            "int_AAG_releves_rincages_circuits"]
        self.int_AAG_as_niveau_bas_NB1.text = app_data.data[
            "int_AAG_as_niveau_bas_NB1"]
        self.int_AAG_as_controle_ARU.text = app_data.data[
            "int_AAG_as_controle_ARU"]
        self.int_AAG_as_alarme_hydraulique_voyant_defaut.text = app_data.data[
            "int_AAG_as_alarme_hydraulique_voyant_defaut"]
        self.int_AAG_verif_zero_mecanique_safran.text = app_data.data[
            "int_AAG_verif_zero_mecanique_safran"]
        self.int_AAG_verif_zero_mecanique_recepteur.text = app_data.data[
            "int_AAG_verif_zero_mecanique_recepteur"]
        self.int_AAG_verif_positionnement_transmetteur_BOPP.text = app_data.data[
            "int_AAG_verif_positionnement_transmetteur_BOPP"]
        self.int_AAG_controle_puissance.text = app_data.data[
            "int_AAG_controle_puissance"]
        self.int_AAG_controle_frequence.text = app_data.data[
            "int_AAG_controle_frequence"]
        self.int_AAG_controle_commande.text = app_data.data[
            "int_AAG_controle_commande"]
        self.int_AAG_controle_presence_24VDC.text = app_data.data[
            "int_AAG_controle_presence_24VDC"]
        self.int_AAG_as_defauts_puissance.text = app_data.data[
            "int_AAG_as_defauts_puissance"]
        self.int_AAG_as_defauts_moteur.text = app_data.data[
            "int_AAG_as_defauts_moteur"]
        self.int_AAG_as_defauts_commande.text = app_data.data[
            "int_AAG_as_defauts_commande"]
        self.int_AAG_as_niveau_bas.text = app_data.data[
            "int_AAG_as_niveau_bas"]
        self.int_AAG_as_test_lampes.text = app_data.data[
            "int_AAG_as_test_lampes"]
        self.int_AAG_as_controle_ARU2.text = app_data.data[
            "int_AAG_as_controle_ARU2"]
        self.int_AAG_signalisation_defauts.text = app_data.data[
            "int_AAG_signalisation_defauts"]
        self.int_AAG_APG_pompe_double_sens_rotation.text = app_data.data[
            "int_AAG_APG_pompe_double_sens_rotation"]
        self.int_AAG_APG_pompe_double_marche_arret_moteur.text = app_data.data[
            "int_AAG_APG_pompe_double_marche_arret_moteur"]
        self.int_AAG_APG_pompe_double_courant_demarrage.text = app_data.data[
            "int_AAG_APG_pompe_double_courant_demarrage"]
        self.int_AAG_APG_pompe_double_courant_service.text = app_data.data[
            "int_AAG_APG_pompe_double_courant_service"]
        self.int_AAG_RTRIB_reglage_limiteur_pression_centrale.text = app_data.data[
            "int_AAG_RTRIB_reglage_limiteur_pression_centrale"]
        self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne.text = app_data.data[
            "int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"]
        self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur.text = app_data.data[
            "int_AAG_RTRIB_controle_vitesses_recepteur_moteur"]
        self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe.text = app_data.data[
            "int_AAG_RTRIB_controle_vitesses_recepteur_pompe"]
        self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax.text = app_data.data[
            "int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"]
        self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros.text = app_data.data[
            "int_AAG_RTRIB_controle_fin_course_electrique_arret_electros"]
        self.int_AAG_RTRIB_controle_fin_course_electrique_PX1.text = app_data.data[
            "int_AAG_RTRIB_controle_fin_course_electrique_PX1"]
        self.int_AAG_RTRIB_controle_fin_course_electrique_PX2.text = app_data.data[
            "int_AAG_RTRIB_controle_fin_course_electrique_PX2"]
        self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle.text = app_data.data[
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"]
        self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre.text = app_data.data[
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"]
        self.int_AAG_RBAB_reglage_limiteur_pression_centrale.text = app_data.data[
            "int_AAG_RBAB_reglage_limiteur_pression_centrale"]
        self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne.text = app_data.data[
            "int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne"]
        self.int_AAG_RBAB_controle_vitesses_recepteur_moteur.text = app_data.data[
            "int_AAG_RBAB_controle_vitesses_recepteur_moteur"]
        self.int_AAG_RBAB_controle_vitesses_recepteur_pompe.text = app_data.data[
            "int_AAG_RBAB_controle_vitesses_recepteur_pompe"]
        self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax.text = app_data.data[
            "int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"]
        self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros.text = app_data.data[
            "int_AAG_RBAB_controle_fin_course_electrique_arret_electros"]
        self.int_AAG_RBAB_controle_fin_course_electrique_PX1.text = app_data.data[
            "int_AAG_RBAB_controle_fin_course_electrique_PX1"]
        self.int_AAG_RBAB_controle_fin_course_electrique_PX2.text = app_data.data[
            "int_AAG_RBAB_controle_fin_course_electrique_PX2"]
        self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle.text = app_data.data[
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"]
        self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre.text = app_data.data[
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"]

        self.int_AAG_schema_synoptique.hint_text = app_data.data[
            "int_AAG_schema_synoptique"]
        self.int_AAG_schema_electrique.hint_text = app_data.data[
            "int_AAG_schema_electrique"]
        self.int_AAG_schema_bornier.hint_text = app_data.data[
            "int_AAG_schema_bornier"]
        self.int_AAG_schema_cablage.hint_text = app_data.data[
            "int_AAG_schema_cablage"]
        self.int_AAG_releves_rincages_circuits.hint_text = app_data.data[
            "int_AAG_releves_rincages_circuits"]
        self.int_AAG_as_niveau_bas_NB1.hint_text = app_data.data[
            "int_AAG_as_niveau_bas_NB1"]
        self.int_AAG_as_controle_ARU.hint_text = app_data.data[
            "int_AAG_as_controle_ARU"]
        self.int_AAG_as_alarme_hydraulique_voyant_defaut.hint_text = app_data.data[
            "int_AAG_as_alarme_hydraulique_voyant_defaut"]
        self.int_AAG_verif_zero_mecanique_safran.hint_text = app_data.data[
            "int_AAG_verif_zero_mecanique_safran"]
        self.int_AAG_verif_zero_mecanique_recepteur.hint_text = app_data.data[
            "int_AAG_verif_zero_mecanique_recepteur"]
        self.int_AAG_verif_positionnement_transmetteur_BOPP.hint_text = app_data.data[
            "int_AAG_verif_positionnement_transmetteur_BOPP"]
        self.int_AAG_controle_puissance.hint_text = app_data.data[
            "int_AAG_controle_puissance"]
        self.int_AAG_controle_frequence.hint_text = app_data.data[
            "int_AAG_controle_frequence"]
        self.int_AAG_controle_commande.hint_text = app_data.data[
            "int_AAG_controle_commande"]
        self.int_AAG_controle_presence_24VDC.hint_text = app_data.data[
            "int_AAG_controle_presence_24VDC"]
        self.int_AAG_as_defauts_puissance.hint_text = app_data.data[
            "int_AAG_as_defauts_puissance"]
        self.int_AAG_as_defauts_moteur.hint_text = app_data.data[
            "int_AAG_as_defauts_moteur"]
        self.int_AAG_as_defauts_commande.hint_text = app_data.data[
            "int_AAG_as_defauts_commande"]
        self.int_AAG_as_niveau_bas.hint_text = app_data.data[
            "int_AAG_as_niveau_bas"]
        self.int_AAG_as_test_lampes.hint_text = app_data.data[
            "int_AAG_as_test_lampes"]
        self.int_AAG_as_controle_ARU2.hint_text = app_data.data[
            "int_AAG_as_controle_ARU2"]
        self.int_AAG_signalisation_defauts.hint_text = app_data.data[
            "int_AAG_signalisation_defauts"]
        self.int_AAG_APG_pompe_double_sens_rotation.hint_text = app_data.data[
            "int_AAG_APG_pompe_double_sens_rotation"]
        self.int_AAG_APG_pompe_double_marche_arret_moteur.hint_text = app_data.data[
            "int_AAG_APG_pompe_double_marche_arret_moteur"]
        self.int_AAG_APG_pompe_double_courant_demarrage.hint_text = app_data.data[
            "int_AAG_APG_pompe_double_courant_demarrage"]
        self.int_AAG_APG_pompe_double_courant_service.hint_text = app_data.data[
            "int_AAG_APG_pompe_double_courant_service"]
        self.int_AAG_RTRIB_reglage_limiteur_pression_centrale.hint_text = app_data.data[
            "int_AAG_RTRIB_reglage_limiteur_pression_centrale"]
        self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne.hint_text = app_data.data[
            "int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"]
        self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_vitesses_recepteur_moteur"]
        self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_vitesses_recepteur_pompe"]
        self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"]
        self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_fin_course_electrique_arret_electros"]
        self.int_AAG_RTRIB_controle_fin_course_electrique_PX1.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_fin_course_electrique_PX1"]
        self.int_AAG_RTRIB_controle_fin_course_electrique_PX2.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_fin_course_electrique_PX2"]
        self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"]
        self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre.hint_text = app_data.data[
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"]
        self.int_AAG_RBAB_reglage_limiteur_pression_centrale.hint_text = app_data.data[
            "int_AAG_RBAB_reglage_limiteur_pression_centrale"]
        self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne.hint_text = app_data.data[
            "int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne"]
        self.int_AAG_RBAB_controle_vitesses_recepteur_moteur.hint_text = app_data.data[
            "int_AAG_RBAB_controle_vitesses_recepteur_moteur"]
        self.int_AAG_RBAB_controle_vitesses_recepteur_pompe.hint_text = app_data.data[
            "int_AAG_RBAB_controle_vitesses_recepteur_pompe"]
        self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax.hint_text = app_data.data[
            "int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"]
        self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros.hint_text = app_data.data[
            "int_AAG_RBAB_controle_fin_course_electrique_arret_electros"]
        self.int_AAG_RBAB_controle_fin_course_electrique_PX1.hint_text = app_data.data[
            "int_AAG_RBAB_controle_fin_course_electrique_PX1"]
        self.int_AAG_RBAB_controle_fin_course_electrique_PX2.hint_text = app_data.data[
            "int_AAG_RBAB_controle_fin_course_electrique_PX2"]
        self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle.hint_text = app_data.data[
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"]
        self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre.hint_text = app_data.data[
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"]

    def link_data(self):
        """ 
        Met à jour les données à partir des données entrées par l'utilisateur
        """
        app_data = AppData()
        self.case_number = app_data.case_number
        
        app_data.AAG_schema_synoptique = self.AAG_schema_synoptique.text
        app_data.AAG_schema_electrique = self.AAG_schema_electrique.text
        app_data.AAG_schema_bornier = self.AAG_schema_bornier.text
        app_data.AAG_schema_cablage = self.AAG_schema_cablage.text
        app_data.AAG_releves_rincages_circuits = self.AAG_releves_rincages_circuits.text
        app_data.AAG_as_niveau_bas_NB1 = self.AAG_as_niveau_bas_NB1.text
        app_data.AAG_as_controle_ARU = self.AAG_as_controle_ARU.text
        app_data.AAG_as_alarme_hydraulique_voyant_defaut = self.AAG_as_alarme_hydraulique_voyant_defaut.text
        app_data.AAG_verif_zero_mecanique_safran = self.AAG_verif_zero_mecanique_safran.text
        app_data.AAG_verif_zero_mecanique_recepteur = self.AAG_verif_zero_mecanique_recepteur.text
        app_data.AAG_verif_positionnement_transmetteur_BOPP = self.AAG_verif_positionnement_transmetteur_BOPP.text
        app_data.AAG_controle_puissance = self.AAG_controle_puissance.text
        app_data.AAG_controle_frequence = self.AAG_controle_frequence.text
        app_data.AAG_controle_commande = self.AAG_controle_commande.text
        app_data.AAG_controle_presence_24VDC = self.AAG_controle_presence_24VDC.text
        app_data.AAG_as_defauts_puissance = self.AAG_as_defauts_puissance.text
        app_data.AAG_as_defauts_moteur = self.AAG_as_defauts_moteur.text
        app_data.AAG_as_defauts_commande = self.AAG_as_defauts_commande.text
        app_data.AAG_as_niveau_bas = self.AAG_as_niveau_bas.text
        app_data.AAG_as_test_lampes = self.AAG_as_test_lampes.text
        app_data.AAG_as_controle_ARU2 = self.AAG_as_controle_ARU2.text
        app_data.AAG_signalisation_defauts = self.AAG_signalisation_defauts.text
        app_data.AAG_APG_pompe_double_sens_rotation = self.AAG_APG_pompe_double_sens_rotation.text
        app_data.AAG_APG_pompe_double_marche_arret_moteur = self.AAG_APG_pompe_double_marche_arret_moteur.text
        app_data.AAG_APG_pompe_double_courant_demarrage = self.AAG_APG_pompe_double_courant_demarrage.text
        app_data.AAG_APG_pompe_double_courant_service = self.AAG_APG_pompe_double_courant_service.text
        app_data.AAG_RTRIB_reglage_limiteur_pression_centrale = self.AAG_RTRIB_reglage_limiteur_pression_centrale.text
        app_data.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne = self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne.text
        app_data.AAG_RTRIB_controle_vitesses_recepteur_moteur = self.AAG_RTRIB_controle_vitesses_recepteur_moteur.text
        app_data.AAG_RTRIB_controle_vitesses_recepteur_pompe = self.AAG_RTRIB_controle_vitesses_recepteur_pompe.text
        app_data.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax = self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax.text
        app_data.AAG_RTRIB_controle_fin_course_electrique_arret_electros = self.AAG_RTRIB_controle_fin_course_electrique_arret_electros.text
        app_data.AAG_RTRIB_controle_fin_course_electrique_PX1 = self.AAG_RTRIB_controle_fin_course_electrique_PX1.text
        app_data.AAG_RTRIB_controle_fin_course_electrique_PX2 = self.AAG_RTRIB_controle_fin_course_electrique_PX2.text
        app_data.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle = self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle.text
        app_data.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre = self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre.text
        app_data.AAG_RBAB_reglage_limiteur_pression_centrale = self.AAG_RBAB_reglage_limiteur_pression_centrale.text
        app_data.AAG_RBAB_reglage_limiteur_pression_double_en_ligne = self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne.text
        app_data.AAG_RBAB_controle_vitesses_recepteur_moteur = self.AAG_RBAB_controle_vitesses_recepteur_moteur.text
        app_data.AAG_RBAB_controle_vitesses_recepteur_pompe = self.AAG_RBAB_controle_vitesses_recepteur_pompe.text
        app_data.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax = self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax.text
        app_data.AAG_RBAB_controle_fin_course_electrique_arret_electros = self.AAG_RBAB_controle_fin_course_electrique_arret_electros.text
        app_data.AAG_RBAB_controle_fin_course_electrique_PX1 = self.AAG_RBAB_controle_fin_course_electrique_PX1.text
        app_data.AAG_RBAB_controle_fin_course_electrique_PX2 = self.AAG_RBAB_controle_fin_course_electrique_PX2.text
        app_data.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle = self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle.text
        app_data.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre = self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre.text

        app_data.int_AAG_schema_synoptique = self.int_AAG_schema_synoptique.text
        app_data.int_AAG_schema_electrique = self.int_AAG_schema_electrique.text
        app_data.int_AAG_schema_bornier = self.int_AAG_schema_bornier.text
        app_data.int_AAG_schema_cablage = self.int_AAG_schema_cablage.text
        app_data.int_AAG_releves_rincages_circuits = self.int_AAG_releves_rincages_circuits.text
        app_data.int_AAG_as_niveau_bas_NB1 = self.int_AAG_as_niveau_bas_NB1.text
        app_data.int_AAG_as_controle_ARU = self.int_AAG_as_controle_ARU.text
        app_data.int_AAG_as_alarme_hydraulique_voyant_defaut = self.int_AAG_as_alarme_hydraulique_voyant_defaut.text
        app_data.int_AAG_verif_zero_mecanique_safran = self.int_AAG_verif_zero_mecanique_safran.text
        app_data.int_AAG_verif_zero_mecanique_recepteur = self.int_AAG_verif_zero_mecanique_recepteur.text
        app_data.int_AAG_verif_positionnement_transmetteur_BOPP = self.int_AAG_verif_positionnement_transmetteur_BOPP.text
        app_data.int_AAG_controle_puissance = self.int_AAG_controle_puissance.text
        app_data.int_AAG_controle_frequence = self.int_AAG_controle_frequence.text
        app_data.int_AAG_controle_commande = self.int_AAG_controle_commande.text
        app_data.int_AAG_controle_presence_24VDC = self.int_AAG_controle_presence_24VDC.text
        app_data.int_AAG_as_defauts_puissance = self.int_AAG_as_defauts_puissance.text
        app_data.int_AAG_as_defauts_moteur = self.int_AAG_as_defauts_moteur.text
        app_data.int_AAG_as_defauts_commande = self.int_AAG_as_defauts_commande.text
        app_data.int_AAG_as_niveau_bas = self.int_AAG_as_niveau_bas.text
        app_data.int_AAG_as_test_lampes = self.int_AAG_as_test_lampes.text
        app_data.int_AAG_as_controle_ARU2 = self.int_AAG_as_controle_ARU2.text
        app_data.int_AAG_signalisation_defauts = self.int_AAG_signalisation_defauts.text
        app_data.int_AAG_APG_pompe_double_sens_rotation = self.int_AAG_APG_pompe_double_sens_rotation.text
        app_data.int_AAG_APG_pompe_double_marche_arret_moteur = self.int_AAG_APG_pompe_double_marche_arret_moteur.text
        app_data.int_AAG_APG_pompe_double_courant_demarrage = self.int_AAG_APG_pompe_double_courant_demarrage.text
        app_data.int_AAG_APG_pompe_double_courant_service = self.int_AAG_APG_pompe_double_courant_service.text
        app_data.int_AAG_RTRIB_reglage_limiteur_pression_centrale = self.int_AAG_RTRIB_reglage_limiteur_pression_centrale.text
        app_data.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne = self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne.text
        app_data.int_AAG_RTRIB_controle_vitesses_recepteur_moteur = self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur.text
        app_data.int_AAG_RTRIB_controle_vitesses_recepteur_pompe = self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe.text
        app_data.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax = self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax.text
        app_data.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros = self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros.text
        app_data.int_AAG_RTRIB_controle_fin_course_electrique_PX1 = self.int_AAG_RTRIB_controle_fin_course_electrique_PX1.text
        app_data.int_AAG_RTRIB_controle_fin_course_electrique_PX2 = self.int_AAG_RTRIB_controle_fin_course_electrique_PX2.text
        app_data.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle = self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle.text
        app_data.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre = self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre.text
        app_data.int_AAG_RBAB_reglage_limiteur_pression_centrale = self.int_AAG_RBAB_reglage_limiteur_pression_centrale.text
        app_data.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne = self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne.text
        app_data.int_AAG_RBAB_controle_vitesses_recepteur_moteur = self.int_AAG_RBAB_controle_vitesses_recepteur_moteur.text
        app_data.int_AAG_RBAB_controle_vitesses_recepteur_pompe = self.int_AAG_RBAB_controle_vitesses_recepteur_pompe.text
        app_data.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax = self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax.text
        app_data.int_AAG_RBAB_controle_fin_course_electrique_arret_electros = self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros.text
        app_data.int_AAG_RBAB_controle_fin_course_electrique_PX1 = self.int_AAG_RBAB_controle_fin_course_electrique_PX1.text
        app_data.int_AAG_RBAB_controle_fin_course_electrique_PX2 = self.int_AAG_RBAB_controle_fin_course_electrique_PX2.text
        app_data.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle = self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle.text
        app_data.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre = self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre.text

    def submit_form(self, instance):
        """
        Valide la saisie utilisateur, sauvegarde et passe à l'écran suivant 
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_int_appareil_gouverne()
        self.manager.current = 'int_recap_intervention'

    def go_to_modif_choix_categorie(self, instance):
        """
        Passe à l'écran de choix de la catégorie à modifier
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        self.link_data()
        app_data = AppData()
        app_data.save_data_int_appareil_gouverne()
        self.manager.current = 'int_cabestan'
