soma = 0
cont = 0
for c in range(1 , 7):
    num = int(input("Informe uma numero:"))
    if num % 2 == 0:
     soma = soma + num
     cont = cont + 1
print("Voce informou só {} numero pares, Soma {}".format(cont, soma))