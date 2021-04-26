# Duas maneiras de fazer, calculo de fatorial
'''from math import factorial
n = int(input("Diga qual numero para somar seu fatorial:"))
fat = factorial(n)
print(" O fatorial do numero {} é {}.".format(n, fat))
# outra maneira'''

n = int(input("Diga qual numero para somar seu fatoria:"))
cont = n
fat = 1
print("Calculando {}! =".format(n), end="")
while cont > 0:
    print("{}".format(cont), end="")
    print(" X " if cont > 1 else " = ", end="")
    fat = fat*cont
    cont = cont-1
print("{}".format(fat))
