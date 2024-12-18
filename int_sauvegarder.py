from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from reportlab.pdfgen import canvas
from kivy.uix.popup import Popup
from datetime import datetime
import os
import shutil
from jnius import autoclass
import time

from writePDF import pdfWriter

Context = autoclass('android.content.Context')
Environment = autoclass('android.os.Environment')
current_activity = autoclass('org.kivy.android.PythonActivity').mActivity
app_storage_path = current_activity.getExternalFilesDir(None).getAbsolutePath()

directory = ""

# Widget de dessin pour la signature
class SignatureWidget(Widget):
    """ 
    Classe de création du widget de signature
    """
    def __init__(self, **kwargs):
        """
        Visuel du widget
        """
        super(SignatureWidget, self).__init__(**kwargs)
        self.line_width = 2
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Ajouter un contour noir à la zone de dessin
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Couleur noire pour les contours
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=1)

    def update_rect(self, *args):
        """
        Met à jour les contours lors des changements.

        Args:
          *args: arg de binding

        Returns:
            None
        """
        self.border.rectangle = (self.x, self.y, self.width, self.height)

    def on_touch_down(self, touch):
        """
        Prépare à dessiner lors de l'appui sur l'écran.
        Args:
          touch: 

        Returns:
            None
        """
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(0, 0, 0)  # Couleur noire pour le dessin
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        """
        Dessine lors du déplacement du doigt
        Args:
          touch: 

        Returns:

        """
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        """ 
        Efface la zone de dessin
        """
        self.canvas.clear()
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Recréer le contour noir après effacement
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=1)

    def save_as_image(self, filename):
        """
        Enregistre le contenu du widget dans un fichier PNG
        Args:
          filename: chemin du fichier enregistré

        Returns:
            None
        """
        # Étape 1 : Ajouter un fond blanc temporaire dans canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Couleur blanche pour le fond
            self.temp_background = Rectangle(pos=self.pos, size=self.size)

        # Étape 2 : Exporter l'image en PNG
        self.export_to_png(filename)
        # print(f"Image PNG sauvegardée : {filename}")

        # Étape 3 : Retirer le fond blanc temporaire
        self.canvas.before.remove(self.temp_background)


# Layout principal de l'application
class SignatureApp(Screen):
    """ 
    Classe du menu de signature pour les intervenants
    """
    def __init__(self, **kwargs):
        """
        Visuel du menu de signature
        """
        super(SignatureApp, self).__init__(**kwargs)

        self.media_path = os.path.join(app_storage_path, 'media')
        self.sign_path = os.path.join(app_storage_path, 'signatures')

        os.makedirs(self.sign_path, exist_ok=True)

        top_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        # GridLayout pour les deux zones de signature côte à côte
        grid_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.9))

        self.back_btn = Button(text="Retour", color=[1, 1, 1, 1], size_hint=(0.3, 0.2))
        self.back_btn.bind(on_press=self.go_to_int_recap_intervention)
        top_layout.add_widget(self.back_btn)

        # Signature 1
        self.signature1 = SignatureWidget()
        self.clear_button1 = Button(text="Effacer Signature Intervenant", size_hint=(1, 0.2), color=[1, 1, 1, 1])
        self.clear_button1.bind(on_press=self.clear_signature1)
        grid_layout.add_widget(self.signature1)

        # Signature 2
        self.signature2 = SignatureWidget()
        self.clear_button2 = Button(text="Effacer Signature Client", size_hint=(1, 0.2), color=[1, 1, 1, 1])
        self.clear_button2.bind(on_press=self.clear_signature2)
        grid_layout.add_widget(self.signature2)
        grid_layout.add_widget(self.clear_button1)
        grid_layout.add_widget(self.clear_button2)

        # Ajouter les zones de signature et les boutons "clear" dans le GridLayout
        grid_layout.add_widget(BoxLayout(orientation='vertical', spacing=5, children=[
            Label(text="Signature intervenant", size_hint=(1, 0.1)),
            self.signature1,
            self.clear_button1
        ]))
        grid_layout.add_widget(BoxLayout(orientation='vertical', spacing=5, children=[
            Label(text="Signature client", size_hint=(1, 0.1)),
            self.signature2,
            self.clear_button2
        ]))

        # Bouton pour enregistrer les signatures en PDF
        save_button = Button(text="Enregistrer les signatures dans le PDF", size_hint=(1, 0.2), color=[1, 1, 1, 1])
        save_button.bind(on_press=self.save_to_pdf)

        # Ajouter les widgets au layout principal
        top_layout.add_widget(grid_layout)
        top_layout.add_widget(save_button)
        self.add_widget(top_layout)

    def clear_signature1(self, instance):
        """
        Efface la signature de l'intervenant
        Args:
          instance: 

        Returns:

        """
        self.signature1.clear_canvas()

    def clear_signature2(self, instance):
        """
        Efface la signature du client
        Args:
          instance: 

        Returns:

        """
        self.signature2.clear_canvas()

    def save_to_pdf(self, instance):
        """
        Engeristre les signatures, valide et génère le PDF des intervenants
        Efface les signatures et les photos après enregistrement du pdf
        Args:
          instance: arg de binding

        Returns:
            None
        """
        # Enregistrer les images des signatures
        # os.makedirs("./signatures", exist_ok=True)
        # image1 = f"./signatures/signature_int.png"
        image1 = os.path.join(self.sign_path, 'signature_int.png')
        # image2 = f"./signatures/signature_client.png"
        image2 = os.path.join(self.sign_path, 'signature_client.png')

        self.signature1.save_as_image(image1)
        self.signature2.save_as_image(image2)

        # Créer un fichier PDF avec les signatures
        # pdf_filename = f"signatures_{timestamp}.pdf"
        # c = canvas.Canvas(pdf_filename)

        # Ajouter les signatures au PDF
        # c.drawString(100, 750, "Signature 1 :")
        # c.drawImage(image1, 100, 600, width=400, height=100)  # Position et taille de l'image

        # c.drawString(100, 450, "Signature 2 :")
        # c.drawImage(image2, 100, 300, width=400, height=100)  # Position et taille de l'image

        # c.save()
        # print(f"PDF généré avec succès : {pdf_filename}")

        # Effacer les signatures après sauvegarde
        self.clear_signature1(None)
        self.clear_signature2(None)
        # print("Signatures effacées après enregistrement.")

        pdf_writer = pdfWriter()
        pdf_writer.execute()

        # self.show_popup("PDF généré avec succès !")

        time.sleep(1)

        # if os.path.exists('./signatures'):
        if os.path.exists(self.sign_path):
            try:
                # shutil.rmtree('./signatures')
                shutil.rmtree(self.sign_path)
            except Exception as e:
                self.show_popup(f"Erreur lors de la suppression des signatures : {e}")
            # os.makedirs('./signatures', exist_ok=True)
            os.makedirs(self.sign_path, exist_ok=True)

        # if os.path.exists('./media'):
        if os.path.exists(self.media_path):
            try:
                # shutil.rmtree('./media')
                shutil.rmtree(self.media_path)
            except Exception as e:
                self.show_popup(f"Erreur lors de la suppression des photos : {e}")
            # os.makedirs('./media', exist_ok=True)
            os.makedirs(self.media_path, exist_ok=True)

        self.manager.current = 'main_menu_int'

    def go_to_int_recap_intervention(self, instance):
        """
        Retourne au récapitulatif de l'intervention pour les intervenants
        Args:
          instance: 

        Returns:

        """
        self.manager.current = 'int_recap_intervention'

    def show_popup(self, message):
        """ 
        Affiche un popup avec un message
        Args:
          message: texte à afficher

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
