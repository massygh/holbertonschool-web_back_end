#!/usr/bin/env python3
"""
SessionAuth module for session-based authentication.
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class for handling session authentication. (Empty for now)
    Inherits from Auth.
    """
    # Attribut de classe pour stocker les sessions
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Crée un identifiant de session pour un user_id donné.
        Retourne None si user_id est invalide.
        Sinon, retourne le session_id (str) et l'enregistre dans le dict.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retourne le user_id associé à un session_id donné.
        Retourne None si session_id est None ou n'est pas une chaîne.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Retourne l'utilisateur courant basé sur le cookie de session dans la requête.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
