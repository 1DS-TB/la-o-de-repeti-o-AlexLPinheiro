#Finalizado
n =1
while n <=10000:
    soma = 0
    i = 1
    while i < n:
        if n % i == 0:
            soma = soma + i
        i+=1
    if soma == n:
        print(n)
    n+=1