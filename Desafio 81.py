lista = []
cont = 0
while True:
    num = int(input("Digite um valor?"))
    if num not in lista:
        lista.append(num)
        cont +=1
    else:
        print("Valor repetido ")
        cont += 1

    com = str(input("Desejá continuar? [S/N]").upper().strip())
    if com == "N":
        break
print("Voce digitou {}, Caso voce repetiu algum numero não sera contado na quantidade de vezes".format(cont))
lista.sort(reverse=True)
print(f"O valores da lista são {lista} , Caso voce repetiu algum numero não sera contado na quantidade de vezes")

if 5 in lista:
    print("O valor 5 faz parte da Lista")
else:
    print("O valor 5 nâo faz parte da lista ")