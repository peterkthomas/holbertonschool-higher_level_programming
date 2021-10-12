#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class for max_integer unit testing"""
    def test_empty_list(self):
        """Test for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_empty(self):
        """Test for empty call"""
        self.assertIsNone(max_integer())

    def test_one(self):
        """Test a list of one number"""
        self.assertEqual(max_integer([1]), 1)

    def test_all_negative(self):
        """Test for list with only negative ints"""
        self.assertEqual(max_integer([-30, -10, -50, -200, -4]), -4)

    def test_none(self):
        """Testing a none type argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_str_arg(self):
        """Testing a string as an argument"""
        string = [1, "BREAK", 3, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

    def test_max_beginning(self):
        """Test for max at beginning"""
        self.assertEqual(max_integer([100, 99, 98, 97, 96, 95]), 100)

    def test_max_middle(self):
        """Test for max in middle"""
        self.assertEqual(max_integer([100, 30, 480, 42, 12]), 480)

if __name__ == "__main__":
    unittest.main()
