import Moeda

meupreço = float(input("Digite o preço: R$"))
print(f"A metade de {meupreço} é {Moeda.metade(meupreço)}")
print(f"A Dobro de {meupreço} é {Moeda.dobro(meupreço)}")
print(f"Aumentado 10%, temos R${Moeda.aumentar(meupreço, 10)}")