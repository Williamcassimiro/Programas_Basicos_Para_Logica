# MENOR E MAIOR VALOR USANDO TUPLAS / COM MAX E MIN
from random import randint
var = (randint (0 , 10),randint (0 , 10),randint (0 , 10),randint (0 , 10),randint (0 , 10))
print(f"Os valores sortiados {var}")
for n in var:
    print(f'{n}', end= " ")
print(f'\nMenor valor sortiados foi {min(var)}')
print(f"Maior valor sortiado foi {max(var)}")