#Finalizado
num1 = int(input("Digite o primeiro numero do intervalo: "))
num2 = int(input("Digite o segundo numero do intervalo: "))
listakaprekar = []
if num1 > num2:
    num1,num2 = num2, num1

if num1 < 0 or num2<0:
    print("INVALIDO")
else:
    for k in range(num1,num2):
        kTxt = str(k)
        tamanhoK = len(kTxt)
        kQuadrado = k **2
        kQuadradoTxt = str(kQuadrado)
        tamanhoKQuadrado = len(kQuadradoTxt)

        if tamanhoKQuadrado % 2 == 0:
            metade = tamanhoKQuadrado //2
            esquerda = kQuadradoTxt[0:metade]
            direita = kQuadradoTxt[metade:tamanhoKQuadrado]
            soma =(int(esquerda)+int(direita))

        else:
            direita = kQuadradoTxt[tamanhoKQuadrado-tamanhoK:tamanhoKQuadrado]
            esquerda = kQuadradoTxt[0:tamanhoKQuadrado-tamanhoK]

            if esquerda == "":
                esquerda = "0"

            soma = (int(esquerda)+int(direita))

        if soma == k:
            listakaprekar.append(k)
textoFinal = ""
for n in listakaprekar:
    textoFinal =textoFinal +  f",{n}"
print(f"Os números de kaprekar no intervalo de {num1} até {num2} são: {textoFinal[1:]}",end=".")
