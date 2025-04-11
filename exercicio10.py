

num1 = int(input("Digite o primeiro numero do intervalo: "))
num2 = int(input("Digite o segundo numero do intervalo: "))

for k in range(num1,num2):
    kQuadrado = k **2
    ktxt = str(kQuadrado)
    n = len(ktxt)
    if n % 2 == 0:
        metade = n //2
        print(metade)
        esquerda = ktxt[0:metade]
        direita = ktxt[metade:n]
        soma = esquerda + direita
        print(kQuadrado, metade, esquerda ,direita, soma,)


