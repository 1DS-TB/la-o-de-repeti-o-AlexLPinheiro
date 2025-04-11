N = int(input("Digite um número inteiro positivo: "))
if N <= 0:
    print("INVALIDO")
else:
    for n in range(N+1):
        texto = ""
        for i in range(n):
            texto = texto + "*"
        print(texto)