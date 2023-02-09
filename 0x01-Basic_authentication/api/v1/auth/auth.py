#!/usr/bin/env python3
"""
Module to manage API authentication
"""

from flask import request
from typing import TypeVar


class Auth():
    """
    Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """
        Method that returns false
        """
        if path is None:
            return (True)
        elif excluded_paths is None or excluded_paths == []:
            return (True)
        elif path in excluded_paths or path + '/' in excluded_paths:
            return (False)
        else:
            return (True)

    def authorization_header(self, request=None) -> TypeVar('User'):
        """
        Method that returns None
        """
        if request is None:
            return (None)
        

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that returns None
        """
        return (None)
