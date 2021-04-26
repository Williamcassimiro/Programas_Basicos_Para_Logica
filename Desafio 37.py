#Programa para converção
n = int(input("\033[7;30mInfome um numero inteiro:"))
print('''\033[1;31mEscolha um das bases para converção:\033[m
\033[1;31m[1] Converção para BiNARIA:\033[m
\033[1;31m[2] Converção para OCTA:\033[m
\033[1;31m[3] Converção para HEXADECIMAL:\033[m''')
opçao = int(input("\033[7;32mSua opção:"))
if opçao == 1:
   print("{} convertido para BINARIO é igual {}\033[m".format(n, bin(n)[2:]))

elif opçao == 2:
    print("{} converção para OCTAL é igual {}\033[m".format(n, oct(n)[2:]))
elif opçao == 3:
    print("{} converção para HEXADECIMAL é igual {}\033[m".format(n, hex(n)[2:]))
else:
    print("Numero invalido\033[m")