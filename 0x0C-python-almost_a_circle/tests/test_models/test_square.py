#!/usr/bin/python3
from models.square import Square
from models.base import Base
import unittest
import pep8
"""Test for class Square"""


class SquareTest(unittest.TestCase):
    """Test for class Square"""

    @classmethod
    def setUpClass(cls):
        """setting up class"""

        Base.clear()

        cls.s1 = Square(10)
        cls.s2 = Square(2, 10)
        cls.s3 = Square(10, 2, 10, 20)
        cls.s4 = Square(10, 2, 10, -10)

    @classmethod
    def tearDownClass(cls):
        """Tearing down class"""

        del cls.s1
        del cls.s2
        del cls.s3
        del cls.s4

    def test_task10(self):
        """test 1"""

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 20)
        self.assertEqual(self.s4.id, -10)

        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s4.y, 10)

        with self.assertRaises(TypeError):
            s5 = Square()
            r6 = Square(1, 1, 1, 1, 1, 1)

    def test_task3(self):
        """test 2"""

        with self.assertRaises(TypeError):
            # size
            s1 = Square("hello")
            s4 = Square(None)
            s5 = Square(10.5)
            s5 = Square(True)
            s5 = Square(float('Nan'))
            s5 = Square(float('inf'))
            # x and y

            s1 = Square(10, 10, "hello")
            s2 = Square(10, "hello", 10)
            s4 = Square(10, 10, None)
            s5 = Square(10, None, 20)
            s5 = Square(10, 10, 10.5)
            s6 = Square(10, 10.5, 20)
            s5 = Square(10, 10, True)
            s6 = Square(10, True, 20)
            s5 = Square(10, 10, float('Nan'))
            s6 = Square(10, float('Nan'), 20)
            s5 = Square(10, 10, float('inf'))
            s6 = Square(10, float('inf'), 20)

        with self.assertRaises(ValueError):
            # size
            s1 = Square(-10)
            s3 = Square(0)

            # x and y
            s1 = Square(10, -10, 10)
            s2 = Square(10, 10, -10)

    def test_task4(self):
        """test 3"""

        s7 = Square(3)
        self.assertEqual(s7.area(), 9)
        s7.size = 10
        self.assertEqual(s7.area(), 100)

    def test_task5(self):
        """test 4"""

        s8 = Square(1)
        self.assertEqual(s8.display(), None)

    def test_task6(self):
        """test 5"""

        s9 = Square(4, 2, 1, 12)
        self.assertEqual(str(s9), "[Square] (12) 2/1 - 4")

    def test_task7(self):
        """test 6"""

        s10 = Square(2, 2, 2)
        self.assertEqual(s10.display(), None)

    def test_task8(self):
        """test 7"""

        s11 = Square(10, 10, 10)

        s11.update(89)
        self.assertEqual(s11.id, 89)

        s11.update(89, 2)
        self.assertEqual(s11.id, 89)
        self.assertEqual(s11.size, 2)

        s11.update(89, 2, 3)
        self.assertEqual(s11.id, 89)
        self.assertEqual(s11.width, 2)
        self.assertEqual(s11.x, 3)

        s11.update(89, 2, 3, 4)
        self.assertEqual(s11.id, 89)
        self.assertEqual(s11.width, 2)
        self.assertEqual(s11.x, 3)
        self.assertEqual(s11.y, 4)

        s11 = Square(10)
        s11.update(89, 2, 4)
        self.assertEqual(s11.id, 89)
        self.assertEqual(s11.size, 2)
        self.assertEqual(s11.x, 4)

    def test_task9(self):
        """test 8"""

        s12 = Square(10, 10, 10)

        s12.update(size=1)
        self.assertEqual(s12.size, 1)

        s12.update(size=1, x=2)
        self.assertEqual(s12.size, 1)
        self.assertEqual(s12.x, 2)

        s12.update(y=1, size=2, id=89, x=3)
        self.assertEqual(s12.size, 2)
        self.assertEqual(s12.x, 3)
        self.assertEqual(s12.y, 1)
        self.assertEqual(s12.id, 89)

        s12.update(3, 4, y=5, size=2, x=0)
        self.assertEqual(s12.size, 4)
        self.assertEqual(s12.x, 3)
        self.assertEqual(s12.y, 1)
        self.assertEqual(s12.id, 3)

    def test_task13(self):
        """test 9"""

        s13 = Square(10, 1, 9, 1)
        s1_dict = s13.to_dictionary()
        self.assertEqual(type(s1_dict), dict)
        self.assertEqual(s1_dict, {'id': 1, 'size': 10,
                                   'x': 1, 'y': 9})
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string(None), "[]")

    def test_task16(self):
        """test 10"""

        s14 = Square(10, 2, 8)
        s15 = Square(2)
        Square.save_to_file([s14, s15])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 3, \
"size": 10, "x": 2, "y": 8}, \
{"id": 4, "size": 2, "x": 0, "y": 0}]')

    def test_task18(self):
        """test 11"""

        my_s_dict = {'size': 5, 'x': 8}
        rect = Square.create(**my_s_dict)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.size, 5)

    def test_task18(self):
        """test 12"""

        s16 = Square(10, 2, 8)
        s17 = Square(2)
        list_Squares_input = [s16, s17]

        Square.save_to_file(list_Squares_input)

        list_Squares_output = Square.load_from_file()
        self.assertEqual(str(list_Squares_output[0]),
                         '[Square] (5) 2/8 - 10')

    def test_pep8_sq(self):
        """test 13"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_sq(self):
        """test 14"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """test 15"""

        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """test 16"""

        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests docstrings functions"""

        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)
        self.assertTrue(len(Square.size.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
