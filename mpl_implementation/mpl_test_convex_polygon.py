"""
Convex/Polygon Test Module
"""

import unittest
from point import Point
from convex_polygon import Polygon, ConvexPolygon


class TestPolygon(unittest.TestCase):
    """ testcase subclass for base polygon testing """
    def test_polygon_creation(self):
        """ testing class creation """
        points = [Point(0, 0), Point(1, 0)]
        self.assertRaises(ValueError, Polygon, *points)

    def test_inside_methof(self):
        """ test class method """
        points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
        polygon = Polygon(*points)
        self.assertRaises(TypeError, polygon.inside, 1)
        self.assertFalse(polygon.inside(Point(3, 0)))
        self.assertTrue(polygon.inside(Point(0, 0)))
        self.assertTrue(polygon.inside(Point(1, 1)))


class TestConvexPolygon(unittest.TestCase):
    """ testcase subclass for convex polygon testing """

    def test_convex_creation(self):
        """ testing class creation"""
        points = [Point(0, 0), Point(2, 1), Point(0, 2)]
        self.assertRaises(ValueError, ConvexPolygon, *points)
        points.append(Point(1, 1))
        self.assertRaises(ValueError, ConvexPolygon, *points)

    def test_convex_inside(self):
        points = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        polygon = ConvexPolygon(*points)
        self.assertTrue(polygon.inside(Point(1, 1)))


if __name__ == "__main__":
    unittest.main()
