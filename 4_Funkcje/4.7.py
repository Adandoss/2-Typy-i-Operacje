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
print(f"flatten(seq): {flatten(seq)}")

