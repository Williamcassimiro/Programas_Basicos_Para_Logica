vel = float(input("Qual a velocidade atula do carro? "))
if vel >= 81:
    valor = (vel-80)*7
    print("MULTADO! Voce passou do limite permitido de 80 Hm/h \nvoce devera pagar {}".format(valor))
else:
    print("OTIMO! esta no limite de 80 Km/h")
print("MUito obrigado tenha bom dia.")

