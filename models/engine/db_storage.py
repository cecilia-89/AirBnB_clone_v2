#!/usr/bin/python3
"""A database storage engine"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session, Session

all_classes = {'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review, 'Place': Place, 'User': User}


class DBStorage:
    """DBStorage of the AirBnB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialises the SQLAlchemy engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop tables if the environment is test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method that queries all objects by class
        Returns: dictionary(<class_name>.<id>: <obj>)
        """
        obj_dict = {}

        if cls:
            # query all objects on the current database session
            for row in self.__session.query(cls).all():
                # populate the dict with objects from storage
                obj_dict.update({'{}.{}'.format
                                (type(row).__name__, row.id,): row})
        else:
            # query all types of objects
            for key, val in all_classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.format
                                    (type(row).__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current session if obj not None"""
        if obj:
            # if an object is provided, determine class from obj
            cls_name = all_classes[type(obj).__name]

            # query class table and delete
            self.__session.query(cls_name) \
                .filter(cls_name.id == obj.id).delete()

    def reload(self):
        """Creates the database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        # allows session to be reused
        self.__session = scoped_session(session)

    def close(self):
        """Closes scoped session"""
        self.__session.remove()
