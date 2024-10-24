x = int(input("Podaj dlugosc miarki: "))

miarka = ''

for i in range(x):
    miarka += "|...."
    
miarka += "|\n0"

for i in range(1, x+1):
    miarka += "{0:>5}".format(i)

print(miarka)
