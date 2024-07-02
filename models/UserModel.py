# models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, db

class User(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, first_name, last_name, is_admin):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin

    def __str__(self):
        return f"User(email={self.email}, name={self.first_name} {self.last_name})"
