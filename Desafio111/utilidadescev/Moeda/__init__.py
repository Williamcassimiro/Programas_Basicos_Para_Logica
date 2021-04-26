#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminur(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if formato is False else moeda(res)
    #return res if not formato else moeda(res)


def metade(preço = 0, formato = False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda ( preço = 0, moeda = "R$"):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

def resumo (preço = 0, taxaa = 10 , taxar = 5):
    print("-"*30)
    print(' Resumo do valor'.center(30))
    print("-" * 30)
    print(f'Preço analizado:\t{moeda(preço)}')
    print(f"A metade do preço:\t{metade(preço, True)}")
    print(f"A Dobro do preço:\t{dobro(preço, True)}")
    print(f"Aumentado {taxaa}:   \t{aumentar(preço,taxaa, True)}")
    print(f"Reduzindo {taxar}:     \t{diminur(preço,taxar, True)}")
    print("-" * 30)
