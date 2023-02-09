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

    def __init__(self):
        """
        Method called during initialization
        """
        pass

    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """
        Method that returns false
        """
        return (False)

    def authorization_header(self, request=None) -> TypeVar('User'):
        """
        Method that returns None
        """
        return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that returns None
        """
        return (None)
