from points import Point # type: ignore
from rectangles import Rectangle

rect1 = Rectangle(0, 0, 4, 2)
rect2 = Rectangle(1, 1, 2, 2)

def test_str():
    assert str(rect1) == "[(0, 0), (4, 2)]"
    assert str(rect2) == "[(1, 1), (2, 2)]"

def test_repr():
    assert repr(rect1) == "Rectangle(0, 0, 4, 2)"
    assert repr(rect2) == "Rectangle(1, 1, 2, 2)"

def test_cmp():
    assert rect1 == Rectangle(0, 0, 4, 2)
    assert rect2 == Rectangle(1, 1, 2, 2)
    assert rect1 != rect2

def test_area():
    assert rect1.area() == 8
    assert rect2.area() == 1

def test_move():
    assert Rectangle(0, 0, 4, 2).move(1, 1) == Rectangle(1, 1, 5, 3)
    assert Rectangle(1, 1, 2, 2).move(-1, -1) == Rectangle(0, 0, 1, 1)

def test_from_points():
    assert Rectangle.from_points((Point(0, 0), Point(4, 2))) == rect1
    assert Rectangle.from_points((Point(1, 1), Point(2, 2))) == rect2

def test_properties():
    assert rect1.top == 2
    assert rect1.bottom == 0
    assert rect1.left == 0
    assert rect1.right == 4
    assert rect1.width == 4
    assert rect1.height == 2
    assert rect1.topleft == Point(0, 2)
    assert rect1.bottomleft == Point(0, 0)
    assert rect1.topright == Point(4, 2)
    assert rect1.bottomright == Point(4, 0)
    assert rect1.center == Point(2, 1)

