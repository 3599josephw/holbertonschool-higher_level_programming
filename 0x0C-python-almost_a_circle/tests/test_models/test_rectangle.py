#!/usr/bin/python3
from models.rectangle import Rectangle
from models.base import Base

import unittest
import pep8
"""Test for class rectangle"""


class RectangleTest(unittest.TestCase):
    """Test for class rectangle"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""

        Base.clear()

        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)
        cls.r4 = Rectangle(10, 2, 0, 0, -12)
        cls.r5 = Rectangle(3, 2)
        cls.r6 = Rectangle(1, 1)
        cls.r7 = Rectangle(4, 6, 2, 1, 12)
        cls.r8 = Rectangle(2, 3, 2, 2)
        cls.r9 = Rectangle(10, 10, 10, 10)
        cls.r10 = Rectangle(10, 10, 10, 10)
        cls.r11 = Rectangle(10, 2, 1, 9, 1)
        cls.r12 = Rectangle(10, 7, 2, 8)
        cls.r13 = Rectangle(2, 4)
        cls.r14 = Rectangle(10, 7, 2, 8)
        cls.r15 = Rectangle(2, 4)

    @classmethod
    def tearDownClass(cls):
        """Tearing down class"""
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
        del cls.r11
        del cls.r12
        del cls.r13
        del cls.r14
        del cls.r15

    def test_task2(self):
        """"test 1"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r4.id, -12)

    def test_task3(self):
        """"test 2"""

        with self.assertRaises(TypeError):
            # width and height
            r1 = Rectangle(10, "hello")
            r2 = Rectangle("hello", 10)
            r4 = Rectangle(10, None)
            r5 = Rectangle(None, 20)
            r5 = Rectangle(10, 10.5)
            r6 = Rectangle(10.5, 20)
            r5 = Rectangle(10, True)
            r6 = Rectangle(True, 20)
            r5 = Rectangle(10, float('Nan'))
            r6 = Rectangle(float('Nan'), 20)
            r5 = Rectangle(10, float('inf'))
            r6 = Rectangle(float('inf'), 20)
            # x and y

            r1 = Rectangle(10, 10, 10, "hello")
            r2 = Rectangle(10, 10, "hello", 10)
            r4 = Rectangle(10, 10, 10, None)
            r5 = Rectangle(10, 10, None, 20)
            r5 = Rectangle(10, 10, 10, 10.5)
            r6 = Rectangle(10, 10, 10.5, 20)
            r5 = Rectangle(10, 10, 10, True)
            r6 = Rectangle(10, 10, True, 20)
            r5 = Rectangle(10, 10, 10, float('Nan'))
            r6 = Rectangle(10, 10, float('Nan'), 20)
            r5 = Rectangle(10, 10, 10, float('inf'))
            r6 = Rectangle(10, 10, float('inf'), 20)

            r7 = Rectangle(1, 1, 1, 1, 1, 1, 1)

        with self.assertRaises(ValueError):
            # width and height
            r1 = Rectangle(10, -10)
            r2 = Rectangle(-10, 10)
            r3 = Rectangle(10, 0)
            r4 = Rectangle(0, 10)

            # x and y
            r1 = Rectangle(10, 10, 10, -10)
            r2 = Rectangle(10, 10, -10, 10)

    def test_task4(self):
        """"test 3"""

        self.assertEqual(self.r5.area(), 6)
        self.r5.width = 10
        self.assertEqual(self.r5.area(), 20)

    def test_task5(self):
        """"test 4"""

        self.assertEqual(self.r6.display(), None)

    def test_task6(self):
        """"test 5"""

        self.assertEqual(str(self.r7), "[Rectangle] (12) 2/1 - 4/6")

    def test_task7(self):
        """"test 6"""

        self.assertEqual(self.r8.display(), None)

    def test_task8(self):
        """"test 7"""

        self.r9.update(89)
        self.assertEqual(self.r9.id, 89)

        self.r9.update(89, 2)
        self.assertEqual(self.r9.id, 89)
        self.assertEqual(self.r9.width, 2)

        self.r9.update(89, 2, 3)
        self.assertEqual(self.r9.id, 89)
        self.assertEqual(self.r9.width, 2)
        self.assertEqual(self.r9.height, 3)

        self.r9.update(89, 2, 3, 4)
        self.assertEqual(self.r9.id, 89)
        self.assertEqual(self.r9.width, 2)
        self.assertEqual(self.r9.height, 3)
        self.assertEqual(self.r9.x, 4)

        self.r9.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r9.id, 89)
        self.assertEqual(self.r9.width, 2)
        self.assertEqual(self.r9.height, 3)
        self.assertEqual(self.r9.x, 4)
        self.assertEqual(self.r9.y, 5)

        self.r9 = Rectangle(10, 10)
        self.r9.update(89, 2, 3, 4)
        self.assertEqual(self.r9.id, 89)
        self.assertEqual(self.r9.width, 2)
        self.assertEqual(self.r9.height, 3)
        self.assertEqual(self.r9.x, 4)

    def test_task9(self):
        """"test 8"""

        self.r10.update(height=1)
        self.assertEqual(self.r10.height, 1)

        self.r10.update(width=1, x=2)
        self.assertEqual(self.r10.height, 1)
        self.assertEqual(self.r10.width, 1)
        self.assertEqual(self.r10.x, 2)

        self.r10.update(y=1, width=2, id=89, x=3)
        self.assertEqual(self.r10.height, 1)
        self.assertEqual(self.r10.width, 2)
        self.assertEqual(self.r10.x, 3)
        self.assertEqual(self.r10.y, 1)
        self.assertEqual(self.r10.id, 89)

        self.r10.update(3, 4, y=5, width=2, x=0)
        self.assertEqual(self.r10.height, 1)
        self.assertEqual(self.r10.width, 4)
        self.assertEqual(self.r10.x, 3)
        self.assertEqual(self.r10.y, 1)
        self.assertEqual(self.r10.id, 3)

    def test_task13(self):
        """"test 9"""

        r1_dict = self.r11.to_dictionary()
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(r1_dict, {'id': 1, 'width': 10, 'height': 2,
                                   'x': 1, 'y': 9})
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string(None), "[]")

    def test_task16(self):
        """"test 10"""

        Rectangle.save_to_file([self.r12, self.r13])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 8, \
"width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_task18(self):
        """"test 11"""

        my_dict = {'height': 5, 'width': 3, 'x': 8}
        rect = Rectangle.create(**my_dict)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)

    def test_task18(self):
        """"test 12"""

        list_rectangles_input = [self.r14, self.r15]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]),
                         '[Rectangle] (10) 2/8 - 10/7')

    def test_pep8_rect(self):
        """"test 13"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_rect(self):
        """"test 14"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """"test 15"""

        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """"test 16"""

        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests docstrings functions"""

        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.width.__doc__) >= 1)
        self.assertTrue(len(Rectangle.height.__doc__) >= 1)
        self.assertTrue(len(Rectangle.x.__doc__) >= 1)
        self.assertTrue(len(Rectangle.y.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
