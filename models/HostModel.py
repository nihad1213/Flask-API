#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from models.BaseModel import BaseModel, db

class Host(BaseModel):
    __tablename__ = 'hosts'
    host_id = db.Column(db.String(60))

    def __init__(self):
        super().__init__()