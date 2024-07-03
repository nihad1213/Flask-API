from flask import Blueprint, jsonify, request
from models.AmenityModel import Amenity, db
import uuid
from datetime import datetime

amenityRoutes = Blueprint('amenity_routes', __name__)

# Utility function to convert Amenity object to dictionary
def amenityToDict(amenity):
    return {
        'id': amenity.id,
        'name': amenity.name,
        'created_at': amenity.created_at,
        'updated_at': amenity.updated_at
    }

# Create a new amenity
@amenityRoutes.route('/amenities', methods=['POST'])
def addAmenity():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Amenity name is required'}), 400
    
    # Check if amenity with the same name already exists
    existing_amenity = Amenity.query.filter_by(name=name).first()
    if existing_amenity:
        return jsonify({'error': 'Amenity with this name already exists'}), 409
    
    amenity = Amenity(id=str(uuid.uuid4()), name=name)
    db.session.add(amenity)
    db.session.commit()
    return jsonify(amenityToDict(amenity)), 201

# Retrieve all amenities
@amenityRoutes.route('/amenities', methods=['GET'])
def getAmenities():
    amenities = Amenity.query.all()
    return jsonify([amenityToDict(amenity) for amenity in amenities]), 200

# Retrieve a specific amenity by ID
@amenityRoutes.route('/amenities/<string:amenity_id>', methods=['GET'])
def getAmenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenityToDict(amenity)), 200

# Update an existing amenity
@amenityRoutes.route('/amenities/<string:amenity_id>', methods=['PUT'])
def updateAmenity(amenity_id):
    data = request.json

    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Amenity name is required'}), 400
    
    # Check for duplicate name
    existing_amenity = Amenity.query.filter(Amenity.name == name, Amenity.id != amenity_id).first()
    if existing_amenity:
        return jsonify({'error': 'Amenity with this name already exists'}), 409
    
    amenity.name = name
    amenity.updated_at = datetime.now()
    db.session.commit()
    return jsonify(amenityToDict(amenity)), 200

# Delete an amenity
@amenityRoutes.route('/amenities/<string:amenity_id>', methods=['DELETE'])
def deleteAmenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    
    db.session.delete(amenity)
    db.session.commit()
    return '', 204