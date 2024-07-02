#!/usr/bin/python3

"""Importing Modules and Models"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db

# Creating Flask App
app = Flask(__name__)

# app Config
                                        #service_name://username:password@servername/Databasename
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hbtn?unix_socket=/opt/lampp/var/mysql/mysql.sock'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Adding Models to Create Table
from models.CityModel import City

if __name__ == '__main__':
    # Creating Table
    with app.app_context():
        db.create_all()

    app.run(debug=True)
