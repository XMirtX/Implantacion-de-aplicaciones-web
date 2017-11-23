import sys
number = int(sys.argv[1])
# Variable
suma = 0
if number <= 0:
    print("Error")
else:
    for i in range(1, number + 1):
        suma += i**2
    print(suma)
