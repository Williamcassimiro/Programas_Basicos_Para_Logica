matriz = [[],[],[]]
spar = maior = scol = 0
for c in range(0,3):
    for a in range(0,3):
        matriz[c].append(int(input(f"Didite um valor para ({c} {a}): ")))
print("#"*30)
for c in range(0,3):
    #print("\n",end="")if c > 0 else""
    for a in range(0, 3):
        print(f"[{matriz[c][a]:^5}]", end="")
        if matriz[c][a] % 2 == 0:
            spar += matriz[c][a]
    print()
print(f"A Soma dos valores pares é {spar}")
for c in range(0,3):
    scol += matriz[c][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")