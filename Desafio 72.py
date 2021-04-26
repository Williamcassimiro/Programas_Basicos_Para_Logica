from  time import  sleep
num = 0
tipo =" "
numeros = ("Zero","um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze",
           "Treze","Quatorze","Quinse","Dezeseis","Dezesete" ,"Dezoito","Dezenove","Vinte")
while tipo != "N":
    while True:
        num = int(input("Digite um valor entre  0 e 20:"))
        if 0 <= num <= 20:
            break
        print("Numero Errado, Digite apenas valores 0 e 20")
    print("Voce digitou o numero {}!".format(numeros[num]))
    tipo = str(input("Deseja continuar?[S/N]")).strip().upper()
    while tipo not in "SN":
        num = int(input("Digite um valor entre  0 e 20:"))
sleep(1)
print("Fim do programa.....")

