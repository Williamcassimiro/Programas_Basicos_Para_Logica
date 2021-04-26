#PESO < > MENOR E MAIOR:
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input("Peso da {}º pessoa:".format(pess)))
    if pess == 1:
     menor = peso
     maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido de {} Kg".format(maior))
print("O menor peso lido de  {}kg".format(menor))


