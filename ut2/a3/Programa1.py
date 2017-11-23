import sys
number = int(sys.argv[1])
if number <= 0:
    sys.exit
else:
    for i in range(2, number):
        if number % i == 0:
            print ("El numero no es primo")
            break
    else:
        print ("Es Primo")
