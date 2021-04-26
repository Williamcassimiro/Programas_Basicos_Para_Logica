'''nome=input('Qual é seu nome')
idade=input('Qual é sua Idade')
peso=input('qual é sua peso')
print(nome,idade,peso)'''

# tuplas

lanche = (" B ", " suco ", "pizza")
for c in lanche:
    print(f"Eu {c}")
print(lanche[0:])

for cont in range(0, len(lanche)):
    print(f"EU {lanche[cont]} posição {cont}")
print(len(lanche))

for pos, c in enumerate(lanche):
    print(f"Eu {c} posiçaõ {pos}")