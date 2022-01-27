"""Unittests for the Base class
"""
from curses.textpad import rectangle
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """Testing Base methods"""
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(-1)
        self.assertEqual(b3.id, -1)
        b4 = Base(None)
        self.assertEqual(b4.id, 2)

    def test_to_json_string(self):
        test_dict = {'x': 2, 'y': 8, 'width': 10, 'height': 7}
        json_dict = Base.to_json_string([test_dict])
        self.assertEqual(type(json_dict), str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(json_dict, '[{"x": 2, "y": 8, "width": \
10, "height": 7}]')

    def test_from_json_string(self):
        json_string = '[{"x": 2, "y": 8, "width": 10, "height": 7}]'
        output = Base.from_json_string(json_string)
        self.assertEqual(output, [{"x": 2, "y": 8, "width": 10, "height": 7}])
