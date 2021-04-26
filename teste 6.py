#Programa melhorado:
from datetime import date
ano_nascimento = int(input('Em que ano você nasceu? '))
sexo = str(input('Você é HOMEM ou MULHER? ')).title().strip()
idade = date.today().year - ano_nascimento
if sexo == 'Mulher':
 print('Você não é obrigada ao alistamento.')
 sim_nao = str(input('Você Gostaria de se alistar nas Forças Armadas? Sim ou Não? ')).title().strip()
 if sim_nao == 'Não':
  print('Tenha um bom dia Senhorita!')
 elif sim_nao == 'Sim':
  print('BEM-VINDA Ao Serviço Militar!')
  if idade == 18:
   print('Você tem que se alistar IMEDIATAMENTE!')
  elif idade > 18:
   alistamento = idade - 18
   ano = date.today().year - alistamento
   print('Você já deveria ter se alistado há {} ano(s)'.format(alistamento))
   print('Seu alistamento foi em {}'.format(ano))
  else:
   alistamento = 18 - idade
   ano = alistamento + date.today().year
   print('Ainda faltam {} ano(s) para o alistamento'.format(alistamento))
   print('Seu alistamento será em {}'.format(ano))
 else:
  print('Entrada inválida, escolhar Sim ou Não')
elif sexo == 'Homem':
 print('BEM-VINDO ao Serviço Militar')
 if idade == 18:
  alistamento = 18
  print('Você tem que se alistar IMEDIATAMENTE!')
 elif idade > 18:
  alistamento = idade - 18
  ano = date.today().year - alistamento
  print('Você já deveria ter se alistado há {} ano(s)'.format(alistamento))
  print('Seu alistamento foi em {}'.format(ano))
 else:
  alistamento = 18 - idade
  ano = alistamento + date.today().year
  print('Ainda faltam {} ano(s) para o alistamento'.format(alistamento))
  print('Seu alistamento será em {}'.format(ano))
else:
 print('As Forças Armadas não aceita DEGENERADO(A)!')