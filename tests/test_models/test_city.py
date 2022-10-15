#!/usr/bin/python3
""" testing models for production"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ testing models for production"""

    def __init__(self, *args, **kwargs):
        """ testing models for production"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing models for production"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.name), str)
