#!/usr/bin/env python3
"""Auth class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return None
