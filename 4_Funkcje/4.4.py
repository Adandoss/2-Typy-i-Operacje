def fibonnaci(n):
    if n < 0:
        return -1
    f0, f1 = 0, 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    for i in range(n-1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        
    return f1
    
assert fibonnaci(-5) == -1
print(f"fibonnaci(-5): {fibonnaci(-5)} (-1 meaning error)")
assert fibonnaci(0) == 0
print(f"fibonnaci(0): {fibonnaci(0)}")
assert fibonnaci(1) == 1
print(f"fibonnaci(1): {fibonnaci(1)}")
assert fibonnaci(2) == 1
print(f"fibonnaci(2): {fibonnaci(2)}")
assert fibonnaci(3) == 2
print(f"fibonnaci(3): {fibonnaci(3)}")
assert fibonnaci(4) == 3
print(f"fibonnaci(4): {fibonnaci(4)}")
assert fibonnaci(5) == 5
print(f"fibonnaci(5): {fibonnaci(5)}")
assert fibonnaci(6) == 8
print(f"fibonnaci(6): {fibonnaci(6)}")
assert fibonnaci(15) == 610
print(f"fibonnaci(15): {fibonnaci(15)}")
