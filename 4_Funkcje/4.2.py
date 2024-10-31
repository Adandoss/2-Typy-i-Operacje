def make_ruler(n): 
    miarka = ''

    for i in range(n):
        miarka += "|...."
    
    miarka += "|\n0"

    for i in range(1, n+1):
        miarka += "{0:>5}".format(i)

    return miarka

def make_grid(rows, cols): 
    siatka1 = '+'
    siatka2 = '|'

    for i in range(rows):
        siatka1 += '---+'
        siatka2 += "{0:>4}".format("|")

    siatka1 += '\n'
    siatka2 += '\n'
    
    siatka = ''    

    for i in range(cols):
        siatka += siatka1
        siatka += siatka2

    siatka += siatka1
    
    return siatka
    
print(f"make_ruler(12): \n{make_ruler(12)}\n\n")
print(f"make_grid(4, 6): \n{make_grid(4, 6)}")


