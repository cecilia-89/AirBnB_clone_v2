#!/usr/bin/python3
"""testing models for production """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(unittest.TestCase):
    """testing models for production"""

    def __init__(self, *args, **kwargs):
        """testing models for production"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """testing models for production"""
        new = self.value()
        self.assertEqual(type(new.name), str)
