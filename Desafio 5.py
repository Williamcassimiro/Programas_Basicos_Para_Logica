n = input("Digite algo")
print("Seu tipo primitivo é", type(n))
print("Tem espaço ", n.isspace())
print("É um número?", n.isnumeric())
print("É alfabetico", n.isalpha())
print("É um alfanumerico", n.isalnum())
print("Esta em maiuculas", n.isupper())
print("Esta em Minuscula", n.islower())
print("Esta capitalizada",n.istitle())