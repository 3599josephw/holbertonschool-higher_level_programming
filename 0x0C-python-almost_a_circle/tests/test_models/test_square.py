"""Unittests for the Square Class
"""
import unittest
from models.square import Square
from models.base import Base
import pep8


class TestSquare(unittest.TestCase):
    """Testing Square methods"""

    def test_pep8_rectangle(self):
            """
            Test that models/square.py is pep8 compliant.
            """
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/square.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """
        Test that tests/test_models/test_square.py is pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests for the Base class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(10)
        cls.s2 = Square(2, 2, 2, -7)

    @classmethod
    def tearDownClass(cls):
        del cls.s1
        del cls.s2

    def test_task_two(self):
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, -7)

        with self.assertRaises(TypeError):
            s3 = Square("hello", 4)
            s4 = Square(4, "hello")
            s5 = Square(10, 10, 5.5)
            s6 = Square(64, 85, True)

        with self.assertRaises(ValueError):
            s7 = Square(0, 5)
            s8 = Square(7, -1)
            s9 = Square(9, -4)
            s10 = Square(-5, 6)
            s11 = Square(1, 2, -6)

    def test_area(self):
        s3 = Square(7, 5, 6, 7)
        self.assertEqual(s3.area(), 49)

    def test_display(self):
        s4 = Square(1, 1, 4, 78)
        self.assertEqual(s4.display(), None)

    def test_str(self):
        s5 = Square(4, 6, 2, 12)
        self.assertEqual(str(s5), "[Square] (12) 6/2 - 4")

    def test_update(self):
        s6 = Square(1, 1, 1, 1)
        s6.update(89)
        self.assertEqual(s6.id, 89)
        s6.update(89, 2, 3, 4)
        self.assertEqual(s6.size, 2)
        self.assertEqual(s6.x, 3)
        self.assertEqual(s6.y, 4)
        s6.update(size=10, x=8, y=7, id=11)
        self.assertEqual(s6.size, 10)
        self.assertEqual(s6.x, 8)
        self.assertEqual(s6.y, 7)
        self.assertEqual(s6.id, 11)

    def test_to_dictionary(self):
        s7 = Square(2, 1, 9, 1)
        s7_dict = s7.to_dictionary()
        self.assertEqual(s7_dict, {'x': 1, 'y': 9, 'id': 1,
                                   'size': 2})
        self.assertEqual(type(s7_dict), dict)
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string(None), "[]")

    def test_save_to_file(self):
        s8 = Square(10, 7, 2)
        s9 = Square(2)
        Square.save_to_file([s8, s9])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 7, "size": 10, "x": 7, "y": 2}, {"id": 8,\
 "size": 2, "x": 0, "y": 0}]')

    def test_create(self):
        s10 = Square(3, 5, 1)
        s10_dict = s10.to_dictionary()
        s11 = Square.create(**s10_dict)
        self.assertEqual(s11.id, 2)
        self.assertEqual(s11.size, 3)
        self.assertEqual(s11.x, 5)
        self.assertEqual(s11.y, 1)
        self.assertNotEqual(s10, s11)

    def test_load_from_file(self):
        s12 = Square(10, 7, 2, 8)
        s13 = Square(2, 4)
        list_Squares_input = [s12, s13]
        Square.save_to_file(list_Squares_input)
        list_Squares_output = Square.load_from_file()
        self.assertEqual(str(list_Squares_output[0]),
                         '[Square] (8) 7/2 - 10')
