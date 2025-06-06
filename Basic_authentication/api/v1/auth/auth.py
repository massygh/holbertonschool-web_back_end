#!/usr/bin/env python3
""" Auth module for authentication management
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Template for all authentication system """

def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    """ Determines if authentication is required """
    if path is None or excluded_paths is None or excluded_paths == []:
        return True

    # Assurer que path finit par un slash pour comparaison slash-tolerant
    if not path.endswith('/'):
        path += '/'

    for excl_path in excluded_paths:
        if excl_path.endswith('*'):
            # Support futur pour wildcard (pas encore requis)
            if path.startswith(excl_path[:-1]):
                return False
        elif path == excl_path:
            return False
        
    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from a request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user from the request """
        return None
