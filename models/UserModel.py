# models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, db

class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    passworda = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"User(email={self.email}, name={self.first_name} {self.last_name})"
