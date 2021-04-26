from datetime import date
atual = date.today().year
nasc = int(input("DIGA SEU ANO QUE VOCE NASCEU:"))
ano = nasc - atual
if ano <= 9:
    print("Mirim")
elif ano > 9 and ano <= 14:
    print("Infantil")
elif ano > 14 and ano <= 19:
    print("Junior")
elif ano > 19 and ano <= 25:
    print("SeNior")
else:
    print("Master")
print("FiM")
