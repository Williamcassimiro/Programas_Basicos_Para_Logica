palavras = ("Livros","William","Karla","Carne", "Controle","Linux")

for pas in palavras:
    print(f"\nNa palavra {pas.upper()} temos:", end=" ")
    for letras in pas:
        if letras in "aeiou":
            print(f"{letras}",end=" ")