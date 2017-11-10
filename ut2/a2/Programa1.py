import sys

from math import sqrt

a = int(sys.argv[1])

b = int(sys.argv[2])

c = int(sys.argv[3])

if a == 0:
    print("x =", -c / b)

elif b**2 - 4 * a * c < 0:
    print ("No tinene solución real")

else:
    print ("x1=", (-b + sqrt(b**2 - 4 * a * c) / 2 * a))
    print ("x2=", (-b - sqrt(b**2 - 4 * a * c) / 2 * a))