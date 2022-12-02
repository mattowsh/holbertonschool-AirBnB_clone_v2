#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, \
                              delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """init state"""
        super().__init__(*args, **kwargs)

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            """cities"""
            from models import storage
            from models.city import City

            result = []
            for key in storage.all(City).values():
                if self.id == key.state_id:
                    result.append(storage.all(City)[key])
            return result

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
