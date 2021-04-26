matriz = [[],[],[]]
for c in range(0,3):
    for a in range(0,3):
        matriz[c].append(int(input(f"Didite um valor para ({c} {a}): ")))
print("#"*30)
for c in range(0,3):
    #print("\n",end="")if c > 0 else""
    for a in range(0, 3):
        print(f"[{matriz[c][a]:^5}]", end="")
    print()