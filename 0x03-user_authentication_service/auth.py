#!/usr/bin/env python3
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt and return the salted hash as bytes."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
