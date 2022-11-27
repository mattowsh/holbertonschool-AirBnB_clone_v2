#!/usr/bin/python3
""" New DB Storage engine - SQLAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.user import User
from models.base_model import BaseModel, Base
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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects in the current database session"""
        our_classes = {"User": User, "State": State, "City": City,
                       "Amenity": Amenity, "Place": Place, "Review": Review}
        result = {}

        if cls is None:
            for cl in our_classes.values():
                for obj in self.__session.query(cl).all():
                    result[type(obj).__name__ + "." + obj.id] = obj
        else:
            for obj in self.__session.query(our_classes[cls]).all():
                result[type(obj).__name__ + "." + obj.id] = obj

        return result

    def new(self, obj):
        """Adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits and save the new object to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object to the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database create the current database
        session (self.__session) from the engine (self.__engine) by using
        a sessionmaker"""
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        # We use scoped_session for thread safety: make sure your Session
        # is thread-safe:
        Session = scoped_session(new_session)
        self.__session = Session

    def close(self):
        """To close our current database session"""
        self.__session.close()
