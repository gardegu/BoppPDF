import os
import asyncio
from pathlib import Path
from string import Template
import aiofiles
import shutil
import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
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
from PIL import Image as PilImage  
from kivy.lang import Builder
from kivy.utils import platform
from jnius import autoclass

from main_menu import MainMenu
from carac_affaire import CaracAffaire
from choix_categorie import ChoixCategorie
from local_machine import LocalMachine
from treuils import Treuils
from cabestan import Cabestan
from appareil_gouverne import AppareilGouverne
from app_data import AppData
from connexion import Connexion
from new_user import NewUser

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

from android.permissions import request_permissions, Permission
from android.storage import primary_external_storage_path

Context = autoclass('android.content.Context')
Environment = autoclass('android.os.Environment')
current_activity = autoclass('org.kivy.android.PythonActivity').mActivity
app_storage_path = current_activity.getExternalFilesDir(None).getAbsolutePath()



class pdfWriter:
    """ 
    Classe du générateur de PDF
    """
    def __init__(self):
        self.app_data = AppData()
        self.page_width, self.page_height = letter
        self.PAGE_WIDTH, PAGE_HEIGHT = A4
        self.MARGIN_LEFT = 40
        self.MARGIN_TOP = PAGE_HEIGHT - 60
        self.LINE_HEIGHT = 20
        self.HEADER_COLOR = HexColor("#cbcefb")
        self.TEXT_COLOR = HexColor("#000000")
        self.media_path = os.path.join(app_storage_path, 'media')
        self.sign_path = os.path.join(app_storage_path, 'signatures')
        self.pdf_path = os.path.join(app_storage_path, 'pdf')
        self.filename = f"{datetime.date.today()}_{self.app_data.case_number}.pdf"
        self.doc = SimpleDocTemplate(os.path.join('./build/', self.filename), pagesize=A4)
        # self.doc = SimpleDocTemplate(os.path.join(self.build_path, self.filename), pagesize=A4)

        os.makedirs(self.pdf_path, exist_ok=True)

    def draw_picture(self, path, x, y, width, height, leftbottom=False):
        """
        Dessine une image sur le document
        Args:
          path: chemin de l'image
          x: position en x du coin inférieur gauche
          y: position en y du coin inférieur gauche
          width: largeur de l'image
          height: hauteur de l'image
          leftbottom: position défaut (Default value = False)

        Returns:
            Image: image dessinée
        """
        img = Image(path, width, height)
        if leftbottom == True:
            img.hAlign = 'LEFT'  # Optionnel, permet d'aligner l'image à gauche
            img.vAlign = 'BOTTOM'  # Optionnel, permet d'aligner l'image en bas
        img.wrapOn(self.doc, self.page_width, self.page_height)  # Le wrap ajuste l'image selon la taille du document
        # Retourne l'image sans utiliser `drawOn`, mais l'ajoute directement aux éléments
        return img
    
    def show_popup(self, message):
        """
        Affiche un popup
        Args:
          message: message à afficher

        Returns:
            None
        """
        layout = BoxLayout(orientation='vertical')
        label = Label(text=message, color=(1,1,1,1))
        dismiss_button = Button(text='Fermer')
        layout.add_widget(label)
        layout.add_widget(dismiss_button)

        popup = Popup(title='Information', content=layout, size_hint=(0.8, 0.4))
        dismiss_button.bind(on_press=popup.dismiss)
        popup.open()

    def write_pdf(self):
        """ 
        Construit le PDF élément par élément puis l'enregistre
        """
        try:
            os.makedirs("./build/pdf", exist_ok=True)
        except Exception as e:
            self.show_popup(f"Erreur lors de la création du dossier de build : {e}")

        try:
            elements = []
            # --------------------------------------------------------------------------
            # Page de garde
            img = self.draw_picture(path="bopp.png", x=self.page_width - 600, y=self.page_height - 290, width=170, height=170, leftbottom=True)
            elements.append(img)

            styles = getSampleStyleSheet()
            title_style = styles['Title']
            title_paragraph = Paragraph(f"{self.app_data.intervention_type}", title_style)
            elements.append(title_paragraph)

            elements.append(Spacer(1, 30))

            data = [
                ["Affaire", f"{self.app_data.case_number}"],
                ["NB", f"{self.app_data.nb_field}"],
                ["Navire", f"{self.app_data.boat_name}"],
                ["Nom", f"{self.app_data.client_name}"],
                ["Chantier", f"{self.app_data.site_name}"],
                ["Armement", f"{self.app_data.armement}"]
            ]
            # data = [
            #     ["Affaire", f"{self.app_data.case_number}"],
            #     ["NB", f"{self.app_data.nb_field}"],
            #     ["Navire", f"{self.app_data.boat_name}"],
            #     ["Nom", f"{self.app_data.client_name}"],
            #     ["Chantier", f"{self.app_data.site_name}"]
            # ]
            elements.append(Table(data, colWidths=[150, 150], rowHeights=40, style=[
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 16),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                # ('BACKGROUND', (0, 0), (-1, 0), self.HEADER_COLOR),
                # ('TEXTCOLOR', (0, 0), (-1, -1), self.TEXT_COLOR),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'CENTER')
            ]))

            elements.append(Spacer(1, 100))

            data = [
                ["BOPP", "", "Chantier", "", "Armement", ""],
                ["Nom", f"{self.app_data.BOPP_name}", "Nom", f"{self.app_data.chantier_name}", "Nom", f"{self.app_data.armement_name}"],
                ["Date", f"{self.app_data.BOPP_date}", "Date", f"{self.app_data.chantier_date}", "Date", f"{self.app_data.armement_date}"],
                ["Visa", f"{self.app_data.BOPP_visa}", "Visa", f"{self.app_data.chantier_visa}", "Visa", f"{self.app_data.armement_visa}"]
            ]
            # data = [
            #     ["BOPP", "", "Chantier", "", "Armement", ""],
            #     ["Nom", "", "Nom", "", "Nom", ""],
            #     ["Date", "", "Date", "", "Date", ""],
            #     ["Visa", "", "Visa", "", "Visa", ""]
            # ]
            elements.append(Table(data, colWidths=[70, 70], rowHeights=20, style=[
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 11),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                # ('BACKGROUND', (0, 0), (-1, 0), self.HEADER_COLOR),
                # ('TEXTCOLOR', (0, 0), (-1, -1), self.TEXT_COLOR),
                ('ALIGN', (0, 0), (0, -1), 'LEFT')
            ]))

            elements.append(PageBreak())

            # --------------------------------------------------------------------------
            # Local Machine
            section_style = styles['Title']
            title_paragraph = Paragraph("Local Machine", section_style)
            elements.append(title_paragraph)

            data = [
                ["ESSAIS A REALISER", "Valeurs BE", "Valeurs Intervenant"],
                ["Vérification conformité hydraulique", "", ""],
                ["Schémas synoptiques", f"{self.app_data.Lm_schema_synoptique}", f"{self.app_data.int_Lm_schema_synoptique}"],
                ["Schémas électriques", f"{self.app_data.Lm_schema_electrique}", f"{self.app_data.int_Lm_schema_electrique}"],
                ["Schéma bornier", f"{self.app_data.Lm_schema_bornier}", f"{self.app_data.int_Lm_schema_bornier}"],
                ["Schéma câblage", f"{self.app_data.Lm_schema_cablage}", f"{self.app_data.int_Lm_schema_cablage}"],
                ["Relevé des rinçages circuits", f"{self.app_data.Lm_releves_rincages_circuits}", f"{self.app_data.int_Lm_releves_rincages_circuits}"],
                ["", "", ""],
                ["Alarmes et sécurités", "", ""],
                ["Niveau bas NB1", f"{self.app_data.Lm_as_niveau_bas_NB1}", f"{self.app_data.int_Lm_as_niveau_bas_NB1}"],
                ["Température haute TH1", f"{self.app_data.Lm_as_temperature_haute_TH1}", f"{self.app_data.int_Lm_as_temperature_haute_TH1}"],
                ["Contrôles des ARU", f"{self.app_data.Lm_as_controle_ARU}", f"{self.app_data.int_Lm_as_controle_ARU}"],
                ["Alarme hydraulique voyant et défaut", f"{self.app_data.Lm_as_alarme_hydraulique_voyant_defaut}", f"{self.app_data.int_Lm_as_alarme_hydraulique_voyant_defaut}"],
                ["", "", ""],
                ["Pompe principale série 45/100", "", ""],
                ["Vérification plein d'huile", f"{self.app_data.Lm_pompe_principale_45_100_verif_plein_huile}", f"{self.app_data.int_Lm_pompe_principale_45_100_verif_plein_huile}"],
                ["Sens de rotation", f"{self.app_data.Lm_pompe_principale_45_100_sens_rotation}", f"{self.app_data.int_Lm_pompe_principale_45_100_sens_rotation}"],
                ["Embrayage / débrayage pompe", f"{self.app_data.Lm_pompe_principale_45_100_embrayage_pompe}", f"{self.app_data.int_Lm_pompe_principale_45_100_embrayage_pompe}"],
                ["Pression HP pompe", f"{self.app_data.Lm_pompe_principale_45_100_pression_HP}", f"{self.app_data.int_Lm_pompe_principale_45_100_pression_HP}"],
                ["Stand-by pompe", f"{self.app_data.Lm_pompe_principale_45_100_stand_by}", f"{self.app_data.int_Lm_pompe_principale_45_100_stand_by}"],
                ["", "", ""],
                ["Pompe principale série HPR165_38", "", ""],
                ["Vérification plein d'huile", f"{self.app_data.Lm_pompe_principale_HPR165_38_verif_plein_huile}", f"{self.app_data.int_Lm_pompe_principale_HPR165_38_verif_plein_huile}"],
                ["Sens de rotation", f"{self.app_data.Lm_pompe_principale_HPR165_38_sens_rotation}", f"{self.app_data.int_Lm_pompe_principale_HPR165_38_sens_rotation}"],
                ["Embrayage / débrayage pompe", f"{self.app_data.Lm_pompe_principale_HPR165_38_embrayage_pompe}", f"{self.app_data.int_Lm_pompe_principale_HPR165_38_embrayage_pompe}"],
                ["Pression HP pompe", f"{self.app_data.Lm_pompe_principale_HPR165_38_pression_HP}", f"{self.app_data.int_Lm_pompe_principale_HPR165_38_pression_HP}"],
                ["Stand-by pompe", f"{self.app_data.Lm_pompe_principale_HPR165_38_stand_by}", f"{self.app_data.int_Lm_pompe_principale_HPR165_38_stand_by}"],
                ["", "", ""],
                ["Groupe de secours 11kW - pompe série 45", "", ""],
                ["Sens de rotation", f"{self.app_data.Lm_groupe_secours_pompe_45_sens_rotation}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_sens_rotation}"],
                ["Calage cylindrée", f"{self.app_data.Lm_groupe_secours_pompe_45_calage}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_calage}"],
                ["Serrage", f"{self.app_data.Lm_groupe_secours_pompe_45_serrage}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_serrage}"],
                ["Vérification plein d'huile", f"{self.app_data.Lm_groupe_secours_pompe_45_verif_plein_huile}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_verif_plein_huile}"],
                ["Marche/Arrêt moteur", f"{self.app_data.Lm_groupe_secours_pompe_45_marche_arret_moteur}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_marche_arret_moteur}"],
                ["Pression HP pompe", f"{self.app_data.Lm_groupe_secours_pompe_45_pression_HP}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_pression_HP}"],
                ["Stand-by pompe", f"{self.app_data.Lm_groupe_secours_pompe_45_stand_by}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_stand_by}"],
                ["Courant de démarrage", f"{self.app_data.Lm_groupe_secours_pompe_45_courant_demarrage}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_courant_demarrage}"],
                ["Courant de service", f"{self.app_data.Lm_groupe_secours_pompe_45_courant_service}", f"{self.app_data.int_Lm_groupe_secours_pompe_45_courant_service}"],
                ["", "", ""],
                ["Réglage limiteur de pression retour REP.10", f"{self.app_data.Lm_reglage_limiteur_pression_REP10}", f"{self.app_data.int_Lm_reglage_limiteur_pression_REP10}"],
                ["", "", ""],
                ["Réglage pressostat retour PR", f"{self.app_data.Lm_reglage_pressostat_retour}", f"{self.app_data.int_Lm_reglage_pressostat_retour}"],
                ["", "", ""],
                ["Réglage réducteur de pression REP.13", f"{self.app_data.Lm_reglage_reducteur_pression_REP13}", f"{self.app_data.int_Lm_reglage_reducteur_pression_REP13}"],
                ["", "", ""],
                ["Réglage réducteur de pression grue REP.16", f"{self.app_data.Lm_reglage_reducteur_pression_grue_REP16}", f"{self.app_data.int_Lm_reglage_reducteur_pression_grue_REP16}"],
                ["", "", ""],
                ["Fonctionnement du système de réfrigération", "", ""],
                ["Dès l'embrayage de la pompe principale", f"{self.app_data.Lm_fonctionnement_sys_refrigeration_embrayage}", f"{self.app_data.int_Lm_fonctionnement_sys_refrigeration_embrayage}"],
                ["", "", ""]
            ]
            elements.append(Table(data, rowHeights=14, style=[('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('BACKGROUND', (0, 0), (2, 0), colors.lightblue),
                        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
                        ('SPAN', (0, 1), (2, 1)),
                        ('SPAN', (0, 7), (2, 7)),
                        ('SPAN', (0, 8), (2, 8)),
                        ('SPAN', (0, 13), (2, 13)),
                        ('SPAN', (0, 14), (2, 14)),
                        ('SPAN', (0, 20), (2, 20)),
                        ('SPAN', (0, 21), (2, 21)),
                        ('SPAN', (0, 27), (2, 27)),
                        ('SPAN', (0, 28), (2, 28)),
                        ('SPAN', (0, 38), (2, 38)),
                        ('SPAN', (0, 40), (2, 40)),
                        ('SPAN', (0, 42), (2, 42)),
                        ('SPAN', (0, 44), (2, 44)),
                        ('SPAN', (0, 46), (2, 46)),
                        ('SPAN', (0, 47), (2, 47)),
                        ('SPAN', (0, 49), (2, 49)),
                        ('FONTNAME', (0, 1), (2, 1), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 8), (2, 8), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 14), (2, 14), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 21), (2, 21), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 28), (2, 28), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 47), (2, 47), 'Helvetica-Bold'),
                        ('ALIGN', (0, 2), (0, 6), 'RIGHT'),
                        ('ALIGN', (0, 9), (0, 12), 'RIGHT'),
                        ('ALIGN', (0, 15), (0, 19), 'RIGHT'),
                        ('ALIGN', (0, 22), (0, 27), 'RIGHT'),
                        ('ALIGN', (0, 29), (0, 37), 'RIGHT'),
                        ('ALIGN', (0, 48), (0, 48), 'RIGHT'),
                        ('VALIGN', (0, 0), (2, 55), 'MIDDLE'),
                        ('FONTSIZE', (0, 0), (2, 55), 8)
                        ])                    
            )

            elements.append(PageBreak())

            # --------------------------------------------------------------------------
            # Treuil
            section_style = styles['Title']
            title_paragraph = Paragraph("Treuil", section_style)
            elements.append(title_paragraph)

            data = [
                ["ESSAIS A REALISER", "Valeurs BE", "Valeurs Intervenant"],
                ["Treuil double TPH 125-0 - Bobine Diam.610", "", ""],
                ["150m de chaîne DN30", "", ""],
                ["Traction à la première couche statique", f"{self.app_data.TPH125_0_traction_premiere_couche_statique}", f"{self.app_data.int_TPH125_0_traction_premiere_couche_statique}"],
                ["Traction à la première couche dynamique", f"{self.app_data.TPH125_0_traction_premiere_couche_dynamique}", f"{self.app_data.int_TPH125_0_traction_premiere_couche_dynamique}"],
                ["Pression ΔP", f"{self.app_data.TPH125_0_pression}", f"{self.app_data.int_TPH125_0_pression}"],
                ["", "", ""],
                ["Vitesse de rotation PV", f"{self.app_data.TPH125_0_vitesse_rotation_PV}", f"{self.app_data.int_TPH125_0_vitesse_rotation_PV}"],
                ["Vitesse de rotation GV", f"{self.app_data.TPH125_0_vitesse_rotation_GV}", f"{self.app_data.int_TPH125_0_vitesse_rotation_GV}"],
                ["Débit", f"{self.app_data.TPH125_0_debit}", f"{self.app_data.int_TPH125_0_debit}"],
                ["", "", ""],
                ["Essais file-vire", f"{self.app_data.TPH125_0_essai_file_vire}", f"{self.app_data.int_TPH125_0_essai_file_vire}"],
                ["Essais freinage", f"{self.app_data.TPH125_0_essai_freinage}", f"{self.app_data.int_TPH125_0_essai_freinage}"],
                ["", "", ""],
                ["Sélection PV ou GV", f"{self.app_data.TPH125_0_selection_PV_GV}", f"{self.app_data.int_TPH125_0_selection_PV_GV}"],
                ["", "", ""],
                ["Treuil double TPH 50-2 - Bobine Diam.292", "", ""],
                ["200m de câble acier diam.20 + 150m de câble textile diam.30", "", ""],
                ["Traction à la première couche statique", f"{self.app_data.TPH50_0_traction_premiere_couche_statique}", f"{self.app_data.int_TPH50_0_traction_premiere_couche_statique}"],
                ["Traction à la première couche dynamique", f"{self.app_data.TPH50_0_traction_premiere_couche_dynamique}", f"{self.app_data.int_TPH50_0_traction_premiere_couche_dynamique}"],
                ["Pression ΔP", f"{self.app_data.TPH50_0_pression}", f"{self.app_data.int_TPH50_0_pression}"],
                ["", "", ""],
                ["Vitesse de rotation PV", f"{self.app_data.TPH50_0_vitesse_rotation_PV}", f"{self.app_data.int_TPH50_0_vitesse_rotation_PV}"],
                ["Vitesse de rotation GV", f"{self.app_data.TPH50_0_vitesse_rotation_GV}", f"{self.app_data.int_TPH50_0_vitesse_rotation_GV}"],
                ["Débit", f"{self.app_data.TPH50_0_debit}", f"{self.app_data.int_TPH50_0_debit}"],
                ["", "", ""],
                ["Essais file-vire", f"{self.app_data.TPH50_0_essai_file_vire}", f"{self.app_data.int_TPH50_0_essai_file_vire}"],
                ["Essais freinage", f"{self.app_data.TPH50_0_essai_freinage}", f"{self.app_data.int_TPH50_0_essai_freinage}"],
                ["", "", ""],
                ["Sélection PV ou GV", f"{self.app_data.TPH50_0_selection_PV_GV}", f"{self.app_data.int_TPH50_0_selection_PV_GV}"],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
            elements.append(Table(data, rowHeights=15, style=[('GRID', (0, 0), (2, 0), 1, colors.black),
                                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                                ('BOX', (0, 1), (2, 2), 1, colors.black),
                                ('GRID', (0, 3), (2, 5), 1, colors.black),
                                ('GRID', (0, 7), (2, 9), 1, colors.black),
                                ('GRID', (0, 11), (2, 12), 1, colors.black),
                                ('GRID', (0, 14), (2, 14), 1, colors.black),
                                ('BOX', (0, 16), (2, 17), 1, colors.black),
                                ('GRID', (0, 18), (2, 20), 1, colors.black),
                                ('GRID', (0, 22), (2, 24), 1, colors.black),
                                ('GRID', (0, 26), (2, 27), 1, colors.black),
                                ('GRID', (0, 29), (2, 29), 1, colors.black),


                                ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
                                ('BACKGROUND', (0, 0), (2, 0), colors.lightblue),
                                ('SPAN', (0, 1), (2, 1)),
                                ('SPAN', (0, 2), (2, 2)),
                                ('SPAN', (0, 16), (2, 16)),
                                ('SPAN', (0, 17), (2, 17)),
                                ('FONTNAME', (0, 1), (2, 1), 'Helvetica-Bold'),
                                ('FONTNAME', (0, 2), (2, 2), 'Helvetica-Oblique'),
                                ('FONTNAME', (0, 16), (2, 16), 'Helvetica-Bold'),
                                ('FONTNAME', (0, 17), (2, 17), 'Helvetica-Oblique'),
                                ('ALIGN', (0, 3), (0, 5), 'RIGHT'),
                                ('ALIGN', (0, 7), (0, 14), 'RIGHT'),
                                ('ALIGN', (0, 18), (0, 30), 'RIGHT'),
                                ('FONTSIZE', (0, 0), (2, 42), 8)
                                ])
            )

            elements.append(PageBreak())

            # --------------------------------------------------------------------------
            # Cabestan
            section_style = styles['Title']
            title_paragraph = Paragraph("Cabestan", section_style)
            elements.append(title_paragraph)

            data = [
                ["ESSAIS A REALISER", "Valeurs BE", "Valeurs Intervenant"],
                ["Cabestan 5T", "", ""],
                ["Traction statique", f"{self.app_data.Cb_5T_traction_statique}", f"{self.app_data.int_Cb_5T_traction_statique}"],
                ["Traction dynamique", f"{self.app_data.Cb_5T_traction_dynamique}", f"{self.app_data.int_Cb_5T_traction_dynamique}"],
                ["Pression ΔP", f"{self.app_data.Cb_5T_pression}", f"{self.app_data.int_Cb_5T_pression}"],
                ["", "", ""],
                ["Vitesse de rotation", f"{self.app_data.Cb_5T_vitesse_rotation}", f"{self.app_data.int_Cb_5T_vitesse_rotation}"],
                ["Débit", f"{self.app_data.Cb_5T_debit}", f"{self.app_data.int_Cb_5T_debit}"],
                ["", "", ""],
                ["Essais file-vire", f"{self.app_data.Cb_5T_essai_file_vire}", f"{self.app_data.int_Cb_5T_essai_file_vire}"],
                ["Freinage - défreinage moteur", f"{self.app_data.Cb_5T_freinage}", f"{self.app_data.int_Cb_5T_freinage}"],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["Cabestan 3T", "", ""],
                ["Traction statique", f"{self.app_data.Cb_3T_traction_statique}", f"{self.app_data.int_Cb_3T_traction_statique}"],
                ["Traction dynamique", f"{self.app_data.Cb_3T_traction_dynamique}", f"{self.app_data.int_Cb_3T_traction_dynamique}"],
                ["Pression ΔP", f"{self.app_data.Cb_3T_pression}", f"{self.app_data.int_Cb_3T_pression}"],
                ["", "", ""],
                ["Vitesse de rotation", f"{self.app_data.Cb_3T_vitesse_rotation}", f"{self.app_data.int_Cb_3T_vitesse_rotation}"],
                ["Débit", f"{self.app_data.Cb_3T_debit}", f"{self.app_data.int_Cb_3T_debit}"],
                ["", "", ""],
                ["Essais file-vire", f"{self.app_data.Cb_3T_essai_file_vire}", f"{self.app_data.int_Cb_3T_essai_file_vire}"],
                ["Freinage - défreinage moteur", f"{self.app_data.Cb_3T_freinage}", f"{self.app_data.int_Cb_3T_freinage}"],
                ["", "", ""],
                ["Sélection PV ou GV", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
            elements.append(Table(data, rowHeights=15, style=[('GRID', (0, 0), (2, 0), 1, colors.black),
                        ('BOX', (0, 0), (-1, -1), 1, colors.black),
                        ('GRID', (0, 2), (2, 10), 1, colors.black),
                        ('GRID', (0, 11), (2, 12), 1, colors.black),
                        ('GRID', (0, 14), (2, 14), 1, colors.black),
                        ('GRID', (0, 16), (2, 32), 1, colors.black),
                        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
                        ('BACKGROUND', (0, 0), (2, 0), colors.lightblue),
                        ('SPAN', (0, 1), (2, 1)),
                        ('SPAN', (0, 5), (2, 5)),
                        ('SPAN', (0, 8), (2, 8)),
                        ('SPAN', (0, 11), (2, 14)),
                        ('SPAN', (0, 19), (2, 19)),
                        ('SPAN', (0, 22), (2, 22)),
                        ('SPAN', (0, 25), (2, 25)),
                        ('SPAN', (0, 27), (2, 30)),
                        ('FONTNAME', (0, 1), (2, 1), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 15), (2, 15), 'Helvetica-Bold'),
                        ('ALIGN', (0, 2), (0, 10), 'RIGHT'),
                        ('ALIGN', (0, 16), (0, 27), 'RIGHT'),
                        ('FONTSIZE', (0, 0), (2, 27), 8)
                        ])
            )

            elements.append(PageBreak())

            # --------------------------------------------------------------------------
            # Appareil Gouverne 1
            section_style = styles['Title']
            title_paragraph = Paragraph("Appareil Gouverne 1", section_style)
            elements.append(title_paragraph)

            data = [
                ["ESSAIS A REALISER", "Valeurs BE", "Valeurs Intervenant"],
                ["Vérification conformité hydraulique", "", ""],
                ["Schémas synoptiques", f"{self.app_data.AAG_schema_synoptique}", f"{self.app_data.int_AAG_schema_synoptique}"],
                ["Schémas électriques", f"{self.app_data.AAG_schema_electrique}", f"{self.app_data.int_AAG_schema_electrique}"],
                ["Schéma bornier", f"{self.app_data.AAG_schema_bornier}", f"{self.app_data.int_AAG_schema_bornier}"],
                ["Schéma câblage", f"{self.app_data.AAG_schema_cablage}", f"{self.app_data.int_AAG_schema_cablage}"],
                ["Relevé des rinçages circuits", f"{self.app_data.AAG_releves_rincages_circuits}", f"{self.app_data.int_AAG_releves_rincages_circuits}"],
                ["", "", ""],
                ["Alarmes et sécurités", "", ""],
                ["Niveau bas NB1", f"{self.app_data.AAG_as_niveau_bas_NB1}", f"{self.app_data.int_AAG_as_niveau_bas_NB1}"],
                ["Contrôles des ARU", f"{self.app_data.AAG_as_controle_ARU}", f"{self.app_data.int_AAG_as_controle_ARU}"],
                ["Alarme hydraulique voyant et défaut", f"{self.app_data.AAG_as_alarme_hydraulique_voyant_defaut}", f"{self.app_data.int_AAG_as_alarme_hydraulique_voyant_defaut}"],
                ["", "", ""],
                ["Vérification du zéro mécanique safran", f"{self.app_data.AAG_verif_zero_mecanique_safran}", f"{self.app_data.int_AAG_verif_zero_mecanique_safran}"],
                ["Vérification du zéro mécanique du transmetteur", f"{self.app_data.AAG_verif_zero_mecanique_recepteur}", f"{self.app_data.int_AAG_verif_zero_mecanique_recepteur}"],
                ["Vérification du positionnement du transmetteur BOPP", f"{self.app_data.AAG_verif_positionnement_transmetteur_BOPP}", f"{self.app_data.int_AAG_verif_positionnement_transmetteur_BOPP}"],
                ["", "", ""],
                ["Contrôle des tensions/fréquences", "", ""],
                ["Puissance", f"{self.app_data.AAG_controle_puissance}", f"{self.app_data.int_AAG_controle_puissance}"],
                ["Fréquence", f"{self.app_data.AAG_controle_frequence}", f"{self.app_data.int_AAG_controle_frequence}"],
                ["Commande", f"{self.app_data.AAG_controle_commande}", f"{self.app_data.int_AAG_controle_commande}"],
                ["Présence 24 VDC secours batterie", f"{self.app_data.AAG_controle_presence_24VDC}", f"{self.app_data.int_AAG_controle_presence_24VDC}"],
                ["", "", ""],
                ["Alarmes et sécurités", "", ""],
                ["Défauts de puissance", f"{self.app_data.AAG_as_defauts_puissance}", f"{self.app_data.int_AAG_as_defauts_puissance}"],
                ["Défauts moteur", f"{self.app_data.AAG_as_defauts_moteur}", f"{self.app_data.int_AAG_as_defauts_moteur}"],
                ["Défauts commande", f"{self.app_data.AAG_as_defauts_commande}", f"{self.app_data.int_AAG_as_defauts_commande}"],
                ["Niveau bas", f"{self.app_data.AAG_as_niveau_bas}", f"{self.app_data.int_AAG_as_niveau_bas}"],
                ["Test lampes", f"{self.app_data.AAG_as_test_lampes}", f"{self.app_data.int_AAG_as_test_lampes}"],
                ["Contrôle des ARU", f"{self.app_data.AAG_as_controle_ARU2}", f"{self.app_data.int_AAG_as_controle_ARU2}"],
                ["", "", ""],
                ["Signalisation visuelle et sonore des défauts sur coffret \n et sur platine passerelle", f"{self.app_data.AAG_signalisation_defauts}", f"{self.app_data.int_AAG_signalisation_defauts}"],
                ["", "", ""],
                ["", "", ""],
                ["Groupe APG 1,5 kW - pompe double 1,2 + 1,cm3/tr", "", ""],
                ["Sens de rotation", f"{self.app_data.AAG_APG_pompe_double_sens_rotation}", f"{self.app_data.int_AAG_APG_pompe_double_sens_rotation}"],
                ["MARCHE / ARRET moteur", f"{self.app_data.AAG_APG_pompe_double_marche_arret_moteur}", f"{self.app_data.int_AAG_APG_pompe_double_marche_arret_moteur}"],
                ["Courant de démarrage", f"{self.app_data.AAG_APG_pompe_double_courant_demarrage}", f"{self.app_data.int_AAG_APG_pompe_double_courant_demarrage}"],
                ["Courant de service", f"{self.app_data.AAG_APG_pompe_double_courant_service}", f"{self.app_data.int_AAG_APG_pompe_double_courant_service}"],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
            elements.append(Table(data, rowHeights=14, style=[('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('BACKGROUND', (0, 0), (2, 0), colors.lightblue),
                        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
                        ('SPAN', (0, 1), (2, 1)),
                        ('SPAN', (0, 7), (2, 7)),
                        ('SPAN', (0, 8), (2, 8)),
                        ('SPAN', (0, 12), (2, 12)),
                        ('SPAN', (0, 16), (2, 16)),
                        ('SPAN', (0, 22), (2, 22)),
                        ('SPAN', (0, 23), (2, 23)),
                        ('SPAN', (0, 30), (2, 30)),
                        ('SPAN', (0, 31), (0, 32)),
                        ('SPAN', (1, 31), (1, 32)),
                        ('SPAN', (2, 31), (2, 32)),
                        ('SPAN', (0, 33), (2, 33)),
                        ('SPAN', (0, 39), (2, 44)),
                        ('FONTNAME', (0, 1), (2, 1), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 8), (2, 8), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 23), (2, 23), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 34), (2, 34), 'Helvetica-Bold'),
                        ('ALIGN', (0, 2), (0, 6), 'RIGHT'),
                        ('ALIGN', (0, 9), (0, 21), 'RIGHT'),
                        ('ALIGN', (0, 24), (0, 33), 'RIGHT'),
                        ('ALIGN', (0, 35), (0, 48), 'RIGHT'),
                        ('VALIGN', (0, 0), (2, 55), 'MIDDLE'),
                        ('FONTSIZE', (0, 0), (2, 55), 8)
                        ])
            )

            elements.append(PageBreak())

            # --------------------------------------------------------------------------
            # Appareil Gouverne 2
            section_style = styles['Title']
            title_paragraph = Paragraph("Appareil Gouverne 2", section_style)
            elements.append(title_paragraph)

            data = [
                ["ESSAIS A REALISER", "Valeurs BE", "Valeurs Intervenant"],
                ["RECEPTEUR TRIBORD", "", ""],
                ["Réglage limiteur de pression sur centrale", f"{self.app_data.AAG_RTRIB_reglage_limiteur_pression_centrale}", f"{self.app_data.int_AAG_RTRIB_reglage_limiteur_pression_centrale}"],
                ["Réglage limiteur de pression en ligne", f"{self.app_data.AAG_RTRIB_reglage_limiteur_pression_double_en_ligne}", f"{self.app_data.int_AAG_RTRIB_reglage_limiteur_pression_double_en_ligne}"],
                ["", "", ""],
                ["Contrôle des vitesses régulateur tribord", "", ""],
                ["Moteur seul", f"{self.app_data.AAG_RTRIB_controle_vitesses_recepteur_moteur}", f"{self.app_data.int_AAG_RTRIB_controle_vitesses_recepteur_moteur}"],
                ["Pompe manuelle (secours)", f"{self.app_data.AAG_RTRIB_controle_vitesses_recepteur_pompe}", f"{self.app_data.int_AAG_RTRIB_controle_vitesses_recepteur_pompe}"],
                ["Réglage de la pression maximale de fonctionnement", f"{self.app_data.AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax}", f"{self.app_data.int_AAG_RTRIB_controle_vitesses_recepteur_reglage_Pmax}"],
                ["", "", ""],
                ["Contrôle des fins de courses électriques Bd / Td", "", ""],
                ["Arrêt des électros par capteurs inductifs (réglage)", f"{self.app_data.AAG_RTRIB_controle_fin_course_electrique_arret_electros}", f"{self.app_data.int_AAG_RTRIB_controle_fin_course_electrique_arret_electros}"],
                ["PX1 : FdC BD", f"{self.app_data.AAG_RTRIB_controle_fin_course_electrique_PX1}", f"{self.app_data.int_AAG_RTRIB_controle_fin_course_electrique_PX1}"],
                ["PX2 : FdC TD", f"{self.app_data.AAG_RTRIB_controle_fin_course_electrique_PX2}", f"{self.app_data.int_AAG_RTRIB_controle_fin_course_electrique_PX2}"],
                ["", "", ""],
                ["Contrôle de fonctionnement des indicateurs d'angle de barre", "", ""],
                ["Angle de passerelle", f"{self.app_data.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle}", f"{self.app_data.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_passerelle}"],
                ["Angle local barre", f"{self.app_data.AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre}", f"{self.app_data.int_AAG_RTRIB_controle_fonctionnement_indicateurs_angle_local_barre}"],
                ["", "", ""],
                ["RECEPTEUR BABORD", "", ""],
                ["Réglage limiteur de pression sur centrale", f"{self.app_data.AAG_RBAB_reglage_limiteur_pression_centrale}", f"{self.app_data.int_AAG_RBAB_reglage_limiteur_pression_centrale}"],
                ["Réglage limiteur de pression en ligne", f"{self.app_data.AAG_RBAB_reglage_limiteur_pression_double_en_ligne}", f"{self.app_data.int_AAG_RBAB_reglage_limiteur_pression_double_en_ligne}"],
                ["", "", ""],
                ["Contrôle des vitesses régulateur tribord", "", ""],
                ["Moteur seul", f"{self.app_data.AAG_RBAB_controle_vitesses_recepteur_moteur}", f"{self.app_data.int_AAG_RBAB_controle_vitesses_recepteur_moteur}"],
                ["Pompe manuelle (secours)", f"{self.app_data.AAG_RBAB_controle_vitesses_recepteur_pompe}", f"{self.app_data.int_AAG_RBAB_controle_vitesses_recepteur_pompe}"],
                ["Réglage de la pression maximale de fonctionnement", f"{self.app_data.AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax}", f"{self.app_data.int_AAG_RBAB_controle_vitesses_recepteur_reglage_Pmax}"],
                ["", "", ""],
                ["Contrôle des fins de courses électriques Bd / Td", "", ""],
                ["Arrêt des électros par capteurs inductifs (réglage)", f"{self.app_data.AAG_RBAB_controle_fin_course_electrique_arret_electros}", f"{self.app_data.int_AAG_RBAB_controle_fin_course_electrique_arret_electros}"],
                ["PX1 : FdC BD", f"{self.app_data.AAG_RBAB_controle_fin_course_electrique_PX1}", f"{self.app_data.int_AAG_RBAB_controle_fin_course_electrique_PX1}"],
                ["PX2 : FdC TD", f"{self.app_data.AAG_RBAB_controle_fin_course_electrique_PX2}", f"{self.app_data.int_AAG_RBAB_controle_fin_course_electrique_PX2}"],
                ["", "", ""],
                ["Contrôle de fonctionnement des indicateurs d'angle de barre", "", ""],
                ["Angle de passerelle", f"{self.app_data.AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle}", f"{self.app_data.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_passerelle}"],
                ["Angle local barre", f"{self.app_data.AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre}", f"{self.app_data.int_AAG_RBAB_controle_fonctionnement_indicateurs_angle_local_barre}"],
            ]
            elements.append(Table(data, rowHeights=14, style=[('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('BACKGROUND', (0, 0), (2, 0), colors.lightblue),
                        ('FONTNAME', (0, 0), (2, 0), 'Helvetica-Bold'),
                        ('SPAN', (0, 1), (2, 1)),
                        ('SPAN', (0, 5), (2, 5)),
                        ('SPAN', (0, 4), (2, 4)),
                        ('SPAN', (0, 9), (2, 9)),
                        ('SPAN', (0, 10), (2, 10)),
                        ('SPAN', (0, 14), (2, 14)),
                        ('SPAN', (0, 15), (2, 15)),
                        ('SPAN', (0, 18), (2, 18)),
                        ('SPAN', (0, 19), (2, 19)),
                        ('SPAN', (0, 22), (2, 22)),
                        ('SPAN', (0, 23), (2, 23)),
                        ('SPAN', (0, 27), (2, 27)),
                        ('SPAN', (0, 28), (2, 28)),
                        ('SPAN', (0, 32), (2, 32)),
                        ('SPAN', (0, 33), (2, 33)),
                        ('SPAN', (0, 33), (2, 33)),
                        ('SPAN', (0, 39), (2, 44)),
                        ('FONTNAME', (0, 1), (2, 1), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 5), (2, 5), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 10), (2, 10), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 15), (2, 15), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 19), (2, 19), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 23), (2, 23), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 28), (2, 28), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 33), (2, 33), 'Helvetica-Bold'),
                        ('ALIGN', (0, 2), (0, 4), 'RIGHT'),
                        ('ALIGN', (0, 11), (0, 14), 'RIGHT'),
                        ('ALIGN', (0, 16), (0, 18), 'RIGHT'),
                        ('ALIGN', (0, 20), (0, 22), 'RIGHT'),
                        ('ALIGN', (0, 24), (0, 27), 'RIGHT'),
                        ('ALIGN', (0, 29), (0, 32), 'RIGHT'),
                        ('ALIGN', (0, 34), (0, 36), 'RIGHT'),
                        ('VALIGN', (0, 0), (2, 55), 'MIDDLE'),
                        ('FONTSIZE', (0, 0), (2, 55), 8)
                        ])
            )

            elements.append(PageBreak())

            #--------------------------------------------------------------------------
            # Infos supplémentaires
            section_style = styles['Title']
            title_paragraph = Paragraph("Récapitulatif", section_style)
            elements.append(title_paragraph)

            data = [
                ["Récapitulatif des événements de l'intervention"],
                ["Matériel remplacé", ""],
                ["Pièces changées", f"{self.app_data.int_pieces_changees}"],
                ["Pièces cassées", f"{self.app_data.int_pieces_cassees}"],
                ["", ""],
                ["Temps d'intervention", ""],
                ["Temps passé", f"{self.app_data.int_temps_passe}"],
                ["Temps mort", f"{self.app_data.int_temps_mort}"],
                ["", ""],
                ["Commentaires :", ""],
                ["", f"{self.app_data.int_commentaires}"],
                ["", ""],
                ["", ""],
                ["", ""],
                ["", ""],
                ["", ""],
                ["", ""],
                ["", ""]
            ]
            elements.append(Table(data, rowHeights=15, style=[('GRID', (0, 0), (-1, -1), 1, colors.black),
                       ('SPAN', (0, 0), (1, 0)),
                       ('SPAN', (0, 1), (1, 1)),
                       ('SPAN', (0, 4), (1, 4)),
                       ('SPAN', (0, 5), (1, 5)),
                       ('SPAN', (0, 8), (1, 8)),
                       ('SPAN', (0, 9), (1, 9)),
                       ('SPAN', (0, 10), (1, 17)),
                       ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
                       ('FONTNAME', (0, 1), (1, 1), 'Helvetica-Bold'),
                       ('FONTNAME', (0, 5), (1, 5), 'Helvetica-Bold'),
                       ('FONTNAME', (0, 8), (1, 8), 'Helvetica-Bold'),
                       ('FONTNAME', (0, 9), (1, 9), 'Helvetica-Bold'),
                       ('BACKGROUND', (0, 0), (1, 0), colors.lightblue),
                       ('FONTSIZE', (0, 0), (1, 27), 8)
                       ])
            )

            elements.append(Spacer(1, 20))

            section_style = styles['Title']
            title_paragraph = Paragraph("Signatures", section_style)
            elements.append(title_paragraph)

            # rep_sign = './signatures'
            # rep_sign = '/signatures'

            # if os.path.isdir(rep_sign):     
            if os.path.isdir(self.sign_path):     
                # if os.listdir(rep_sign):   
                if os.listdir(self.sign_path):   
                    sign_style = styles['Heading1']
                    # sign_int = './signatures/signature_int.png'  
                    # sign_int = '/signatures/signature_int.png'  
                    sign_int = os.path.join(self.sign_path,'signature_int.png')
                    # sign_client = './signatures/signature_client.png'
                    # sign_client = '/signatures/signature_client.png'
                    sign_client = os.path.join(self.sign_path,'signature_client.png')
                    try:
                        img_width = 150
                        img_height = 50
                        margin = 10
                        page_width, page_height = A4  
                        x_start = (page_width - (3 * img_width + 2 * margin)) / 2  
                        y_start = page_height - 100  

                        sign_paragraph = Paragraph("Signature intervenant : ", sign_style)

                        elements.append(sign_paragraph)

                        img = self.draw_picture(
                            path=sign_int, 
                            x=x_start,
                            y=y_start,
                            width=img_width,
                            height=img_height
                        )

                        elements.append(img)
                        elements.append(Spacer(1, 10))

                        sign_paragraph = Paragraph("Signature client : ", sign_style)

                        elements.append(sign_paragraph)

                        img = self.draw_picture(
                            path=sign_client, 
                            x=x_start,
                            y=y_start - img_height - margin,
                            width=img_width,
                            height=img_height
                        )

                        elements.append(img)
                    
                    except Exception as e:
                        self.show_popup(f"Problème avec l'ajout des signatures : {e}")


            elements.append(PageBreak())

            # --------------------------------------------------------------------------
            # Galerie de photos

            if self.app_data.is_galerie:
                section_style = styles['Title']
                title_paragraph = Paragraph("Galerie de photos", section_style)
                elements.append(title_paragraph)

                elements.append(Spacer(1, 50))
                
                # images = [f for f in os.listdir('./media') if f.endswith('.png')]
                images = [f for f in os.listdir(self.media_path) if f.endswith('.png')]

                # Dimensions des images
                img_width = 400
                img_height = 150
                margin = 10
                page_width, page_height = A4  
                x_start = (page_width - (3 * img_width + 2 * margin)) / 2  
                y_start = page_height - 100  
                x_positions = [x_start, x_start + img_width + margin, x_start + 2 * (img_width + margin)]

                y_position = y_start
                images_on_page = 0

                for img in images:
                    try:
                        # Calcule la position en fonction du nombre d'images sur la page
                        x_position = x_positions[images_on_page % 3]
                        img = self.draw_picture(
                            # path=f"./media/{img_path}",
                            # path=f"{self.media_path}/{img}",
                            path= os.path.join(self.media_path,img),
                            x=x_position,
                            y=y_position,
                            width=img_width,
                            height=img_height
                        )
                        elements.append(img)
                        elements.append(Spacer(1, 10))
                        images_on_page += 1

                        # Passe à la ligne suivante après 3 images
                        if images_on_page % 3 == 0:
                            y_position -= img_height + margin

                        # Saut de page si on dépasse la hauteur de la page
                        if y_position - img_height < 50:
                            elements.append(PageBreak())
                            y_position = y_start
                            images_on_page = 0

                    except Exception as e:
                        self.show_popup(f"Problème avec l'ajout des images : {e}")

            #--------------------------------------------------------------------------
            # Fin du document

            self.doc.build(elements)
            self.show_popup(f"Le fichier PDF a été créé avec succès !")
        except Exception as e:
            self.show_popup(f"Erreur lors de la création du fichier PDF : {e}")

        # Déplacer le fichier PDF vers le dossier Documents
        documents_path = Path('/storage/emulated/0/Documents')
        try:
            # shutil.move(os.path.join(self.build_path, self.filename), os.path.join(documents_path, self.filename))
            shutil.move(os.path.join('./build/',self.filename), os.path.join(documents_path, self.filename))
            self.show_popup(f"Le fichier PDF a été déplacé dans le dossier Documents.")
        except Exception as e:
            self.show_popup(f"Erreur lors du déplacement du fichier : {e}")

        try:
            shutil.move(os.path.join('./build/',self.filename), os.path.join(self.pdf_path, self.filename))
            self.show_popup(f"Le fichier PDF a été déplacé dans le dossier PDF.")
        except Exception as e:
            self.show_popup(f"Erreur lors du déplacement du fichier : {e}")

    def execute(self):
        """ 
        Génère le fichier PDF
        """
        # app_data = AppData()
        # app_data.save_data()
        self.write_pdf()