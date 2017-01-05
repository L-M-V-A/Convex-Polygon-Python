"""
Point Test Module - Simple Unit Testing for the Point Class
"""

import unittest
from point import Point


class TestPoint(unittest.TestCase):
    """ TestCase Subclass to perform the testing """

    def test_point_creation(self):
        """ Testing Class Creation """
        self.assertRaises(ValueError, Point, 1, 2, 3)
        self.assertRaises(TypeError, Point, 'as', 1)
        self.assertRaises(TypeError, Point, 1, 'as')
        self.assertRaises(TypeError, Point, data=1)

    def test_coordinate(self):
        """ Testing Coordinates """
        self.assertEqual(Point(1, 2).get_coord(), (1, 2))

if __name__ == "__main__":
    unittest.main()
