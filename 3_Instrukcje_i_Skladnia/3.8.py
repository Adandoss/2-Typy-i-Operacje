A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [0, 2, 4, 6, 8, 10, 12, 14]
C = []
D = []

for a in A:
    if a in B and a not in C:
        C.append(a)

D = A.copy()
for b in B:
    if b not in D:
        D.append(b)


print(f"Podstawowe operacje: \nA: {A}\nB: {B}\nC: {C}\nD: {D}\n")

# Mozna tez na zbiorach: 

C = list(set(A) & set(B))
D = list(set(A) | set(B))

print(f"Zbiory: \nA: {A}\nB: {B}\nC: {C}\nD: {D}\n")