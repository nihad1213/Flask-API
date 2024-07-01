#!/usr/bin/python3

"""Importing Libraries and Modules"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.BaseModel import dataBase
from persistence.routes.country_routes import countryRoutes

# Creating Flask App
app = Flask(__name__)
app.register_blueprint(countryRoutes)

# Configuration for MySQL
DB_URI = "mysql://root:''@localhost/hbtn" # dbusername:'dbpassword'@servername/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Improve performace. Doesnt show warnings. Using: (Optinal)

# Setting Up Database 
dataBase = SQLAlchemy(app)

# Basic Route send us to welcome page
@app.route('/')
def welcome():
    return "Sagopa Kajmer"

if __name__ == "__main__":
    # Used to create an application context
    with app.app_context():
        # Create all tables if they do not exist
        dataBase.create_all()
    
    # Run the Flask application
    app.run(debug=True)
