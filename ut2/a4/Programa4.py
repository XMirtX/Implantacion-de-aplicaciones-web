import sys

# Variable
number = sys.argv[1:]
suma = 0
count = len(number)
for i in number:
    i = float(i)
    suma += i
avg = suma / count
print("La media de los valores es:", avg)
