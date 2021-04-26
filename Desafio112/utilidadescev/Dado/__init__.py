def leiadinhero(msg):
    valido =False
    while not valido:
        entrada = str(input(msg)).replace(',' , '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f"\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m")
        else:
            valido = True
            return float(entrada)

# LEIAINT Feito no exercio 104

def leiaint(mensagem):
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
    return valor


