#!/usr/bin/env python3
""" BasicAuth module """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic Authentication class """

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a Base64-encoded authorization header
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extract user email and password from Base64 decoded value
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ':' not in decoded_base64_authorization_header):
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users or users == []:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None  # Pas d'Authorization -> accès refusé (API doit renvoyer 401 ou 403 selon config)

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None  # Format Basic mal formé -> 403 Forbidden

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None  # Impossible de décoder -> 403 Forbidden

        email, password = self.extract_user_credentials(decoded_auth)
        if email is None or password is None:
            return None  # Pas de credentials valides -> 403 Forbidden

        user = self.user_object_from_credentials(email, password)
        if user is None:
            return None  # Utilisateur non trouvé ou mauvais mot de passe -> 403 Forbidden

        return user  # Auth OK -> 200
