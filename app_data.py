from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivy.uixinput import TextInput
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
from PIL import Image as PilImage  
from kivy.lang import Builder
import shutil
import json
import os
import datetime

class AppData:
    """ 
    Classe permettant de stocker les données de l'application
    L'utilisation de _instance et de cls permet manipuler une instance unique de cette classe
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:

            # -------------------------------------
            # Définition des variables BE
            # -------------------------------------

            cls._instance = super(AppData, cls).__new__(cls)
            
            cls._instance.case_number = ""
            cls._instance.client_name = ""
            cls._instance.boat_name = ""
            cls._instance.nb_field = ""
            cls._instance.site_name = ""
            cls._instance.armement = ""
            # cls._instance.visa = ""
            cls._instance.intervention_type = ""
            
            cls._instance.BOPP_name = ""
            cls._instance.BOPP_date = ""
            cls._instance.BOPP_visa = ""
            
            cls._instance.chantier_name = ""
            cls._instance.chantier_date = ""
            cls._instance.chantier_visa = ""

            cls._instance.armement_name = ""
            cls._instance.armement_date = ""
            cls._instance.armement_visa = ""

            cls._instance.Lm_schema_synoptique = ""
            cls._instance.Lm_schema_electrique = ""
            cls._instance.Lm_schema_bornier = ""
            cls._instance.Lm_schema_cablage = ""
            cls._instance.Lm_releves_rincages_circuits = ""
            cls._instance.Lm_as_niveau_bas_NB1 = ""
            cls._instance.Lm_as_temperature_haute_TH1 = ""
            cls._instance.Lm_as_controle_ARU = ""
            cls._instance.Lm_as_alarme_hydraulique_voyant_defaut = ""
            cls._instance.Lm_pompe_principale_45_100_verif_plein_huile = ""
            cls._instance.Lm_pompe_principale_45_100_sens_rotation = ""
            cls._instance.Lm_pompe_principale_45_100_embrayage_pompe = ""
            cls._instance.Lm_pompe_principale_45_100_pression_HP = ""
            cls._instance.Lm_pompe_principale_45_100_stand_by = ""
            cls._instance.Lm_pompe_principale_HPR165_38_verif_plein_huile = ""
            cls._instance.Lm_pompe_principale_HPR165_38_sens_rotation = ""
            cls._instance.Lm_pompe_principale_HPR165_38_embrayage_pompe = ""
            cls._instance.Lm_pompe_principale_HPR165_38_pression_HP = ""
            cls._instance.Lm_pompe_principale_HPR165_38_stand_by = ""
            cls._instance.Lm_groupe_secours_pompe_45_sens_rotation = ""
            cls._instance.Lm_groupe_secours_pompe_45_calage = ""
            cls._instance.Lm_groupe_secours_pompe_45_serrage = ""
            cls._instance.Lm_groupe_secours_pompe_45_verif_plein_huile = ""
            cls._instance.Lm_groupe_secours_pompe_45_marche_arret_moteur = ""
            cls._instance.Lm_groupe_secours_pompe_45_pression_HP = ""
            cls._instance.Lm_groupe_secours_pompe_45_stand_by = ""
            cls._instance.Lm_groupe_secours_pompe_45_courant_demarrage = ""
            cls._instance.Lm_groupe_secours_pompe_45_courant_service = ""
            cls._instance.Lm_reglage_limiteur_pression_REP10 = ""
            cls._instance.Lm_reglage_pressostat_retour = ""
            cls._instance.Lm_reglage_reducteur_pression_REP13 = ""
            cls._instance.Lm_reglage_reducteur_pression_grue_REP16 = ""
            cls._instance.Lm_fonctionnement_sys_refrigeration_embrayage = ""

            cls._instance.TPH125_0_traction_premiere_couche_statique = ""
            cls._instance.TPH125_0_traction_premiere_couche_dynamique = ""
            cls._instance.TPH125_0_pression = ""
            cls._instance.TPH125_0_vitesse_rotation_PV = ""
            cls._instance.TPH125_0_vitesse_rotation_GV = ""
            cls._instance.TPH125_0_debit = ""
            cls._instance.TPH125_0_essai_file_vire = ""
            cls._instance.TPH125_0_essai_freinage = ""
            cls._instance.TPH125_0_selection_PV_GV = ""
            cls._instance.TPH50_0_traction_premiere_couche_statique = ""
            cls._instance.TPH50_0_traction_premiere_couche_dynamique = ""
            cls._instance.TPH50_0_pression = ""
            cls._instance.TPH50_0_vitesse_rotation_PV = ""
            cls._instance.TPH50_0_vitesse_rotation_GV = ""
            cls._instance.TPH50_0_debit = ""
            cls._instance.TPH50_0_essai_file_vire = ""
            cls._instance.TPH50_0_essai_freinage = ""
            cls._instance.TPH50_0_selection_PV_GV = ""

            cls._instance.AAG_schema_synoptique = ""
            cls._instance.AAG_schema_electrique = ""
            cls._instance.AAG_schema_bornier = ""
            cls._instance.AAG_schema_cablage = ""
            cls._instance.AAG_releves_rincages_circuits = ""
            cls._instance.AAG_as_niveau_bas_NB1 = ""
            cls._instance.AAG_as_controle_ARU = ""
            cls._instance.AAG_as_alarme_hydraulique_voyant_defaut = ""
            cls._instance.AAG_verif_zero_mecanique_safran = ""
            cls._instance.AAG_verif_zero_mecanique_recepteur = ""
            cls._instance.AAG_verif_positionnement_transmetteur_BOPP = ""
            cls._instance.AAG_controle_puissance = ""
            cls._instance.AAG_controle_frequence = ""
            cls._instance.AAG_controle_commande = ""
            cls._instance.AAG_controle_presence_24VDC = ""
            cls._instance.AAG_as_defauts_puissance = ""
            cls._instance.AAG_as_defauts_moteur = ""
            cls._instance.AAG_as_defauts_commande = ""
            cls._instance.AAG_as_niveau_bas = ""
            cls._instance.AAG_as_test_lampes = ""
            cls._instance.AAG_as_controle_ARU2 = ""
            cls._instance.AAG_signalisation_defauts = ""
            cls._instance.AAG_APG_pompe_double_sens_rotation = ""
            cls._instance.AAG_APG_pompe_double_marche_arret_moteur = ""
            cls._instance.AAG_APG_pompe_double_courant_demarrage = ""
            cls._instance.AAG_APG_pompe_double_courant_service = ""
            cls._instance.AAG_RTRIB_reglage_limiteur_pression_centrale = ""
            cls._instance.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne = ""
            cls._instance.AAG_RTRIB_controle_vitesses_recepteur_moteur = ""
            cls._instance.AAG_RTRIB_controle_vitesses_recepteur_pompe = ""
            cls._instance.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax = ""
            cls._instance.AAG_RTRIB_controle_fin_course_electrique_arret_electros = ""
            cls._instance.AAG_RTRIB_controle_fin_course_electrique_PX1 = ""
            cls._instance.AAG_RTRIB_controle_fin_course_electrique_PX2 = ""
            cls._instance.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle = ""
            cls._instance.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre = ""
            cls._instance.AAG_RBAB_reglage_limiteur_pression_centrale = ""
            cls._instance.AAG_RBAB_reglage_limiteur_pression_double_en_ligne = ""
            cls._instance.AAG_RBAB_controle_vitesses_recepteur_moteur = ""
            cls._instance.AAG_RBAB_controle_vitesses_recepteur_pompe = ""
            cls._instance.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax = ""
            cls._instance.AAG_RBAB_controle_fin_course_electrique_arret_electros = ""
            cls._instance.AAG_RBAB_controle_fin_course_electrique_PX1 = ""
            cls._instance.AAG_RBAB_controle_fin_course_electrique_PX2 = ""
            cls._instance.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle = ""
            cls._instance.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre = ""
            cls._instance.Cb_5T_traction_statique = ""
            cls._instance.Cb_5T_traction_dynamique = ""
            cls._instance.Cb_5T_pression = ""
            cls._instance.Cb_5T_vitesse_rotation = ""
            cls._instance.Cb_5T_debit = ""
            cls._instance.Cb_5T_essai_file_vire = ""
            cls._instance.Cb_5T_freinage = ""
            cls._instance.Cb_3T_traction_statique = ""
            cls._instance.Cb_3T_traction_dynamique = ""
            cls._instance.Cb_3T_pression = ""
            cls._instance.Cb_3T_vitesse_rotation = ""
            cls._instance.Cb_3T_debit = ""
            cls._instance.Cb_3T_essai_file_vire = ""
            cls._instance.Cb_3T_freinage = ""

            cls._instance.picture = []
            cls._instance.is_galerie = False

            #-------------------------------------
            # Définition des variables intervenant
            # -------------------------------------

            cls._instance.int_Lm_schema_synoptique = ""
            cls._instance.int_Lm_schema_electrique = ""
            cls._instance.int_Lm_schema_bornier = ""
            cls._instance.int_Lm_schema_cablage = ""
            cls._instance.int_Lm_releves_rincages_circuits = ""
            cls._instance.int_Lm_as_niveau_bas_NB1 = ""
            cls._instance.int_Lm_as_temperature_haute_TH1 = ""
            cls._instance.int_Lm_as_controle_ARU = ""
            cls._instance.int_Lm_as_alarme_hydraulique_voyant_defaut = ""
            cls._instance.int_Lm_pompe_principale_45_100_verif_plein_huile = ""
            cls._instance.int_Lm_pompe_principale_45_100_sens_rotation = ""
            cls._instance.int_Lm_pompe_principale_45_100_embrayage_pompe = ""
            cls._instance.int_Lm_pompe_principale_45_100_pression_HP = ""
            cls._instance.int_Lm_pompe_principale_45_100_stand_by = ""
            cls._instance.int_Lm_pompe_principale_HPR165_38_verif_plein_huile = ""
            cls._instance.int_Lm_pompe_principale_HPR165_38_sens_rotation = ""
            cls._instance.int_Lm_pompe_principale_HPR165_38_embrayage_pompe = ""
            cls._instance.int_Lm_pompe_principale_HPR165_38_pression_HP = ""
            cls._instance.int_Lm_pompe_principale_HPR165_38_stand_by = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_sens_rotation = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_calage = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_serrage = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_verif_plein_huile = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_marche_arret_moteur = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_pression_HP = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_stand_by = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_courant_demarrage = ""
            cls._instance.int_Lm_groupe_secours_pompe_45_courant_service = ""
            cls._instance.int_Lm_reglage_limiteur_pression_REP10 = ""
            cls._instance.int_Lm_reglage_pressostat_retour = ""
            cls._instance.int_Lm_reglage_reducteur_pression_REP13 = ""
            cls._instance.int_Lm_reglage_reducteur_pression_grue_REP16 = ""
            cls._instance.int_Lm_fonctionnement_sys_refrigeration_embrayage = ""

            cls._instance.int_TPH125_0_traction_premiere_couche_statique = ""
            cls._instance.int_TPH125_0_traction_premiere_couche_dynamique = ""
            cls._instance.int_TPH125_0_pression = ""
            cls._instance.int_TPH125_0_vitesse_rotation_PV = ""
            cls._instance.int_TPH125_0_vitesse_rotation_GV = ""
            cls._instance.int_TPH125_0_debit = ""
            cls._instance.int_TPH125_0_essai_file_vire = ""
            cls._instance.int_TPH125_0_essai_freinage = ""
            cls._instance.int_TPH125_0_selection_PV_GV = ""
            cls._instance.int_TPH50_0_traction_premiere_couche_statique = ""
            cls._instance.int_TPH50_0_traction_premiere_couche_dynamique = ""
            cls._instance.int_TPH50_0_pression = ""
            cls._instance.int_TPH50_0_vitesse_rotation_PV = ""
            cls._instance.int_TPH50_0_vitesse_rotation_GV = ""
            cls._instance.int_TPH50_0_debit = ""
            cls._instance.int_TPH50_0_essai_file_vire = ""
            cls._instance.int_TPH50_0_essai_freinage = ""
            cls._instance.int_TPH50_0_selection_PV_GV = ""

            cls._instance.int_AAG_schema_synoptique = ""
            cls._instance.int_AAG_schema_electrique = ""
            cls._instance.int_AAG_schema_bornier = ""
            cls._instance.int_AAG_schema_cablage = ""
            cls._instance.int_AAG_releves_rincages_circuits = ""
            cls._instance.int_AAG_as_niveau_bas_NB1 = ""
            cls._instance.int_AAG_as_controle_ARU = ""
            cls._instance.int_AAG_as_alarme_hydraulique_voyant_defaut = ""
            cls._instance.int_AAG_verif_zero_mecanique_safran = ""
            cls._instance.int_AAG_verif_zero_mecanique_recepteur = ""
            cls._instance.int_AAG_verif_positionnement_transmetteur_BOPP = ""
            cls._instance.int_AAG_controle_puissance = ""
            cls._instance.int_AAG_controle_frequence = ""
            cls._instance.int_AAG_controle_commande = ""
            cls._instance.int_AAG_controle_presence_24VDC = ""
            cls._instance.int_AAG_as_defauts_puissance = ""
            cls._instance.int_AAG_as_defauts_moteur = ""
            cls._instance.int_AAG_as_defauts_commande = ""
            cls._instance.int_AAG_as_niveau_bas = ""
            cls._instance.int_AAG_as_test_lampes = ""
            cls._instance.int_AAG_as_controle_ARU2 = ""
            cls._instance.int_AAG_signalisation_defauts = ""
            cls._instance.int_AAG_APG_pompe_double_sens_rotation = ""
            cls._instance.int_AAG_APG_pompe_double_marche_arret_moteur = ""
            cls._instance.int_AAG_APG_pompe_double_courant_demarrage = ""
            cls._instance.int_AAG_APG_pompe_double_courant_service = ""
            cls._instance.int_AAG_RTRIB_reglage_limiteur_pression_centrale = ""
            cls._instance.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne = ""
            cls._instance.int_AAG_RTRIB_controle_vitesses_recepteur_moteur = ""
            cls._instance.int_AAG_RTRIB_controle_vitesses_recepteur_pompe = ""
            cls._instance.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax = ""
            cls._instance.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros = ""
            cls._instance.int_AAG_RTRIB_controle_fin_course_electrique_PX1 = ""
            cls._instance.int_AAG_RTRIB_controle_fin_course_electrique_PX2 = ""
            cls._instance.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle = ""
            cls._instance.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre = ""
            cls._instance.int_AAG_RBAB_reglage_limiteur_pression_centrale = ""
            cls._instance.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne = ""
            cls._instance.int_AAG_RBAB_controle_vitesses_recepteur_moteur = ""
            cls._instance.int_AAG_RBAB_controle_vitesses_recepteur_pompe = ""
            cls._instance.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax = ""
            cls._instance.int_AAG_RBAB_controle_fin_course_electrique_arret_electros = ""
            cls._instance.int_AAG_RBAB_controle_fin_course_electrique_PX1 = ""
            cls._instance.int_AAG_RBAB_controle_fin_course_electrique_PX2 = ""
            cls._instance.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle = ""
            cls._instance.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre = ""
            cls._instance.int_Cb_5T_traction_statique = ""
            cls._instance.int_Cb_5T_traction_dynamique = ""
            cls._instance.int_Cb_5T_pression = ""
            cls._instance.int_Cb_5T_vitesse_rotation = ""
            cls._instance.int_Cb_5T_debit = ""
            cls._instance.int_Cb_5T_essai_file_vire = ""
            cls._instance.int_Cb_5T_freinage = ""
            cls._instance.int_Cb_3T_traction_statique = ""
            cls._instance.int_Cb_3T_traction_dynamique = ""
            cls._instance.int_Cb_3T_pression = ""
            cls._instance.int_Cb_3T_vitesse_rotation = ""
            cls._instance.int_Cb_3T_debit = ""
            cls._instance.int_Cb_3T_essai_file_vire = ""
            cls._instance.int_Cb_3T_freinage = ""

            cls._instance.int_pieces_changees = ""
            cls._instance.int_pieces_cassees = ""
            cls._instance.int_temps_passe = ""
            cls._instance.int_temps_mort = ""
            cls._instance.int_commentaires = ""

        return cls._instance
    
    def save_data(self):
        """ 
        Sauvegarde les données dans un fichier json
        """
        self.data = {
            "case_number": self.case_number,
            "client_name": self.client_name,
            "boat_name": self.boat_name,
            "nb_field": self.nb_field,
            "site_name": self.site_name,
            "intervention_type": self.intervention_type,
            "armement": self.armement,
            # "visa": self.visa,
            "BOPP_name": self.BOPP_name,
            "BOPP_date": self.BOPP_date,
            "BOPP_visa": self.BOPP_visa,
            "chantier_name": self.chantier_name,
            "chantier_date": self.chantier_date,
            "chantier_visa": self.chantier_visa,
            "armement_name": self.armement_name,
            "armement_date": self.armement_date,
            "armement_visa": self.armement_visa,
            "Lm_schema_synoptique": self.Lm_schema_synoptique,
            "Lm_schema_electrique": self.Lm_schema_electrique,
            "Lm_schema_bornier": self.Lm_schema_bornier,
            "Lm_schema_cablage": self.Lm_schema_cablage,
            "Lm_releves_rincages_circuits": self.Lm_releves_rincages_circuits,
            "Lm_as_niveau_bas_NB1": self.Lm_as_niveau_bas_NB1,
            "Lm_as_temperature_haute_TH1": self.Lm_as_temperature_haute_TH1,
            "Lm_as_controle_ARU": self.Lm_as_controle_ARU,
            "Lm_as_alarme_hydraulique_voyant_defaut": self.Lm_as_alarme_hydraulique_voyant_defaut,
            "Lm_pompe_principale_45_100_verif_plein_huile": self.Lm_pompe_principale_45_100_verif_plein_huile,
            "Lm_pompe_principale_45_100_sens_rotation": self.Lm_pompe_principale_45_100_sens_rotation,
            "Lm_pompe_principale_45_100_embrayage_pompe": self.Lm_pompe_principale_45_100_embrayage_pompe,
            "Lm_pompe_principale_45_100_pression_HP": self.Lm_pompe_principale_45_100_pression_HP,
            "Lm_pompe_principale_45_100_stand_by": self.Lm_pompe_principale_45_100_stand_by,
            "Lm_pompe_principale_HPR165_38_verif_plein_huile": self.Lm_pompe_principale_HPR165_38_verif_plein_huile,
            "Lm_pompe_principale_HPR165_38_sens_rotation": self.Lm_pompe_principale_HPR165_38_sens_rotation,
            "Lm_pompe_principale_HPR165_38_embrayage_pompe": self.Lm_pompe_principale_HPR165_38_embrayage_pompe,
            "Lm_pompe_principale_HPR165_38_pression_HP": self.Lm_pompe_principale_HPR165_38_pression_HP,
            "Lm_pompe_principale_HPR165_38_stand_by": self.Lm_pompe_principale_HPR165_38_stand_by,
            "Lm_groupe_secours_pompe_45_sens_rotation": self.Lm_groupe_secours_pompe_45_sens_rotation,
            "Lm_groupe_secours_pompe_45_calage": self.Lm_groupe_secours_pompe_45_calage,
            "Lm_groupe_secours_pompe_45_serrage": self.Lm_groupe_secours_pompe_45_serrage,
            "Lm_groupe_secours_pompe_45_verif_plein_huile": self.Lm_groupe_secours_pompe_45_verif_plein_huile,
            "Lm_groupe_secours_pompe_45_marche_arret_moteur": self.Lm_groupe_secours_pompe_45_marche_arret_moteur,
            "Lm_groupe_secours_pompe_45_pression_HP": self.Lm_groupe_secours_pompe_45_pression_HP,
            "Lm_groupe_secours_pompe_45_stand_by": self.Lm_groupe_secours_pompe_45_stand_by,
            "Lm_groupe_secours_pompe_45_courant_demarrage": self.Lm_groupe_secours_pompe_45_courant_demarrage,
            "Lm_groupe_secours_pompe_45_courant_service": self.Lm_groupe_secours_pompe_45_courant_service,
            "Lm_reglage_limiteur_pression_REP10": self.Lm_reglage_limiteur_pression_REP10,
            "Lm_reglage_pressostat_retour": self.Lm_reglage_pressostat_retour,
            "Lm_reglage_reducteur_pression_REP13": self.Lm_reglage_reducteur_pression_REP13,
            "Lm_reglage_reducteur_pression_grue_REP16": self.Lm_reglage_reducteur_pression_grue_REP16,
            "Lm_fonctionnement_sys_refrigeration_embrayage": self.Lm_fonctionnement_sys_refrigeration_embrayage,
            "TPH125_0_traction_premiere_couche_statique": self.TPH125_0_traction_premiere_couche_statique,
            "TPH125_0_traction_premiere_couche_dynamique": self.TPH125_0_traction_premiere_couche_dynamique,
            "TPH125_0_pression": self.TPH125_0_pression,
            "TPH125_0_vitesse_rotation_PV": self.TPH125_0_vitesse_rotation_PV,
            "TPH125_0_vitesse_rotation_GV": self.TPH125_0_vitesse_rotation_GV,
            "TPH125_0_debit": self.TPH125_0_debit,
            "TPH125_0_essai_file_vire": self.TPH125_0_essai_file_vire,
            "TPH125_0_essai_freinage": self.TPH125_0_essai_freinage,
            "TPH125_0_selection_PV_GV": self.TPH125_0_selection_PV_GV,
            "TPH50_0_traction_premiere_couche_statique": self.TPH50_0_traction_premiere_couche_statique,
            "TPH50_0_traction_premiere_couche_dynamique": self.TPH50_0_traction_premiere_couche_dynamique,
            "TPH50_0_pression": self.TPH50_0_pression,
            "TPH50_0_vitesse_rotation_PV": self.TPH50_0_vitesse_rotation_PV,
            "TPH50_0_vitesse_rotation_GV": self.TPH50_0_vitesse_rotation_GV,
            "TPH50_0_debit": self.TPH50_0_debit,
            "TPH50_0_essai_file_vire": self.TPH50_0_essai_file_vire,
            "TPH50_0_essai_freinage": self.TPH50_0_essai_freinage,
            "TPH50_0_selection_PV_GV": self.TPH50_0_selection_PV_GV,
            "AAG_schema_synoptique": self.AAG_schema_synoptique,
            "AAG_schema_electrique": self.AAG_schema_electrique,
            "AAG_schema_bornier": self.AAG_schema_bornier,
            "AAG_schema_cablage": self.AAG_schema_cablage,
            "AAG_releves_rincages_circuits": self.AAG_releves_rincages_circuits,
            "AAG_as_niveau_bas_NB1": self.AAG_as_niveau_bas_NB1,
            "AAG_as_controle_ARU": self.AAG_as_controle_ARU,
            "AAG_as_alarme_hydraulique_voyant_defaut": self.AAG_as_alarme_hydraulique_voyant_defaut,
            "AAG_verif_zero_mecanique_safran": self.AAG_verif_zero_mecanique_safran,
            "AAG_verif_zero_mecanique_recepteur": self.AAG_verif_zero_mecanique_recepteur,
            "AAG_verif_positionnement_transmetteur_BOPP": self.AAG_verif_positionnement_transmetteur_BOPP,
            "AAG_controle_puissance": self.AAG_controle_puissance,
            "AAG_controle_frequence": self.AAG_controle_frequence,
            "AAG_controle_commande": self.AAG_controle_commande,
            "AAG_controle_presence_24VDC": self.AAG_controle_presence_24VDC,
            "AAG_as_defauts_puissance": self.AAG_as_defauts_puissance,
            "AAG_as_defauts_moteur": self.AAG_as_defauts_moteur,
            "AAG_as_defauts_commande": self.AAG_as_defauts_commande,
            "AAG_as_niveau_bas": self.AAG_as_niveau_bas,
            "AAG_as_test_lampes": self.AAG_as_test_lampes,
            "AAG_as_controle_ARU2": self.AAG_as_controle_ARU2,
            "AAG_signalisation_defauts": self.AAG_signalisation_defauts,
            "AAG_APG_pompe_double_sens_rotation": self.AAG_APG_pompe_double_sens_rotation,
            "AAG_APG_pompe_double_marche_arret_moteur": self.AAG_APG_pompe_double_marche_arret_moteur,
            "AAG_APG_pompe_double_courant_demarrage": self.AAG_APG_pompe_double_courant_demarrage,
            "AAG_APG_pompe_double_courant_service": self.AAG_APG_pompe_double_courant_service,
            "AAG_RTRIB_reglage_limiteur_pression_centrale": self.AAG_RTRIB_reglage_limiteur_pression_centrale,
            "AAG_RTRIB_reglage_limiteur_pression_double_en_ligne": self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne,
            "AAG_RTRIB_controle_vitesses_recepteur_moteur": self.AAG_RTRIB_controle_vitesses_recepteur_moteur,
            "AAG_RTRIB_controle_vitesses_recepteur_pompe": self.AAG_RTRIB_controle_vitesses_recepteur_pompe,
            "AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax": self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax,
            "AAG_RTRIB_controle_fin_course_electrique_arret_electros": self.AAG_RTRIB_controle_fin_course_electrique_arret_electros,
            "AAG_RTRIB_controle_fin_course_electrique_PX1": self.AAG_RTRIB_controle_fin_course_electrique_PX1,
            "AAG_RTRIB_controle_fin_course_electrique_PX2": self.AAG_RTRIB_controle_fin_course_electrique_PX2,
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle": self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle,
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre": self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre,
            "AAG_RBAB_reglage_limiteur_pression_centrale": self.AAG_RBAB_reglage_limiteur_pression_centrale,
            "AAG_RBAB_reglage_limiteur_pression_double_en_ligne": self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne,
            "AAG_RBAB_controle_vitesses_recepteur_moteur": self.AAG_RBAB_controle_vitesses_recepteur_moteur,
            "AAG_RBAB_controle_vitesses_recepteur_pompe": self.AAG_RBAB_controle_vitesses_recepteur_pompe,
            "AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax": self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax,
            "AAG_RBAB_controle_fin_course_electrique_arret_electros": self.AAG_RBAB_controle_fin_course_electrique_arret_electros,
            "AAG_RBAB_controle_fin_course_electrique_PX1": self.AAG_RBAB_controle_fin_course_electrique_PX1,
            "AAG_RBAB_controle_fin_course_electrique_PX2": self.AAG_RBAB_controle_fin_course_electrique_PX2,
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle": self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle,
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre": self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre,
            "Cb_5T_traction_statique": self.Cb_5T_traction_statique,
            "Cb_5T_traction_dynamique": self.Cb_5T_traction_dynamique,
            "Cb_5T_pression": self.Cb_5T_pression,
            "Cb_5T_vitesse_rotation": self.Cb_5T_vitesse_rotation,
            "Cb_5T_debit": self.Cb_5T_debit,
            "Cb_5T_essai_file_vire": self.Cb_5T_essai_file_vire,
            "Cb_5T_freinage": self.Cb_5T_freinage,
            "Cb_3T_traction_statique": self.Cb_3T_traction_statique,
            "Cb_3T_traction_dynamique": self.Cb_3T_traction_dynamique,
            "Cb_3T_pression": self.Cb_3T_pression,
            "Cb_3T_vitesse_rotation": self.Cb_3T_vitesse_rotation,
            "Cb_3T_debit": self.Cb_3T_debit,
            "Cb_3T_essai_file_vire": self.Cb_3T_essai_file_vire,
            "Cb_3T_freinage": self.Cb_3T_freinage,
            "galerie": self.picture,

            "int_Lm_schema_synoptique": self.int_Lm_schema_synoptique,
            "int_Lm_schema_electrique": self.int_Lm_schema_electrique,
            "int_Lm_schema_bornier": self.int_Lm_schema_bornier,
            "int_Lm_schema_cablage": self.int_Lm_schema_cablage,
            "int_Lm_releves_rincages_circuits": self.int_Lm_releves_rincages_circuits,
            "int_Lm_as_niveau_bas_NB1": self.int_Lm_as_niveau_bas_NB1,
            "int_Lm_as_temperature_haute_TH1": self.int_Lm_as_temperature_haute_TH1,
            "int_Lm_as_controle_ARU": self.int_Lm_as_controle_ARU,
            "int_Lm_as_alarme_hydraulique_voyant_defaut": self.int_Lm_as_alarme_hydraulique_voyant_defaut,
            "int_Lm_pompe_principale_45_100_verif_plein_huile": self.int_Lm_pompe_principale_45_100_verif_plein_huile,
            "int_Lm_pompe_principale_45_100_sens_rotation": self.int_Lm_pompe_principale_45_100_sens_rotation,
            "int_Lm_pompe_principale_45_100_embrayage_pompe": self.int_Lm_pompe_principale_45_100_embrayage_pompe,
            "int_Lm_pompe_principale_45_100_pression_HP": self.int_Lm_pompe_principale_45_100_pression_HP,
            "int_Lm_pompe_principale_45_100_stand_by": self.int_Lm_pompe_principale_45_100_stand_by,
            "int_Lm_pompe_principale_HPR165_38_verif_plein_huile": self.int_Lm_pompe_principale_HPR165_38_verif_plein_huile,
            "int_Lm_pompe_principale_HPR165_38_sens_rotation": self.int_Lm_pompe_principale_HPR165_38_sens_rotation,
            "int_Lm_pompe_principale_HPR165_38_embrayage_pompe": self.int_Lm_pompe_principale_HPR165_38_embrayage_pompe,
            "int_Lm_pompe_principale_HPR165_38_pression_HP": self.int_Lm_pompe_principale_HPR165_38_pression_HP,
            "int_Lm_pompe_principale_HPR165_38_stand_by": self.int_Lm_pompe_principale_HPR165_38_stand_by,
            "int_Lm_groupe_secours_pompe_45_sens_rotation": self.int_Lm_groupe_secours_pompe_45_sens_rotation,
            "int_Lm_groupe_secours_pompe_45_calage": self.int_Lm_groupe_secours_pompe_45_calage,
            "int_Lm_groupe_secours_pompe_45_serrage": self.int_Lm_groupe_secours_pompe_45_serrage,
            "int_Lm_groupe_secours_pompe_45_verif_plein_huile": self.int_Lm_groupe_secours_pompe_45_verif_plein_huile,
            "int_Lm_groupe_secours_pompe_45_marche_arret_moteur": self.int_Lm_groupe_secours_pompe_45_marche_arret_moteur,
            "int_Lm_groupe_secours_pompe_45_pression_HP": self.int_Lm_groupe_secours_pompe_45_pression_HP,
            "int_Lm_groupe_secours_pompe_45_stand_by": self.int_Lm_groupe_secours_pompe_45_stand_by,
            "int_Lm_groupe_secours_pompe_45_courant_demarrage": self.int_Lm_groupe_secours_pompe_45_courant_demarrage,
            "int_Lm_groupe_secours_pompe_45_courant_service": self.int_Lm_groupe_secours_pompe_45_courant_service,
            "int_Lm_reglage_limiteur_pression_REP10": self.int_Lm_reglage_limiteur_pression_REP10,
            "int_Lm_reglage_pressostat_retour": self.int_Lm_reglage_pressostat_retour,
            "int_Lm_reglage_reducteur_pression_REP13": self.int_Lm_reglage_reducteur_pression_REP13,
            "int_Lm_reglage_reducteur_pression_grue_REP16": self.int_Lm_reglage_reducteur_pression_grue_REP16,
            "int_Lm_fonctionnement_sys_refrigeration_embrayage": self.int_Lm_fonctionnement_sys_refrigeration_embrayage,
            "int_TPH125_0_traction_premiere_couche_statique": self.int_TPH125_0_traction_premiere_couche_statique,
            "int_TPH125_0_traction_premiere_couche_dynamique": self.int_TPH125_0_traction_premiere_couche_dynamique,
            "int_TPH125_0_pression": self.int_TPH125_0_pression,
            "int_TPH125_0_vitesse_rotation_PV": self.int_TPH125_0_vitesse_rotation_PV,
            "int_TPH125_0_vitesse_rotation_GV": self.int_TPH125_0_vitesse_rotation_GV,
            "int_TPH125_0_debit": self.int_TPH125_0_debit,
            "int_TPH125_0_essai_file_vire": self.int_TPH125_0_essai_file_vire,
            "int_TPH125_0_essai_freinage": self.int_TPH125_0_essai_freinage,
            "int_TPH125_0_selection_PV_GV": self.int_TPH125_0_selection_PV_GV,
            "int_TPH50_0_traction_premiere_couche_statique": self.int_TPH50_0_traction_premiere_couche_statique,
            "int_TPH50_0_traction_premiere_couche_dynamique": self.int_TPH50_0_traction_premiere_couche_dynamique,
            "int_TPH50_0_pression": self.int_TPH50_0_pression,
            "int_TPH50_0_vitesse_rotation_PV": self.int_TPH50_0_vitesse_rotation_PV,
            "int_TPH50_0_vitesse_rotation_GV": self.int_TPH50_0_vitesse_rotation_GV,
            "int_TPH50_0_debit": self.int_TPH50_0_debit,
            "int_TPH50_0_essai_file_vire": self.int_TPH50_0_essai_file_vire,
            "int_TPH50_0_essai_freinage": self.int_TPH50_0_essai_freinage,
            "int_TPH50_0_selection_PV_GV": self.int_TPH50_0_selection_PV_GV,
            "int_AAG_schema_synoptique": self.int_AAG_schema_synoptique,
            "int_AAG_schema_electrique": self.int_AAG_schema_electrique,
            "int_AAG_schema_bornier": self.int_AAG_schema_bornier,
            "int_AAG_schema_cablage": self.int_AAG_schema_cablage,
            "int_AAG_releves_rincages_circuits": self.int_AAG_releves_rincages_circuits,
            "int_AAG_as_niveau_bas_NB1": self.int_AAG_as_niveau_bas_NB1,
            "int_AAG_as_controle_ARU": self.int_AAG_as_controle_ARU,
            "int_AAG_as_alarme_hydraulique_voyant_defaut": self.int_AAG_as_alarme_hydraulique_voyant_defaut,
            "int_AAG_verif_zero_mecanique_safran": self.int_AAG_verif_zero_mecanique_safran,
            "int_AAG_verif_zero_mecanique_recepteur": self.int_AAG_verif_zero_mecanique_recepteur,
            "int_AAG_verif_positionnement_transmetteur_BOPP": self.int_AAG_verif_positionnement_transmetteur_BOPP,
            "int_AAG_controle_puissance": self.int_AAG_controle_puissance,
            "int_AAG_controle_frequence": self.int_AAG_controle_frequence,
            "int_AAG_controle_commande": self.int_AAG_controle_commande,
            "int_AAG_controle_presence_24VDC": self.int_AAG_controle_presence_24VDC,
            "int_AAG_as_defauts_puissance": self.int_AAG_as_defauts_puissance,
            "int_AAG_as_defauts_moteur": self.int_AAG_as_defauts_moteur,
            "int_AAG_as_defauts_commande": self.int_AAG_as_defauts_commande,
            "int_AAG_as_niveau_bas": self.int_AAG_as_niveau_bas,
            "int_AAG_as_test_lampes": self.int_AAG_as_test_lampes,
            "int_AAG_as_controle_ARU2": self.int_AAG_as_controle_ARU2,
            "int_AAG_signalisation_defauts": self.int_AAG_signalisation_defauts,
            "int_AAG_APG_pompe_double_sens_rotation": self.int_AAG_APG_pompe_double_sens_rotation,
            "int_AAG_APG_pompe_double_marche_arret_moteur": self.int_AAG_APG_pompe_double_marche_arret_moteur,
            "int_AAG_APG_pompe_double_courant_demarrage": self.int_AAG_APG_pompe_double_courant_demarrage,
            "int_AAG_APG_pompe_double_courant_service": self.int_AAG_APG_pompe_double_courant_service,
            "int_AAG_RTRIB_reglage_limiteur_pression_centrale": self.int_AAG_RTRIB_reglage_limiteur_pression_centrale,
            "int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne": self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne,
            "int_AAG_RTRIB_controle_vitesses_recepteur_moteur": self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur,
            "int_AAG_RTRIB_controle_vitesses_recepteur_pompe": self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe,
            "int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax": self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax,
            "int_AAG_RTRIB_controle_fin_course_electrique_arret_electros": self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros,
            "int_AAG_RTRIB_controle_fin_course_electrique_PX1": self.int_AAG_RTRIB_controle_fin_course_electrique_PX1,
            "int_AAG_RTRIB_controle_fin_course_electrique_PX2": self.int_AAG_RTRIB_controle_fin_course_electrique_PX2,
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle": self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle,
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre": self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre,
            "int_AAG_RBAB_reglage_limiteur_pression_centrale": self.int_AAG_RBAB_reglage_limiteur_pression_centrale,
            "int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne": self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne,
            "int_AAG_RBAB_controle_vitesses_recepteur_moteur": self.int_AAG_RBAB_controle_vitesses_recepteur_moteur,
            "int_AAG_RBAB_controle_vitesses_recepteur_pompe": self.int_AAG_RBAB_controle_vitesses_recepteur_pompe,
            "int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax": self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax,
            "int_AAG_RBAB_controle_fin_course_electrique_arret_electros": self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros,
            "int_AAG_RBAB_controle_fin_course_electrique_PX1": self.int_AAG_RBAB_controle_fin_course_electrique_PX1,
            "int_AAG_RBAB_controle_fin_course_electrique_PX2": self.int_AAG_RBAB_controle_fin_course_electrique_PX2,
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle": self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle,
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre": self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre,
            "int_Cb_5T_traction_statique": self.int_Cb_5T_traction_statique,
            "int_Cb_5T_traction_dynamique": self.int_Cb_5T_traction_dynamique,
            "int_Cb_5T_pression": self.int_Cb_5T_pression,
            "int_Cb_5T_vitesse_rotation": self.int_Cb_5T_vitesse_rotation,
            "int_Cb_5T_debit": self.int_Cb_5T_debit,
            "int_Cb_5T_essai_file_vire": self.int_Cb_5T_essai_file_vire,
            "int_Cb_5T_freinage": self.int_Cb_5T_freinage,
            "int_Cb_3T_traction_statique": self.int_Cb_3T_traction_statique,
            "int_Cb_3T_traction_dynamique": self.int_Cb_3T_traction_dynamique,
            "int_Cb_3T_pression": self.int_Cb_3T_pression,
            "int_Cb_3T_vitesse_rotation": self.int_Cb_3T_vitesse_rotation,
            "int_Cb_3T_debit": self.int_Cb_3T_debit,
            "int_Cb_3T_essai_file_vire": self.int_Cb_3T_essai_file_vire,
            "int_Cb_3T_freinage": self.int_Cb_3T_freinage,

            "int_pieces_changees": self.int_pieces_changees,
            "int_pieces_cassees": self.int_pieces_cassees,
            "int_temps_passe": self.int_temps_passe,
            "int_temps_mort": self.int_temps_mort,
            "int_commentaires": self.int_commentaires

        }

        filename = f"./data/data{datetime.date.today()}_{self.case_number}.json"

        with open(filename, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

        # print(f"\nFormulaire sauvegardé dans le fichier {filename} avec les données suivantes :")
        # print(json.dumps(self.data, indent=4))


    def update(self, path):
        """
        Récupère les valeurs d'un fichier json pour les associer à l'affaire en cours
        Args:
          path: chemin du fichier json

        Returns:
            None
        """
        with open(path, 'r') as file:
            donnees = json.load(file)

        self.data = {
            "case_number": donnees["case_number"],
            "client_name": donnees["client_name"],
            "boat_name": donnees["boat_name"],
            "nb_field": donnees["nb_field"],
            "site_name": donnees["site_name"],
            "armement": donnees["armement"],
            # "visa": donnees["visa"],
            "intervention_type": donnees["intervention_type"],
            "BOPP_name": donnees["BOPP_name"],
            "BOPP_date": donnees["BOPP_date"],
            "BOPP_visa": donnees["BOPP_visa"],
            "chantier_name": donnees["chantier_name"],
            "chantier_date": donnees["chantier_date"],
            "chantier_visa": donnees["chantier_visa"],
            "armement_name": donnees["armement_name"],
            "armement_date": donnees["armement_date"],
            "armement_visa": donnees["armement_visa"],
            "Lm_schema_synoptique": donnees["Lm_schema_synoptique"],
            "Lm_schema_electrique": donnees["Lm_schema_electrique"],
            "Lm_schema_bornier": donnees["Lm_schema_bornier"],
            "Lm_schema_cablage": donnees["Lm_schema_cablage"],
            "Lm_releves_rincages_circuits": donnees["Lm_releves_rincages_circuits"],
            "Lm_as_niveau_bas_NB1": donnees["Lm_as_niveau_bas_NB1"],
            "Lm_as_temperature_haute_TH1": donnees["Lm_as_temperature_haute_TH1"],
            "Lm_as_controle_ARU": donnees["Lm_as_controle_ARU"],
            "Lm_as_alarme_hydraulique_voyant_defaut": donnees["Lm_as_alarme_hydraulique_voyant_defaut"],
            "Lm_pompe_principale_45_100_verif_plein_huile": donnees["Lm_pompe_principale_45_100_verif_plein_huile"],
            "Lm_pompe_principale_45_100_sens_rotation": donnees["Lm_pompe_principale_45_100_sens_rotation"],
            "Lm_pompe_principale_45_100_embrayage_pompe": donnees["Lm_pompe_principale_45_100_embrayage_pompe"],
            "Lm_pompe_principale_45_100_pression_HP": donnees["Lm_pompe_principale_45_100_pression_HP"],
            "Lm_pompe_principale_45_100_stand_by": donnees["Lm_pompe_principale_45_100_stand_by"],
            "Lm_pompe_principale_HPR165_38_verif_plein_huile": donnees["Lm_pompe_principale_HPR165_38_verif_plein_huile"],
            "Lm_pompe_principale_HPR165_38_sens_rotation": donnees["Lm_pompe_principale_HPR165_38_sens_rotation"],
            "Lm_pompe_principale_HPR165_38_embrayage_pompe": donnees["Lm_pompe_principale_HPR165_38_embrayage_pompe"],
            "Lm_pompe_principale_HPR165_38_pression_HP": donnees["Lm_pompe_principale_HPR165_38_pression_HP"],
            "Lm_pompe_principale_HPR165_38_stand_by": donnees["Lm_pompe_principale_HPR165_38_stand_by"],
            "Lm_groupe_secours_pompe_45_sens_rotation": donnees["Lm_groupe_secours_pompe_45_sens_rotation"],
            "Lm_groupe_secours_pompe_45_calage": donnees["Lm_groupe_secours_pompe_45_calage"],
            "Lm_groupe_secours_pompe_45_serrage": donnees["Lm_groupe_secours_pompe_45_serrage"],
            "Lm_groupe_secours_pompe_45_verif_plein_huile": donnees["Lm_groupe_secours_pompe_45_verif_plein_huile"],
            "Lm_groupe_secours_pompe_45_marche_arret_moteur": donnees["Lm_groupe_secours_pompe_45_marche_arret_moteur"],
            "Lm_groupe_secours_pompe_45_pression_HP": donnees["Lm_groupe_secours_pompe_45_pression_HP"],
            "Lm_groupe_secours_pompe_45_stand_by": donnees["Lm_groupe_secours_pompe_45_stand_by"],
            "Lm_groupe_secours_pompe_45_courant_demarrage": donnees["Lm_groupe_secours_pompe_45_courant_demarrage"],
            "Lm_groupe_secours_pompe_45_courant_service": donnees["Lm_groupe_secours_pompe_45_courant_service"],
            "Lm_reglage_limiteur_pression_REP10": donnees["Lm_reglage_limiteur_pression_REP10"],
            "Lm_reglage_pressostat_retour": donnees["Lm_reglage_pressostat_retour"],
            "Lm_reglage_reducteur_pression_REP13": donnees["Lm_reglage_reducteur_pression_REP13"],
            "Lm_reglage_reducteur_pression_grue_REP16": donnees["Lm_reglage_reducteur_pression_grue_REP16"],
            "Lm_fonctionnement_sys_refrigeration_embrayage": donnees["Lm_fonctionnement_sys_refrigeration_embrayage"],
            "TPH125_0_traction_premiere_couche_statique": donnees["TPH125_0_traction_premiere_couche_statique"],
            "TPH125_0_traction_premiere_couche_dynamique": donnees["TPH125_0_traction_premiere_couche_dynamique"],
            "TPH125_0_pression": donnees["TPH125_0_pression"],
            "TPH125_0_vitesse_rotation_PV": donnees["TPH125_0_vitesse_rotation_PV"],
            "TPH125_0_vitesse_rotation_GV": donnees["TPH125_0_vitesse_rotation_GV"],
            "TPH125_0_debit": donnees["TPH125_0_debit"],
            "TPH125_0_essai_file_vire": donnees["TPH125_0_essai_file_vire"],
            "TPH125_0_essai_freinage": donnees["TPH125_0_essai_freinage"],
            "TPH125_0_selection_PV_GV": donnees["TPH125_0_selection_PV_GV"],
            "TPH50_0_traction_premiere_couche_statique": donnees["TPH50_0_traction_premiere_couche_statique"],
            "TPH50_0_traction_premiere_couche_dynamique": donnees["TPH50_0_traction_premiere_couche_dynamique"],
            "TPH50_0_pression": donnees["TPH50_0_pression"],
            "TPH50_0_vitesse_rotation_PV": donnees["TPH50_0_vitesse_rotation_PV"],
            "TPH50_0_vitesse_rotation_GV": donnees["TPH50_0_vitesse_rotation_GV"],
            "TPH50_0_debit": donnees["TPH50_0_debit"],
            "TPH50_0_essai_file_vire": donnees["TPH50_0_essai_file_vire"],
            "TPH50_0_essai_freinage": donnees["TPH50_0_essai_freinage"],
            "TPH50_0_selection_PV_GV": donnees["TPH50_0_selection_PV_GV"],
            "AAG_schema_synoptique": donnees["AAG_schema_synoptique"],
            "AAG_schema_electrique": donnees["AAG_schema_electrique"],
            "AAG_schema_bornier": donnees["AAG_schema_bornier"],
            "AAG_schema_cablage": donnees["AAG_schema_cablage"],
            "AAG_releves_rincages_circuits": donnees["AAG_releves_rincages_circuits"],
            "AAG_as_niveau_bas_NB1": donnees["AAG_as_niveau_bas_NB1"],
            "AAG_as_controle_ARU": donnees["AAG_as_controle_ARU"],
            "AAG_as_alarme_hydraulique_voyant_defaut": donnees["AAG_as_alarme_hydraulique_voyant_defaut"],
            "AAG_verif_zero_mecanique_safran": donnees["AAG_verif_zero_mecanique_safran"],
            "AAG_verif_zero_mecanique_recepteur": donnees["AAG_verif_zero_mecanique_recepteur"],
            "AAG_verif_positionnement_transmetteur_BOPP": donnees["AAG_verif_positionnement_transmetteur_BOPP"],
            "AAG_controle_puissance": donnees["AAG_controle_puissance"],
            "AAG_controle_frequence": donnees["AAG_controle_frequence"],
            "AAG_controle_commande": donnees["AAG_controle_commande"],
            "AAG_controle_presence_24VDC": donnees["AAG_controle_presence_24VDC"],
            "AAG_as_defauts_puissance": donnees["AAG_as_defauts_puissance"],
            "AAG_as_defauts_moteur": donnees["AAG_as_defauts_moteur"],
            "AAG_as_defauts_commande": donnees["AAG_as_defauts_commande"],
            "AAG_as_niveau_bas": donnees["AAG_as_niveau_bas"],
            "AAG_as_test_lampes": donnees["AAG_as_test_lampes"],
            "AAG_as_controle_ARU2": donnees["AAG_as_controle_ARU2"],
            "AAG_signalisation_defauts": donnees["AAG_signalisation_defauts"],
            "AAG_APG_pompe_double_sens_rotation": donnees["AAG_APG_pompe_double_sens_rotation"],
            "AAG_APG_pompe_double_marche_arret_moteur": donnees["AAG_APG_pompe_double_marche_arret_moteur"],
            "AAG_APG_pompe_double_courant_demarrage": donnees["AAG_APG_pompe_double_courant_demarrage"],
            "AAG_APG_pompe_double_courant_service": donnees["AAG_APG_pompe_double_courant_service"],
            "AAG_RTRIB_reglage_limiteur_pression_centrale": donnees["AAG_RTRIB_reglage_limiteur_pression_centrale"],
            "AAG_RTRIB_reglage_limiteur_pression_double_en_ligne": donnees["AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"],
            "AAG_RTRIB_controle_vitesses_recepteur_moteur": donnees["AAG_RTRIB_controle_vitesses_recepteur_moteur"],
            "AAG_RTRIB_controle_vitesses_recepteur_pompe": donnees["AAG_RTRIB_controle_vitesses_recepteur_pompe"],
            "AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax": donnees["AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"],
            "AAG_RTRIB_controle_fin_course_electrique_arret_electros": donnees["AAG_RTRIB_controle_fin_course_electrique_arret_electros"],
            "AAG_RTRIB_controle_fin_course_electrique_PX1": donnees["AAG_RTRIB_controle_fin_course_electrique_PX1"],
            "AAG_RTRIB_controle_fin_course_electrique_PX2": donnees["AAG_RTRIB_controle_fin_course_electrique_PX2"],
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle": donnees["AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"],
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre": donnees["AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"],
            "AAG_RBAB_reglage_limiteur_pression_centrale": donnees["AAG_RBAB_reglage_limiteur_pression_centrale"],
            "AAG_RBAB_reglage_limiteur_pression_double_en_ligne": donnees["AAG_RBAB_reglage_limiteur_pression_double_en_ligne"],
            "AAG_RBAB_controle_vitesses_recepteur_moteur": donnees["AAG_RBAB_controle_vitesses_recepteur_moteur"],
            "AAG_RBAB_controle_vitesses_recepteur_pompe": donnees["AAG_RBAB_controle_vitesses_recepteur_pompe"],
            "AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax": donnees["AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"],
            "AAG_RBAB_controle_fin_course_electrique_arret_electros": donnees["AAG_RBAB_controle_fin_course_electrique_arret_electros"],
            "AAG_RBAB_controle_fin_course_electrique_PX1": donnees["AAG_RBAB_controle_fin_course_electrique_PX1"],
            "AAG_RBAB_controle_fin_course_electrique_PX2": donnees["AAG_RBAB_controle_fin_course_electrique_PX2"],
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle": donnees["AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"],
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre": donnees["AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"],
            "Cb_5T_traction_statique": donnees["Cb_5T_traction_statique"],
            "Cb_5T_traction_dynamique": donnees["Cb_5T_traction_dynamique"],
            "Cb_5T_pression": donnees["Cb_5T_pression"],
            "Cb_5T_vitesse_rotation": donnees["Cb_5T_vitesse_rotation"],
            "Cb_5T_debit": donnees["Cb_5T_debit"],
            "Cb_5T_essai_file_vire": donnees["Cb_5T_essai_file_vire"],
            "Cb_5T_freinage": donnees["Cb_5T_freinage"],
            "Cb_3T_traction_statique": donnees["Cb_3T_traction_statique"],
            "Cb_3T_traction_dynamique": donnees["Cb_3T_traction_dynamique"],
            "Cb_3T_pression": donnees["Cb_3T_pression"],
            "Cb_3T_vitesse_rotation": donnees["Cb_3T_vitesse_rotation"],
            "Cb_3T_debit": donnees["Cb_3T_debit"],
            "Cb_3T_essai_file_vire": donnees["Cb_3T_essai_file_vire"],
            "Cb_3T_freinage": donnees["Cb_3T_freinage"],

            "int_Lm_schema_synoptique": donnees["int_Lm_schema_synoptique"],
            "int_Lm_schema_electrique": donnees["int_Lm_schema_electrique"],
            "int_Lm_schema_bornier": donnees["int_Lm_schema_bornier"],
            "int_Lm_schema_cablage": donnees["int_Lm_schema_cablage"],
            "int_Lm_releves_rincages_circuits": donnees["int_Lm_releves_rincages_circuits"],
            "int_Lm_as_niveau_bas_NB1": donnees["int_Lm_as_niveau_bas_NB1"],
            "int_Lm_as_temperature_haute_TH1": donnees["int_Lm_as_temperature_haute_TH1"],
            "int_Lm_as_controle_ARU": donnees["int_Lm_as_controle_ARU"],
            "int_Lm_as_alarme_hydraulique_voyant_defaut": donnees["int_Lm_as_alarme_hydraulique_voyant_defaut"],
            "int_Lm_pompe_principale_45_100_verif_plein_huile": donnees["int_Lm_pompe_principale_45_100_verif_plein_huile"],
            "int_Lm_pompe_principale_45_100_sens_rotation": donnees["int_Lm_pompe_principale_45_100_sens_rotation"],
            "int_Lm_pompe_principale_45_100_embrayage_pompe": donnees["int_Lm_pompe_principale_45_100_embrayage_pompe"],
            "int_Lm_pompe_principale_45_100_pression_HP": donnees["int_Lm_pompe_principale_45_100_pression_HP"],
            "int_Lm_pompe_principale_45_100_stand_by": donnees["int_Lm_pompe_principale_45_100_stand_by"],
            "int_Lm_pompe_principale_HPR165_38_verif_plein_huile": donnees["int_Lm_pompe_principale_HPR165_38_verif_plein_huile"],
            "int_Lm_pompe_principale_HPR165_38_sens_rotation": donnees["int_Lm_pompe_principale_HPR165_38_sens_rotation"],
            "int_Lm_pompe_principale_HPR165_38_embrayage_pompe": donnees["int_Lm_pompe_principale_HPR165_38_embrayage_pompe"],
            "int_Lm_pompe_principale_HPR165_38_pression_HP": donnees["int_Lm_pompe_principale_HPR165_38_pression_HP"],
            "int_Lm_pompe_principale_HPR165_38_stand_by": donnees["int_Lm_pompe_principale_HPR165_38_stand_by"],
            "int_Lm_groupe_secours_pompe_45_sens_rotation": donnees["int_Lm_groupe_secours_pompe_45_sens_rotation"],
            "int_Lm_groupe_secours_pompe_45_calage": donnees["int_Lm_groupe_secours_pompe_45_calage"],
            "int_Lm_groupe_secours_pompe_45_serrage": donnees["int_Lm_groupe_secours_pompe_45_serrage"],
            "int_Lm_groupe_secours_pompe_45_verif_plein_huile": donnees["int_Lm_groupe_secours_pompe_45_verif_plein_huile"],
            "int_Lm_groupe_secours_pompe_45_marche_arret_moteur": donnees["int_Lm_groupe_secours_pompe_45_marche_arret_moteur"],
            "int_Lm_groupe_secours_pompe_45_pression_HP": donnees["int_Lm_groupe_secours_pompe_45_pression_HP"],
            "int_Lm_groupe_secours_pompe_45_stand_by": donnees["int_Lm_groupe_secours_pompe_45_stand_by"],
            "int_Lm_groupe_secours_pompe_45_courant_demarrage": donnees["int_Lm_groupe_secours_pompe_45_courant_demarrage"],
            "int_Lm_groupe_secours_pompe_45_courant_service": donnees["int_Lm_groupe_secours_pompe_45_courant_service"],
            "int_Lm_reglage_limiteur_pression_REP10": donnees["int_Lm_reglage_limiteur_pression_REP10"],
            "int_Lm_reglage_pressostat_retour": donnees["int_Lm_reglage_pressostat_retour"],
            "int_Lm_reglage_reducteur_pression_REP13": donnees["int_Lm_reglage_reducteur_pression_REP13"],
            "int_Lm_reglage_reducteur_pression_grue_REP16": donnees["int_Lm_reglage_reducteur_pression_grue_REP16"],
            "int_Lm_fonctionnement_sys_refrigeration_embrayage": donnees["int_Lm_fonctionnement_sys_refrigeration_embrayage"],
            "int_TPH125_0_traction_premiere_couche_statique": donnees["int_TPH125_0_traction_premiere_couche_statique"],
            "int_TPH125_0_traction_premiere_couche_dynamique": donnees["int_TPH125_0_traction_premiere_couche_dynamique"],
            "int_TPH125_0_pression": donnees["int_TPH125_0_pression"],
            "int_TPH125_0_vitesse_rotation_PV": donnees["int_TPH125_0_vitesse_rotation_PV"],
            "int_TPH125_0_vitesse_rotation_GV": donnees["int_TPH125_0_vitesse_rotation_GV"],
            "int_TPH125_0_debit": donnees["int_TPH125_0_debit"],
            "int_TPH125_0_essai_file_vire": donnees["int_TPH125_0_essai_file_vire"],
            "int_TPH125_0_essai_freinage": donnees["int_TPH125_0_essai_freinage"],
            "int_TPH125_0_selection_PV_GV": donnees["int_TPH125_0_selection_PV_GV"],
            "int_TPH50_0_traction_premiere_couche_statique": donnees["int_TPH50_0_traction_premiere_couche_statique"],
            "int_TPH50_0_traction_premiere_couche_dynamique": donnees["int_TPH50_0_traction_premiere_couche_dynamique"],
            "int_TPH50_0_pression": donnees["int_TPH50_0_pression"],
            "int_TPH50_0_vitesse_rotation_PV": donnees["int_TPH50_0_vitesse_rotation_PV"],
            "int_TPH50_0_vitesse_rotation_GV": donnees["int_TPH50_0_vitesse_rotation_GV"],
            "int_TPH50_0_debit": donnees["int_TPH50_0_debit"],
            "int_TPH50_0_essai_file_vire": donnees["int_TPH50_0_essai_file_vire"],
            "int_TPH50_0_essai_freinage": donnees["int_TPH50_0_essai_freinage"],
            "int_TPH50_0_selection_PV_GV": donnees["int_TPH50_0_selection_PV_GV"],
            "int_AAG_schema_synoptique": donnees["int_AAG_schema_synoptique"],
            "int_AAG_schema_electrique": donnees["int_AAG_schema_electrique"],
            "int_AAG_schema_bornier": donnees["int_AAG_schema_bornier"],
            "int_AAG_schema_cablage": donnees["int_AAG_schema_cablage"],
            "int_AAG_releves_rincages_circuits": donnees["int_AAG_releves_rincages_circuits"],
            "int_AAG_as_niveau_bas_NB1": donnees["int_AAG_as_niveau_bas_NB1"],
            "int_AAG_as_controle_ARU": donnees["int_AAG_as_controle_ARU"],
            "int_AAG_as_alarme_hydraulique_voyant_defaut": donnees["int_AAG_as_alarme_hydraulique_voyant_defaut"],
            "int_AAG_verif_zero_mecanique_safran": donnees["int_AAG_verif_zero_mecanique_safran"],
            "int_AAG_verif_zero_mecanique_recepteur": donnees["int_AAG_verif_zero_mecanique_recepteur"],
            "int_AAG_verif_positionnement_transmetteur_BOPP": donnees["int_AAG_verif_positionnement_transmetteur_BOPP"],
            "int_AAG_controle_puissance": donnees["int_AAG_controle_puissance"],
            "int_AAG_controle_frequence": donnees["int_AAG_controle_frequence"],
            "int_AAG_controle_commande": donnees["int_AAG_controle_commande"],
            "int_AAG_controle_presence_24VDC": donnees["int_AAG_controle_presence_24VDC"],
            "int_AAG_as_defauts_puissance": donnees["int_AAG_as_defauts_puissance"],
            "int_AAG_as_defauts_moteur": donnees["int_AAG_as_defauts_moteur"],
            "int_AAG_as_defauts_commande": donnees["int_AAG_as_defauts_commande"],
            "int_AAG_as_niveau_bas": donnees["int_AAG_as_niveau_bas"],
            "int_AAG_as_test_lampes": donnees["int_AAG_as_test_lampes"],
            "int_AAG_as_controle_ARU2": donnees["int_AAG_as_controle_ARU2"],
            "int_AAG_signalisation_defauts": donnees["int_AAG_signalisation_defauts"],
            "int_AAG_APG_pompe_double_sens_rotation": donnees["int_AAG_APG_pompe_double_sens_rotation"],
            "int_AAG_APG_pompe_double_marche_arret_moteur": donnees["int_AAG_APG_pompe_double_marche_arret_moteur"],
            "int_AAG_APG_pompe_double_courant_demarrage": donnees["int_AAG_APG_pompe_double_courant_demarrage"],
            "int_AAG_APG_pompe_double_courant_service": donnees["int_AAG_APG_pompe_double_courant_service"],
            "int_AAG_RTRIB_reglage_limiteur_pression_centrale": donnees["int_AAG_RTRIB_reglage_limiteur_pression_centrale"],
            "int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne": donnees["int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"],
            "int_AAG_RTRIB_controle_vitesses_recepteur_moteur": donnees["int_AAG_RTRIB_controle_vitesses_recepteur_moteur"],
            "int_AAG_RTRIB_controle_vitesses_recepteur_pompe": donnees["int_AAG_RTRIB_controle_vitesses_recepteur_pompe"],
            "int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax": donnees["int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"],
            "int_AAG_RTRIB_controle_fin_course_electrique_arret_electros": donnees["int_AAG_RTRIB_controle_fin_course_electrique_arret_electros"],
            "int_AAG_RTRIB_controle_fin_course_electrique_PX1": donnees["int_AAG_RTRIB_controle_fin_course_electrique_PX1"],
            "int_AAG_RTRIB_controle_fin_course_electrique_PX2": donnees["int_AAG_RTRIB_controle_fin_course_electrique_PX2"],
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle": donnees["int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"],
            "int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre": donnees["int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"],
            "int_AAG_RBAB_reglage_limiteur_pression_centrale": donnees["int_AAG_RBAB_reglage_limiteur_pression_centrale"],
            "int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne": donnees["int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne"],
            "int_AAG_RBAB_controle_vitesses_recepteur_moteur": donnees["int_AAG_RBAB_controle_vitesses_recepteur_moteur"],
            "int_AAG_RBAB_controle_vitesses_recepteur_pompe": donnees["int_AAG_RBAB_controle_vitesses_recepteur_pompe"],
            "int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax": donnees["int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"],
            "int_AAG_RBAB_controle_fin_course_electrique_arret_electros": donnees["int_AAG_RBAB_controle_fin_course_electrique_arret_electros"],
            "int_AAG_RBAB_controle_fin_course_electrique_PX1": donnees["int_AAG_RBAB_controle_fin_course_electrique_PX1"],
            "int_AAG_RBAB_controle_fin_course_electrique_PX2": donnees["int_AAG_RBAB_controle_fin_course_electrique_PX2"],
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle": donnees["int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"],
            "int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre": donnees["int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"],
            "int_Cb_5T_traction_statique": donnees["int_Cb_5T_traction_statique"],
            "int_Cb_5T_traction_dynamique": donnees["int_Cb_5T_traction_dynamique"],
            "int_Cb_5T_pression": donnees["int_Cb_5T_pression"],
            "int_Cb_5T_vitesse_rotation": donnees["int_Cb_5T_vitesse_rotation"],
            "int_Cb_5T_debit": donnees["int_Cb_5T_debit"],
            "int_Cb_5T_essai_file_vire": donnees["int_Cb_5T_essai_file_vire"],
            "int_Cb_5T_freinage": donnees["int_Cb_5T_freinage"],
            "int_Cb_3T_traction_statique": donnees["int_Cb_3T_traction_statique"],
            "int_Cb_3T_traction_dynamique": donnees["int_Cb_3T_traction_dynamique"],
            "int_Cb_3T_pression": donnees["int_Cb_3T_pression"],
            "int_Cb_3T_vitesse_rotation": donnees["int_Cb_3T_vitesse_rotation"],
            "int_Cb_3T_debit": donnees["int_Cb_3T_debit"],
            "int_Cb_3T_essai_file_vire": donnees["int_Cb_3T_essai_file_vire"],
            "int_Cb_3T_freinage": donnees["int_Cb_3T_freinage"],
            "int_pieces_changees": donnees["int_pieces_changees"],
            "int_pieces_cassees": donnees["int_pieces_cassees"],
            "int_temps_passe": donnees["int_temps_passe"],
            "int_temps_mort": donnees["int_temps_mort"],
            "int_commentaires": donnees["int_commentaires"]
        }
        # print(json.dumps(self.data, indent=4))

    def save_data_modif_carac(self):
        """ 
        Sauvegarde les données de la caractérisation de l'affaire dans le dictionnaire data
        """
        self.data["case_number"] = self.case_number
        self.data["client_name"] = self.client_name
        self.data["boat_name"] = self.boat_name
        self.data["nb_field"] = self.nb_field
        self.data["site_name"] = self.site_name
        self.data["armement"] = self.armement
        # self.data["visa"] = self.visa
        self.data["intervention_type"] = self.intervention_type
        self.data["BOPP_name"] = self.BOPP_name
        self.data["BOPP_date"] = self.BOPP_date
        self.data["BOPP_visa"] = self.BOPP_visa
        self.data["chantier_name"] = self.chantier_name
        self.data["chantier_date"] = self.chantier_date
        self.data["chantier_visa"] = self.chantier_visa
        self.data["armement_name"] = self.armement_name
        self.data["armement_date"] = self.armement_date
        self.data["armement_visa"] = self.armement_visa

    def save_data_mofid_local_machine(self):
        """ 
        Sauvegarde les données du menu modif local machine dans le dictionnaire data
        """
        self.data["Lm_schema_synoptique"] = self.Lm_schema_synoptique
        self.data["Lm_schema_electrique"] = self.Lm_schema_electrique
        self.data["Lm_schema_bornier"] = self.Lm_schema_bornier
        self.data["Lm_schema_cablage"] = self.Lm_schema_cablage
        self.data["Lm_releves_rincages_circuits"] = self.Lm_releves_rincages_circuits
        self.data["Lm_as_niveau_bas_NB1"] = self.Lm_as_niveau_bas_NB1
        self.data["Lm_as_temperature_haute_TH1"] = self.Lm_as_temperature_haute_TH1
        self.data["Lm_as_controle_ARU"] = self.Lm_as_controle_ARU
        self.data["Lm_as_alarme_hydraulique_voyant_defaut"] = self.Lm_as_alarme_hydraulique_voyant_defaut
        self.data["Lm_pompe_principale_45_100_verif_plein_huile"] = self.Lm_pompe_principale_45_100_verif_plein_huile
        self.data["Lm_pompe_principale_45_100_sens_rotation"] = self.Lm_pompe_principale_45_100_sens_rotation
        self.data["Lm_pompe_principale_45_100_embrayage_pompe"] = self.Lm_pompe_principale_45_100_embrayage_pompe
        self.data["Lm_pompe_principale_45_100_pression_HP"] = self.Lm_pompe_principale_45_100_pression_HP
        self.data["Lm_pompe_principale_45_100_stand_by"] = self.Lm_pompe_principale_45_100_stand_by
        self.data["Lm_pompe_principale_HPR165_38_verif_plein_huile"] = self.Lm_pompe_principale_HPR165_38_verif_plein_huile
        self.data["Lm_pompe_principale_HPR165_38_sens_rotation"] = self.Lm_pompe_principale_HPR165_38_sens_rotation
        self.data["Lm_pompe_principale_HPR165_38_embrayage_pompe"] = self.Lm_pompe_principale_HPR165_38_embrayage_pompe
        self.data["Lm_pompe_principale_HPR165_38_pression_HP"] = self.Lm_pompe_principale_HPR165_38_pression_HP
        self.data["Lm_pompe_principale_HPR165_38_stand_by"] = self.Lm_pompe_principale_HPR165_38_stand_by
        self.data["Lm_groupe_secours_pompe_45_sens_rotation"] = self.Lm_groupe_secours_pompe_45_sens_rotation
        self.data["Lm_groupe_secours_pompe_45_calage"] = self.Lm_groupe_secours_pompe_45_calage
        self.data["Lm_groupe_secours_pompe_45_serrage"] = self.Lm_groupe_secours_pompe_45_serrage
        self.data["Lm_groupe_secours_pompe_45_verif_plein_huile"] = self.Lm_groupe_secours_pompe_45_verif_plein_huile
        self.data["Lm_groupe_secours_pompe_45_marche_arret_moteur"] = self.Lm_groupe_secours_pompe_45_marche_arret_moteur
        self.data["Lm_groupe_secours_pompe_45_pression_HP"] = self.Lm_groupe_secours_pompe_45_pression_HP
        self.data["Lm_groupe_secours_pompe_45_stand_by"] = self.Lm_groupe_secours_pompe_45_stand_by
        self.data["Lm_groupe_secours_pompe_45_courant_demarrage"] = self.Lm_groupe_secours_pompe_45_courant_demarrage
        self.data["Lm_groupe_secours_pompe_45_courant_service"] = self.Lm_groupe_secours_pompe_45_courant_service
        self.data["Lm_reglage_limiteur_pression_REP10"] = self.Lm_reglage_limiteur_pression_REP10
        self.data["Lm_reglage_pressostat_retour"] = self.Lm_reglage_pressostat_retour
        self.data["Lm_reglage_reducteur_pression_REP13"] = self.Lm_reglage_reducteur_pression_REP13
        self.data["Lm_reglage_reducteur_pression_grue_REP16"] = self.Lm_reglage_reducteur_pression_grue_REP16
        self.data["Lm_fonctionnement_sys_refrigeration_embrayage"] = self.Lm_fonctionnement_sys_refrigeration_embrayage

    def save_data_modif_treuil(self):
        """ 
        Sauvegarde les données du menu modif treuil dans le dictionnaire data
        """
        self.data["TPH125_0_traction_premiere_couche_statique"] = self.TPH125_0_traction_premiere_couche_statique
        self.data["TPH125_0_traction_premiere_couche_dynamique"] = self.TPH125_0_traction_premiere_couche_dynamique
        self.data["TPH125_0_pression"] = self.TPH125_0_pression
        self.data["TPH125_0_vitesse_rotation_PV"] = self.TPH125_0_vitesse_rotation_PV
        self.data["TPH125_0_vitesse_rotation_GV"] = self.TPH125_0_vitesse_rotation_GV
        self.data["TPH125_0_debit"] = self.TPH125_0_debit
        self.data["TPH125_0_essai_file_vire"] = self.TPH125_0_essai_file_vire
        self.data["TPH125_0_essai_freinage"] = self.TPH125_0_essai_freinage
        self.data["TPH125_0_selection_PV_GV"] = self.TPH125_0_selection_PV_GV
        self.data["TPH50_0_traction_premiere_couche_statique"] = self.TPH50_0_traction_premiere_couche_statique
        self.data["TPH50_0_traction_premiere_couche_dynamique"] = self.TPH50_0_traction_premiere_couche_dynamique
        self.data["TPH50_0_pression"] = self.TPH50_0_pression
        self.data["TPH50_0_vitesse_rotation_PV"] = self.TPH50_0_vitesse_rotation_PV
        self.data["TPH50_0_vitesse_rotation_GV"] = self.TPH50_0_vitesse_rotation_GV
        self.data["TPH50_0_debit"] = self.TPH50_0_debit
        self.data["TPH50_0_essai_file_vire"] = self.TPH50_0_essai_file_vire
        self.data["TPH50_0_essai_freinage"] = self.TPH50_0_essai_freinage
        self.data["TPH50_0_selection_PV_GV"] = self.TPH50_0_selection_PV_GV

    def save_data_modif_cabestan(self):
        """ 
        Sauvegarde les données du menu modif cabestan dans le dictionnaire data
        """
        self.data["Cb_5T_traction_statique"] = self.Cb_5T_traction_statique
        self.data["Cb_5T_traction_dynamique"] = self.Cb_5T_traction_dynamique
        self.data["Cb_5T_pression"] = self.Cb_5T_pression
        self.data["Cb_5T_vitesse_rotation"] = self.Cb_5T_vitesse_rotation
        self.data["Cb_5T_debit"] = self.Cb_5T_debit
        self.data["Cb_5T_essai_file_vire"] = self.Cb_5T_essai_file_vire
        self.data["Cb_5T_freinage"] = self.Cb_5T_freinage
        self.data["Cb_3T_traction_statique"] = self.Cb_3T_traction_statique
        self.data["Cb_3T_traction_dynamique"] = self.Cb_3T_traction_dynamique
        self.data["Cb_3T_pression"] = self.Cb_3T_pression
        self.data["Cb_3T_vitesse_rotation"] = self.Cb_3T_vitesse_rotation
        self.data["Cb_3T_debit"] = self.Cb_3T_debit
        self.data["Cb_3T_debit"] = self.Cb_3T_essai_file_vire
        self.data["Cb_3T_freinage"] = self.Cb_3T_freinage

    def save_data_modif_appareil_gouverne(self):
        """ 
        Sauvegarde les données du menu modif appareil gouverne dans le dictionnaire data
        """
        self.data["AAG_schema_synoptique"] = self.AAG_schema_synoptique
        self.data["AAG_schema_electrique"] = self.AAG_schema_electrique
        self.data["AAG_schema_bornier"] = self.AAG_schema_bornier
        self.data["AAG_schema_cablage"] = self.AAG_schema_cablage
        self.data["AAG_releves_rincages_circuits"] = self.AAG_releves_rincages_circuits
        self.data["AAG_as_niveau_bas_NB1"] = self.AAG_as_niveau_bas_NB1
        self.data["AAG_as_controle_ARU"] = self.AAG_as_controle_ARU
        self.data["AAG_as_alarme_hydraulique_voyant_defaut"] = self.AAG_as_alarme_hydraulique_voyant_defaut
        self.data["AAG_verif_zero_mecanique_safran"] = self.AAG_verif_zero_mecanique_safran
        self.data["AAG_verif_zero_mecanique_recepteur"] = self.AAG_verif_zero_mecanique_recepteur
        self.data["AAG_verif_positionnement_transmetteur_BOPP"] = self.AAG_verif_positionnement_transmetteur_BOPP
        self.data["AAG_controle_puissance"] = self.AAG_controle_puissance
        self.data["AAG_controle_frequence"] = self.AAG_controle_frequence
        self.data["AAG_controle_commande"] = self.AAG_controle_commande
        self.data["AAG_controle_presence_24VDC"] = self.AAG_controle_presence_24VDC
        self.data["AAG_as_defauts_puissance"] = self.AAG_as_defauts_puissance
        self.data["AAG_as_defauts_moteur"] = self.AAG_as_defauts_moteur
        self.data["AAG_as_defauts_commande"] = self.AAG_as_defauts_commande
        self.data["AAG_as_niveau_bas"] = self.AAG_as_niveau_bas
        self.data["AAG_as_test_lampes"] = self.AAG_as_test_lampes
        self.data["AAG_as_controle_ARU2"] = self.AAG_as_controle_ARU2
        self.data["AAG_signalisation_defauts"] = self.AAG_signalisation_defauts
        self.data["AAG_APG_pompe_double_sens_rotation"] = self.AAG_APG_pompe_double_sens_rotation
        self.data["AAG_APG_pompe_double_marche_arret_moteur"] = self.AAG_APG_pompe_double_marche_arret_moteur
        self.data["AAG_APG_pompe_double_courant_demarrage"] = self.AAG_APG_pompe_double_courant_demarrage
        self.data["AAG_APG_pompe_double_courant_service"] = self.AAG_APG_pompe_double_courant_service
        self.data["AAG_RTRIB_reglage_limiteur_pression_centrale"] = self.AAG_RTRIB_reglage_limiteur_pression_centrale
        self.data["AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"] = self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne
        self.data["AAG_RTRIB_controle_vitesses_recepteur_moteur"] = self.AAG_RTRIB_controle_vitesses_recepteur_moteur
        self.data["AAG_RTRIB_controle_vitesses_recepteur_pompe"] = self.AAG_RTRIB_controle_vitesses_recepteur_pompe
        self.data["AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"] = self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax
        self.data["AAG_RTRIB_controle_fin_course_electrique_arret_electros"] = self.AAG_RTRIB_controle_fin_course_electrique_arret_electros
        self.data["AAG_RTRIB_controle_fin_course_electrique_PX1"] = self.AAG_RTRIB_controle_fin_course_electrique_PX1
        self.data["AAG_RTRIB_controle_fin_course_electrique_PX2"] = self.AAG_RTRIB_controle_fin_course_electrique_PX2
        self.data["AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"] = self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle
        self.data["AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"] = self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre
        self.data["AAG_RBAB_reglage_limiteur_pression_centrale"] = self.AAG_RBAB_reglage_limiteur_pression_centrale
        self.data["AAG_RBAB_reglage_limiteur_pression_double_en_ligne"] = self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne
        self.data["AAG_RBAB_controle_vitesses_recepteur_moteur"] = self.AAG_RBAB_controle_vitesses_recepteur_moteur
        self.data["AAG_RBAB_controle_vitesses_recepteur_pompe"] = self.AAG_RBAB_controle_vitesses_recepteur_pompe
        self.data["AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"] = self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax
        self.data["AAG_RBAB_controle_fin_course_electrique_arret_electros"] = self.AAG_RBAB_controle_fin_course_electrique_arret_electros
        self.data["AAG_RBAB_controle_fin_course_electrique_PX1"] = self.AAG_RBAB_controle_fin_course_electrique_PX1
        self.data["AAG_RBAB_controle_fin_course_electrique_PX2"] = self.AAG_RBAB_controle_fin_course_electrique_PX2
        self.data["AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"] = self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle
        self.data["AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"] = self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre

    def modif_finale(self, direc):
        """
        Sauvegarde les données du formulaire dans un fichier json
        Args:
          direc: chemin du fichier json

        Returns:
            None
        """
        # print(f"Le dossier est : {direc}")

        with open(direc, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

        # print(f"\nFormulaire sauvegardé dans le fichier {direc} avec les données suivantes :")
        # print("FDP ------------------")
        # print(json.dumps(self.data, indent=4))

    # MISE A JOUR BDD INTERVENANT

    def save_data_int_local_machine(self):
        """ 
        Sauvegarde les données du menu intervenant local machine dans le dictionnaire data
        """
        self.data["Lm_schema_synoptique"] = self.Lm_schema_synoptique
        self.data["Lm_schema_electrique"] = self.Lm_schema_electrique
        self.data["Lm_schema_bornier"] = self.Lm_schema_bornier
        self.data["Lm_schema_cablage"] = self.Lm_schema_cablage
        self.data["Lm_releves_rincages_circuits"] = self.Lm_releves_rincages_circuits
        self.data["Lm_as_niveau_bas_NB1"] = self.Lm_as_niveau_bas_NB1
        self.data["Lm_as_temperature_haute_TH1"] = self.Lm_as_temperature_haute_TH1
        self.data["Lm_as_controle_ARU"] = self.Lm_as_controle_ARU
        self.data["Lm_as_alarme_hydraulique_voyant_defaut"] = self.Lm_as_alarme_hydraulique_voyant_defaut
        self.data["Lm_pompe_principale_45_100_verif_plein_huile"] = self.Lm_pompe_principale_45_100_verif_plein_huile
        self.data["Lm_pompe_principale_45_100_sens_rotation"] = self.Lm_pompe_principale_45_100_sens_rotation
        self.data["Lm_pompe_principale_45_100_embrayage_pompe"] = self.Lm_pompe_principale_45_100_embrayage_pompe
        self.data["Lm_pompe_principale_45_100_pression_HP"] = self.Lm_pompe_principale_45_100_pression_HP
        self.data["Lm_pompe_principale_45_100_stand_by"] = self.Lm_pompe_principale_45_100_stand_by
        self.data["Lm_pompe_principale_HPR165_38_verif_plein_huile"] = self.Lm_pompe_principale_HPR165_38_verif_plein_huile
        self.data["Lm_pompe_principale_HPR165_38_sens_rotation"] = self.Lm_pompe_principale_HPR165_38_sens_rotation
        self.data["Lm_pompe_principale_HPR165_38_embrayage_pompe"] = self.Lm_pompe_principale_HPR165_38_embrayage_pompe
        self.data["Lm_pompe_principale_HPR165_38_pression_HP"] = self.Lm_pompe_principale_HPR165_38_pression_HP
        self.data["Lm_pompe_principale_HPR165_38_stand_by"] = self.Lm_pompe_principale_HPR165_38_stand_by
        self.data["Lm_groupe_secours_pompe_45_sens_rotation"] = self.Lm_groupe_secours_pompe_45_sens_rotation
        self.data["Lm_groupe_secours_pompe_45_calage"] = self.Lm_groupe_secours_pompe_45_calage
        self.data["Lm_groupe_secours_pompe_45_serrage"] = self.Lm_groupe_secours_pompe_45_serrage
        self.data["Lm_groupe_secours_pompe_45_verif_plein_huile"] = self.Lm_groupe_secours_pompe_45_verif_plein_huile
        self.data["Lm_groupe_secours_pompe_45_marche_arret_moteur"] = self.Lm_groupe_secours_pompe_45_marche_arret_moteur
        self.data["Lm_groupe_secours_pompe_45_pression_HP"] = self.Lm_groupe_secours_pompe_45_pression_HP
        self.data["Lm_groupe_secours_pompe_45_stand_by"] = self.Lm_groupe_secours_pompe_45_stand_by
        self.data["Lm_groupe_secours_pompe_45_courant_demarrage"] = self.Lm_groupe_secours_pompe_45_courant_demarrage
        self.data["Lm_groupe_secours_pompe_45_courant_service"] = self.Lm_groupe_secours_pompe_45_courant_service
        self.data["Lm_reglage_limiteur_pression_REP10"] = self.Lm_reglage_limiteur_pression_REP10
        self.data["Lm_reglage_pressostat_retour"] = self.Lm_reglage_pressostat_retour
        self.data["Lm_reglage_reducteur_pression_REP13"] = self.Lm_reglage_reducteur_pression_REP13
        self.data["Lm_reglage_reducteur_pression_grue_REP16"] = self.Lm_reglage_reducteur_pression_grue_REP16
        self.data["Lm_fonctionnement_sys_refrigeration_embrayage"] = self.Lm_fonctionnement_sys_refrigeration_embrayage

        self.data["int_Lm_schema_synoptique"] = self.int_Lm_schema_synoptique
        self.data["int_Lm_schema_electrique"] = self.int_Lm_schema_electrique
        self.data["int_Lm_schema_bornier"] = self.int_Lm_schema_bornier
        self.data["int_Lm_schema_cablage"] = self.int_Lm_schema_cablage
        self.data["int_Lm_releves_rincages_circuits"] = self.int_Lm_releves_rincages_circuits
        self.data["int_Lm_as_niveau_bas_NB1"] = self.int_Lm_as_niveau_bas_NB1
        self.data["int_Lm_as_temperature_haute_TH1"] = self.int_Lm_as_temperature_haute_TH1
        self.data["int_Lm_as_controle_ARU"] = self.int_Lm_as_controle_ARU
        self.data["int_Lm_as_alarme_hydraulique_voyant_defaut"] = self.int_Lm_as_alarme_hydraulique_voyant_defaut
        self.data["int_Lm_pompe_principale_45_100_verif_plein_huile"] = self.int_Lm_pompe_principale_45_100_verif_plein_huile
        self.data["int_Lm_pompe_principale_45_100_sens_rotation"] = self.int_Lm_pompe_principale_45_100_sens_rotation
        self.data["int_Lm_pompe_principale_45_100_embrayage_pompe"] = self.int_Lm_pompe_principale_45_100_embrayage_pompe
        self.data["int_Lm_pompe_principale_45_100_pression_HP"] = self.int_Lm_pompe_principale_45_100_pression_HP
        self.data["int_Lm_pompe_principale_45_100_stand_by"] = self.int_Lm_pompe_principale_45_100_stand_by
        self.data["int_Lm_pompe_principale_HPR165_38_verif_plein_huile"] = self.int_Lm_pompe_principale_HPR165_38_verif_plein_huile
        self.data["int_Lm_pompe_principale_HPR165_38_sens_rotation"] = self.int_Lm_pompe_principale_HPR165_38_sens_rotation
        self.data["int_Lm_pompe_principale_HPR165_38_embrayage_pompe"] = self.int_Lm_pompe_principale_HPR165_38_embrayage_pompe
        self.data["int_Lm_pompe_principale_HPR165_38_pression_HP"] = self.int_Lm_pompe_principale_HPR165_38_pression_HP
        self.data["int_Lm_pompe_principale_HPR165_38_stand_by"] = self.int_Lm_pompe_principale_HPR165_38_stand_by
        self.data["int_Lm_groupe_secours_pompe_45_sens_rotation"] = self.int_Lm_groupe_secours_pompe_45_sens_rotation
        self.data["int_Lm_groupe_secours_pompe_45_calage"] = self.int_Lm_groupe_secours_pompe_45_calage
        self.data["int_Lm_groupe_secours_pompe_45_serrage"] = self.int_Lm_groupe_secours_pompe_45_serrage
        self.data["int_Lm_groupe_secours_pompe_45_verif_plein_huile"] = self.int_Lm_groupe_secours_pompe_45_verif_plein_huile
        self.data["int_Lm_groupe_secours_pompe_45_marche_arret_moteur"] = self.int_Lm_groupe_secours_pompe_45_marche_arret_moteur
        self.data["int_Lm_groupe_secours_pompe_45_pression_HP"] = self.int_Lm_groupe_secours_pompe_45_pression_HP
        self.data["int_Lm_groupe_secours_pompe_45_stand_by"] = self.int_Lm_groupe_secours_pompe_45_stand_by
        self.data["int_Lm_groupe_secours_pompe_45_courant_demarrage"] = self.int_Lm_groupe_secours_pompe_45_courant_demarrage
        self.data["int_Lm_groupe_secours_pompe_45_courant_service"] = self.int_Lm_groupe_secours_pompe_45_courant_service
        self.data["int_Lm_reglage_limiteur_pression_REP10"] = self.int_Lm_reglage_limiteur_pression_REP10
        self.data["int_Lm_reglage_pressostat_retour"] = self.int_Lm_reglage_pressostat_retour
        self.data["int_Lm_reglage_reducteur_pression_REP13"] = self.int_Lm_reglage_reducteur_pression_REP13
        self.data["int_Lm_reglage_reducteur_pression_grue_REP16"] = self.int_Lm_reglage_reducteur_pression_grue_REP16
        self.data["int_Lm_fonctionnement_sys_refrigeration_embrayage"] = self.int_Lm_fonctionnement_sys_refrigeration_embrayage

    def save_data_int_appareil_gouverne(self):
        """ 
        Sauvegarde les données du menu intervenant appareil gouverne dans le dictionnaire data
        """
        self.data["AAG_schema_synoptique"] = self.AAG_schema_synoptique
        self.data["AAG_schema_electrique"] = self.AAG_schema_electrique
        self.data["AAG_schema_bornier"] = self.AAG_schema_bornier
        self.data["AAG_schema_cablage"] = self.AAG_schema_cablage
        self.data["AAG_releves_rincages_circuits"] = self.AAG_releves_rincages_circuits
        self.data["AAG_as_niveau_bas_NB1"] = self.AAG_as_niveau_bas_NB1
        self.data["AAG_as_controle_ARU"] = self.AAG_as_controle_ARU
        self.data["AAG_as_alarme_hydraulique_voyant_defaut"] = self.AAG_as_alarme_hydraulique_voyant_defaut
        self.data["AAG_verif_zero_mecanique_safran"] = self.AAG_verif_zero_mecanique_safran
        self.data["AAG_verif_zero_mecanique_recepteur"] = self.AAG_verif_zero_mecanique_recepteur
        self.data["AAG_verif_positionnement_transmetteur_BOPP"] = self.AAG_verif_positionnement_transmetteur_BOPP
        self.data["AAG_controle_puissance"] = self.AAG_controle_puissance
        self.data["AAG_controle_frequence"] = self.AAG_controle_frequence
        self.data["AAG_controle_commande"] = self.AAG_controle_commande
        self.data["AAG_controle_presence_24VDC"] = self.AAG_controle_presence_24VDC
        self.data["AAG_as_defauts_puissance"] = self.AAG_as_defauts_puissance
        self.data["AAG_as_defauts_moteur"] = self.AAG_as_defauts_moteur
        self.data["AAG_as_defauts_commande"] = self.AAG_as_defauts_commande
        self.data["AAG_as_niveau_bas"] = self.AAG_as_niveau_bas
        self.data["AAG_as_test_lampes"] = self.AAG_as_test_lampes
        self.data["AAG_as_controle_ARU2"] = self.AAG_as_controle_ARU2
        self.data["AAG_signalisation_defauts"] = self.AAG_signalisation_defauts
        self.data["AAG_APG_pompe_double_sens_rotation"] = self.AAG_APG_pompe_double_sens_rotation
        self.data["AAG_APG_pompe_double_marche_arret_moteur"] = self.AAG_APG_pompe_double_marche_arret_moteur
        self.data["AAG_APG_pompe_double_courant_demarrage"] = self.AAG_APG_pompe_double_courant_demarrage
        self.data["AAG_APG_pompe_double_courant_service"] = self.AAG_APG_pompe_double_courant_service
        self.data["AAG_RTRIB_reglage_limiteur_pression_centrale"] = self.AAG_RTRIB_reglage_limiteur_pression_centrale
        self.data[
            "AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"] = self.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne
        self.data["AAG_RTRIB_controle_vitesses_recepteur_moteur"] = self.AAG_RTRIB_controle_vitesses_recepteur_moteur
        self.data["AAG_RTRIB_controle_vitesses_recepteur_pompe"] = self.AAG_RTRIB_controle_vitesses_recepteur_pompe
        self.data[
            "AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"] = self.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax
        self.data[
            "AAG_RTRIB_controle_fin_course_electrique_arret_electros"] = self.AAG_RTRIB_controle_fin_course_electrique_arret_electros
        self.data["AAG_RTRIB_controle_fin_course_electrique_PX1"] = self.AAG_RTRIB_controle_fin_course_electrique_PX1
        self.data["AAG_RTRIB_controle_fin_course_electrique_PX2"] = self.AAG_RTRIB_controle_fin_course_electrique_PX2
        self.data[
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"] = self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle
        self.data[
            "AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"] = self.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre
        self.data["AAG_RBAB_reglage_limiteur_pression_centrale"] = self.AAG_RBAB_reglage_limiteur_pression_centrale
        self.data[
            "AAG_RBAB_reglage_limiteur_pression_double_en_ligne"] = self.AAG_RBAB_reglage_limiteur_pression_double_en_ligne
        self.data["AAG_RBAB_controle_vitesses_recepteur_moteur"] = self.AAG_RBAB_controle_vitesses_recepteur_moteur
        self.data["AAG_RBAB_controle_vitesses_recepteur_pompe"] = self.AAG_RBAB_controle_vitesses_recepteur_pompe
        self.data[
            "AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"] = self.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax
        self.data[
            "AAG_RBAB_controle_fin_course_electrique_arret_electros"] = self.AAG_RBAB_controle_fin_course_electrique_arret_electros
        self.data["AAG_RBAB_controle_fin_course_electrique_PX1"] = self.AAG_RBAB_controle_fin_course_electrique_PX1
        self.data["AAG_RBAB_controle_fin_course_electrique_PX2"] = self.AAG_RBAB_controle_fin_course_electrique_PX2
        self.data[
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"] = self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle
        self.data[
            "AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"] = self.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre

        self.data["int_AAG_schema_synoptique"] = self.int_AAG_schema_synoptique
        self.data["int_AAG_schema_electrique"] = self.int_AAG_schema_electrique
        self.data["int_AAG_schema_bornier"] = self.int_AAG_schema_bornier
        self.data["int_AAG_schema_cablage"] = self.int_AAG_schema_cablage
        self.data["int_AAG_releves_rincages_circuits"] = self.int_AAG_releves_rincages_circuits
        self.data["int_AAG_as_niveau_bas_NB1"] = self.int_AAG_as_niveau_bas_NB1
        self.data["int_AAG_as_controle_ARU"] = self.int_AAG_as_controle_ARU
        self.data["int_AAG_as_alarme_hydraulique_voyant_defaut"] = self.int_AAG_as_alarme_hydraulique_voyant_defaut
        self.data["int_AAG_verif_zero_mecanique_safran"] = self.int_AAG_verif_zero_mecanique_safran
        self.data["int_AAG_verif_zero_mecanique_recepteur"] = self.int_AAG_verif_zero_mecanique_recepteur
        self.data["int_AAG_verif_positionnement_transmetteur_BOPP"] = self.int_AAG_verif_positionnement_transmetteur_BOPP
        self.data["int_AAG_controle_puissance"] = self.int_AAG_controle_puissance
        self.data["int_AAG_controle_frequence"] = self.int_AAG_controle_frequence
        self.data["int_AAG_controle_commande"] = self.int_AAG_controle_commande
        self.data["int_AAG_controle_presence_24VDC"] = self.int_AAG_controle_presence_24VDC
        self.data["int_AAG_as_defauts_puissance"] = self.int_AAG_as_defauts_puissance
        self.data["int_AAG_as_defauts_moteur"] = self.int_AAG_as_defauts_moteur
        self.data["int_AAG_as_defauts_commande"] = self.int_AAG_as_defauts_commande
        self.data["int_AAG_as_niveau_bas"] = self.int_AAG_as_niveau_bas
        self.data["int_AAG_as_test_lampes"] = self.int_AAG_as_test_lampes
        self.data["int_AAG_as_controle_ARU2"] = self.int_AAG_as_controle_ARU2
        self.data["int_AAG_signalisation_defauts"] = self.int_AAG_signalisation_defauts
        self.data["int_AAG_APG_pompe_double_sens_rotation"] = self.int_AAG_APG_pompe_double_sens_rotation
        self.data["int_AAG_APG_pompe_double_marche_arret_moteur"] = self.int_AAG_APG_pompe_double_marche_arret_moteur
        self.data["int_AAG_APG_pompe_double_courant_demarrage"] = self.int_AAG_APG_pompe_double_courant_demarrage
        self.data["int_AAG_APG_pompe_double_courant_service"] = self.int_AAG_APG_pompe_double_courant_service
        self.data["int_AAG_RTRIB_reglage_limiteur_pression_centrale"] = self.int_AAG_RTRIB_reglage_limiteur_pression_centrale
        self.data["int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne"] = self.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne
        self.data["int_AAG_RTRIB_controle_vitesses_recepteur_moteur"] = self.int_AAG_RTRIB_controle_vitesses_recepteur_moteur
        self.data["int_AAG_RTRIB_controle_vitesses_recepteur_pompe"] = self.int_AAG_RTRIB_controle_vitesses_recepteur_pompe
        self.data["int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax"] = self.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax
        self.data["int_AAG_RTRIB_controle_fin_course_electrique_arret_electros"] = self.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros
        self.data["int_AAG_RTRIB_controle_fin_course_electrique_PX1"] = self.int_AAG_RTRIB_controle_fin_course_electrique_PX1
        self.data["int_AAG_RTRIB_controle_fin_course_electrique_PX2"] = self.int_AAG_RTRIB_controle_fin_course_electrique_PX2
        self.data["int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle"] = self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle
        self.data["int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre"] = self.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre
        self.data["int_AAG_RBAB_reglage_limiteur_pression_centrale"] = self.int_AAG_RBAB_reglage_limiteur_pression_centrale
        self.data["int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne"] = self.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne
        self.data["int_AAG_RBAB_controle_vitesses_recepteur_moteur"] = self.int_AAG_RBAB_controle_vitesses_recepteur_moteur
        self.data["int_AAG_RBAB_controle_vitesses_recepteur_pompe"] = self.int_AAG_RBAB_controle_vitesses_recepteur_pompe
        self.data["int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax"] = self.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax
        self.data["int_AAG_RBAB_controle_fin_course_electrique_arret_electros"] = self.int_AAG_RBAB_controle_fin_course_electrique_arret_electros
        self.data["int_AAG_RBAB_controle_fin_course_electrique_PX1"] = self.int_AAG_RBAB_controle_fin_course_electrique_PX1
        self.data["int_AAG_RBAB_controle_fin_course_electrique_PX2"] = self.int_AAG_RBAB_controle_fin_course_electrique_PX2
        self.data["int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle"] = self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle
        self.data["int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre"] = self.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre

    def save_data_int_treuil(self):
        """ 
        Sauvegarde les données du menu intervenant treuil dans le dictionnaire data
        """
        self.data["TPH125_0_traction_premiere_couche_statique"] = self.TPH125_0_traction_premiere_couche_statique
        self.data["TPH125_0_traction_premiere_couche_dynamique"] = self.TPH125_0_traction_premiere_couche_dynamique
        self.data["TPH125_0_pression"] = self.TPH125_0_pression
        self.data["TPH125_0_vitesse_rotation_PV"] = self.TPH125_0_vitesse_rotation_PV
        self.data["TPH125_0_vitesse_rotation_GV"] = self.TPH125_0_vitesse_rotation_GV
        self.data["TPH125_0_debit"] = self.TPH125_0_debit
        self.data["TPH125_0_essai_file_vire"] = self.TPH125_0_essai_file_vire
        self.data["TPH125_0_essai_freinage"] = self.TPH125_0_essai_freinage
        self.data["TPH125_0_selection_PV_GV"] = self.TPH125_0_selection_PV_GV
        self.data["TPH50_0_traction_premiere_couche_statique"] = self.TPH50_0_traction_premiere_couche_statique
        self.data["TPH50_0_traction_premiere_couche_dynamique"] = self.TPH50_0_traction_premiere_couche_dynamique
        self.data["TPH50_0_pression"] = self.TPH50_0_pression
        self.data["TPH50_0_vitesse_rotation_PV"] = self.TPH50_0_vitesse_rotation_PV
        self.data["TPH50_0_vitesse_rotation_GV"] = self.TPH50_0_vitesse_rotation_GV
        self.data["TPH50_0_debit"] = self.TPH50_0_debit
        self.data["TPH50_0_essai_file_vire"] = self.TPH50_0_essai_file_vire
        self.data["TPH50_0_essai_freinage"] = self.TPH50_0_essai_freinage
        self.data["TPH50_0_selection_PV_GV"] = self.TPH50_0_selection_PV_GV

        self.data["int_TPH125_0_traction_premiere_couche_statique"] = self.int_TPH125_0_traction_premiere_couche_statique
        self.data["int_TPH125_0_traction_premiere_couche_dynamique"] = self.int_TPH125_0_traction_premiere_couche_dynamique
        self.data["int_TPH125_0_pression"] = self.int_TPH125_0_pression
        self.data["int_TPH125_0_vitesse_rotation_PV"] = self.int_TPH125_0_vitesse_rotation_PV
        self.data["int_TPH125_0_vitesse_rotation_GV"] = self.int_TPH125_0_vitesse_rotation_GV
        self.data["int_TPH125_0_debit"] = self.int_TPH125_0_debit
        self.data["int_TPH125_0_essai_file_vire"] = self.int_TPH125_0_essai_file_vire
        self.data["int_TPH125_0_essai_freinage"] = self.int_TPH125_0_essai_freinage
        self.data["int_TPH125_0_selection_PV_GV"] = self.int_TPH125_0_selection_PV_GV
        self.data["int_TPH50_0_traction_premiere_couche_statique"] = self.int_TPH50_0_traction_premiere_couche_statique
        self.data["int_TPH50_0_traction_premiere_couche_dynamique"] = self.int_TPH50_0_traction_premiere_couche_dynamique
        self.data["int_TPH50_0_pression"] = self.int_TPH50_0_pression
        self.data["int_TPH50_0_vitesse_rotation_PV"] = self.int_TPH50_0_vitesse_rotation_PV
        self.data["int_TPH50_0_vitesse_rotation_GV"] = self.int_TPH50_0_vitesse_rotation_GV
        self.data["int_TPH50_0_debit"] = self.int_TPH50_0_debit
        self.data["int_TPH50_0_essai_file_vire"] = self.int_TPH50_0_essai_file_vire
        self.data["int_TPH50_0_essai_freinage"] = self.int_TPH50_0_essai_freinage
        self.data["int_TPH50_0_selection_PV_GV"] = self.int_TPH50_0_selection_PV_GV

    def save_data_int_cabestan(self):
        """ 
        Sauvegarde les données du menu intervenant cabestan dans le dictionnaire data
        """
        self.data["Cb_5T_traction_statique"] = self.Cb_5T_traction_statique
        self.data["Cb_5T_traction_dynamique"] = self.Cb_5T_traction_dynamique
        self.data["Cb_5T_pression"] = self.Cb_5T_pression
        self.data["Cb_5T_vitesse_rotation"] = self.Cb_5T_vitesse_rotation
        self.data["Cb_5T_debit"] = self.Cb_5T_debit
        self.data["Cb_5T_essai_file_vire"] = self.Cb_5T_essai_file_vire
        self.data["Cb_5T_freinage"] = self.Cb_5T_freinage
        self.data["Cb_3T_traction_statique"] = self.Cb_3T_traction_statique
        self.data["Cb_3T_traction_dynamique"] = self.Cb_3T_traction_dynamique
        self.data["Cb_3T_pression"] = self.Cb_3T_pression
        self.data["Cb_3T_vitesse_rotation"] = self.Cb_3T_vitesse_rotation
        self.data["Cb_3T_debit"] = self.Cb_3T_debit
        self.data["Cb_3T_debit"] = self.Cb_3T_essai_file_vire
        self.data["Cb_3T_freinage"] = self.Cb_3T_freinage

        self.data["int_Cb_5T_traction_statique"] = self.int_Cb_5T_traction_statique
        self.data["int_Cb_5T_traction_dynamique"] = self.int_Cb_5T_traction_dynamique
        self.data["int_Cb_5T_pression"] = self.int_Cb_5T_pression
        self.data["int_Cb_5T_vitesse_rotation"] = self.int_Cb_5T_vitesse_rotation
        self.data["int_Cb_5T_debit"] = self.int_Cb_5T_debit
        self.data["int_Cb_5T_essai_file_vire"] = self.int_Cb_5T_essai_file_vire
        self.data["int_Cb_5T_freinage"] = self.int_Cb_5T_freinage
        self.data["int_Cb_3T_traction_statique"] = self.int_Cb_3T_traction_statique
        self.data["int_Cb_3T_traction_dynamique"] = self.int_Cb_3T_traction_dynamique
        self.data["int_Cb_3T_pression"] = self.int_Cb_3T_pression
        self.data["int_Cb_3T_vitesse_rotation"] = self.int_Cb_3T_vitesse_rotation
        self.data["int_Cb_3T_debit"] = self.int_Cb_3T_debit
        self.data["int_Cb_3T_debit"] = self.int_Cb_3T_essai_file_vire
        self.data["int_Cb_3T_freinage"] = self.int_Cb_3T_freinage

    def save_data_int_recap(self):
        """ 
        Sauvegarde les données du menu intervenant recap dans le dictionnaire data
        """
        self.data["int_pieces_changees"] = self.int_pieces_changees
        self.data["int_pieces_cassees"] = self.int_pieces_cassees
        self.data["int_temps_passe"]  =self.int_temps_passe
        self.data["int_temps_mort"] = self.int_temps_mort
        self.data["int_commentaires"] = self.int_commentaires

    def int_finale(self, direc):
        """
        Sauvegarde les données du formulaire intervenant dans un fichier json
        Args:
          direc: chemin du fichier json

        Returns:
            None
        """
        # print(f"Le dossier est : {direc}")

        with open(direc, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

        # print(f"\nFormulaire sauvegardé dans le fichier {direc} avec les données suivantes :")
        # print(json.dumps(self.data, indent=4))