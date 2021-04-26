from time import sleep
n1 = int(input("Primero valor:"))
n2 = int(input("Segundo valor:"))
opção = 0
while opção != 5:
   print("""     [1]Somar
     [2]Multiplicar
     [3]Maior
     [4]Novos números
     [5]Sair do programa""")
   opção = int(input(" >>>> Qual sua Opção:"))
   if opção == 1:
       soma = n1 + n2
       print("A soma entre {} + {} é {}".format(n1, n2, soma))
   elif opção == 2:
       soma = n1 * n2
       print("A Multiplicação entre {} X {} é {}".format(n1,n2,soma))

   elif opção == 3:
        if n1 > n2 :
           maior = n1
        else:
           maior = n2
        print("Entre {} e {} o maior numero é {}".format(n1,n2,maior))
   elif opção == 4:
       print("Informer novamente os valores")
       n1 = int(input("Primero valor:"))
       n2 = int(input("Segundo valor:"))

   elif opção == 5:
       print("Finalizando... ")
       sleep(0.8)

   else:
       print("Opção Invalida. Tente novamente.")
       print("-_-" * 10)
print("Fim do Programa...\n Obrigado volte sempre!")