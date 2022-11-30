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
                            cascade="all, delete-orphan")
    else:
        name = ""

        # @property
        # def cities(self):
        #     from models.city import City
        #     from models import storage

        #     results = []
        #     for element in storage.all(City).values():
        #         if self.id == element.state_id:
        #             results.append(storage.all(City)[element])
        #     return results

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            """cities"""
            from models import storage
            stacit = []
            for stat in storage.all(City).values():
                if self.id == city.state_id:
                    stacit.append(storage.all(City)[stat])
            return stacit
