"""Unittests for max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([100, -4, 5]), 100)
        self.assertEqual(max_integer([5, 7, 1]), 7)
        self.assertEqual(max_integer([-3 -4, -6]), -6)
        self.assertEqual(max_integer([100]), 100)