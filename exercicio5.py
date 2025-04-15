#Finalizado
numero = int(input("Digite um número inteiro positivo: "))
if numero <= 0:
    print("INVALIDO")
else:
    if numero == 1:
        print(f"O número {numero} não é primo!")
    else:
        primo = True
        contador = 2
        while contador < numero:
            if numero % contador == 0:
                primo = False
                contador = contador + 1


            else:
                contador = contador +1


        if primo:
            print(f"O número {numero} é primo!")
        else:
            print(f"O número {numero} não é primo!")

