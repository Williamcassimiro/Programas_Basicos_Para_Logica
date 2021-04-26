peso =  float(input("Qual seu peso?(KG)"))
altura = float(input("Qual sua altura?(M)"))
IMC = peso / (altura ** 2)
print("O IMC Dessa pessoa é de {:.1f}".format(IMC))
if IMC < 18.5:
    print("VOCÊ ESTÁ ABAIXO DO PESO")
elif IMC >= 18.5 and IMC < 25:
    print("VOCÊ ESTÁ NO PESO IDEAL, PARABENS")
elif IMC >= 25 and IMC < 30:
    print("VOCÊ ESTA NA CATEGORIA SOBREPESO")
elif IMC >= 30 and IMC <= 40:
    print("ATEÇÂO >>>>>>>> OBESIDADE")
else:
    print("URGENTE >>>>>>>> OBESIDADE MÓRBIDA")
print("FIM")