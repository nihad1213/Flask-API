from flask import Blueprint, jsonify, request
from models.UserModel import db, User
from flask_bcrypt import check_password_hash
from datetime import datetime
from flask_jwt_extended import create_access_token

userRoutes = Blueprint('user_routes', __name__)

def userToDict(user):
    return {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_admin': user.is_admin,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    }

@userRoutes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([userToDict(user) for user in users]), 200

@userRoutes.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email', None)
    password = data.get('password', None)

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

@userRoutes.route('/users', methods=['POST'])
def add_user():
    data = request.json

    # Validate input
    if not all(key in data for key in ['email', 'password', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing fields'}), 400

    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409

    # Create new user
    new_user_data = {
        'email': data['email'],
        'password': data['password'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'is_admin': data.get('is_admin', False)
    }

    new_user = User(**new_user_data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(userToDict(new_user)), 201

@userRoutes.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(userToDict(user)), 200

@userRoutes.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return '', 204

@userRoutes.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json

    if not all(key in data for key in ['email', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing fields'}), 400

    if data['email'] != user.email and User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409

    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.is_admin = data.get('is_admin', user.is_admin)  # Update isAdmin if provided

    # Update password if provided
    if 'password' in data:
        user.set_password(data['password'])

    user.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify(userToDict(user)), 200
