primeiro = int(input("Primeiro termo:"))
razão = int(input("Razâo:"))
decimo = primeiro + (10 -1) * razão
for c in range( primeiro, decimo + razão, razão):
    print("{}".format(c), end=" -> ")
print("<<<<FIM>>>>")