import sys
number = int(sys.argv[1])
number2 = int(sys.argv[2])

if number <= 0:
    print("Error es negativo")
elif number < number2:
    for i in range(number, 0, -1):
        if number % i == 0 and number2 % i == 0:
            print("El mcd es =", i)
            break
elif number > number2:
    number, number2 = number2, number
    for i in range(number, 0, -1):
        if number % i == 0 and number2 % i == 0:
            print("El mcd es =", i)
            break
