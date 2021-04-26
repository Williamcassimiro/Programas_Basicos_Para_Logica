""" num = cont = soma = 0 outra maneira mais siples de ser feita"""
num = 0
cont = 0
soma = 0
num = int(input("Digite um numero [ 999 para parar]: "))
while num != 999:
    soma = num + num
    cont = cont + 1
    num = int(input("Digite um numero [ 99 para parar]: "))
print("Voce digitou {} numeros e a soma entre eles foi {}".format(cont, soma))
print("Acabou")