#!/usr/bin/env python3
"""Auth class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns True if the path is not in the
        list of strings excluded_paths
        """
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            else:
                if excluded_path == path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header"""
        if request is None:
            return None

        if not request.headers.get('Authorization'):
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return None
