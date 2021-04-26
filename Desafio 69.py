# Analizando dados
total1 = totalH = total20 = 0
while True:

    print("-"*25)
    print("   CADASTRE UMA PESSOA ")
    print("-" *25)
    idade = int(input("Idade:"))
    sexo =" "
    while sexo not in "MF":
         sexo = str(input("Sexo[M/F]:")).strip().upper()[0]
    if idade >= 18:
        total1 += 1
    if sexo == "M":
        totalH +=1
    if sexo == "F" and idade < 20:
        total20
    tipo =" "
    while tipo not  in "SN":
        tipo = str(input("Quer continar? [S/N]")).strip().upper()[0]
    if tipo == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {total1},\nAo todo temos  {totalH} homens cadastrado,\nE temos {total20} mulheures com menos de 20 anos ")

