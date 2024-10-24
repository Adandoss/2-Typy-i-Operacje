print('3.1:')
# x = 2; y = 3;
x, y = 2, 3  #obydwie wersje działaja, srednik rozdziela instrukcje podobnie jak w bashu
if (x > y):
    result = x;
else:
    result = y;
    
print(f"result: {result}")

# for i in "axby": if ord(i) < 100: print (i)

for i in "axby": 
    if ord(i) < 100: print(i)

# for i in "axby": print (ord(i) if ord(i) < 100 else i)
# dziala, po dwukropku w jednej linii może być tylko jedna instrukcja prosta

for i in "axby": 
    print (ord(i) if ord(i) < 100 else i)   # Podobne do:  boll ? "t" : "f"


print('\n\n3.2:')
print(
"""
L = [3, 5, 4] ; L = L.sort() 
# sort sortuje inplace, domyślnie zwraca None
# tutaj powinnismy zrobic albo L.sort(), albo L = sorted(L)

x, y = 1, 2, 3  
# to jest przypisywanie pozycyjne, a mamy 2 zmienne do 3 wartosci

X = 1, 2, 3 ; X[1] = 4  
# X to krotka a one nie sa mutowalne

X = [1, 2, 3] ; X[3] = 4 
# 3 jest poza zasiegiem, mozemy sobie dodac element poprzez X.append(4)

X = "abc" ; X.append("d")  
# stringi nie maja metody append, "d" mozemy dodac wykonujac X += "d"

L = list(map(pow, range(8))) 
# pow przyjmuje 2 argumenty, tu mamy 1

"""
)

print('3.3:')
for i in range(31): #moza tez for i in range(1,30)
    if(i%3 != 0):
        print(f"{i} ", end='')
        
print('')

print('\n3.8:')
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

print('3.9:')
L = [[],[4],(1,2),[3,4],(5,6,7)]
    
result = [sum(x) for x in L]
    
print(f"{L} \n{result}")

print('\n3.10:')
roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_to_arabic_2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

roman_to_arabic_3 = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic = [1, 5, 10, 50, 100, 500, 1000]

roman_to_arabic_4 = dict(zip(roman, arabic))

print(f"klasycznie: \n{roman_to_arabic}")
print(f"dict(): \n{roman_to_arabic_2}")
print(f"lista krotek: \n{roman_to_arabic_3}")
print(f"zip: \n{roman_to_arabic_4}")

def roman2int(s: str) -> int:

    sum = roman_to_arabic[s[-1]]

    for i in range(len(s) - 1):
        if (roman_to_arabic[s[i + 1]] <= roman_to_arabic[s[i]]):
            sum += roman_to_arabic[s[i]]
        else:
            sum -= roman_to_arabic[s[i]]
    
    return sum

print(f"III: {roman2int("III")}")  
print(f"XIV: {roman2int("XIV")}")  
print(f"CXXIII: {roman2int("CXXIII")}") 
print(f"CMLXXXVII: {roman2int("CMLXXXVII")}")  
print(f"MMXXIV: {roman2int("MMXXIV")}") 
print(f"MMDCCXVIII: {roman2int("MMDCCXVIII")}\n")

print("Funckja nie sprawdza bledow i nie rzuca wyjatkow, \
ale sama konwersja dziala dobrze")
