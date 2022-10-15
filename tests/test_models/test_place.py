#!/usr/bin/python3
"""testing models for production """
import unittest
from models.place import Place


class test_Place(unittest.TestCase):
    """testing models for production """

    def __init__(self, *args, **kwargs):
        """ test the init method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ testing models for production"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
