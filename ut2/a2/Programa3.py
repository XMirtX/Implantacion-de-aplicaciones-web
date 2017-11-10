import sys

nota = float(sys.argv[1])

if nota >= 0 and nota <= 10:
    if nota < 5:
        print("Suspenso")
    if nota == 5:
        print("Aprovado")
    if 5 + 1 <= nota < 6 + 1:
        print("Bien")
    if 7 <= nota < 8:
        print("Notable")
    if nota == 8:
        print("Notable_alto")
    if nota == 9:
        print("Sobresaliente")
    if nota == 10:
        print("Matricula de honor")
else:
    print("Error, Número no valido")
