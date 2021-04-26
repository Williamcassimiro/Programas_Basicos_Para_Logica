
from Desafio115.LIB.arquivo import *
from time import sleep

arq = 'PessoasCastradas.txt'

if not arquicoExiste(arq):
    criarArquivo(arq)




cabeçalho("SISTEMA ARQUIVO v1.0")
while True:
     resposta = menu(["Ver pessoas cadastrar", "Cadastrar uma nova pessoa", "Sair do Sistema"])
     if resposta  ==  1:
        #Opção de listar o conteudo de um arquivo!
       LerArquivo(arq)



     elif resposta == 2:
         cabeçalho("NOVO CADASTRO")
         nome = str(input("Nome: "))
         idade = leiaint("Idade: ")
         cadastar(arq, nome, idade )


     elif resposta == 3:
         cabeçalho("Saindo do SISTEMA... ATE LOGO!")
         break
     else:
         print("\033[31mErro! Digite uma opção válida!\033[m")
         sleep(2)