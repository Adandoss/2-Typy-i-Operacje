import keyword
# import __builtins__

# Zadanie 1 - wyświetlenie słów kluczowych
"""
kwl = keyword.kwlist
print(kwl)

print('')

print(dir(__builtins__))


# Zadanie 2

print(5 == 5) 
print(4 > 5)              
print(type(True))
print(type(False))       
print(type(1))
print(type(0))              
x = 5
print(x == 5 and 3)                  # 3
print(x == 4 and 3)                  # False
print(3 and x == 5)                  # True
print(3 and x == 4)                 # False
print(1 < x < 9)              # łączenie operatorów porównania
print(isinstance(True, int))        # True
print(isinstance(True, bool))        # True



# Zadanie 4

# Funkcja len().
print(len("napis"))                  # 5
print(str(2 ** 10))            # konwersja liczby do napisu

"abc", 'abc'                  # identyczne
S = "ab"   'cd'               # niejawna konkatenacja do "abcd"
"ab'cd", 'ab"cd'              # zastosowanie
S = "a\tb\nc\"d"              # znaki specjalne
print ( "{} {}".format(len(S), S) )   # 7

# Sprawdzić indeksowanie i wycinki.
S = "abrakadabra"
print(S)

print(S[2])
print(S[-3])
print(S[3:5])
print(S[3:])
print(S[:4])

# Sprawdzić konkatenację (łączenie) i powtórzenie napisów.
L = ["a", "b", "c"]
print(L)
print(L[0] + L[1] + L[2])            # ręczne dodawanie
print(L[0] + "=" + L[1] + "=" + L[2])

print("".join(L))
print("=".join(L))
# S.join([S1,S2,S3]) daje S1+S+S2+S+S3

# Sprawdzić niezmienność napisów.

L = [3, "xyz", [10, 20]]
print(L)
print(len(L))

print(L[1])
print(L[1][0])
print(L[2])
print(L[2][1])
M = L
L[1] = 5     # zmienia się też M!

print(L)
print(M)

# Indeksowanie 

# Wycinki.

# Konkatenacja i powtórzenie.

# Podstawianie pod element lub wycinek.

# Generowanie list funkcją range().

# Kopiowanie list.

# Sortowanie list.

# Listy składane.

"""





