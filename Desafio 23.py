#numero = int(input("Infome um numero:"))
#num = str(numero)
#print("Analizando numero{}".format(numero))
#print("Unidade:{}".format(num[3]))
#print("Dezena: {}".format(num[2]))
#print("Centena: {}".format(num[1]))
#print("Milhar: {}".format(num[0]))
# funciona mais tem que ser só 4 digitos.

numero = int(input("Infome um numero:"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analizando numero{}".format(numero))
print("Unidade:{}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

 # Essa maneira correta sem usar modo de repetição
