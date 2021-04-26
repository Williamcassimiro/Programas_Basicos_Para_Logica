viagem = float(input("Qual distancia da sua viagem?"))
'''if viagem <= 200:
    saldo = viagem*0.50
    print("Sua viagem de {} ira custar R${}".format(viagem, saldo))
else:
    saldo = viagem*0.45
    print("Sua viagem de {} ira custar R${}".format(viagem,saldo))
print("Obrigado tenha bom dia!")'''
saldo = viagem*0.50 if viagem <= 200 else viagem*0.45
print("Sua viagem de {} ira custar R${}".format(viagem, saldo))
print("Obrigado tenha bom dia!")

'''Existe duas maneiras ser feitas'''