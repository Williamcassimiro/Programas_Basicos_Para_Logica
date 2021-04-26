r1 = float(input("Primeiro seguimento:"))
r2 = float(input("Segundo seguimento:"))
r3 = float(input("Terceiro seguimento:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
  print("Sim, Com {}, {} e {} podem ser montados um trianagulo.".format(r1,r2,r3))
  if r1 == r2 and r2 == r3:
      print("EQUILATERO")
  elif r1 != r2 and r2 != r3 and r1 != r3 : #Outra forma é r1 != r2 != r3 != r1
      print("ESCALENO")
  else:
      print("ISOSCELES")
else:
    print("Não foi posivel montar um triangulo")
