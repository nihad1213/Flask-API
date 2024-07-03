from flask import Blueprint, jsonify, request
from models.CityModel import City
from models.CountryModel import Country
from db import db
from datetime import datetime
import uuid

cityRoutes = Blueprint('city_routes', __name__)

# Utility function to convert City object to dictionary
def cityToDict(city):
    return {
        'id': str(city.id),  # Convert UUID to string
        'name': city.name,
        'country_code': city.country_code,
        'created_at': city.created_at.isoformat(),
        'updated_at': city.updated_at.isoformat() if city.updated_at else None
    }

# Get all cities
@cityRoutes.route('/cities', methods=['GET'])
def getCities():
    cities = City.query.all()
    return jsonify([cityToDict(city) for city in cities]), 200

# Add City
@cityRoutes.route('/cities', methods=['POST'])
def addCity():
    data = request.json
    country_code = data.get('country_code')

    # Check if country code exists
    country = Country.query.filter_by(code=country_code).first()
    if not country:
        return jsonify({"error": "Invalid country code"}), 400

    # Check if city already exists in this country
    existing_city = City.query.filter_by(name=data['name'], country_code=country_code).first()
    if existing_city:
        return jsonify({"error": "City already exists in this country"}), 409

    new_city = City(name=data['name'], country_id=country.id, country_code=country_code)
    db.session.add(new_city)
    db.session.commit()
    return jsonify(cityToDict(new_city)), 201

# Get City With Specific ID
@cityRoutes.route('/cities/<string:city_id>', methods=['GET'])
def getCity(city_id):
    city = City.query.get(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(cityToDict(city)), 200

# Delete City with Specific ID
@cityRoutes.route('/cities/<string:city_id>', methods=['DELETE'])
def deleteCity(city_id):
    city = City.query.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404
    db.session.delete(city)
    db.session.commit()
    return '', 204

# Update City with ID
@cityRoutes.route('/cities/<string:city_id>', methods=['PUT'])
def updateCity(city_id):
    data = request.json
    city = City.query.get(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    country_code = data.get('country_code')
    country = Country.query.filter_by(code=country_code).first()
    if not country:
        return jsonify({'error': 'Invalid country code'}), 400

    # Check if city already exists in this country
    existing_city = City.query.filter(City.id != city.id, City.name == data['name'], City.country_code == country_code).first()
    if existing_city:
        return jsonify({'error': 'City already exists in this country'}), 409

    city.name = data['name']
    city.country_id = country.id
    city.country_code = country_code
    city.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify(cityToDict(city)), 200

# Retrieve all cities belonging to a specific country
@cityRoutes.route('/countries/<string:country_code>/cities', methods=['GET'])
def getCitiesByCountry(country_code):
    country = Country.query.filter_by(code=country_code).first()
    if not country:
        return jsonify({'error': 'Country not found'}), 404

    cities = City.query.filter_by(country_code=country_code).all()
    return jsonify([cityToDict(city) for city in cities]), 200
