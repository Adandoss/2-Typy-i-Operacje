line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Fusce interdum molestie dictum. Curabitur non consequat nisl. 
Praesent ultricies vehicula libero. Orci varius natoque 
penatibus et magnis dis parturient montes, nascetur ridiculus mus."""

print("{}\n".format(line))

print("Wyraz z pierwszych znakow kazdego wiersza: ")

for l in line.splitlines():
    print(l.split()[0][0], end='')

print("\nWyraz z ostatnich znakow kazdego wiersza: ")
    
for l in line.splitlines():
    print(l.split()[-1][-1], end='')

print('')

print("\nWyraz z pierwszego znaku kazdego wyrazu: ")

for w in line.split():
    print(w[0], end='')
    
print("\n\nWyraz z ostatniego znaku kazdego wyrazu: ")    

for w in line.split():
    print(w[-1], end='')
    
print('') 

