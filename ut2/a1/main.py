import sys

cash = sys.argv[1]

cash = int(cash)

# Varialbles
div_50 = cash // 50
resto_50 = cash % 50

div_20 = resto_50 // 20
resto_20 = resto_50 % 20

div_10 = resto_20 // 10
resto_10 = resto_20 % 10

div_5 = resto_10 // 5
resto_5 = resto_10 % 5

div_2 = resto_5 // 2
resto_2 = resto_5 % 2

div_1 = resto_2 // 1
resto_1 = resto_2 % 1

if div_50 > 0:
    print(div_50, "billetes de 50 €")


if div_20 > 0:
    print(div_20, "billetes de 20 €")


if div_10 > 0:
    print(div_10, "billetes de 10 €")


if div_5 > 0:
    print(div_5, "billetes de 5 €")


if div_2 > 0:
    print(div_2, "billetes de 2 €")

if div_1 > 0:
    print(div_1, "billetes de 1 €")