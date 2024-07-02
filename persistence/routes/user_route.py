from flask import Blueprint, jsonify, request
from models.UserModel import db, User
from datetime import datetime

userRoutes = Blueprint('user_routes', __name__)

# Convert Dictionary
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

# List All users
@userRoutes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([userToDict(user) for user in users]), 200

# Add user
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
    }
    if 'is_admin' in data:
        new_user_data['is_admin'] = data['is_admin']

    new_user = User(**new_user_data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(userToDict(new_user)), 201

# Get Specific User with ID
@userRoutes.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(userToDict(user)), 200

# Delete user with ID
@userRoutes.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return '', 204

# Update User with ID
@userRoutes.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json

    # Validate input
    if not all(key in data for key in ['email', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing fields'}), 400

    # Check if email already exists
    if data['email'] != user.email and User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409

    # Update user attributes
    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.password = data.get('password', user.password)  # Update password if provided
    if 'is_admin' in data:
        user.is_admin = data['is_admin']  # Update is_admin if provided
    user.updated_at = datetime.now()

    db.session.commit()
    return jsonify(userToDict(user)), 200
