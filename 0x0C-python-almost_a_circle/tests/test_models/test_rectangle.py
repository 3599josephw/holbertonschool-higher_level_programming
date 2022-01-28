"""Unittests for the Rectangle Class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import pep8


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

    def test_pep8_test_base(self):
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
        """
        Tests for the Base class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    @classmethod
    def setUpClass(cls):
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
        self.assertEqual(self.r3.area(), 35)

    def test_display(self):
        self.assertEqual(self.r4.display(), None)

    def test_str(self):
        self.assertEqual(str(self.r5), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        self.r6.update(89)
        self.assertEqual(self.r6.id, 89)
        self.r6.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r6.width, 2)
        self.assertEqual(self.r6.height, 3)
        self.assertEqual(self.r6.x, 4)
        self.assertEqual(self.r6.y, 5)
        self.r6.update(width=10, height=9, x=8, y=7, id=11)
        self.assertEqual(self.r6.width, 10)
        self.assertEqual(self.r6.height, 9)
        self.assertEqual(self.r6.x, 8)
        self.assertEqual(self.r6.y, 7)
        self.assertEqual(self.r6.id, 11)

    def test_to_dictionary(self):
        r7_dict = self.r7.to_dictionary()
        self.assertEqual(r7_dict, {'x': 1, 'y': 9, 'id': 1,
                                   'height': 2, 'width': 10})
        self.assertEqual(type(r7_dict), dict)
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string(None), "[]")

    def test_save_to_file(self):
        Rectangle.save_to_file([self.r8, self.r9])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 4,\
 "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_create(self):
        r10_dict = self.r10.to_dictionary()
        r11 = Rectangle.create(**r10_dict)
        self.assertEqual(r11.id, 5)
        self.assertEqual(r11.width, 3)
        self.assertEqual(r11.height, 5)
        self.assertEqual(r11.x, 1)
        self.assertEqual(r11.y, 0)
        self.assertNotEqual(self.r10, r11)

    def test_load_from_file(self):
        list_rectangles_input = [self.r12, self.r13]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]),
                         '[Rectangle] (6) 2/8 - 10/7')
