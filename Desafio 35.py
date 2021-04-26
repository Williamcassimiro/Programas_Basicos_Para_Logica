print("\033[7;30m_+\033[m"*50)
r1 = float(input("Primeiro numero:"))
r2 = float(input("Segundo numero:"))
r3 = float(input("Terceiro numero:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esse valores podem ser criado um triangulo")
else:
    print("Esse valores NÂO pode ser criado um triangulo")
print("FIM")
print("\033[7;30m_+\033[m"*50)