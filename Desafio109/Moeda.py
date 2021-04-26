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