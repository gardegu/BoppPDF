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
from PIL import Image as PilImage  # Pillow pour le traitement d'images (si nécessaire)
from kivy.lang import Builder
import shutil
import json

from user import User, UserManager




class Connexion(Screen):
    """ 
    Classe de la page de connexion
    """
    def __init__(self, **kwargs):
        """
        Visuel de la page de connexion
        """
        super(Connexion, self).__init__(**kwargs)

        top_layout = BoxLayout(orientation='vertical', padding=[20,50,20,20], spacing=20)

        self.logo = Image(source="bopp.png", opacity=1)
        top_layout.add_widget(self.logo)

        scrollView = ScrollView(size_hint=(1,1))

        layout = GridLayout(cols=1, padding=[10,10], spacing=20, size_hint=(1,1))
        layout.bind(minimum_height=layout.setter('height'))

        # layout.add_widget(Label(text="Nom d'utilisateur :"))
        # self.user_id = TextInput(hint_text="Entrez votre identifiant", multiline=False)
        self.user_id = TextInput(hint_text="Entrez votre identifiant", multiline=False, size_hint=(1, None), height=100)
        layout.add_widget(self.user_id)

        # layout.add_widget(Label(text="Mot de passe :"))
        # self.user_mdp = TextInput(hint_text="Entrez votre mot de passe", multiline=False, password=True)
        self.user_mdp = TextInput(hint_text="Entrez votre mot de passe", password=True, multiline=False, size_hint=(1, None), height=100)
        layout.add_widget(self.user_mdp)

        self.show_password_btn = Button(text="Afficher", color=[1,1,1,1], size_hint=(0.3, None), height=100)
        self.show_password_btn.bind(on_press=self.toggle_password_visibility)
        layout.add_widget(self.show_password_btn)

        scrollView.add_widget(layout)
        top_layout.add_widget(scrollView)

        # self.connexion_btn = Button(text="Connexion", size_hint=(0.3, 0.2))
        self.connexion_btn = Button(text="Connexion", color=[1,1,1,1], size_hint=(1, None), height=100, pos_hint={'center_x':0.5})
        self.connexion_btn.bind(on_press=self.connect)
        top_layout.add_widget(self.connexion_btn)

        # self.new_user_btn = Button(text="Créer nouvel utilisateur", size_hint=(0.3, 0.2))
        self.new_user_btn = Button(text="Créer nouvel utilisateur", color=[1,1,1,1], size_hint=(1, None), height=100, pos_hint={'center_x':0.5})
        self.new_user_btn.bind(on_press=self.create_user)
        top_layout.add_widget(self.new_user_btn)

        # self.exit_btn = Button(text="Quitter", size_hint=(0.3, 0.2))
        self.exit_btn = Button(text="Quitter", color=[1,1,1,1], size_hint=(1, None), height=100, pos_hint={'center_x':0.5})
        self.exit_btn.bind(on_press=self.exit)
        top_layout.add_widget(self.exit_btn)
        
        self.add_widget(top_layout)

    def connect(self, instance):
        """
        Fonction de connexion pour les données rentrées
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        id = self.user_id.text
        pw = self.user_mdp.text

        user_manager = UserManager()
        user = user_manager.authenticate(id, pw)

        if user:
            # print(f"Connexion réussie pour {user.user_id} avec le rôle {user.role}.")
            self.show_popup("Connexion réussie", f"{user.user_id} avec le rôle {user.role}")
            if user.role == "BE":
                self.manager.current = 'main_menu'
            elif user.role == "Technicien":
                self.manager.current = "main_menu_int"
            elif user.role == "Developpeur":
                self.manager.current = "main_menu_dev"
            elif user.role == "Visiteur":
                # self.manager.current == "main_menu_dev"
                pass
        else:
            # print("Identifiant ou mot de passe incorrect.")
            self.show_popup("Erreur", "Identifiant ou mot de passe incorrect")

    def create_user(self, instance):
        """
        Passe à l'écran de création d'utilisateur
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        self.manager.current='new_user'

    def exit(self, instance):
        """
        Fonction pour quitter l'application
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        App.get_running_app().stop()

    def show_popup(self, title, message):
        """
        Affiche une popup avec un message
        Args:
          title: titre du popup
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

    def toggle_password_visibility(self, instance):
        """
        Masque ou affiche le mot de passe tapé par l'utilisateur
        Args:
          instance: argument nécessaire pour le binding de la fonction

        Returns:
            None
        """
        if self.user_mdp.password: 
            self.user_mdp.password = False
            self.show_password_btn.text = "Masquer"
        else:  
            self.user_mdp.password = True
            self.show_password_btn.text = "Afficher"