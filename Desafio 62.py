# Gerador de PA
print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primero termo:"))
razão = int(input("Razâo:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:

        print("{} -> ".format(termo), end=(""))
        termo = termo + razão
        cont = cont + 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais:"))
print("Progreção finalisada com {} termos".format(total))
print("Fim")