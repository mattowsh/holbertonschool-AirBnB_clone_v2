#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """ Getter method """
            from models.city import City
            return [obj for obj in models.storage.all(City).values() if
                    obj.state_id == self.id]

    # if getenv("HBNB_TYPE_STORAGE") == "db":
    #     __tablename__ = "states"
    #     name = Column(String(128), nullable=False)
    #     cities = relationship("City", backref="state", cascade="delete")
    # else:
    #     name = ""

        # @property
        # def cities(self):
        #     from models.city import City
        #     from models import storage

        #     results = []
        #     for element in storage.all(City).values():
        #         if self.id == element.state_id:
        #             results.append(storage.all(City)[element])
        #     return results

        # @property
        # def cities(self):
        #     """ Getter method """
        #     from models.city import City
        #     return [obj for obj in models.storage.all(City).values() if
        #             obj.state_id == self.id]
