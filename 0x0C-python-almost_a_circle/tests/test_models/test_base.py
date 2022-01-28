#!/usr/bin/python3
import unittest
from models.base import Base
import pep8
"""Unittests for the Base class
"""


class TestBaseMethods(unittest.TestCase):
    """Testing Base methods"""

    def test_pep8_base(self):
        """
        Test that models/base.py is pep8 compliant.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """
        Test that tests/test_models/test_base.py is pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests docstrings functions
        """
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

    @classmethod
    def setUpClass(cls):
        """Sets __nb_object to 0 and creates objects to be tested"""
        Base.clear()
        cls.b1 = Base()
        cls.b2 = Base(12)
        cls.b3 = Base(-1)
        cls.b4 = Base(None)

    @classmethod
    def tearDownClass(cls):
        """Deletes the objects set up"""
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4

    def test_init(self):
        """checks base IDs"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, -1)
        self.assertEqual(self.b4.id, 2)

        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_to_json_string(self):
        """tests to_json_string function"""
        test_dict = {'x': 2, 'y': 8, 'width': 10, 'height': 7}
        json_dict = Base.to_json_string([test_dict])
        self.assertEqual(type(json_dict), str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(json_dict, '[{"x": 2, "y": 8, "width": \
10, "height": 7}]')

    def test_from_json_string(self):
        """Tests from_json_string function"""
        json_string = '[{"x": 2, "y": 8, "width": 10, "height": 7}]'
        output = Base.from_json_string(json_string)
        self.assertEqual(output, [{"x": 2, "y": 8, "width": 10, "height": 7}])

if __name__ == '__main__':
    unittest.main()