#!/usr/bin/env python3
"""Auth class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path"""
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return None
