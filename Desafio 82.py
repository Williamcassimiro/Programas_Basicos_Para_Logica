lista = []
lista2 = []
lista3 = []
while True:
    lista.append(int(input("Digite uma numero?")))
    com = str(input("Desejá continuar? [S/N]").upper().strip())
    if com in "N":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista2.append(v)
    elif v % 2 == 1:
        lista3.append(v)
print(f"Os valores digitados são {lista}")
print(f"A lista de pares são {lista2}\ne lista de impates {lista3}")