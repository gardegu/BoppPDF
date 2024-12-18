# Tester l'application

## Installer l'application
- l'apk (application compilée) est dans le dossier /bin
- autoriser l'appareil Android à installer des applications de sources inconnues
- la télécharger 
- **bien accorder les autorisations demandées**
- il est possible que l'application crash au premier lancement si les autorisations n'ont pas été accordées assez vite
- une fois les autorisations accordées, relancer l'application, elle devrait fonctionner

## Option de connexion

Avec cette version de l'application, si possible : 
- se connecter avec l'id : forceg
- le mot de passe : Forceg1* 

**Ne pas essayer de créer d'utilisateur avec le rôle BE/Technicien/Développeur avec cette version**
Il est en revanche possible de créer un utilisateur en visiteur.

## La génération de PDF
Lorsque l'on clique sur "générer un pdf", l'application va essayer de télécharger le pdf dans 3 endroits différents.
Il est possible que l'un des 3 téléchargement échoue (message d'erreur dans ce cas), mais au moins un devrait fonctionner.
Le message de confirmation peut être caché sous un message d'erreur car les notifications s'affichent par ordre anti-chronologique (dernier message généré >> affiché en premier).