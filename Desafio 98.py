from time import sleep

def contador(i, f, p):
    # Para resover numeros negativos  e o passo 0 (Como se da passo Zero né) kkkk
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"Contador de {i} até {f} de {p} em {p}")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont += p
        print("fim")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont -= p
        print("fim")


contador(1, 10, 1)
contador(10, 0 , 2 )
print("Personalize voçê a contagem! ")
i = int(input("Inicio:"))
f = int(input("Fim:   "))
p = int(input("Passo: "))
contador(i, f, p)

