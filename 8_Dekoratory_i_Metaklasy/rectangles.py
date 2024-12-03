from points import Point # type: ignore

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other): 	    # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        
    def area(self):                 # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)
        return self
    
    @classmethod
    def from_points(cls, tuple):
        if not (isinstance(tuple[0], Point) and isinstance(tuple[1], Point)):
            raise ValueError
        rect = cls(tuple[0].x, tuple[0].y, tuple[1].x, tuple[1].y,)
        return rect
    
    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x)

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)



        

