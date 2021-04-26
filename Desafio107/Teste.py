#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from Desafio109 import Moeda

meupreço = float(input("Digite o preço: R$"))
print(f"A metade de {Moeda.moeda(meupreço)} é {Moeda.metade(meupreço, True)}")
print(f"A Dobro de {Moeda.moeda(meupreço)} é {Moeda.dobro(meupreço, True)}")
print(f"Aumentado 10%, temos R${Moeda.aumentar(meupreço, 10, True)}")
print(f'Reduzindo 13%, temos {Moeda.diminur(meupreço, 13, True)}')