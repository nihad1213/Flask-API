#!/usr/bin/python3

from models.BaseModel import BaseModel, db

class Place(BaseModel):
    __tablename__ = 'places'
    
    place_id = db.Column(db.String(60))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(255), nullable=False)
    city_id = db.Column(db.String(60))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(60))
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    amenity_ids = db.Column(db.String(255), nullable=True)

    def __init__(self, name, description, address, city_id, latitude, longitude, host_id,
                 number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids

    def __str__(self):
        return f"Place(name={self.name}, address={self.address}, city_id={self.city_id})"