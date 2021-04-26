from datetime import datetime
dado = dict()
dado["Nome"]= str(input("Nome:"))
nasc = int(input("Ano de Nascimento?"))
dado["idade"] = datetime.now().year - nasc
dado["ctps"] = int(input("Carteira de Trabalho (0 não ten):"))
if dado["ctps"] != 0:
    dado["Contratação"] = int(input("Ano de Contratação:"))
    dado["salario" ] = float(input("Salario: R$"))
    dado["aposetadoria"] = dado["idade"] + ((dado["Contratação"] + 35)  - datetime.now().year)
print("="*30)
for k, v in dado.items():
    print(f' - {k} tem o valor {v}')
