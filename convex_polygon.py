"""
Redo of convex polygon class not using matplotlib

The code was originally written by Charles Marsh:
Repo it was found in and re implemented from: https://github.com/crm416/point-location
Also:
https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
"""


class ConvexPolygon:
    """
    ConvexPolygon Class
    """
    def __init__(self, *data):
        """init"""
        if len(data) < 3:
            raise ValueError
        self.vertices = data
        self.amount = len(data)

    def is_in_path(self, point):
        """
        walking through the sequence of vetices in the function and determining
        wether the point parameter
		Retrieved from: 
		https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
        """
        j = self.amount - 1
        in_path = False
        for i in range(self.amount):
            if(
                    (self.vertices[i].y > point.y) !=
                    (self.vertices[j].y > point.y)
            ) and (
                point.x < (self.vertices[j].x - self.vertices[i].x) *
                (point.y - self.vertices[i].y) /
                (self.vertices[j].y - self.vertices[i].y) +
                self.vertices[i].x
            ):
                in_path = not in_path
            j = i
        return in_path

    def contains(self, point):
        """
        test if point paramaeter falls within the boundaries of the vertices
        """
        inside = False
        point1 = self.vertices[0]
        for i in range(self.amount + 1):
            if inside:
                break
            point2 = self.vertices[i % self.amount]
            if point.y > min(point1.y, point2.y):
                if point.y <= max(point1.y, point2.y):
                    if point.x <= max(point1.x, point2.x):
                        if point1.y != point2.y:
                            par1 = (point.y - point1.y)
                            par2 = (point2.x - point1.x)
                            par3 = (point2.y - point1.y)
                            xints = par1 * par2 / par3 + point1.x
                        if point1.x == point2.x or point.x <= xints:
                            inside = not inside
            point1 = point2
        return inside

    def inside(self, point):
        """
        funtion to be implemented that runs the above two to determine if the
        point paramaeter is inside the polygon
        """
        return self.is_in_path(point) or self.contains(point)
