res = "S"
quant = 0
maior = 0
menor = 0
media = 0
soma = 0
while res in "Ss":
    num = int(input("Digite um valor:"))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input("Quer continuar? [S/N}")).upper().strip()[0]
media = soma / quant
print("Voce Digitou {} numeros e a media foi {:.2f}\n O maior numero foi {} e menor numero foi {}".format(quant, media, maior,menor))
print("FiM")
