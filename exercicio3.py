#Finalizado
numero = int(input("Digite um número para ser calculado sua tabuada: "))
print(f"\nA tabuada do {numero} é: ")
for n in range (1,11):
    multiplicacao = numero * n
    print(f"{numero} x {n} = {multiplicacao}")
