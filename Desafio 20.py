import random
n1= str(input("Primero nome:"))
n2 = str(input("Segundo nome:"))
n3 = str(input("Terceito nome"))
n4 = str(input("QUarto nome: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem sera:")
print(lista)