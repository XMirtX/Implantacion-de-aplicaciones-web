import sys
number = int(sys.argv[1])
if number <= 0:
    print("Error es negativo")
else:
    for i in range(1, number + 1):
        factor = 1
        for f in range(1, i + 1):
            factor *= f
        print(i, "!", factor)
