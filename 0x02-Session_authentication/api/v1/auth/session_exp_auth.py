#!/usr/bin/env python3
"""SessionExpAuth class"""
from datetime import datetime, timedelta
from .session_auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class with session expiration"""

    def __init__(self):
        """Initializes the SessionExpAuth instance"""
        super().__init__()

        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a session ID for a user_id with expiration"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID, considering expiration"""
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None

        if self.session_duration <= 0:
            return session_dict.get('user_id')

        created_at = session_dict.get('created_at')
        if created_at is None:
            return None

        if datetime.now() > created_at + timedelta(seconds=self.session_duration):
            return None

        return session_dict.get('user_id')
