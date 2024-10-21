line = """   To see a World in a Grain of Sand
And a Heaven in a Wild Flower
Hold Infinity in the palm of your hand
And Eternity in an hour     """

# line = "a b c"

print(line)

count = 0

for char in line.strip():
    if char.isspace():
        count += 1
        
if count != 0:
    count += 1
        
print("\nLiczba slow: {}\n".format(count))

# Powyzszy kod dziala dla "ladnych" tekstow, ponizej dla brzydszych

line = """    To see a 	World in a 	Grain of 
Sand
And a Heaven   in a 	Wild Flower
Hold 	infinity in the 
palm of your 
hand
And Eternity in an    hour"""

print(line)

# Najszybciej: 

print("\nLiczba slow: {}\n".format(len(line.split())))


count = 0
in_word = False

for char in line.strip():
    if char.isalnum() and in_word == False:
        count += 1
        in_word = True
    elif not char.isalnum():
    	in_word = False
    	
print("\nLiczba slow: {}\n".format(count))

        
        
        
