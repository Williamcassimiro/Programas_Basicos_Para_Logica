#Exercício Python 105: Faça um programa que tenha uma função notas()
#que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
def notas (*numeros, situação = False):
    """ > Função para analisar notas e situações de vários alunos.
    1:param args: Uma ou mais notas dos alunos (aceita várias)
    2:param sit: valor opcional, indicando se deve ou não adicionar a situação
    3:return: dicionário com várias informações sobre a situação da turma
    """

    respostas = dict()
    respostas["Total"] = len(numeros)
    respostas["maior"] = max(numeros)
    respostas["menor"] = min(numeros)
    respostas["media"] = sum(numeros)/len(numeros)
    if situação:
        if respostas['media'] >= 7:
            respostas['situaçao'] = 'BOA'
        elif respostas['media'] > 5:
            respostas['situaçao'] = 'RAZOAVEL'
        else:
            respostas['situaçao'] = 'RUIM'

    return respostas


#Programa princimapal
respostas = notas(5.5, 2.5, 9 , 1.50, situação=True)
print(respostas)
help(notas)