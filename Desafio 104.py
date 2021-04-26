#Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')
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





#Programa principal
numero = leiaint('Digite um numero:')
print(f'Voce acabou de digitar o número {numero}')
