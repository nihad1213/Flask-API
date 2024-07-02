#!/usr/bin/python3
"""Importing Modules and Files"""
from db import db
from persistence.persistence import IPersistanceManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


class DataManager(IPersistanceManager):
    def __init__(self):
        pass

    def save(self, entity):
        try:
            db.session.add(entity)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def get(self, entityID, entityType):
        try:
            return db.session.query(entityType).get(entityID)
        except SQLAlchemyError as e:
            raise e

    def update(self, entity):
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def delete(self, entityID, entityType):
        try:
            entity = db.session.query(entityType).get(entityID)
            db.session.delete(entity)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e