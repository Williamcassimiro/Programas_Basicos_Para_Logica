pessoas = dict()
listapessoas = list()
mulheres = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input("Nome:"))
    while True:
        pessoas['Sexo'] = str(input("Sexo:[F/M]")).upper().strip()
        if pessoas['Sexo'] in "FM":
                break
        print("Erro... Digite apenas [F/ M]")
    pessoas['Idade'] = int(input("Idade:"))
    soma += pessoas['Idade']
    listapessoas.append(pessoas.copy())
    while True:
        opçao = str(input("Deseja continuar?[S/N]")).strip().upper()
        if opçao in "SN":
            break
        print("Digite apenas S ou N.")
    if opçao == 'N':
        break
# A) Quantas pessoa tem na lista
print(f"Ao todo temos {len(listapessoas)} pessoas cadastratadas.")

# B) Media da galetada lista
media = soma / len(listapessoas)
print(f"A media de idade da galera  é {media:5.2f}")

# c) Uma lista com toda as mulheres

print("As  mulheres cadastradas foran", end= " ")
for p in listapessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end= " ")
print()

# lista de pessoas acima da media

print("Lista das pessoas que estão acima da media: ", end=" ")
for p in listapessoas:
    if p["Idade"] >= media:
        print(f"{p['Nome']}")
print()







