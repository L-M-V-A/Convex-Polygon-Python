"""
convex_polygon Module
"""

from point import Point
from matplotlib.mlab import inside_poly
from matplotlib.path import Path

# Disabling too few methods checks, casued by ConvexPolygon subclass
# pylint: disable=R0903

# Disabling attribute %r defined outside __init__ warning, caused by setters
# pylint: disable=W0201

# Disabling unused variable warning, caused by line 37
# pylint: disable=W0612

# Disabling message about locally disabling checks
# pylint: disable=I0011


class Polygon:
    """
    base class polygon
    """

    def __init__(self, *data):
        """ instantiation of base polygon class """

        if len(data) < 3:
            raise ValueError
        self.vertices = [x for x in data]
        path_verts = [x.get_coord() for x in self.vertices]
        path_verts.append(path_verts[0])
        code = [Path.MOVETO]
        for i in range(len(self.vertices) - 1):
            code.append(Path.LINETO)
        code.append(Path.CLOSEPOLY)
        self.path = Path(path_verts, code)

    @property
    def vertices(self):
        """ getter for x """
        return self.__vertices

    @vertices.setter
    def vertices(self, vertices):
        """setter for vertices"""
        self.__vertices = vertices

    @property
    def path(self):
        """getter for path"""
        return self.__path

    @path.setter
    def path(self, path):
        """ setter for path """
        self.__path = path

    def inside(self, point_t):
        """check if point is inside"""
        if not isinstance(point_t, Point):
            raise TypeError
        return self.path.contains_point(point_t.get_coord(), radius=1.0)


class ConvexPolygon(Polygon):
    """
    Subclass of Polygon, that only creates a polygon if the sequence of
    points doesn't represent a concave polygon
    """

    def __init__(self, *data):
        """ instantiation of convex_polygon class """
        if len(data) < 4:
            raise ValueError
        for i in range(len(data)):
            sub_vertices = [x.get_coord() for x in data if x != data[i]]
            if len(inside_poly([data[i].get_coord()], sub_vertices)) > 0:
                raise ValueError
        super().__init__(*data)
