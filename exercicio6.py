n = int(input("Digite um número inteiro: "))
a = 0
b = 1
c = 1
fibonacci = []

if n < 0:
    print("INVALIDO")
else:
    for num in range(n):
        fibonacci.append(a)
        c = a + b
        a = b
        b = c

    texto = ",".join(str(numero) for numero in fibonacci)
    print(texto)
