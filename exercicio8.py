N = int(input("Digite o limite de termos da função: "))
s = 0
for n in range(N):
    s = s + (1/(n+1))

print(f"A soma da série harmônica até o termo 1/{N} é igual a :{s:.2f}")

