from random import randint
from time import sleep
# Bibloteca que mostra que da um atrazo no time( tempo)
comp = randint(0, 5)  # Faz computador pensar.
#print(comp) #colinha haha
jogador = int(input("ADVINHE QUEM NUMERO EU PENSEI:"))
print("PROSSESANDO......")
sleep(1)
if comp == jogador:
     print("PARABENS VOCE ACERTOU")
else:
    print("VOCE ERROU")
    print("EU PENSEI NUMERO {} E VC NO NUMERO {}".format(comp, jogador))
print("TENTE NOVAMENTE!")