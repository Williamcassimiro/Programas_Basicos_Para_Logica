#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#ndicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    """
      função para calcular o fatorial de um numero
      1:param n: numero a se calcular o fatorial
      2:param show: True = mostra o cauculo / False = esconde o calculo
      3:return: o resultado do fatorial
      """
    f = 1
    for c in range(n, 0 , -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f' X ', end=' ')
            else:
                print(' = ', end=' ')
        f *=c
    return f


print(fatorial(5, show=False))
help(fatorial)