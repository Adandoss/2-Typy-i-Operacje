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
