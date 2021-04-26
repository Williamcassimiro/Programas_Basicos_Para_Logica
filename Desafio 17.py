#co = float(input("Informe valor do cateto oposto:"))
#ca = float(input("Infome valor do cateto adjacente:"))
#hi = (co ** 2 + ca**2) ** (1/2)
#print("A hipotenusa será {:.2f}".format(hi))

from math import hypot
co = float(input("Informe valor do cateto oposto:"))
ca = float(input("Infome valor do cateto adjacente:"))
hi= hypot(co, ca)
print("A hipotenusa será {:.2f}".format(hi))
