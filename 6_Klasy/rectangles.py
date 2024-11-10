from points import Point

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

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        
    def area(self):                 # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)
        return self

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 
    
    def setUp(self):
        self.rect1 = Rectangle(0, 0, 4, 2)
        self.rect2 = Rectangle(1, 1, 2, 2)
        
    def test_str(self):
        self.assertEqual(str(self.rect1), "[(0, 0), (4, 2)]")
        self.assertEqual(str(self.rect2), "[(1, 1), (2, 2)]")
        
    def test_repr(self):
        self.assertEqual(repr(self.rect1), "Rectangle(0, 0, 4, 2)")
        self.assertEqual(repr(self.rect2), "Rectangle(1, 1, 2, 2)")
        
    def test_cmp(self):
        self.assertTrue(self.rect1 == Rectangle(0, 0, 4, 2))
        self.assertFalse(self.rect1 == self.rect2)
        self.assertTrue(self.rect1 != self.rect2)
        self.assertFalse(self.rect2 != Rectangle(1, 1, 2, 2))
        
    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2, 1))
        self.assertEqual(self.rect2.center(), Point(1.5, 1.5))
        
    def test_area(self):
        self.assertEqual(self.rect1.area(), 8)
        self.assertEqual(self.rect2.area(), 1)
        
    def test_move(self):
        self.assertEqual(self.rect1.move(1, 1), Rectangle(1, 1, 5, 3))
        self.assertEqual(self.rect2.move(-1, -1), Rectangle(0, 0, 1, 1))
        
if __name__ == "__main__":
    unittest.main()
        

