#!/usr/bin/env python3
"""
SessionAuth module for session-based authentication.
"""
from api.v1.auth.auth import Auth
import uuid


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
