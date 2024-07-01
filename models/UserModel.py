#!/usr/bin/python3

"""Import BaseModel class"""
from models.BaseModel import BaseModel

class User(BaseModel):
    """Creating User Classs"""
    emails = set()  # Class-level attribute to store emails

    def __init__(self, email, password, first_name, last_name):
        if email in User.emails:
            raise ValueError("Email must be unique")
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        User.emails.add(email)
    
    def __str__(self):
        return f"User(email={self.email}, name={self.first_name} {self.last_name})"