total= total1000 = menor = cont = 0
barato =" "
while True:
    nome = str(input("Nome do Produto:"))

    preço =float(input("Preço:R$"))
    cont = cont + 1
    total = total + preço
    if preço > 1000:
        total1000 = total1000 + 1
    if cont == 1: # "or" preço < menor
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    tipo = ' '
    while tipo not in "SsNn":
        tipo = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if tipo == "N":
        break
print("Fim do pragrama ")
print(f"Valor total de todos os produtos {total}")
print(f"Temos {total1000} produto custando Mil reais")
print(f"O produto mais bararto foi {barato} e custa R$ {menor}")