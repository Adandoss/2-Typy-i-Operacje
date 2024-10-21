line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Fusce interdum molestie dictum. Curabitur non consequat nisl. 
Praesent ultricies vehicula libero. Orci varius natoque 
penatibus et magnis dis parturient montes, nascetur ridiculus mus."""

# Sposob 1:

count = 0

for char in line:
    if char.isalnum():
        count += 1
        
print(count)

# Sposob 2:

count = 0

for w in line.split():
    count += len(w)
    
print(count)

# Sposob 3:

print(sum(len(w) for w in line.split()))
