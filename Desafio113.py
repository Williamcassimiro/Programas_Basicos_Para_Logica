"""def leiaint(mensagem):
    ok =False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print("\033[0:31mErro! Informe um numero inteiro valido.\033[m")
        if ok:
            break
    return valor"""

def leiadinhero(msg):
    valido =False
    while not valido:
        entrada = str(input(msg)).replace(',' , '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f"\033[0;31mERRO: \"{entrada}\" é um numero invalido!\033[m")
        else:
            valido = True
            return float(entrada)

def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digitar um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return  numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digitar um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return numero





#Programa principal
numero1 = leiaint('Digite um numero interio:')
numero2 = leiadinhero('Digite um numero real:')
print(f'Voce acabou de digitar o número {numero1} e o real foi {numero2}')
