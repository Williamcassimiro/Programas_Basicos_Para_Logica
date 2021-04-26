from random import sample
from time import sleep
jogos = []
print("\033[:32m="*30)
print("     JOGOS DA MEGA SENA   ")
print("="*30)
numeros = int(input("Quantos jogos voçe deseja sortiar:\033[m"))
print("\033[36m="*6, f"SORTIANDO {numeros} JOGOS", "="*6)
sleep(1)
for c in range(numeros):
     a = sorted(sample(range(1,61),6))
     jogos.append(a[:])
     print(f"Jogo {c+1}: {a}")
     sleep(1.5)
print("="*10, "BOA SORTE","="*10)
