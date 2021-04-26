jogadores = list()
jogador = dict()
gol = list()

#Capitura de dados

while True:
    gol.clear()
    jogador["Nome"] = str(input("Nome:"))
    partidas = int(input(f"Quantas partidas jogador {jogador['Nome']} jogou:will"))
    for p in range (1, partidas + 1):
         gol.append(int(input(f"Quanto gol na {p}º foram feitos? ")))
    jogador["Gols"] = gol[:]
    jogador["Total"] = sum(gol)
    jogadores.append(jogador.copy())

    continuar = str(input("Deseja continuar [S/N]")).strip().upper()

    while continuar not in 'N':
            print("Erro, Digite S ou N ")
            continuar = str(input("Deseja continuar [S/N]")).strip().upper()
    if continuar == "N":
        break

#Mostra de Resultados

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

#Terminar aindaaaaa.....