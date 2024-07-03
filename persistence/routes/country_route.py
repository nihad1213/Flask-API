#!/usr/bin/python3

from flask import Blueprint, jsonify
from models.CountryModel import Country, countryToDict
from db import db

countryRoutes = Blueprint('country_routes', __name__)

# Define routes
# Get list of all countries
@countryRoutes.route('/countries', methods=['GET'])
def getCountries():
    countries = Country.query.all()
    country_list = [countryToDict(country) for country in countries]
    return jsonify(country_list), 200

# Get country by country code
@countryRoutes.route('/countries/<string:countryCode>', methods=['GET'])
def getCountryWithCode(countryCode):
    country = Country.query.filter_by(code=countryCode).first()
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(countryToDict(country)), 200
