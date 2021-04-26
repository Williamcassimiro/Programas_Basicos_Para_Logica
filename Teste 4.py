def serieResistor():
    r1 = int(input("Digite o valor do resistor 1: "))
    r2 = int(input("Digite o valor do resistor 2: "))
    r3 = int(input("Digite o valor do resistor 3: "))
    if r1 < 0 or r2 < 0 or r3 < 0:
        print("Valor inválido")
    valores = r1 + r2 + r3
    itotal = int(input("Digite o valor de I: "))
    utotal = itotal * valores
    itotal = utotal / valores
    print("O valor da resistencia em série é: ", valores, "e a intensidade da corrente é de: ", itotal)


def paraleloResistor():
    R1 = int(input("Digite o valor do primeiro resistor: "))
    R2 = int(input("Digite o valor do segundo resistor: "))
    R3 = int(input("Digite o valor do terceiro resistor: "))
    if R1 < 0 or R2 < 0 or R3 < 0:
        print("Valor inválido: ")
        R1 = int(input("Digite o valor do primeiro resistor: "))
        R2 = int(input("Digite o valor do segundo resistor: "))
        R3 = int(input("Digite o valor do terceiro resistor: "))
    Req = 1 / ((1 / R1) + (1 / R2) + (1 / R3))
    i1 = int(input("Digite o valor de I1: "))
    i2 = int(input("Digite o valor de I2: "))
    i3 = int(input("Digite o valor de I3: "))
    itotal = i1 + i2 + i3
    vtotal = itotal * Req
    itotal2 = vtotal / Req
    print("O valor da resistência em paralelo é: ", Req, "e a intensidade é de: ", itotal2)


def circuitoMisto():
    aux = '0.0'
    R1 = int(input("Digite o valor de R1: "))
    R2 = int(input("Digite o valor de R2: "))
    R3 = int(input("Digite o valor de R3: "))
    aux = ((R1 * R2) / (R1 + R2))
    Req = aux + R3
    if R1 < 0 or R2 < 0 or R3 < 0:
        print("Valor inválido: ")
        R1 = int(input("Digite o valor de R1: "))
        R2 = int(input("Digite o valor de R2: "))
        R3 = int(input("Digite o valor de R3: "))
    print("O valor das resistências é de ", Req)


def CodigoCores():
    print("Digite o número correspondente da cor da primeira faixa do seu resistor")
    faixa11 = int(
        input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    while faixa11 > 9:
        print("Valor Inválido")
        faixa11 = int(input(
            "0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    print("Digite o número correspondente da cor da segunda faixa do seu resistor")
    faixa21 = int(
        input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    while faixa21 > 9:
        print("Valor Inválido")
        faixa21 = int(input(
            "0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    print("Digite o número correspondente da cor da terceira faixa do seu resistor")
    faixa31 = int(input("1=marrom, 2=vermelho, 3=laranja, 4=amarelo: "))
    while faixa31 > 4:
        print("Valor inválido")
        faixa31 = int(input("Digite um valor de 1 até 4: "))
    faixa11 = (str(faixa11))
    faixa21 = (str(faixa21))
    resistor1 = faixa11 + faixa21
    resistor1 = (int(resistor1))
    if faixa31 == 1:
        resistortot = (resistor1 * 10)
    if faixa31 == 2:
        resistortot = (resistor1 * 100)
    if faixa31 == 3:
        resistortot = (resistor1 * 1000)
    if faixa31 == 4:
        resistortot = (resistor1 * 10000)
    print("O valor do seu resistor é de: ", resistortot)
    print("Digite o número correspondente da cor da primeira faixa do seu resistor")
    faixa12 = int(input(
        "'0' preto, '1' marrom, '2' vermelho, '3' laranja, '4' amarelo, '5' verde, '6' azul, '7' violeta, '8' cinza e '9' branco : "))
    while faixa12 > 9:
        print("Valor Inválido")
        faixa12 = int(input(
            "0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    print("Digite o número correspondente da cor da segunda faixa do seu resistor")
    faixa22 = int(
        input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    while faixa22 > 9:
        print("Valor Inválido")
        faixa22 = int(input(
            "0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    print("Digite o número correspondente da cor da terceira faixa do seu resistor")
    faixa32 = int(input("'1' marrom, '2' vermelho, '3' laranja, '4' amarelo: "))
    while faixa32 > 4:
        print("Valor inválido")
        faixa32 = int(input("Digite um valor de 1 até 4: "))
    faixa12 = (str(faixa12))
    faixa22 = (str(faixa22))
    resistor2 = faixa12 + faixa22
    resistor2 = (int(resistor2))
    if faixa32 == 1:
        resistortot = (resistor2 * 10)
    if faixa32 == 2:
        resistortot = (resistor2 * 100)
    if faixa32 == 3:
        resistortot = (resistor2 * 1000)
    if faixa32 == 4:
        resistortot = (resistor2 * 10000)
    print("O valor do seu resistor é de: ", resistor2)
    print("Digite o número correspondente da cor da primeira faixa do seu resistor")
    faixa13 = int(input(
        "'0' preto, '1' marrom, '2' vermelho, '3' laranja, '4' amarelo, '5' verde, '6' azul, '7' violeta, '8' cinza e '9' branco : "))
    while faixa13 > 9:
        print("Valor Inválido")
        faixa13 = int(input(
            "0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    print("Digite o número correspondente da cor da segunda faixa do seu resistor")
    faixa23 = int(
        input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    while faixa13 > 9:
        print("Valor Inválido")
        faixa11 = int(input(
            "0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
    print("Digite o número correspondente da cor da terceira faixa do seu resistor")
    faixa33 = int(input("'1' marrom, '2' vermelho, '3' laranja, '4' amarelo: "))
    while faixa33 > 4:
        print("Valor inválido")
        faixa33 = int(input("Digite um valor de 1 até 4: "))
    faixa13 = (str(faixa13))
    faixa23 = (str(faixa23))
    resistor3 = faixa13 + faixa23
    resistor3 = (int(resistor3))
    if faixa33 == 1:
        resistortot = (resistor3 * 10)
    if faixa31 == 2:
        resistortot = (resistor3 * 100)
    if faixa31 == 3:
        resistortot = (resistor3 * 1000)
    if faixa31 == 4:
        resistortot = (resistor3 * 10000)
    print("O valor do seu resistor é de: ", resistor3)

    resistoreserie = resistor1 + resistor2 + resistor3
    resistormisto = ((resistor1 * resistor2) / (resistor1 + resistor2)) + resistor3
    resistorparalelo = 1 / ((1 / resistor1) + (1 / resistor2) + (1 / resistor3))
    resistoreserie = "%.2f" % (resistoreserie)
    resistormisto = "%.2f" % (resistormisto)
    resistorparalelo = "%.2f" % (resistorparalelo)
    print("As resistências em misto tem o valor de: ", resistormisto)
    print("As resistencias em paralelo tem o valor de: ", resistorparalelo)
    print("As resistencias em serie tem o valor de: ", resistoreserie)


def maisumaoperacao():
    operatmod = input("Digite se gostaria de dar entrada de valores = 1 ou código de cores = 2: ")
    if operatmod == "1":
        tipocircuito = input("Qudef serieResistor ():
  r1 = int(input("Digite o valor do resistor 1: "))
  r2 = int(input("Digite o valor do resistor 2: "))
  r3 = int(input("Digite o valor do resistor 3: "))
  if r1 < 0 or r2 < 0 or r3 < 0:
    print("Valor inválido")
  valores = r1 + r2 + r3
  itotal = int(input("Digite o valor de I: "))
  utotal = itotal*valores
  itotal = utotal/valores
  print ("O valor da resistencia em série é: ", valores, "e a intensidade da corrente é de: ", itotal)

def paraleloResistor ():
  R1 = int(input("Digite o valor do primeiro resistor: "))
  R2 = int(input("Digite o valor do segundo resistor: "))
  R3 = int(input("Digite o valor do terceiro resistor: "))
  if R1 < 0 or R2 < 0 or R3 <0:
    print("Valor inválido: ")
    R1 = int(input("Digite o valor do primeiro resistor: "))
    R2 = int(input("Digite o valor do segundo resistor: "))
    R3 = int(input("Digite o valor do terceiro resistor: "))
  Req = 1/((1/R1)+(1/R2)+(1/R3))
  i1 = int(input("Digite o valor de I1: "))
  i2 = int(input("Digite o valor de I2: "))
  i3 = int(input("Digite o valor de I3: "))
  itotal = i1+i2+i3
  vtotal = itotal*Req
  itotal2 = vtotal/Req
  print("O valor da resistência em paralelo é: ", Req, "e a intensidade é de: ", itotal2)

def circuitoMisto():
  aux = '0.0'
  R1 = int(input("Digite o valor de R1: "))
  R2 = int(input("Digite o valor de R2: "))
  R3 = int(input("Digite o valor de R3: "))
  aux = ((R1*R2)/(R1+R2))
  Req = aux + R3
  if R1 < 0 or R2 < 0 or R3 <0:
    print("Valor inválido: ")
    R1 = int(input("Digite o valor de R1: "))
    R2 = int(input("Digite o valor de R2: "))
    R3 = int(input("Digite o valor de R3: "))
  print ("O valor das resistências é de ", Req)

def CodigoCores ():
  print ("Digite o número correspondente da cor da primeira faixa do seu resistor")
  faixa11 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  while faixa11 > 9:
    print("Valor Inválido")
    faixa11 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  print ("Digite o número correspondente da cor da segunda faixa do seu resistor")
  faixa21 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  while faixa21 > 9:
    print("Valor Inválido")
    faixa21 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  print ("Digite o número correspondente da cor da terceira faixa do seu resistor")
  faixa31 = int(input("1=marrom, 2=vermelho, 3=laranja, 4=amarelo: "))
  while faixa31 > 4:
    print("Valor inválido")
    faixa31 = int(input("Digite um valor de 1 até 4: "))
  faixa11 = (str(faixa11))
  faixa21 = (str(faixa21))
  resistor1 = faixa11 + faixa21
  resistor1 = (int(resistor1))
  if faixa31 == 1:
    resistortot = (resistor1 * 10)
  if faixa31 == 2:
    resistortot = (resistor1 * 100)
  if faixa31 == 3:
    resistortot = (resistor1 * 1000)
  if faixa31 == 4:
    resistortot = (resistor1 * 10000)  
  print ("O valor do seu resistor é de: ", resistortot)
  print ("Digite o número correspondente da cor da primeira faixa do seu resistor")
  faixa12 = int(input("'0' preto, '1' marrom, '2' vermelho, '3' laranja, '4' amarelo, '5' verde, '6' azul, '7' violeta, '8' cinza e '9' branco : "))
  while faixa12 > 9:
    print("Valor Inválido")
    faixa12 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  print ("Digite o número correspondente da cor da segunda faixa do seu resistor")
  faixa22 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  while faixa22 > 9:
    print("Valor Inválido")
    faixa22 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  print ("Digite o número correspondente da cor da terceira faixa do seu resistor")
  faixa32 = int(input("'1' marrom, '2' vermelho, '3' laranja, '4' amarelo: "))
  while faixa32 > 4:
    print("Valor inválido")
    faixa32 = int(input("Digite um valor de 1 até 4: "))
  faixa12 = (str(faixa12))
  faixa22 = (str(faixa22))
  resistor2 = faixa12 + faixa22
  resistor2 = (int(resistor2))
  if faixa32 == 1:
    resistortot = (resistor2 * 10)
  if faixa32 == 2:
    resistortot = (resistor2 * 100)
  if faixa32 == 3:
    resistortot = (resistor2 * 1000)
  if faixa32 == 4:
    resistortot = (resistor2 * 10000)  
  print ("O valor do seu resistor é de: ", resistor2)
  print ("Digite o número correspondente da cor da primeira faixa do seu resistor")
  faixa13 = int(input("'0' preto, '1' marrom, '2' vermelho, '3' laranja, '4' amarelo, '5' verde, '6' azul, '7' violeta, '8' cinza e '9' branco : "))
  while faixa13 > 9:
    print("Valor Inválido")
    faixa13 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  print ("Digite o número correspondente da cor da segunda faixa do seu resistor")
  faixa23 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  while faixa13 > 9:
    print("Valor Inválido")
    faixa11 = int(input("0=preto, 1=marrom, 2=vermelho, 3=laranja, 4=amarelo, 5=verde, 6=azul, 7=violeta, 8=cinza e 9=branco : "))
  print ("Digite o número correspondente da cor da terceira faixa do seu resistor")
  faixa33 = int(input("'1' marrom, '2' vermelho, '3' laranja, '4' amarelo: "))
  while faixa33 > 4:
    print("Valor inválido")
    faixa33 = int(input("Digite um valor de 1 até 4: "))
  faixa13 = (str(faixa13))
  faixa23 = (str(faixa23))
  resistor3 = faixa13 + faixa23
  resistor3 = (int(resistor3))
  if faixa33 == 1:
    resistortot = (resistor3 * 10)
  if faixa31 == 2:
    resistortot = (resistor3 * 100)
  if faixa31 == 3:
    resistortot = (resistor3 * 1000)
  if faixa31 == 4:
    resistortot = (resistor3 * 10000)  
  print ("O valor do seu resistor é de: ", resistor3)
  
  resistoreserie = resistor1 + resistor2 + resistor3
  resistormisto = ((resistor1*resistor2)/(resistor1+resistor2)) + resistor3
  resistorparalelo = 1/((1/resistor1)+(1/resistor2)+(1/resistor3))
  resistoreserie = "%.2f"%(resistoreserie)
  resistormisto = "%.2f"%(resistormisto)
  resistorparalelo = "%.2f"%(resistorparalelo)
  print("As resistências em misto tem o valor de: ", resistormisto)
  print("As resistencias em paralelo tem o valor de: ", resistorparalelo)
  print("As resistencias em serie tem o valor de: ", resistoreserie)

def maisumaoperacao():
  operatmod = input("Digite se gostaria de dar entrada de valores = 1 ou código de cores = 2: ")
  if operatmod == "1":
    tipocircuito = input("Qual o tipo do circuito? 1 = série, 2 = paralelo e 3 = misto: ")
    if tipocircuito == "1":
      serieResistor()
    if tipocircuito == "2":
      paraleloResistor()
    if tipocircuito == "3":
      circuitoMisto()
  if operatmod == "2":
   CodigoCores()

print("Bem vindo, por favor apenas digite valores válidos")
operatmod = input("Digite se gostaria de dar entrada de valores = 1 ou código de cores = 2: ")
if operatmod == "1":  
  tipocircuito = input("Qual o tipo do circuito? 1 = série, 2 = paralelo e 3 = misto: ")
  if tipocircuito == "1":
    serieResistor()
  if tipocircuito == "2":
    paraleloResistor()
  if tipocircuito == "3":
    circuitoMisto()
if operatmod == "2":
  CodigoCores()
outraoperacao = int(input("Deseja fazer mais uma operação? Sim = 5, Não = 6: "))
while outraoperacao == 5:
  maisumaoperacao()
if outraoperacao == 6:
  print("Muito obrigado! Tenha um bom dia :D")al o tipo do circuito? 1 = série, 2 = paralelo e 3 = misto: ")
        if tipocircuito == "1":
            serieResistor()
        if tipocircuito == "2":
            paraleloResistor()
        if tipocircuito == "3":
            circuitoMisto()
    if operatmod == "2":
        CodigoCores()


print("Bem vindo, por favor apenas digite valores válidos")
operatmod = input("Digite se gostaria de dar entrada de valores = 1 ou código de cores = 2: ")
if operatmod == "1":
    tipocircuito = input("Qual o tipo do circuito? 1 = série, 2 = paralelo e 3 = misto: ")
    if tipocircuito == "1":
        serieResistor()
    if tipocircuito == "2":
        paraleloResistor()
    if tipocircuito == "3":
        circuitoMisto()
if operatmod == "2":
    CodigoCores()
outraoperacao = int(input("Deseja fazer mais uma operação? Sim = 5, Não = 6: "))
while outraoperacao == 5:
    maisumaoperacao()
if outraoperacao == 6:
    print("Muito obrigado! Tenha um bom dia :D")