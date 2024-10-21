line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Fusce interdum molestie dictum. Curabitur non consequat nisl. 
Praesent ultricies vehicula libero. Orci varius natoque 
penatibus et magnis dis parturient montes, nascetur ridiculus mus."""

alf_sorted = sorted(line.split())

length_sorted = sorted(line.split(), key=len)

print("alf_sorted: \n{} \nlength_sorted: \n{}".format(alf_sorted, length_sorted ))
