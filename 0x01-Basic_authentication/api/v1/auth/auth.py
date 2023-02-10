#!/usr/bin/env python3
"""
Module to manage API authentication
"""

from flask import request
from typing import TypeVar, List


class Auth:
    """
    Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns true if a path requires authentication
        """
        if path is None:
            return (True)
        elif excluded_paths is None or excluded_paths == []:
            return (True)
        elif (path in excluded_paths) or ((path + '/') in excluded_paths):
            return (False)
        for i in excluded_paths:
            if i[-1] == "*":
                if path.startswith(i[:-1]):
                    return (False)
        else:
            return (True)

    def authorization_header(self, request=None) -> str:
        """
        Method that returns None
        """
        if request is None:
            return (None)
        header = request.headers.get('Authorization')
        if header is None:
            return (None)
        return (header)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that returns None
        """
        return (None)
