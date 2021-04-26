from datetime import date
ano = int(input("Informe ano que voce nasceu? "))
sexo = str(input("Digite voce é Mulher ou Homem:")).title().strip()
idade = date.today().year - ano
if sexo == 'Mulher':
 print("Voce não e obrigada a se alistar")
 sim_nao = str(input("Voce gostaria de se alistar? Sim ou Nao?")).title().strip()
 if sim_nao == 'Não':
  print("OK, Muito obrigado, tenha Bom dia!")
 elif sim_nao == 'Sim':
  print("Seja bem vindo ao site do exercito.")
 if idade == 18:
  print("DEVERA SE ALISTAR QUANTO ANTES...")
 elif idade > 18 :
  alistamento = idade - 18
  ano = date.today().year - alistamento
  print("Voce deveria ter se alistado {} anos. \nSeu alistamendo foi a {}".format(alistamento,ano))
 elif idade < 18:
     alistamento = 18 - idade
     ano = alistamento - date.today().year
     print("Você ira se alistar me daqui {}, \nSeu alistamento sera {}".format(alistamento,ano))
elif sexo == "Homem":
    if idade == 18:
        print("DEVERA SE ALISTAR QUANTO ANTES...")
    elif idade > 18:
        alistamento = idade - 18
        ano = date.today().year - alistamento
        print("Voce deveria ter se alistado {} anos. \nSeu alistamendo foi a {}".format(alistamento, ano))
    elif idade < 18:
        alistamento = 18 - idade
        ano = alistamento - date.today().year
        print("Você ira se alistar me daqui {}, \nSeu alistamento sera {}".format(alistamento, ano))
else:
    print("Erro.. Digite novamente corretamente!")


















#print(("OK, Tenha bom dia!"))
 #elif sim_nao == "sim":
  # print("Seja bem vindo a serviço militar!")
   #if idade == 18:
    # print("Voce tem que se alistar imediatamente! ")
   #elif idade > 18:
    #  alis = idade - 18
     # ano = date.today().year - alis
      #print("Voce já deveria ter se alistado ha {} anos".format(alis))
      #print("Seu alistamento foi a {}".format(ano))
   #elif idade < 18:
    #   alis = 18 - idade
     #  ano = alis = date.today().year
      # print("Voce ira se alistar daqui {} ".format(alis))
       #print("Seu alistamento sera {}".format(ano))
 #else:
  #  print("Entrada invalida, Sim ou Nao!")
#if sexo == 'Homem':
 #   print("Entrada invalida, Sim ou Nao!")


