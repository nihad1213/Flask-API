# routes/user_routes.py

from flask import Blueprint, jsonify, request
from models.UserModel import db, User
from datetime import datetime

userRoutes = Blueprint('user_routes', __name__)

def user_to_dict(user):
    return {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    }

@userRoutes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user_to_dict(user) for user in users]), 200

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
    new_user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_to_dict(new_user)), 201

@userRoutes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user_to_dict(user)), 200

@userRoutes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return '', 204

@userRoutes.route('/users/<int:user_id>', methods=['PUT'])
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

    # Update user
    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.password = data.get('password', user.password)  # Update password if provided
    user.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify(user_to_dict(user)), 200
