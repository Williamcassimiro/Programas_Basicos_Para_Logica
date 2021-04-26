num = []
men = 0
maior = 0

for cont in range(0, 5):
    num.append(int(input(f"Digite um valor na posição {cont} :")))
    if cont == 0:
        men = num[cont]
        maior = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]

        if num[cont] < men:
            men = num[cont]
print("="*30)
print(f"Você digitou o valor {num}")

print(f"O menor valor foi:{men} ", end="")
for p ,v in enumerate(num):
    if v == men:
        print(f"Na poseição {p}")

print(f"maior valor foi:{maior} ", end="")
for p ,v in enumerate(num):
    if v == maior:
        print(f"Na posisçaõ {p}")
