cont = 0
soma = 0

while True:
    num = int(input("Digite um Valor( 999  para parar):"))
    if num == 999:

        break
    cont += 1
    soma += num
print(f"Total de valores digitados foram {cont}, Sua soma entre eles é {soma}")
print("Fim do programa ")