#Analidor completo
media = 0
soma = 0
maioridade = 0
nomemaior = ""
totalmulheres = 0
for pess in range(1,5):
    print("========= {}º Pessoa ++++++++".format(pess))
    nome = str(input("NOME:"))
    idade =int(input("IDADE:"))
    Sexo = str(input("SEXO:[M/F]"))
    soma = soma + idade
    if pess == 1 and Sexo in "Mn":
        nomemaior = nome
        maioridade = idade
    if Sexo in "Mm" and idade > maioridade:
        maioridade = idade
        nomemaior = nome
    if Sexo in "Ff" and idade < 20:
        totalmulheres = totalmulheres + 1
media = soma / pess
print("A media de idade do grupo é {} anos".format(media))
print("Nome do mais velho {} e sua idade é {}".format(nomemaior,maioridade))
print("Total de Mulheres é {} ".format(totalmulheres))



