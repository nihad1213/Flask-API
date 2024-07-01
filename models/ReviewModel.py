#!/usr/bin/python3

from models.BaseModel import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = None
        self.updated_at = None

    def __str__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, place_id={self.place_id}, rating={self.rating})"

    def validate_rating(self):
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5")