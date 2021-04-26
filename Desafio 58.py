from random import randint
comp = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    num = int(input("Advinhe valor sortiado pelo computador:"))
    palpites = palpites + 1
    if num == comp:
        acertou = True
    else:
        if num < comp:
            print("Mais... Tente novamente.")
        elif num > comp :
            print("Menos... Tente novamente.")
print("Parabéns, você acertou: Computador pensou em {} e vocé usou {} tentativas  ".format(comp,palpites))
