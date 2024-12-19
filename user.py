import hashlib
import json
import os

class User:
    """ 
    Classe pour représenter un utilisateur
    """
    def __init__(self, user_id, password, role, is_new=True):
        """
        Variables d'instance:
        user_id: Identifiant de l'utilisateur
        password: Mot de passe de l'utilisateur
        role: Rôle de l'utilisateur
        is_new: Indique si l'utilisateur est nouveau ou non
        """
        self.user_id = user_id
        if is_new:
            self.password = self.hash_password(password)
        else:
            self.password = password 
        self.role = role

    def hash_password(self, password):
        """
        Crypte le mot de passe en utilisant l'algorithme SHA-256
        Args:
          password: mot de passe à crypter

        Returns:
            mot de passe crypté
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, input_password):
        """ 
        Vérifie si le mot de passe entré correspond au mot de passe de l'utilisateur
        Args:
          input_password: mot de passe entré par l'utilisateur

        Returns:
            True si les mots de passe correspondent, False sinon
        """
        return self.password == self.hash_password(input_password)  





class UserManager:
    """ 
    Classe de gestion des utilisateurs
    """
    def __init__(self, storage_file='./users/users.json'):
        self.storage_file = storage_file
        os.makedirs(os.path.dirname(self.storage_file), exist_ok=True)
        self.load_users()

    def load_users(self):
        """ 
        Permet de charger les utilisateurs à partir du fichier de stockage
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                users_data = json.load(f)
                self.users = {u['user_id']: User(u['user_id'], u['password'], u['role'], is_new=False) for u in users_data}
        else:
            self.users = {}
            with open(self.storage_file, 'w') as f:
                json.dump([], f)

    def save_users(self):
        """ 
        Enregistre les utilisateurs dans le fichier de stockage
        """
        with open(self.storage_file, 'w') as f:
            json.dump([{'user_id': u.user_id, 'password': u.password, 'role': u.role} for u in self.users.values()], f, indent=4)

    def add_user(self, user_id, password, role, code=None):
        """
        Ajoute un utilisateur
        Args:
          user_id: identifiant de l'utilisateur
          password: mot de passe de l'utilisateur
          role: rôle de l'utilisateur
          code: code associé au rôle (Default value = None)

        Returns:
            None
        """
        role_codes = {
        'BE': '?WVBX7sy',
        'Technicien': 'e4Zz#{R2',
        'Developpeur': 'T-k3bP5Y',
        'Visiteur': ''
        }
        if role not in role_codes:
            return False, f"Rôle '{role}' non reconnu."
        
        if code != role_codes[role]:
            return False, f"Code d'autorisation incorrect pour le rôle {role}."
        
        self.users[user_id] = User(user_id, password, role, is_new=True)
        self.save_users()

        return True, "Utilisateur validé"

    def authenticate(self, user_id, input_password):
        """
        Authentifie un utilisateur
        Args:
          user_id: identifiant de l'utilisateur
          input_password: mot de passe entré par l'utilisateur

        Returns:
            l'utilisateur authentifié ou None
        """
        user = self.users.get(user_id)
        if user and user.check_password(input_password):
            return user
        return None
    

