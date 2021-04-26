numero = int(input("Informe um valor?"))
rest = numero % 2
if rest == 0:
    print("Este numero {} e par!".format(numero))
else:
    print("Esse numero é {} impar!".format(numero))