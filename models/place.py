#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy.orm import relationship
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")

    else:

        @property
        def reviews(self):
            from models.__init__ import storage
            from models.review import Review

            reviews_list = []
            for key, val in storage.all(Review).items():
                if val["place_id"] == self.id:
                    reviews_list.append(val)
            return reviews_list
