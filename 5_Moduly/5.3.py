def add_poly(poly1, poly2):		# poly1(x) + poly2(x)
    result = []
    longer_list_size = max(len(poly1), len(poly2))
    smaller_list_size = min(len(poly1), len(poly2))
    for i in range(longer_list_size):
        if i < smaller_list_size:
            result.append(poly1[i] + poly2[i])
        elif i >= len(poly1):
            result.append(poly2[i])
        elif i >= len(poly2):
            result.append(poly1[i])
    return result
        
def sub_poly(poly1, poly2): 	        # poly1(x) - poly2(x)
    result = []
    longer_list_size = max(len(poly1), len(poly2))
    smaller_list_size = min(len(poly1), len(poly2))
    for i in range(longer_list_size):
        if i < smaller_list_size:
            result.append(poly1[i] - poly2[i])
        elif i >= len(poly1):
            result.append(-poly2[i])
        elif i >= len(poly2):
            result.append(poly1[i])
    return result

# Bardzo bardzo tragicznie napisana funkcja -> duzo lepiej w zestawie 7!!!
def mul_poly(poly1, poly2): 	        # poly1(x) * poly2(x)

    if is_zero(poly1) or is_zero(poly2):
        return [0]
        
    for i in range(len(poly1)-1, 0, -1):
        if poly1[i] == 0:
            poly1.pop()
        else:
            break
    for i in range(len(poly2)-1, 0, -1):
        if poly2[i] == 0:
            poly2.pop()
        else:
            break

    longer_list = poly1 if len(poly1) >= len(poly2) else poly2
    smaller_list = poly1 if len(poly1) < len(poly2) else poly2
            
    coefficient_table = []
    tmp = []
    for a in smaller_list:
        for b in longer_list:
            tmp.append(a * b)
        coefficient_table.append(list(tmp))
        tmp.clear()
    
    result = []
    coefficient = 0
    for i in range(len(smaller_list) + len(longer_list) - 1):
        a = i
        b = 0
        coefficient = 0
        while 0 <= a and b < len(coefficient_table):
            if a >= len(coefficient_table[0]):
                a -= 1
                b += 1
                continue
            coefficient += coefficient_table[b][a]
            a -= 1
            b += 1
        result.append(coefficient)
       
    return result

def is_zero(poly):                  	# bool, [0], [0,0], itp.
    for i in range(len(poly)):
        if poly[i] != 0:
            return False
    return True

def eq_poly(poly1, poly2):	        # bool, porównywanie poly1(x) == poly2(x)
    longer_list_size = max(len(poly1), len(poly2))
    smaller_list_size = min(len(poly1), len(poly2))
    for i in range(smaller_list_size):
        if poly1[i] != poly2[i]:
            return False
    longer_list = poly1 if len(poly1) == longer_list_size else poly2
    if is_zero(longer_list[smaller_list_size:]):
        return True
    else:
        return False

def eval_poly(poly, x0):                # poly(x0), algorytm Hornera
    result = 0
    for i in range(len(poly) - 1, -1, -1):
        result *= x0
        result += poly[i]
    return result

# Tragicznie napisana funkcja -> duzo lepiej w zestawie 7!!!
def combine_poly(poly1, poly2):         # poly1(poly2(x)), trudne!
    result = [poly1[0]]
    temp = []
    for i in range(1, len(poly1)):
        temp = pow_poly(poly2, i)
        for j in range(len(temp)):
            temp[j] *= poly1[i]
        result = add_poly(result, temp)
        temp.clear()
    return result

def pow_poly(poly, n):	                # poly(x) ** n
    result = [1]
    for i in range(n):
        result = mul_poly(poly, result)
    return result

def diff_poly(poly):                    # pochodna wielomianu
    result = []
    for i in range(1, len(poly)):
        result.append(i*poly[i])
    return result

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)

mul_poly([0, 1], [0, 0, 1])

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self): 
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly([1, 1, 1], [1, 1, 1]), [1, 2, 3, 2, 1])
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
        self.assertEqual(mul_poly(self.p1, [0, 0, 0]), [0])
        self.assertEqual(mul_poly([1, 3], [1, 3]), [1, 6, 9])

    def test_is_zero(self): 
        self.assertEqual(is_zero(self.p1), False)
        self.assertEqual(is_zero([0, 0, 0, 0]), True)

    def test_eq_poly(self):
        self.assertEqual(eq_poly(self.p1, self.p2), False)
        self.assertEqual(eq_poly(self.p1, [0, 1]), True)
        self.assertEqual(eq_poly(self.p1, [0, 1, 0, 0, 0]), True)
        self.assertEqual(eq_poly([0, 1, 0], self.p1), True)

    def test_eval_poly(self): 
        self.assertEqual(eval_poly([1], 10), 1)
        self.assertEqual(eval_poly(self.p1, 10), 10)
        self.assertEqual(eval_poly(self.p2, 10), 100)

    def test_combine_poly(self): 
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])
        self.assertEqual(combine_poly([1, 1], [0, 1, 1]), [1, 1, 1])
        self.assertEqual(combine_poly([1, 1, 1], [1, 3]), [3, 9, 9])
        # 10 + 9*(1 + 2x + 3x^2) + 8*(1 + 2x + 3x^2)^2 + 7*(1 + 2x + 3x^2)^3 w Wolframa dla sprawdzenia
        self.assertEqual(combine_poly([10, 9, 8, 7], [1, 2, 3]), [34, 92, 254, 404, 513, 378, 189])
        self.assertEqual(combine_poly([9, 1, 2, 3, 4, 5], [0]), [9])
        self.assertEqual(combine_poly([0], [1, 2, 3, 4, 5]), [0])
        self.assertEqual(combine_poly([10, 90], [1]), [100])
        
    def test_pow_poly(self): 
        self.assertEqual(pow_poly([1, 3], 2), [1, 6, 9])
        self.assertEqual(pow_poly([0, 1], 5), [0, 0, 0, 0, 0, 1])
        self.assertEqual(pow_poly([2], 10), [1024])
        self.assertEqual(pow_poly(self.p2, 1), self.p2)
    
    def test_diff_poly(self): 
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p2), [0, 2])
        self.assertEqual(diff_poly([10, 12, 6, 4]), [12, 12, 12])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    
    
