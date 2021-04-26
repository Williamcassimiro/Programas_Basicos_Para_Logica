from Desafio109 import Moeda
meupreço = float(input("Digite o preço: R$"))
print(f"A metade de {meupreço} é {Moeda.metade(meupreço, True)}")
print(f"A Dobro de {meupreço} é {Moeda.dobro(meupreço, True)}")
print(f"Aumentado 10%, temos R${Moeda.aumentar(meupreço, 10, True)}")
print(f"Reduzindo 13%,  temos R${Moeda.diminur(meupreço, 13, True)}")