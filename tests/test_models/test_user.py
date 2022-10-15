#!/usr/bin/python3
"""testing models for production """
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """testing models for production """

    def __init__(self, *args, **kwargs):
        """ test the testing models for production"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """testing models for production """
        new = self.value()
        self.assertEqual(type(new.password), str)
