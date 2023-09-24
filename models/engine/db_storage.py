#!/usr/bi/python3
"""
Implementation of a  database storage engine.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """ Database storage engine for hbnb project."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes our objects."""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries on the current db session for all cls objects."""
        if not self.__session:
            self.reload()
        objects = {}
        if type(cls) == str:
            cls = classes.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def new(self, obj):
        """ Adds object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """ Commit all current changes of the current db session."""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current session if it is not None."""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads the db."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ Closes the current sqlalchemy session."""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieves the instance of a class object."""
        if cls is not None and type(cls) is str and id is not None and\
           type(id) is str and cls in classes:
            cls = classes[cls]
            result = self.__session.query(cls).filter(cls.id == id).first()
            return result
        else:
            return None

    def count(self, cls=None):
        """Counts the number of instances of an obj in storage."""
        total = 0
        if type(cls) == str and cls in classes:
            cls = classes[cls]
            total = self.__session.query(cls).count()
        elif cls is None:
            for cls in classes.values():
                total += self.__session.query(cls).count()
        return total
