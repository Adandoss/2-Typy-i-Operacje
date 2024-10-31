print('\nZadanie 4.2: \n')

def make_ruler(n): 
    miarka = ''

    for i in range(n):
        miarka += "|...."
    
    miarka += "|\n0"

    for i in range(1, n+1):
        miarka += "{0:>5}".format(i)

    return miarka

def make_grid(rows, cols): 
    siatka1 = '+'
    siatka2 = '|'

    for i in range(rows):
        siatka1 += '---+'
        siatka2 += "{0:>4}".format("|")

    siatka1 += '\n'
    siatka2 += '\n'
    
    siatka = ''    

    for i in range(cols):
        siatka += siatka1
        siatka += siatka2

    siatka += siatka1
    
    return siatka
    
print(f"make_ruler(12): \n{make_ruler(12)}\n\n")
print(f"make_grid(4, 6): \n{make_grid(4, 6)}")


print('\nZadanie 4.3:\n')

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


print('\nZadanie 4.4: \n')

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


print('\nZadanie 4.5: \n')

def odwracanie_i(L, left, right):
    for i in range((right - left)//2 + 1):
        tmp = L[left + i]
        L[left + i] = L[right - i]
        L[right - i] = tmp
    
def odwracanie_r(L, left, right): 
    tmp = L[left]
    L[left] = L[right]
    L[right] = tmp
    if not (left + 1 == right - 1 or left + 1 == right):    
        odwracanie_r(L, left + 1, right - 1)


L = [0, 1, 2, 3, 4, 5, 6, 7]
print(f"L: {'':27} {L}")
odwracanie_i(L, 0, 2)
print(f"odwracanie_i(L, 0, 2): {'':7} {L}")
odwracanie_i(L, 1, 6)
print(f"odwracanie_i(L, 1, 6): {'':7} {L}")
odwracanie_i(L, 0, len(L)-1)
print(f"odwracanie_i(L, 0, len(L)-1):  {L}\n")

L = [0, 1, 2, 3, 4, 5, 6, 7]
print(f"L: {'':27} {L}")
odwracanie_r(L, 0, 2)
print(f"odwracanie_r(L, 0, 2): {'':7} {L}")
odwracanie_r(L, 1, 6)
print(f"odwracanie_r(L, 1, 6): {'':7} {L}")
odwracanie_r(L, 0, len(L)-1)
print(f"odwracanie_r(L, 0, len(L)-1):  {L}\n")


print('\nZadanie 4.6:\n')

def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
            
    return result
    
S = [0, 1, 2, 3, 4, (0, 1, 2, 3, 4), [5, (2, 3)]]
assert sum_seq(S) == 30
print(f"S: {S}")
print(f"sum_seq(S): {sum_seq(S)}")


print('\nZadanie 4.7:\n')

def flatten(sequence):
    result = []
    
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L = flatten(item)
            for x in L:
                #if x not in result:
                result.append(x)
        else:
            #if item not in result:
            result.append(item)
            
    return result
    
            
    
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(f"seq: {seq}")
print(f"flatten(seq): {flatten(seq)}\n")

