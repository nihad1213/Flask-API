#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from models.BaseModel import BaseModel
from datetime import datetime
from db import db

class Review(BaseModel):
    __tablename__ = 'reviews'

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(60), db.ForeignKey('places.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, place_id={self.place_id}, rating={self.rating})"
