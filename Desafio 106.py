#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
# o programa se encerrará. Importante: use cores.


from time import sleep
cores = ('\033[m',          # 0 - sem cor
         '\033[7;30m',      # 1 - branco
         '\033[1;30;41m',   # 2 - vermelho
         '\033[1;30;42m',   # 3 - verde
         '\033[1;30;43m',   # 4 - amarelo
         '\033[1;30;44m',   # 5 - roxo
         '\033[1;30:45m',   # 6 - cinza
         '\033[1;30;46m',   # 7 - magenta
         '\033[1:30;47m',   # 8 - cinza
         )


def ajuda(com):
    titulo(f"ACESSANDO O MANULA DO COMODANDO \'{com}\' ", 4)
    print(cores[1], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def titulo (msg, cor=0):
    tamanho = len(msg) +4
    print(cores[cor], end='')
    print("~"*tamanho)
    print(f' {msg}' )
    print("~"*tamanho)
    print(cores[0], end='')
    sleep(1)


#Programa principal

comando =''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Funçao ou Biclioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo("ATE LOGO!", 2)