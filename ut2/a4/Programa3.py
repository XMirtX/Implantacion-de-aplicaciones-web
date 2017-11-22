import sys

number = int(sys.argv[1])
string = str(sys.argv[2])

# Variables
count = 0
if number <= 0:
    print("Error es negativo")
else:
	cadena = string.split(" ")
	for i in cadena:
		if len(i) == number:
			count += 1
	print("Tenemos", count, "palabras de tamaño", number)
