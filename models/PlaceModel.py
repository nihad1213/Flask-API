from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel
from db import db

# Association table definition for many-to-many relationship
place_amenities = Table('place_amenities', db.Model.metadata,
    Column('place_id', String(256), ForeignKey('places.id')),
    Column('amenity_id', String(256), ForeignKey('amenities.id'))
)

class Place(BaseModel, db.Model):
    __tablename__ = 'places'
    
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(255), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    host_id = Column(String(60), nullable=False)
    number_of_rooms = Column(Integer, nullable=False)
    number_of_bathrooms = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    max_guests = Column(Integer, nullable=False)
    amenity_ids = Column(String(255), nullable=True)

    # Relationship to amenities via the association table
    amenities = relationship("Amenity", secondary=place_amenities, backref="places")

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
