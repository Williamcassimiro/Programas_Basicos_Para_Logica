n1 = float(input("Informe sua primeira nota?"))
n2 = float(input("Infome sua segunda nota?"))
media = (n1+n2)/2
print("Tirando {:.1f} e {:.1f}, a media sera {:.1f}".format(n1,n2,media))
if media >= 5 and media < 7 : # 7 > media >=5: funciona!
     print("aluno esta em recuperação")
elif media <= 5:
    print("Esta reprovado!")
elif media >= 7:
    print("Aprovado!")
else:
    print("FIM")
