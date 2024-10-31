def factorial(n):
    if n < 0:
        return -1
    result = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n+1):
        result *= i
        
    return result
    
assert factorial(-3) == -1
print(f"factorial(-3): {factorial(-3)} (-1 meaning error)")
assert factorial(0) == 1
print(f"factorial(0): {factorial(0)}")
assert factorial(1) == 1
print(f"factorial(1): {factorial(1)}")
assert factorial(5) == 120
print(f"factorial(5): {factorial(5)}")
assert factorial(10) == 3628800
print(f"factorial(10): {factorial(10)}")
