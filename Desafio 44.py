print("\033[1;7;32m STOR BIT CELL\033[m"*10)
print("{:^40}".format("\033[1;4;7;30mPrograma de formas de pagamentos para uma loja.\033[m"))
valor = float(input("\033[7;30mInforme valor da sua compra?\033[m"))
print('''\033[7;30mFormas de pagamento:
[1] Pagamento à vista, Tera 10% de desconto.
[2] Pagamento à vista NO CARTÂO, Tera 5% de desconto.
[3] Em ate 2x NO CARTÂO, sera preço normal.
[4] Em 3x ou mais..., 20% de juros.\033[m''')
opção = int(input("\033[7;30mQual das opção sera sua forma de pagamento?\033[m"))
if opção == 1:
    valornovo = valor - (valor*10/100)
    print("\033[7;30mObrigado por pagar avistas, Voce ganhou um desconto de 10%, Valor final {:.2f}\033[m".format(valornovo))
elif opção == 2:
    valornovo = valor -(valor*5/100)
    print("\033[7;30mObrigado por pagamento avistas no cartão, voce ganhou um desconto de 5%, valor final {:.2f}\033[m".format(valornovo))
elif opção == 3:
    valornovo = valor/2
    print("\033[7;30mSua escolha foi em 2x no cartão, valor de cada parcela sera 2x{:.2f}\033[m".format(valornovo))
elif opção == 4:
    print("\033[7;30mEssa opção e valida somente acima de 3 parcelas.\033[m")
    quantidade =int(input("\033[7;30mQuanta vez deseja parcelar?\033[m"))
    valornovo = valor + (valor*20/100)
    parcela = (valornovo/quantidade)
    print("\033[7;30mSua escolha foi em {}x no cartão, valor de cada parcela sera {}x{:.2f}.\033[m ".format(quantidade,quantidade,parcela))
else:
    print("\033[7;30mOpção invalida...\033[m")
print("\033[7;30mObrigado por comprar com gente\033[m")
print("\033[1;7;32m STOR BIT CELL\033[m"*10)