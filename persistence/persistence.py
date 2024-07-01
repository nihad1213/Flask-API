#!/usr/bin/python3


from abc import ABC, abstractmethod

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