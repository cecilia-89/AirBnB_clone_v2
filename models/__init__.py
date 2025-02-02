#!/usr/bin/python3
"""This module creates a unique storage instance for the project"""
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "State": State, "City": City,
               "User": User, "Place": Place,
               "Review": Review, "Amenity": Amenity}

# check environ var to determine storage method
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:  # file storage selected
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
