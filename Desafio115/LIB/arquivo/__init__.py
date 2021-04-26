from Desafio115.LIB.Interface import *

def arquicoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
from Desafio115.LIB.Interface import *



def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criaçao do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalho("PESSOAS CADASTREDAS")
        for linha in a:
            dado = linha.split(":")
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]}{dado[1]}')
    finally:
        a.close()

def cadastar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome}: {idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo resgistro de {nome} adicionado.")
            a.close()