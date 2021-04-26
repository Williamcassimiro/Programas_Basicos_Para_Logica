lista= []
while True:
    numero =[int(input("Digite uma valor:").upper().strip())]
    if numero not in lista:
        lista.append(numero)
        print("Valor adicionado com sucesso...")

    else:
        print("Valor duplicado, não foi posivel adicionar.")
    seguir = str(input("Deseja continuar: [S/N]").strip().upper())
    if seguir == "N":
        break
print(sorted(lista))


