# Lista ordernada sem repetição
lista = []
for c in range (0,5):
    num = int(input("Digite um valor ?"))
    if c == 0 :
        lista.append(num)
        print("Adicionado no final da lista...")
    elif num > lista[-1]:
        lista.append(num)
        print("adicionado no final da lista....")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print(lista)

