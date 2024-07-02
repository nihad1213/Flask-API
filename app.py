#!/usr/bin/python3

"""Importing Modules and Models"""
from flask import Flask
from db import db
from dotenv import load_dotenv
import os

load_dotenv()

# Creating Flask App
app = Flask(__name__)

# Database Config
DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER_NAME = os.getenv('DATABASE_USER_NAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

                                        #service_name://username:password@servername/Databasename
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE_TYPE}://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Adding Models to Create Table
from models.CityModel import City

if __name__ == '__main__':
    # Creating Table
    with app.app_context():
        db.create_all()

    app.run(debug=True)
