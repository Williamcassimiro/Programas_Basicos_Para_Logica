#Analise de dados
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1,8):
    nasc = int(input("Em que ano {}º a pessoa nasceu?".format(pess)))
    idade = atual - nasc
    if idade >= 21:
     totalmaior = totalmaior + 1
    else:
     totalmenor = totalmenor + 1

print("Ao todo tivemos {} pessoas maiores de  idade".format(totalmaior))
print("E tambem tivemos {} pessoas menores de idade".format(totalmenor))