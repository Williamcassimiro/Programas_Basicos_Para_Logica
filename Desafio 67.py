# Tabuada v.3
from time import sleep
num = 0
soma = 0
while True:
    print("==TABUADA=="* 5)
    num = int(input("Qual Tabuada gostaria de ver?"))
    if num < 0:
        print("Finalizandoo..")
        sleep(1)
        print("Obrigado volte sempre...")
        break
    print("==TABUADA==" * 5)

    for c in range (1, 11):
        soma = num * c
        print("{} X  {} = {}".format(num,c, soma))
