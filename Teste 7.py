 # Usando Listas
valores = list()
valores.append(5)
valores.append(4)
valores.append(9)
for c,n in enumerate(valores):
     print(f"Na posição {c} encontrei o valor {n}")
print("Fim da lista")


valores = list()
for cont in range (0,5):
    valores.append(int(input("Informe um valor: ")))
for c, n in enumerate(valores):
     print(f"Na posição {c} encontrei o valor {n}")
print("Fim da lista")

a = [4,5,4,75,7]
b = a[:]
b[2] = 8
print(f"Valor de {b}")