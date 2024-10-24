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
