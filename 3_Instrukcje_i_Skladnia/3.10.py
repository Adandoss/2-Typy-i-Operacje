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