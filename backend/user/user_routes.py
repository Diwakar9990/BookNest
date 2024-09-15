from flask import Blueprint, jsonify, request
from flask_cors import CORS
from sqlalchemy.exc import OperationalError
from main import app, cors
import re 
from user.user_model import User
from user.user_schema import UserSchema
from flask_jwt_extended import (
    JWTManager, 
    jwt_required,
    get_jwt_identity, 
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies
)

jwt = JWTManager(app)
user_bp = Blueprint('user', __name__)
cors 
def is_valid_email(email):
    # Simple regex for validating an Email
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return email_regex.match(email) is not None

def is_valid_password(password):
    # Password validation criteria: min 8 characters, at least one letter and one number
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

#creating a new user
@user_bp.post('/register')
def register_user():
    userData = request.get_json()
    username = userData.get('username')
    userEmail = userData.get('email')
    password = userData.get('password')
    
    # Validate email
    if not is_valid_email(userEmail):
        return jsonify({
            "error": "Invalid email format"
        }), 400

    # Validate password
    if not is_valid_password(password):
        return jsonify({
            "error": "Password must be at least 8 characters long and include both letters and numbers"
        }), 400
    
    # Check if username already exists
    user = User.get_user_by_username(username=username)
    if user is not None:
        return jsonify({
            "error": "User already exists"
        }), 403
    
    # Check if email already exists
    user = User.query.filter_by(email=userEmail).first()
    if user is not None:
        return jsonify({
            "error": "Email already exists"
        }), 403
    # Create new user
    new_user = User(
        username=username,
        email=userEmail,
    )
    new_user.set_password(password=password)
    new_user.save()

    result = UserSchema().dump(new_user, many=False)
    resp = jsonify({
        "message": "User created successfully",
        "res": result,
    })
    return resp, 201

#logging an existing user
@user_bp.post('/login')
def login_user():
    data = request.get_json()
    user = User.get_user_by_username(username=data.get('username'))

    # check if username and password is valid or not
    if user and user.check_password(password=data.get('password')):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        resp = jsonify({'login': True})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        return resp, 200
    return jsonify({'error': 'Invalid username and password'}), 401

#admin login
@user_bp.post('/admin-login')
def admin_login():
    data = request.get_json()
    if data.get('username') != 'admin':
        return jsonify({'error': 'Invalid Credentials'}), 401
    user = User.get_user_by_username(username=data.get('username'))

    # check if username and password is valid or not
    if user and user.check_password(password=data.get('password')):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        resp = jsonify({'login': True})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        return resp, 200
    return jsonify({'error': 'Invalid username and password'}), 401

@user_bp.post('/logout')
def logout_user():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200

@user_bp.get('/protected')
@jwt_required()
def protected_user():
    username = get_jwt_identity()
    if username:
        return jsonify({'hello': 'from {}'.format(username)}), 200
    
@user_bp.get('/details')
@jwt_required()
def details():
    username = get_jwt_identity()
    user_details = User.query.filter(User.username == username).first()
    #complete this request
    if not user_details:
        return jsonify({'msg': 'User not found'}), 404

    result = UserSchema().dump(user_details)
    return jsonify({
        "msg": "User details fetched successfully",
        "res": result
    }), 200

