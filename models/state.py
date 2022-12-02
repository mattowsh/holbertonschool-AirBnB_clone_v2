#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy.orm import relationship
        cities = relationship("City", backref="state", cascade="all, delete")

    else:

        @property
        def cities(self):
            from models.__init__ import storage
            from models.city import City

            result = []
            for element in storage.all(City).values():
                if element.state_id == self.id:
                    result.append(element)
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
