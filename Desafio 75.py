num = (int(input("Informe um numero:")),
          int(input("Informe outro numero:")),
          int(input("Informe mais um numero:")),
          int(input("Informe o ultimo numero:")))
print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 aparceu na {num.index(3)+1}° posição")
else:
    print("O valor 3 não foi digitado em nem uma posição.")
print("Os valores pares digitados foram:", end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")