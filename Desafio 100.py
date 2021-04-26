from random import randint
from time import sleep

def sorteia(lista):
    print("Sortenado 5 numeros da lista: " , end=" ")
    for cont in range(0 , 5):
        n = randint(1, 10)
        lista.append(n)
        print(f" {n}", end=" ")
        sleep(0.3)
    print("Pronto...")

def somaPAr(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista} é {soma} ")




numero = list()
sorteia(numero)
somaPAr(numero)