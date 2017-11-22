import sys

dni = int(sys.argv[1])

# Variables
rest = (dni % 23)
id_dni = ("TRWAGMYFPDXBNJZSQVHLCKE")
letter = id_dni[rest]
print(f"{dni}-{letter}")
