from time import sleep
print("="*50)
print("             LANÇAMENTOS DE NOTAS     ")
print("="*50)

estudantes = []
temporaria = []
media = []
while True:
    temporaria.append(str(input("NOME:")))
    temporaria.append(float(input("NOTA 1: ")))
    temporaria.append(float(input("NOTA 2: ")))
    media.append((temporaria[:][1] + temporaria[:][2])/2)
    estudantes.append(temporaria[:])
    temporaria.clear()
    continuar = (str(input("DESEJA CONTINUAR?[S/N]").strip().upper()))
    if continuar == "N":
        break
print("="*50)
print("BOLETIM DA CLASSE")
print("="*50)
print(f'{"NU°"}|{"Nome":^15}|{"MEDIA":^8}')
for c in range(len(estudantes)):
    print(f"{c}  |{estudantes[c][0]:^15}|{media[c]:^8.1f}")
    sleep(1)
print("="*50)
while True:
    print("=" * 50)
    var = int(input("DESEJA VER ALGUMA NOTA DO ALUNO X (DIGITE 999 PARA SAIR: "))
    print("=" * 50)
    if var != 999:
        for a in range(1):
            print(f"NOTA DE {estudantes[var][0]}: {estudantes[var][1:]}")
    elif var == 999:
        break
print("="*50)
print("FINALIZANDO.............")
sleep(1)
print("VOLTE SEMPRE")