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

