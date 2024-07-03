#!/usr/bin/python3

"""Importing Modules and Models"""
from flask import Flask
from db import db
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager
import json

load_dotenv()

# Creating Flask App
app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a secure secret key
jwt = JWTManager(app)

# Database Config
DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER_NAME = os.getenv('DATABASE_USER_NAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE_TYPE}://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Adding Models to Create Table
from models.UserModel import User
from models.CountryModel import Country

# Importing Routes
from persistence.routes.user_route import userRoutes
from persistence.routes.country_route import countryRoutes
from persistence.routes.city_route import cityRoutes

# Registering blueprints
app.register_blueprint(userRoutes)
app.register_blueprint(countryRoutes)
app.register_blueprint(cityRoutes)


# Path to your JSON file containing country data
json_file = 'data/country_codes.json'


# Route for index
@app.route('/')
def index():
    return 'Index'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables based on models

    app.run(debug=True)
