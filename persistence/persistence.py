#!/usr/bin/python3
"""Importing File and Modules"""
from db import db
from abc import abstractmethod

class IPersistanceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entityId, entityType):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entityID, entityType):
        pass