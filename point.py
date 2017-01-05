"""
point module
"""

from numbers import Number


class Point:    # pylint: disable=R0903
    """
    Point class
    """

    def __init__(self, *data):
        """
        Point Class Creation
        """

        if len(data) != 2:
            raise ValueError
        if not isinstance(data[0], Number):
            raise TypeError
        if not isinstance(data[1], Number):
            raise TypeError
        self.x = data[0]
        self.y = data[1]

    def get_coord(self):
        """
        Retireve Tuple from Coordinates Stored
        """
        return self.x, self.y
