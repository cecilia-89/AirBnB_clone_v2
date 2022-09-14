#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.engine.db_storage import DBStorage


class test_db_storage(unittest.TestCase):
    """class to test database storage"""

    def test_create(self):
        """test create"""
        s1 = State(name="california")
        db = DBStorage()
        length = len(db.all(s1).keys())
