numero = int(input("Digite um número inteiro positivo: "))
if numero <= 0:
    print("INVALIDO")
else:
    contador = 0
    soma = 0
    while contador <= numero:
        soma = soma + contador
        contador = contador +1

    print(soma)