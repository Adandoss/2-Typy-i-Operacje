L = [32, 123, 2, 4, 23, 34, 231, 123, 3, 4]

print(L)

L_str_list = [str(n).zfill(3) for n in L]

print(L_str_list)

L_str = "".join(L_str_list)

print(L_str)
