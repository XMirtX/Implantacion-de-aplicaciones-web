import sys

from math import pi

radio = int(sys.argv[1])

if radio >= 0:
    print("Menú 1 Diametro")
    print("Menú 2 Perimetro")
    print("Menú 3 Area")
    print("Menú 4 Exit")

shell = int(input("Elige Menú"))
if shell >= 1 and shell <= 4:
    if shell == 1:
        print("Diametro", 2 * radio)
    if shell == 2:
        print("Perimetro", 2 * pi * radio)
    if shell == 3:
        print("Area", pi * radio**2)
    if shell == 4:
        print("Bye")
