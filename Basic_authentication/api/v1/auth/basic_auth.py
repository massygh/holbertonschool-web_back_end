#!/usr/bin/env python3
""" BasicAuth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth """
    def extract_base64_authorization_header(self, authorization: str) -> str:
        """ Extracts the Base64 part of the Authorization header """
        if authorization is None or not isinstance(authorization, str):
            return None
        if not authorization.startswith("Basic "):
            return None
        return authorization.split(" ")[1]