import sys

from math import sqrt

x1 = int(sys.argv[1])

y1 = int(sys.argv[2])

x2 = int(sys.argv[3])

y2 = int(sys.argv[4])

x3 = int(sys.argv[5])

y3 = int(sys.argv[6])

# Variables
d1 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
d2 = sqrt((x1 - x3)**2 + (y1 - y3)**2)

if d1 > d2:
    print("El punto mas cercano de", "(", x1, ",", y1, ")", "es", "(", x3, ",", y3, ")", "distancia de", d2)
elif d1 < d2:
    print("El punto mas cercano de", "(", x1, ",", y1, ")", "es", "(", x2, ",", y2, ")", "distancia de", d1)
