from random import randint
from  time import sleep
print("\033[7:331mJOKENPÔ")
itens = ("Pedra", "Papel","Tesoura")
comp = randint(0 , 2)
print('''Suas opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = (int(input("Qual é sua jogada?")))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
sleep(1)
print("-="*11)
print("Computador jogou {}".format(itens[comp]))
print("Jogador jogou {}".format(itens[jogador]))
print("-="*11)
if comp == 0:
    if jogador == 0:
     print("EMPATE")

    elif jogador == 1:
     print("JOGADOR VENCE")


    elif jogador == 2:
     print("COMPUTADOR VENCE")

    else:
     print("Jogada invalida!")

elif comp == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")

    elif jogador == 1:
        print("EMPATE")


    elif jogador == 2:
        print("COMPUTADOR VENCE")

    else:
        print("Jogada invalida!")



elif comp == 2:
    if jogador == 0:
        print("JOGADOR VENCE")

    elif jogador == 1:
        print("COMPUTADOR VENCE")


    elif jogador == 2:
        print("EMPATE")

    else:
        print("Jogada invalida!")






