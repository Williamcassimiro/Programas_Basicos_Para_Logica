num = int(input("Informe um numero?"))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[31m", end=" ")
        total = total + 1
    else:
        print("\033[32m", end="")
    print("{}".format(c), end=" ")
print("Numero {} foi divisivel {} vezes".format(num,total))
if total == 2:
    print("ELE É 1PRIMO")
else:
    print("ELE E NÂO É PRIMO")