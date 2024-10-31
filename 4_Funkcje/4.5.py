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

