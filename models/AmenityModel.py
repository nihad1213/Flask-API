#!/usr/bin/python3

"""Importing Models"""
from models.BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name={self.name}"