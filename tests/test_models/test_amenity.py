#!/usr/bin/python3
""" testing models for production"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """testing models for production"""

    def __init__(self, *args, **kwargs):
        """testing models for production"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """testing models for production"""
        new = self.value()
        self.assertEqual(type(new.name), str)
