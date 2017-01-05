"""
Redo of convex polygon unittesting
"""


import unittest
from point import Point
from convex_polygon import ConvexPolygon


class TestConvexPolygon(unittest.TestCase):
    """TestCase subclass to test ConvexPolygon class"""
    def test_convex_creation(self):
        """test creation of polygon"""
        points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
        self.assertIsInstance(ConvexPolygon(*points), ConvexPolygon)
        points.pop()
        points.pop()
        self.assertRaises(ValueError, ConvexPolygon, *points)

    def test_convex_methods(self):
        """test methods of polygon"""
        points = [Point(*p) for p in [(0, 2), (2, 0), (4, 2), (2, 4)]]
        polygon = ConvexPolygon(*points)
        self.assertFalse(polygon.inside(Point(3, 0)))
        self.assertFalse(polygon.inside(Point(0, 0)))
        self.assertTrue(polygon.inside(Point(1, 1)))
        self.assertTrue(polygon.inside(Point(2, 2)))

if __name__ == "__main__":
    unittest.main()
