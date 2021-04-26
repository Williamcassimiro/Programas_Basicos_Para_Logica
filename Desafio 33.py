a = int(input("PRIMEIRO VALOR:"))
b = int(input("SEGUNDO VALOR:"))
c = int(input("TERCEIRO VALOR:"))
'''Para melhorar codigo tirando if menor = a ja no começo, fazer apenas duas comparação'''
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if a > b and a > c:
        maior = a
if b > a and b > c:
        maior = b
if c > a and c > b:
        maior = c
print("O MENOR VALOR {}".format(menor))
print("O MAIOR VALOR {}".format(maior))