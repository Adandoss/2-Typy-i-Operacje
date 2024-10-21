line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Fusce interdum molestie dictum. Curabitur non consequat nisl. 
Praesent ultricies vehicula libero. Orci varius natoque 
penatibus et magnis dis parturient montes, nascetur ridiculus mus."""

words = sorted([w for w in line.split()], key=len)
sorted_words = sorted([len(w) for w in line.split()])

print("{} - {}".format(words[-1], sorted_words[-1]))

