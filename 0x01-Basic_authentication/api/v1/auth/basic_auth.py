#!/usr/bin/env python3
"""
Module for BasicAuth
"""

from .auth import Auth
import base64
from typing import TypeVar, List
from models.user import User


class BasicAuth(Auth):
    """
    Class to implement basic authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str
                                            ) -> str:
        """
        Returns the Base64 part of the Authorization header 
        for a Basic Authentication
        """
        if authorization_header is None:
            return (None)
        if type(authorization_header) is not str:
            return (None)
        base64 = authorization_header[6:]
        if authorization_header[0:6] == "Basic ":
            return (base64)
        return (None)

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Returns decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return (None)
        if type(base64_authorization_header) == str:
            return (None)
        try:
            decoded = base64_authorization_header.decode('utf-8')
            return decoded
        except Exception:
            return None
        
    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str):
        """
        Returns user email and password from Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email = decoded_base64_authorization_header.split(":")[0]
        password = decoded_base64_authorization_header[len(email) + 1:]
        return (email, password)
    
    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Return a User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None
        
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance based on a received request
        """
        Auth_header = self.authorization_header(request)
        if Auth_header is not None:
            token = self.extract_base64_authorization_header(Auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, pword = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(email, pword)
        return