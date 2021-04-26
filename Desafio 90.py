nomemedia = dict()
#nomemedia2 = list()
#for c in range(1):
nomemedia["nome"]= str(input("NOME:"))
nomemedia["media"] = float(input("MEDIA:"))
if nomemedia["media"] >= 7.0:
       nomemedia["situação"] = "APROVADO"
elif 5.0 <= nomemedia["media"] < 7.0:
       nomemedia["situação"] = "RECUPERAÇÂO"
else:
       nomemedia["situação"] = "REPROVADO"
#nomemedia2.append(nomemedia.copy())

print(f"Nome é igual {nomemedia['nome']}")
print(f"Media é  igual {nomemedia['media']}")
print(f"Situação é {nomemedia['situação']}")