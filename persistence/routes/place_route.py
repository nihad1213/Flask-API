from flask import Blueprint, jsonify, request
from models.PlaceModel import Place
from db import db
from models.AmenityModel import Amenity  # Adjust import as per your Amenity model

placeRoutes = Blueprint('place_routes', __name__)

# Utility function to convert Place object to dictionary
def place_to_dict(place):
    return {
        'id': place.id,
        'name': place.name,
        'description': place.description,
        'address': place.address,
        'city_id': place.city_id,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'host_id': place.host_id,
        'number_of_rooms': place.number_of_rooms,
        'number_of_bathrooms': place.number_of_bathrooms,
        'price_per_night': place.price_per_night,
        'max_guests': place.max_guests,
        'amenity_ids': place.amenity_ids.split(',') if place.amenity_ids else []
    }

def validate_uuids_exist(model, uuids):
    existing_uuids = model.query.filter(model.id.in_(uuids)).all()
    return len(existing_uuids) == len(uuids)

# Create a new place
@placeRoutes.route('/places', methods=['POST'])
def create_place():
    data = request.json
    required_fields = ['name', 'address', 'city_id', 'latitude', 'longitude', 'host_id',
                       'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']

    # Validate required fields
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    # Convert amenity_ids list to string
    amenity_ids = ','.join(data.get('amenity_ids', []))

    # Create a new Place object
    try:
        new_place = Place(
            name=data['name'],
            description=data.get('description'),
            address=data['address'],
            city_id=data['city_id'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            host_id=data['host_id'],
            number_of_rooms=data['number_of_rooms'],
            number_of_bathrooms=data['number_of_bathrooms'],
            price_per_night=data['price_per_night'],
            max_guests=data['max_guests'],
            amenity_ids=amenity_ids
        )

        db.session.add(new_place)
        db.session.commit()

        return jsonify({'message': 'Place created successfully', 'place': place_to_dict(new_place)}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error creating place', 'details': str(e)}), 500

# Retrieve all places
@placeRoutes.route('/places', methods=['GET'])
def get_all_places():
    places = Place.query.all()
    return jsonify([place_to_dict(place) for place in places]), 200

# Retrieve a specific place by ID
@placeRoutes.route('/places/<string:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place_to_dict(place)), 200

# Update an existing place
@placeRoutes.route('/places/<string:place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json

    place = Place.query.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)
    place.address = data.get('address', place.address)
    place.city_id = data.get('city_id', place.city_id)
    place.latitude = data.get('latitude', place.latitude)
    place.longitude = data.get('longitude', place.longitude)
    place.host_id = data.get('host_id', place.host_id)
    place.number_of_rooms = data.get('number_of_rooms', place.number_of_rooms)
    place.number_of_bathrooms = data.get('number_of_bathrooms', place.number_of_bathrooms)
    place.price_per_night = data.get('price_per_night', place.price_per_night)
    place.max_guests = data.get('max_guests', place.max_guests)

    amenity_ids = data.get('amenity_ids')
    if amenity_ids:
        if not validate_uuids_exist(Amenity, amenity_ids):
            return jsonify({'error': 'One or more amenity_ids are invalid'}), 400
        place.amenity_ids = ','.join(amenity_ids)

    db.session.commit()
    return jsonify(place_to_dict(place)), 200

# Delete a specific place
@placeRoutes.route('/places/<string:place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    db.session.delete(place)
    db.session.commit()
    return '', 204
