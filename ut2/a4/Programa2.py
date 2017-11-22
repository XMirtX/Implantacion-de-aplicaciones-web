import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

# Variable
a = 0
g = 0
c = 0
t = 0
for char in sequence:
    if char == "A":
        a += 1
    elif char == "G":
        g += 1
    elif char == "C":
        c += 1
    elif char == "T":
        t += 1
print("Adenune:", a)
print("Guanine:", g)
print("Cytosine:", c)
print("Thymine:", t)
