#!/usr/bin/env python3
"""Handles session authentication routes"""

from flask import jsonify, request, abort
from models.user import User
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """POST /auth_session/login to handle user login with session creation"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)

    session_name = getenv('SESSION_NAME')

    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)
    
    return response

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def auth_session_logout():
    """DELETE /auth_session/logout to handle user logout"""
    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
