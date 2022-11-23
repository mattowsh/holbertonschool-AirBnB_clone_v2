#!/usr/bin/python3
""" New DB Storage engine - SQLAlchemy """


from os import getenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from models.user import User
from models.base_model import BaseModel
from models.base_model import Base
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class DBStorage():
    """New Database"""
    __engine = None
    __session = None

    
    def __init__(self):
         """init method"""
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)


    def new(self, obj):
        """new method"""
        self.__session.add(obj)

    def save(self):
        """save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete method"""
        if obj == None:
            self.__session.delete(obj)
            self.save()
