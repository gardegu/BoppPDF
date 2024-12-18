# main.py
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
import shutil
import json
import os

from main_menu import MainMenu
from carac_affaire import CaracAffaire
from choix_categorie import ChoixCategorie
from local_machine import LocalMachine
from treuils import Treuils
from cabestan import Cabestan
from appareil_gouverne import AppareilGouverne
from app_data import AppData
from connexion import Connexion
from closure import Closure
from new_user import NewUser
from supp_affaire import SupprimerAffaire
from modif_choix_affaire import ModifAffaire
from modif_carac_affaire import ModifCaracAffaire
from modif_choix_categorie import ModifChoixCategorie
from modif_appareil_gouverne import ModifAppareilGouverne
from modif_cabestan import ModifCabestan
from modif_local_machine import ModifLocalMachine
from modif_treuils import ModifTreuils
from modif_closure import ModifClosure
from main_menu_dev import MainMenuDev
from main_menu_int import MainMenuInt
from int_carac_affaire import IntCaracAffaire
from int_choix_categorie import IntChoixCategorie
from int_local_machine import IntLocalMachine
from int_cabestan import IntCabestan
from int_appareil_gouverne import IntAppareilGouverne
from int_treuils import IntTreuils
# from capture import Capture
from int_sauvegarder import SignatureApp
from int_recap_intervention import IntRecapInter
from int_capture import IntCapture

from android.permissions import request_permissions, Permission
from android.storage import primary_external_storage_path


class MyApp(App):
    """ 
    Classe principale de l'application
    """
    def build(self):
        """ 
        Création des différents écrans et répertoires de l'application
        Gestion des permissions de l'application
        """
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.CAMERA])
        Builder.load_file('style.kv')

        os.makedirs('./media/', exist_ok=True)
        os.makedirs('./signatures/', exist_ok=True)
        os.makedirs('./build/', exist_ok=True)
        os.makedirs('./data/', exist_ok=True)
        os.makedirs('./users', exist_ok=True)

        # Gestionnaire d'écrans
        sm = ScreenManager()

        sm.add_widget(Connexion(name='connexion'))
        sm.add_widget(NewUser(name='new_user'))
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(MainMenuDev(name='main_menu_dev'))
        sm.add_widget(MainMenuInt(name='main_menu_int'))
        sm.add_widget(CaracAffaire(name='carac_affaire'))
        # sm.add_widget(Capture(name='capture'))

        sm.add_widget(SupprimerAffaire(name='supp_affaire'))

        sm.add_widget(ModifAffaire(name='modif_affaire'))
        sm.add_widget(ModifCaracAffaire(name='modif_carac_affaire'))
        sm.add_widget(ModifChoixCategorie(name='modif_choix_categorie'))
        sm.add_widget(ModifAppareilGouverne(name='modif_appareil_gouverne'))
        sm.add_widget(ModifCabestan(name='modif_cabestan'))
        sm.add_widget(ModifLocalMachine(name='modif_local_machine'))
        sm.add_widget(ModifTreuils(name='modif_treuils'))
        sm.add_widget(ModifClosure(name='modif_closure'))

        sm.add_widget(IntCaracAffaire(name="int_carac_affaire"))
        sm.add_widget(IntChoixCategorie(name='int_choix_categorie'))
        sm.add_widget(IntLocalMachine(name='int_local_machine'))
        sm.add_widget(IntCabestan(name='int_cabestan'))
        sm.add_widget(IntAppareilGouverne(name='int_appareil_gouverne'))
        sm.add_widget(IntTreuils(name='int_treuils'))
        sm.add_widget(IntCapture(name='int_capture'))

        sm.add_widget(ChoixCategorie(name='choix_categorie'))
        sm.add_widget(LocalMachine(name='local_machine'))
        sm.add_widget(Treuils(name='treuils'))
        sm.add_widget(Cabestan(name='cabestan'))
        sm.add_widget(AppareilGouverne(name='appareil_gouverne'))
        sm.add_widget(Closure(name='closure'))

        sm.add_widget(IntRecapInter(name='int_recap_intervention'))
        sm.add_widget(SignatureApp(name='int_sauvegarder'))

        return sm
    
if __name__ == '__main__':
    MyApp().run()
