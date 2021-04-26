lista = [[],[]]
cont1 = cont2 = num = 0
for c in range(0,8):
    num=int(input(f"Digite o {c}° valor:"))
    if num % 2 == 0:
        lista[0].append(num)
        cont1 +=1
    else:
        lista[1].append(num)
        cont2 +=1
    lista[0].sort()
    lista[1].sort()
if cont1 > 0 or cont2 >0 :
 print(f"Os valores PAR digitado {lista[0]},E os valores IMPAR digitados {lista[1]}")
