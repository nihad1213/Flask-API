#!/usr/bin/python3

"""Importing Models and libraries"""
from persistence.persistence import IPersistanceManager
from models.BaseModel import dataBase

class DataManager(IPersistanceManager):
    def __init__(self):
        # Store Entities. SQLAlchemy do that
        pass
    
    # Save Entity entity can be City, Country ...
    def save(self, entity):
        dataBase.session.add(entity)
        dataBase.session.commit()
    
    # Get Entities
    def get(self, entityID, entityType):
        model_class = self._get_model_class(entityType)
        return dataBase.session.query(model_class).get(entityID)
    
    # Upadte Entities
    def update(self, entity):
        dataBase.session.commit()
    
    # Delete Entities
    def delete(self, entityID, entityType):
        model_class = self._get_model_class(entityType)
        entity = dataBase.session.query(model_class).get(entityID)
        if entity:
            dataBase.session.delete(entity)
            dataBase.session.commit()
        else:
            raise ValueError(f"{entityID} and {entityType} doesn't exist")
    
    def getModelClass(self, entityType):
        if entityType == "Amenity":
            from models.AmenityModel import Amenity
            return Amenity
        elif entityType == "City":
            from models.CityModel import City
            return City
        elif entityType == "Country":
            from models.CountryModel import Country
            return Country
        elif entityType == "Place":
            from models.PlaceModel import Place
            return Place
        elif entityType == "Review":
            from models.ReviewModel import Review
            return Review
        elif entityType == "User":
            from models.UserModel import User
            return User
        else:
            raise ValueError(f"Unknown entity type: {entityType}")