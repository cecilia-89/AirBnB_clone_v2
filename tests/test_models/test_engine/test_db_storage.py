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


db = DBStorage()
s1 = State(name="california")


class test_db_storage(unittest.TestCase):
    """class to test database storage"""

    def test_create(self):
        """test create method of the db storage"""
        pass

    def test_delete(self):
        """test delete method of db storage"""
        pass

    def test_close(self):
        """test close method of the db storage"""
        pass

    def test_reload(self):
        """test reload method of the db storage"""
        pass

    def all(self):
        """test all method of the db storage"""
        pass