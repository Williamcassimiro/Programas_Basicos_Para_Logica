#validaçõa de dados
sexo = str(input("Informe seu sexo:[M/F]")).strip().upper()[0]
while sexo not in "MnFf":
    sexo = str(input("Dados invalidos, Por favor informe seu sexo:")).strip().upper()[0]
print("Sexo {} regitrado com sucesso".format(sexo))
