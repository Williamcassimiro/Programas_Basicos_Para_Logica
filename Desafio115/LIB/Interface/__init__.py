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
def linha(tam = 45):
    return '-' * tam

def cabeçalho( txt ):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(Lista):
    cabeçalho("MENU PRINCIPAL")
    contador = 1
    for item in Lista:
        print(f'\033[33m{contador}\033[m - \033[32m{item}\033[m')
        contador += 1
    print(linha())
    opção = leiaint("\033[36mSua Opção:\033[m")
    return opção
