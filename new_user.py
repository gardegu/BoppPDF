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
from kivy.core.window import Window
from PIL import Image as PilImage  
from kivy.lang import Builder
import shutil
import json
import re

from user import User, UserManager



class NewUser(Screen):
    """ 
    Classe de création d'un utilisateur
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu de création d'un nouvel utilisateur
        """
        super(NewUser, self).__init__(**kwargs)

        self.user_manager = UserManager()
         
        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=2, padding=20, spacing=20, size_hint=(1,1))

        self.back_btn = Button(text="Retour", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_connexion)
        top_layout.add_widget(self.back_btn)

        layout.add_widget(Label(text="Nom d'utilisateur :"))
        self.user_id = TextInput(hint_text="Choisir un identifiant")
        layout.add_widget(self.user_id)

        layout.add_widget(Label(text="Mot de passe :"))
        self.user_mdp = TextInput(hint_text="Choisir un mot de passe d'au moins 8 caractères avec au moins une Majuscule, une minuscule, un chiffre et un caractère spécial")
        layout.add_widget(self.user_mdp)

        layout.add_widget(Label(text="Rôle :"))
        self.role_spinner = Spinner(text='Choisir un rôle', color=[1,1,1,1], values=("BE", 'Technicien', 'Visiteur', 'Developpeur'))
        layout.add_widget(self.role_spinner)

        layout.add_widget(Label(text="Code de rôle : (vide si visiteur)"))
        self.role_code = TextInput(hint_text="Saisir code de rôle")
        layout.add_widget(self.role_code)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        self.create_account_btn = Button(text="Créer un compte", color=[1,1,1,1], size_hint=(0.3, 0.2))
        self.create_account_btn.bind(on_press=self.create_account)
        top_layout.add_widget(self.create_account_btn)

        self.add_widget(top_layout)

    def go_to_connexion(self, instance):
        """
        Revenir à l'écran de connexion
        Args:
          instance: 

        Returns:

        """
        self.manager.current='connexion'

    def create_account(self, instance):
        """
        Création d'un compte utilisateur
        Args:
          instance: arg de binding

        Returns:
          None
        """
        try:
          id = self.user_id.text
          pw = self.user_mdp.text
          role = self.role_spinner.text
          code = self.role_code.text #if (role == 'BE' or role == 'Technicien' or role == 'Developpeur') else None

          if not self.validate_password(pw):
              self.show_popup("Erreur : le mot de passe n'est pas assez fort (au moins 8 caractères, une Majuscule, une minuscule, un chiffre et un caractère spécial)")
              # return 
          
          if not self.validate_id(id):
              self.show_popup("Erreur : Cet identifiant existe déjà.")
              # return 
          
          try:
              create, err = self.user_manager.add_user(id, pw, role, code)
              if create == True:
                self.show_popup("Succès : compte créé avec succès!")
                self.go_to_main_menu(role)
              else:
                  self.show_popup(f"Erreur lors de la création du compte : {err}")
          except Exception as e:
              self.show_popup(f"Erreur : {e}")
        except Exception as e:
          self.show_popupf(f"Erreur : {e}")

    def validate_password(self, password):
        """
        Vérifie que le mot de passe est assez fort
        Args:
          password: 

        Returns:

        """
        return (len(password) >= 8 
                and  re.search(r"[A-Z]", password) 
                and re.search(r"[a-z]", password)
                and re.search(r"[0-9]", password)
                and re.search(r"[&~#{}()\-_@*.,?;/:!<>\|+=]", password))

    def validate_id(self, id):
        """
        Vérifie que l'identifiant est valide
        Args:
          id: 

        Returns:

        """
        user_manager = UserManager()
        user_manager.load_users()
        return (len(id) >= 4
                and id not in user_manager.users)

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

    def go_to_main_menu(self,role):
        """ 
        Passe à l'écran du menu principal
        """
        if role == "BE":
            self.manager.current = 'main_menu'
        elif role == "Technicien":
            self.manager.current = "main_menu_int"
        elif role == "Developpeur":
            self.manager.current = "main_menu_dev"
        elif role == "Visiteur":
            # self.manager.current == "main_menu_dev"
            pass
        