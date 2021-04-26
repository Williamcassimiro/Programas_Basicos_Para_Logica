#import math
#angulo = float(input("Informe uma valor Angulo desejado:"))
#seno = math.sin(math.radians(angulo))
#cos = math.cos(math.radians(angulo))
#tan = math.tan(math.radians(angulo))
#print("O angulo de {}, tem \nSeno {:.2f},\nCosseno {:.2f},\nTangente {:.2f}  ".format(angulo, seno, cos, tan)

from math import  radians, sin, cos, tan
angulo = float(input("Informe uma valor angulo desejado:"))
seno = sin(radians(angulo))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
print("O angulo de {}, tem \nSeno {:.2f},\nCosseno {:.2f},\nTangente {:.2f}  ".format(angulo, seno, cose, tang))
