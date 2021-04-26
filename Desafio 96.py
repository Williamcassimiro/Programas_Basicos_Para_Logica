# Usando funçoes

def area (l, c):
    a = l * c
    print(f"A área de um terreno {l} x {c} é de {a}m² ")


# Programa para receber os valores

print("Controle de Terrenos ")
print("+"*20)
l = float(input("Largura: "))
c = float(input("Comprimento: "))
area(l,c)