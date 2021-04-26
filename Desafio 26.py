frase = str(input("Infome um frase: ")).upper().strip()
print("A letra A aparece {} vezer na frase".format(frase.count("A")))
print(" A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print(" A Ultima letra A apareceu na posição {} ".format(frase.rfind("A")+1))