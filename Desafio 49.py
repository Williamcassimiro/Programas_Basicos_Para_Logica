num = int(input("Informe um valor para ver sua tabuada:"))
print("-="*11)
for c in range(1,11):
   print("{} X {} = {}".format(c, num, num*c))
print("-="*11)