#Finalizado
numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("INVALIDO")
else:
    contador = 1
    fatorial = 1
    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1

    print(fatorial)