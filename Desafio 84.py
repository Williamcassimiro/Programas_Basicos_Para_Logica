nomepeso = []
principal = []
contuar = " "
Maior = Menor = cont = 0
while True:
    nomepeso.append(str(input("NOME:")))
    nomepeso.append(float(input("PESO:")))
    if len(principal) == 0:
        Maior = Menor = nomepeso[1]
    else:
        if nomepeso[1] > Maior:
            Maior = nomepeso[1]
        if nomepeso[1] < Menor:
            Menor = nomepeso[1]

    principal.append(nomepeso[:])
    nomepeso.clear()
    cont += 1
    contuar = str(input("DESEJA CONTINUAR? [S/N]").upper().strip())
    if contuar in "N":
        break
print(f"Todo os cantidatos são{principal}")
print(f"Ao todo foi cadastrado {cont} pessoas.")
"""DUAS MANEIRAS LUGAR DO CONTADOR USAR len(lista principal)"""
print(f"O Menor peso é {Menor} da pessoa", end=" ")
for p in principal:
    if p[1] == Menor:
        print(f"{p[0]}", end=" ")
print(f"\nO Maior peso é {Maior} da pessoa", end=" ")
for p in  principal:
    if p[1] == Maior:
        print(f"{p[0]}", end=" ")


