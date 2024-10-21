word = "jakistamnapis"

for i in range(len(word)):
    print(word[i], end='')
    if i != len(word) - 1:
        print("_", end='')
    
print("")

#Szybciej: 

print("_".join(word))
