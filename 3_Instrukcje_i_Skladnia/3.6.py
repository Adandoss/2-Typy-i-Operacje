x = int(input("Podaj dlugosc siatki: "))
y = int(input("Podaj wysokosc siatki: "))

siatka1 = '+'
siatka2 = '|'

for i in range(x):
    siatka1 += '---+'
    siatka2 += "{0:>4}".format("|")

siatka1 += '\n'
siatka2 += '\n'
    
siatka = ''    

for i in range(y):
    siatka += siatka1
    siatka += siatka2

siatka += siatka1

print(siatka)
