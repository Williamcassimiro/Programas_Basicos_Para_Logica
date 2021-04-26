import uteis #modulos  
#programa principal
num = int(input("Digite um valor:"))
fat = uteis.fatorial(num)
print(f" O fatorial de {num} é {fat}")
print(f" O dobro de {num} é {uteis.dobro(num)}")
print(f" O Triplo de {num} é {uteis.triplo(num)}")