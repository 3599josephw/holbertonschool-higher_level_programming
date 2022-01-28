#!/usr/bin/python3
from models.base import Base
import unittest
import pep8
"""Test for class base"""


class BaseTest(unittest.TestCase):
    """Test for class base"""

    @classmethod
    def setUpClass(cls):
        """Setting up class"""
        Base.clear()

        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(5)
        cls.b5 = Base(-5)
        cls.b6 = Base(42)
        cls.b7 = Base()
        cls.b8 = Base(None)

    @classmethod
    def tearDownClass(cls):
        """Tearing down class"""
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5
        del cls.b6
        del cls.b7
        del cls.b8

    def test_task1(self):
        """Test 1"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 5)
        self.assertEqual(self.b5.id, -5)
        self.assertEqual(self.b6.id, 42)
        self.assertEqual(self.b7.id, 4)
        self.assertEqual(self.b8.id, 5)

        with self.assertRaises(TypeError):
            b9 = Base(1, 1, 1)

    def test_task15(self):
        """Test 2"""

        my_dict = {'width': 10, 'height': 7, 'x': 2, 'y': 8, 'id': 1}
        json_dict = Base.to_json_string([my_dict])

        self.assertEqual(type(my_dict), dict)
        self.assertEqual(type(json_dict), str)
        self.assertEqual(my_dict, {'x': 2, 'width': 10, 'id': 1,
                                   'height': 7, 'y': 8})
        self.assertEqual(json_dict, '[{"width": 10, "height": 7, \
"x": 2, "y": 8, "id": 1}]')
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_task17(self):
        """Test 3"""

        json_str = '[{"width": 10, "height": 7, "x": 2, "y": 8, "id": 1}]'
        output = Base.from_json_string(json_str)
        self.assertEqual(output, [{"width": 10, "height": 7,
                                   "x": 2, "y": 8, "id": 1}])

    def test_pep8_base(self):
        """Test 4"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """Test 5"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test 6"""

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Test 7"""

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests docstrings functions"""

        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
