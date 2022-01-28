#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
import pep8
"""Unittests for the Rectangle Class
"""


class TestRectangle(unittest.TestCase):
    """Testing Rectangle methods"""

    def test_pep8_rectangle(self):
        """
        Test that models/rectanlge.py is pep8 compliant.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_rectangle(self):
        """
        Test that tests/test_models/test_rectangle.py is pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests docstrings functions
        """
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.width.__doc__) >= 1)
        self.assertTrue(len(Rectangle.height.__doc__) >= 1)
        self.assertTrue(len(Rectangle.x.__doc__) >= 1)
        self.assertTrue(len(Rectangle.y.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

    @classmethod
    def setUpClass(cls):
        """Sets __nb_object to 0 and creates objects to be tested"""
        Base.clear()
        cls.r1 = Rectangle(10, 5)
        cls.r2 = Rectangle(2, 2, 2, 2, -7)
        cls.r3 = Rectangle(7, 5, 6, 7, 8)
        cls.r4 = Rectangle(1, 1, 4, 2, 78)
        cls.r5 = Rectangle(4, 6, 2, 1, 12)
        cls.r6 = Rectangle(1, 1, 1, 1)
        cls.r7 = Rectangle(10, 2, 1, 9, 1)
        cls.r8 = Rectangle(10, 7, 2, 8)
        cls.r9 = Rectangle(2, 4)
        cls.r10 = Rectangle(3, 5, 1)
        cls.r12 = Rectangle(10, 7, 2, 8)
        cls.r13 = Rectangle(2, 4)

    @classmethod
    def tearDownClass(cls):
        """Deletes all the objects"""
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4
        del cls.r5
        del cls.r6
        del cls.r7
        del cls.r8
        del cls.r9
        del cls.r10
        del cls.r12
        del cls.r13

    def test_task_two(self):
        """basic id tests"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, -7)

        with self.assertRaises(TypeError):
            r3 = Rectangle("hello", 4)
            r4 = Rectangle(4, "hello")
            r5 = Rectangle(10, 10, 5.5, 6)
            r6 = Rectangle(64, 85, 3, True)

        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 5)
            r8 = Rectangle(7, 0)
            r9 = Rectangle(9, -4)
            r10 = Rectangle(-5, 6)
            r11 = Rectangle(1, 2, -6, 7)
            r12 = Rectangle(3, 4, 7, -6)

    def test_area(self):
        """tests the area"""
        self.assertEqual(self.r3.area(), 35)
