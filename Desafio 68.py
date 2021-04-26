from random import randint
v = 0
while True:
    jogador = int(input("Diga um valor:"))

    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in "PpIi":
        tipo = str(input("Par ou Impar?[P/I]")).strip().upper()[0]
    print(f"Voce jogou {jogador} e o computador {comp}. Total e {total}")
    print("DEU PAR" if total % 2 == 0 else "Deu Impar")
    if tipo == "P":
        if total % 2 == 0:
            print("Voce venceu...")
            v += 1
        else:
            print("Voce perdeu...")
            break

    elif tipo == "I":
        if total % 2 == 1:
            print("Voce venceu...")
            v += 1
        else:
            print("Voce perdeu...")
            break
    print("Vamos jpgar novamente...")
print("Gamer Over! Voce venceu {} vezes".format(v))



