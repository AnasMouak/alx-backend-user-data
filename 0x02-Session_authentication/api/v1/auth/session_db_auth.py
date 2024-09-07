#!/usr/bin/env python3
"""SessionDBAuth class"""
from datetime import datetime
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from models.user import User
from sqlalchemy.exc import NoResultFound


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class with database session management"""

    def create_session(self, user_id=None):
        """Creates a new session and stores it in the database"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        try:
            user_session = UserSession(session_id=session_id, user_id=user_id, created_at=datetime.now())
            user_session.save()
        except Exception:
            return None
        
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID by querying the database"""
        if session_id is None:
            return None

        try:
            user_session = UserSession.query.filter_by(session_id=session_id).one()
        except NoResultFound:
            return None

        if self.session_duration > 0:
            if datetime.now() > user_session.created_at + timedelta(seconds=self.session_duration):
                return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """Destroys a UserSession based on the Session ID from the request cookie"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        try:
            user_session = UserSession.query.filter_by(session_id=session_id).one()
            user_session.delete()
            user_session.save()
        except NoResultFound:
            return False
        except Exception:
            return False

        return True
