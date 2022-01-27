"""Unittests for the Square Class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing Square methods"""

    @classmethod
    def setUpClass(cls):
        cls.r1 = Square(10)
        cls.r2 = Square(2, 2, 2, -7)

    @classmethod
    def tearDownClass(cls):
        del cls.r1
        del cls.r2

    def test_task_two(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, -7)

        with self.assertRaises(TypeError):
            r3 = Square("hello", 4)
            r4 = Square(4, "hello")
            r5 = Square(10, 10, 5.5)
            r6 = Square(64, 85, True)

        with self.assertRaises(ValueError):
            r7 = Square(0, 5)
            r8 = Square(7, -1)
            r9 = Square(9, -4)
            r10 = Square(-5, 6)
            r11 = Square(1, 2, -6)

    def test_area(self):
        r1 = Square(7, 5, 6, 7)
        self.assertEqual(r1.area(), 49)

    def test_display(self):
        r1 = Square(1, 1, 4, 78)
        self.assertEqual(r1.display(), None)

    def test_str(self):
        r1 = Square(4, 6, 2, 12)
        self.assertEqual(str(r1), "[Square] (12) 6/2 - 4")

    def test_update(self):
        r1 = Square(1, 1, 1, 1)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        r1.update(size=10, x=8, y=7, id=11)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 7)
        self.assertEqual(r1.id, 11)

    def test_to_dictionary(self):
        r1 = Square(2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 1, 'y': 9, 'id': 1,
                                   'size': 2})
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string(None), "[]")

    def test_save_to_file(self):
        r1 = Square(10, 7, 2)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 7, "size": 10, "x": 7, "y": 2}, {"id": 8,\
 "size": 2, "x": 0, "y": 0}]')

    def test_create(self):
        r1 = Square(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.size, 3)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 1)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_Squares_input = [r1, r2]
        Square.save_to_file(list_Squares_input)
        list_Squares_output = Square.load_from_file()
        self.assertEqual(str(list_Squares_output[0]),
                         '[Square] (8) 7/2 - 10')
