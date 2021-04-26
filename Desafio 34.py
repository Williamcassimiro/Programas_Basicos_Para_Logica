salario = float(input("Informe seu salario:"))
if salario <= 1249:
    salario = salario+(salario*15/100)
    print("SEU SALARIO TERA UM ALMENTO DE 15% ")
else:
    salario = salario+(salario*10/100)
    print("SEU SALARIO TERA UM ALMENTO DE 10% ")
print("SEU SALARIO É {}".format(salario))
