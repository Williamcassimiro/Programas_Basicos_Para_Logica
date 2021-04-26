
frase = str(input("Digite uma Frase:")).split()
paravras = frase
junto = "".join(paravras)
inverso = junto[::-1]
"""for letra in range (len(junto) -1, -1, -1): # usando outras maneira... 
    inverso = inverso + junto[letra]"""

if inverso == junto:
    print("Temos um Palindromo")
    print("Você digitou a frase {}".format(junto))
    print("A inversão {}".format(inverso))
else:
    print("A frase não é um Palindromo")
    print("Você digitou a frase {}".format(junto))
print("fim... ")