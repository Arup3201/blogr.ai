import json, traceback
from flask import Blueprint, request, make_response, jsonify

from api.service.auth import BlogrAuthenticator, GoogleAuthenticator

auth_app = Blueprint('auth', __name__)

def signup():
    payload = json.loads(request.data.decode('UTF-8'))    
    email = payload.pop("email")
    password = payload.pop("password")
    
    authenticator = BlogrAuthenticator()
    try:
        data = authenticator.signup(email, password)
        return make_response(jsonify({"data": data}))
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({"message": str(e)}), 400)

def google_signup():
    payload = json.loads(request.data.decode('UTF-8'))
    credential = payload.pop("credential")
    authenticator = GoogleAuthenticator()
    try:
        data = authenticator.signup(credential)
        return make_response(jsonify({"data": data}))
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({"message": str(e)}), 400)
        
def login():
    payload = json.loads(request.data.decode('UTF-8'))
    email = payload.pop("email")
    password = payload.pop("password")
    
    authenticator = BlogrAuthenticator()
    try:
        data = authenticator.login(email, password)
        return make_response(jsonify({"data": data}))
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({"message": str(e)}), 400)

def google_login():
    payload = json.loads(request.data.decode('UTF-8'))
    credential = payload.pop("credential")
    
    authenticator = GoogleAuthenticator()
    try:
        data = authenticator.login(credential)
        return make_response(jsonify({"data": data}))
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({"message": str(e)}), 400)

auth_app.add_url_rule('/signup', view_func=signup, methods=['POST'])
auth_app.add_url_rule('/google-signup', view_func=google_signup, methods=['POST'])
auth_app.add_url_rule('/login', view_func=login, methods=['POST'])
auth_app.add_url_rule('/login-google', view_func=google_login, methods=['POST'])