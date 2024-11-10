class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):             # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):        # obsługa point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 
    
    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(3, 4)
    
    def test_str(self):
        self.assertEqual(str(self.p1), "(0, 0)")
        self.assertEqual(str(self.p2), "(3, 4)")
        
    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(0, 0)")
        self.assertEqual(repr(self.p2), "Point(3, 4)")
        
    def test_cmp(self):
        self.assertTrue(self.p1 == Point(0, 0))
        self.assertFalse(self.p1 == self.p2)
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p2 != Point(3, 4))
        
    def test_arithmetic(self):
        self.assertEqual(self.p1 + self.p2, Point(3, 4))
        self.assertEqual(self.p2 + self.p2, Point(6, 8))
        self.assertEqual(self.p2 - self.p1, Point(3, 4))
        self.assertEqual(self.p2 - self.p2, Point(0, 0))
        self.assertEqual(self.p1 * self.p2, 0)
        self.assertEqual(self.p2 * self.p2, 25)
        self.assertEqual(self.p1.cross(self.p2), 0)
        self.assertEqual(self.p1.cross(Point(10, 10)), 0)
        self.assertEqual(self.p2.cross(Point(3, 4)), 0)
        self.assertEqual(self.p2.cross(Point(5, 5)), -5)
        self.assertEqual(self.p1.length(), 0)
        self.assertEqual(self.p2.length(), 5)
        
        
if __name__ == "__main__":
    unittest.main()

