class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.size = n + 1    # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)
        
    def __repr__(self):
        return f'Poly({str(self.a)})'

    def __add__(self, other): 	    # poly1+poly2, poly+liczba
        if not isinstance(other, (int, float, Poly)):
            raise ValueError
        if isinstance(other, (int, float)):
            result = list(self)
            result[0] += other
            return Poly.from_list(result)
        elif isinstance(other, Poly):
            result = []
            longer_list_size = max(len(self), len(other))
            smaller_list_size = min(len(self), len(other))
            for i in range(longer_list_size):
                if i < smaller_list_size:
                    result.append(self[i] + other[i])
                elif i >= len(self):
                    result.append(other[i])
                elif i >= len(other):
                    result.append(self[i])
            return Poly.from_list(result)

    __radd__ = __add__              # liczba+poly

    def __sub__(self, other): 	    # poly1-poly2, poly-liczba
        if not isinstance(other, (int, float, Poly)):
            raise ValueError
        if isinstance(other, (int, float)):
            result = list(self)
            result[0] -= other
            return Poly.from_list(result)
        elif isinstance(other, Poly):
            result = []
            longer_list_size = max(len(self), len(other))
            smaller_list_size = min(len(self), len(other))
            for i in range(longer_list_size):
                if i < smaller_list_size:
                    result.append(self[i] - other[i])
                elif i >= len(self):
                    result.append(-other[i])
                elif i >= len(other):
                    result.append(self[i])
            return Poly.from_list(result)        

    def __rsub__(self, other):      # liczba-poly
        if not isinstance(other, (int, float, Poly)):
            raise ValueError
        result = list(-self)
        result[0] += other
        return Poly.from_list(result)

    def __mul__(self, other):       # poly1*poly2, poly*liczba
        if not isinstance(other, (int, float, Poly)):
            raise ValueError
        if isinstance(other, (int, float)):
            result = list(self)
            for i in range(len(result)):
                result[i] *= other
            return Poly.from_list(result)
        elif self.is_zero() or other.is_zero():
            return Poly(0, 0)
        
        result = [0]*(len(self) + len(other) - 1)
        for i in range(len(self.a)):
            for j in range(len(other.a)):
                result[i+j] += self.a[i]*other.a[j]
        
        return Poly.from_list(result)
    
            
    __rmul__ = __mul__              # liczba*poly

    def __pos__(self):              # +poly1 = (+1)*poly1
        return self

    def __neg__(self):              # -poly1 = (-1)*poly1
        result = list(self)
        for i in range(len(result)):
            result[i] *= -1
        return Poly.from_list(result)

    def is_zero(self): 	            # bool, True dla [0], [0, 0],...
        for i in range(len(self)):
            if self[i] != 0:
                return False
        return True

    def __eq__(self, other):    # obsluga poly1 == poly2
        if not isinstance(other, (int, float, Poly)):
            raise ValueError
        longer_list_size = max(len(self), len(other))
        smaller_list_size = min(len(self), len(other))
        for i in range(smaller_list_size):
            if self[i] != other[i]:
                return False
        longer_list = self.a if len(self) == longer_list_size else other.a
        for coeff in longer_list[smaller_list_size:]:
            if coeff != 0:
                return False
        return True        

    def __ne__(self, other):        # obsluga poly1 != poly2
        return not self == other

    def eval(self, x): 	            # schemat Hornera
        if not isinstance(x, (int, float)):
            raise ValueError
        result = 0
        for i in range(len(self) - 1, -1, -1):
            result = result*x + self[i]
        return result

    def combine(self, other):       # zlozenie poly1(poly2(x))
        if not isinstance(other, (Poly)):
            raise ValueError
        result = Poly(0, 0)
        for i in range(len(self.a) - 1, -1, -1):
            result = result*other + self[i]
        return result

    def __pow__(self, n):           # poly(x)**n lub pow(poly(x),n)
        if not isinstance(n, (int)):
            raise ValueError
        result = Poly.from_list([1])
        for i in range(n):
            result = self * result
    
        return Poly.from_list(result)

    def diff(self): 	            # rozniczkowanie
        if self.is_zero():
            return Poly.from_list([0])
        result = []
        for i in range(1, len(self.a)):
            result.append(i*self[i])
        return Poly.from_list(result)

    def integrate(self):            # calkowanie
        if self.is_zero():
            return Poly.from_list([0])
        result = [0]
        for i in range(0, len(self.a)):
            result.append(self[i]/(i+1))
        return Poly.from_list(result)

    def __len__(self): 	            # len(poly), rozmiar self.a
        return len(self.a)

    def __getitem__(self, i):                 # poly[i], wspolczynnik przy x^i
        return self.a[i]

    def __setitem__(self, i, value): 	      # poly[i] = value
        if not (isinstance(i, (int))) or (not isinstance(value, (int, float))):
            raise ValueError
        elif i < 0:
            raise IndexError
        elif i < len(self.a):
            self.a[i] = value
# kolejne dwa sa moze dziwne, ale chyba przydatne
        elif i == len(self.a):
            self.a.append(value)
        elif i > len(self.a):
            poly = self + Poly(value, i)
            self.a = poly.a

    # dla isinstance(x, (int,long,float)) odpowiada eval(),
    # dla isinstance(x, Poly) odpowiada combine()
    def __call__(self, x):          # poly(x)
        if not isinstance(x, (int, float, Poly)):
            raise ValueError
        if isinstance(x, (int, float)):
            return self.eval(x)
        elif isinstance(x, Poly):
            return self.combine(x)
            
    def __iter__(self):
        return iter(self.a)
        
    @classmethod
    def from_list(cls, l):
        poly = cls(0, len(l) - 1)
        poly.a = l
        return poly

# Kod testujacy modul.

import unittest

class TestPoly(unittest.TestCase): 

    def setUp(self):
        self.p1 = Poly(1, 1)      # W(x) = x
        self.p2 = Poly(1, 2)      # W(x) = x^2
        self.p3 = Poly()          # W(x) = 0
    
    def test_str(self):
        self.assertEqual(str(self.p1), '[0, 1]')
        self.assertEqual(str(self.p2), '[0, 0, 1]')
        self.assertEqual(str(self.p3), '[0]')
       
    def test_adding_polys(self):
        self.assertEqual(self.p1 + self.p2, Poly.from_list([0, 1, 1]))
        self.assertEqual(self.p2 + self.p2, Poly.from_list([0, 0, 2]))
        self.assertEqual(self.p1 + self.p2 + Poly(1, 0), Poly.from_list([1, 1, 1]))
        with self.assertRaises(ValueError):
            self.p1 + "hello!"

    def test_adding_numbers_to_polys(self):
        self.assertEqual(self.p1 + 3, Poly.from_list([3, 1]))
        self.assertEqual(self.p2 + 9, Poly.from_list([9, 0, 1]))
        self.assertEqual(3 + self.p1, Poly.from_list([3, 1]))
        self.assertEqual(9 + self.p2, Poly.from_list([9, 0, 1]))
   
    def test_subtracting_polys(self):
        self.assertEqual(self.p1 - self.p2, Poly.from_list([0, 1, -1]))
        self.assertEqual(self.p2 - self.p2, Poly.from_list([0, 0, 0]))
        self.assertEqual(self.p2 - self.p1, Poly.from_list([0, -1, 1]))
        self.assertEqual(self.p1 - self.p3, self.p1)
        
    def test_subtracting_numbers_from_polys(self):
        self.assertEqual(self.p1 - 3, Poly.from_list([-3, 1]))
        self.assertEqual(self.p2 - 9, Poly.from_list([-9, 0, 1]))
        self.assertEqual(3 - self.p1, Poly.from_list([3, -1]))
        self.assertEqual(9 - self.p2, Poly.from_list([9, 0, -1]))
        
    def test_multiplying_polys(self):
        self.assertEqual(self.p1*3, Poly.from_list([0, 3]))
        self.assertEqual(3*self.p1, Poly.from_list([0, 3]))
        self.assertEqual(self.p3*20, self.p3)
        self.assertEqual(0*self.p2, self.p3)
        self.assertEqual(self.p1*(-3), Poly.from_list([0, -3]))
        self.assertEqual((-1)*self.p2, Poly.from_list([0, 0, -1]))
        self.assertEqual(self.p1*3, Poly.from_list([0, 3]))
        self.assertEqual(3*self.p1, Poly.from_list([0, 3]))
        self.assertEqual(self.p1 * self.p2, Poly.from_list([0, 0, 0, 1]))
        self.assertEqual(self.p2 * self.p1, Poly.from_list([0, 0, 0, 1]))
        self.assertEqual(Poly.from_list([1, 1]) * Poly.from_list([1, 1]), Poly.from_list([1, 2, 1]))
        self.assertEqual(Poly.from_list([-3, 1]) * Poly.from_list([2, 1]), Poly.from_list([-6, -1, 1]))
        
    def test_pos(self):
        self.assertEqual(+self.p1, self.p1)
        self.assertEqual(+self.p2, self.p2)
        self.assertEqual(+self.p3, self.p3)    
    
    def test_neg(self):
        self.assertEqual(-self.p1, Poly.from_list([0, -1]))
        self.assertEqual(-self.p2, Poly.from_list([0, 0, -1]))
        self.assertEqual(-self.p3, self.p3)
        
    def test_eval(self):
        self.assertEqual(self.p1.eval(10), 10)
        self.assertEqual(self.p1.eval(-10), -10)
        self.assertEqual(self.p2.eval(2), 4)
        self.assertEqual(self.p2.eval(-2), 4)
        self.assertEqual(self.p3.eval(9999), 0)
        self.assertEqual(self.p3.eval(0), 0)
        
    def test_combine(self): 
        self.assertEqual(self.p1.combine(self.p2), Poly.from_list([0, 0, 1]))
        self.assertEqual(Poly.from_list([1, 1]).combine(Poly.from_list([0, 1, 1])), Poly.from_list([1, 1, 1]))
        self.assertEqual(Poly.from_list([1, 1, 1]).combine(Poly.from_list([1, 3])), Poly.from_list([3, 9, 9]))
        # 10 + 9*(1 + 2x + 3x^2) + 8*(1 + 2x + 3x^2)^2 + 7*(1 + 2x + 3x^2)^3 w Wolframa dla sprawdzenia
        self.assertEqual(Poly.from_list([10, 9, 8, 7]).combine(Poly.from_list([1, 2, 3])), Poly.from_list([34, 92, 254, 404, 513, 378, 189]))
        self.assertEqual(Poly.from_list([9, 1, 2, 3, 4, 5]).combine(Poly.from_list([0])), Poly.from_list([9]))
        self.assertEqual(Poly.from_list([0]).combine(Poly.from_list([1, 2, 3, 4, 5])), Poly.from_list([0]))
        self.assertEqual(Poly.from_list([10, 90]).combine(Poly.from_list([1])), Poly.from_list([100]))    
        
    def test_pow(self):
        self.assertEqual(self.p1**1, self.p1)
        self.assertEqual(self.p1**2, Poly.from_list([0, 0, 1]))
        self.assertEqual(self.p1**5, Poly.from_list([0, 0, 0, 0, 0, 1]))
        self.assertEqual(pow(self.p2, 2), Poly.from_list([0, 0, 0, 0, 1]))
        self.assertEqual(Poly.from_list([1, 1, 1])**2, Poly.from_list([1, 2, 3, 2, 1]))
        self.assertEqual(self.p3**999, self.p3)
        
    def test_diff(self):
        self.assertEqual(self.p1.diff(), Poly.from_list([1]))
        self.assertEqual(self.p2.diff(), Poly.from_list([0, 2]))
        self.assertEqual(Poly.from_list([999, 1, 1, 1, 1]).diff(), Poly.from_list([1, 2, 3, 4]))
        self.assertEqual(self.p3.diff(), Poly.from_list([0]))
    
    def test_integration(self):
        self.assertEqual(self.p1.integrate(), Poly.from_list([0, 0, 1/2]))
        self.assertEqual(Poly.from_list([10, 4, 9, 16]).integrate(), Poly.from_list([0, 10, 2, 3, 4]))
        self.assertEqual(Poly.from_list([1, 2, 3, 4]).integrate(), Poly.from_list([0, 1, 1, 1, 1]))
        self.assertEqual(self.p3.integrate(), Poly.from_list([0]))
    
    def test_len(self):
        self.assertEqual(len(self.p1), 2)
        self.assertEqual(len(self.p2), 3)
        self.assertEqual(len(self.p3), 1)
        self.assertEqual(len(Poly.from_list([1, 2, 3, 4, 5, 6, 7])), 7)
    
    def test_get(self):
        self.assertEqual(self.p1[0], 0)
        self.assertEqual(self.p1[1], 1)
        with self.assertRaises(IndexError):
            self.p1[2] == 0
        with self.assertRaises(IndexError):
            self.p1[999] == 0

    def test_set(self):
        with self.assertRaises(ValueError):
            self.p1["hello"] = 0
        with self.assertRaises(ValueError):
            self.p1[1] = [1, 2, 3]  
        with self.assertRaises(IndexError):
            self.p1[-1] = 10
        with self.assertRaises(IndexError):
            self.p1[-9] = 1
        poly = Poly.from_list([0, 0, 0])  
        poly[0] = 1
        self.assertEqual(poly[0], 1)
        poly[1] = 1
        poly[2] = 1
        self.assertEqual(poly, Poly.from_list([1, 1, 1]))
        poly[3] = 1
        self.assertEqual(poly, Poly.from_list([1, 1, 1, 1]))
        poly[5] = 1
        self.assertEqual(poly, Poly.from_list([1, 1, 1, 1, 0, 1]))
        
    def test_evaluation(self):
        self.assertEqual(self.p1(12), 12)
        self.assertEqual(self.p1(self.p2), self.p2)

    def test_iter(self):
        test = [coeff for coeff in self.p1]
        self.assertEqual(test, [0, 1])
        test = [coeff for coeff in self.p2]
        self.assertEqual(test, [0, 0, 1])
        test = [coeff for coeff in Poly.from_list([1, 2, 3, 4, 5, 6])]
        self.assertEqual(test, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    
    
