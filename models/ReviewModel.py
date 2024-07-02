#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.BaseModel import BaseModel, db

class Review(BaseModel):
    __tablename__ = 'reviews'

    review_id = db.Column(db.String(60))
    user_id = db.Column(db.String(60))
    place_id = db.Column(db.String(60))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)


    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, place_id={self.place_id}, rating={self.rating})"

    def validate_rating(self):
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

