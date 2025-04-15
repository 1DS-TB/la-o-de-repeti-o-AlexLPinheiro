import random
hp = random.randint(200, 1000)
vidaJogador = hp
vidaCpu = hp
critico = [1,1,1,1,1,1,1,1,2,1]
while True:
    danoJogador = random.randint(1, 50)
    danoCpu = random.randint(1, 50)
    defesaJogador = random.randint(1, 50)
    defesaCpu = random.randint(1, 50)
    if defesaCpu < danoJogador and defesaJogador < danoCpu:
        break

while True:
    escolha = int(input("BLASPHEMOUS 3\n\nDIGITE 1 PARA INICIAR\nDIGITE 2 PARA SAIR\n"))
    if escolha == 2:
        break
    else:
        nomeJogador = input("Digite o nome do  seu personagem: ")

        print(f"\n{nomeJogador}:\nHP: {hp}\nDano: {danoJogador}||Defesa: {defesaJogador}\n\nInimigo:\nHP: {hp}\nDano: {danoCpu}||Defesa: {defesaCpu}")
        rodada = 0
        listaPocoes = ["1 - Super Força\n\n", "2 - Super cura\n\n", "3 - Super vida\n\n", "4 - Pula Pula"]
        while vidaCpu and vidaJogador > 0 :
            rodada +=1
            pocaoUsada = 0
            print(f"\nRodada {rodada}")
            print(f"Seu HP: {vidaJogador} || HP do inimigo: {vidaCpu}")
            dano = 0
            multPocaoDano = 1
            multPocaoCura = 1
            multPocaoVida = 0
            multPocaoPula = 1


            while True:
                vidaJogador = vidaJogador + multPocaoVida
                texto = ""
                acao = int(input("\nSeu turno:1- para atacar, 2 -para curar, 3 -para acessar ao inventário"))
                if acao == 1:

                    danoCritico: int = random.randint(0,9)
                    dano = ((danoJogador - defesaCpu) * critico[danoCritico])*multPocaoDano
                    vidaCpu = vidaCpu - dano
                    print(f"\nVocê ataca!!! inimigo perde {dano} de hp")
                    break
                elif acao == 2:
                    if vidaJogador < (hp-20) * multPocaoCura:
                        vidaJogador = vidaJogador+ (20 * 2)
                        print("\nVocê ganha +20 de HP!")
                    else:
                        cura = hp-vidaJogador
                        vidaJogador = vidaJogador + cura
                        print(f"\nVocê ganha +{cura} de HP!")
                    break
                else:
                    if pocaoUsada == 1:
                        print("Você já usou uma poção nessa rodada!\n\n")
                    else:

                        for i in listaPocoes:
                            texto = texto + i
                        pocao = int(input(f"\nInventário:\n\n{texto}\n\n5- Sair"))
                        if multPocaoDano != 2:
                            if pocao == 1:
                                multPocaoDano = 2
                                pocaoUsada +=1
                                listaPocoes.remove("1 - Super Força\n\n")
                        else:
                            multPocaoDano = 1
                        if multPocaoCura !=2:
                            if pocao == 2:
                                multPocaoCura = 2
                                pocaoUsada +=1
                                listaPocoes.remove("2 - Super cura\n\n")
                        else:
                            multPocaoCura = 1
                        if multPocaoVida != 50:
                            if pocao == 3:
                                multPocaoVida = 50
                                pocaoUsada +=1
                                listaPocoes.remove("3 - Super vida\n\n")
                        else:
                            multPocaoVida = 0
                        if multPocaoVida != 2:
                            if pocao == 4:
                                multPocaoPula = 2
                                pocaoUsada +=1
                                listaPocoes.remove("4 - Pula Pula")
                        else:
                            multPocaoPula = 1
            if multPocaoPula == 1:
                dano = 0
                acaoCpu = random.randint(1,2)
                if acaoCpu == 1:
                    danoCritico= random.randint(0, 9)
                    dano = (danoCpu - defesaJogador) * critico[danoCritico]
                    vidaJogador = vidaJogador - dano
                    print(f"Inimigo ataca!!! Você perde {dano} de hp")
                else:
                    if vidaCpu < hp-20:
                        vidaCpu = vidaCpu + 20
                        print(f"Inimigo se cura!!! Ganhou 20 pontos de vida.")
                    else:
                        cura = hp-vidaCpu
                        vidaCpu= vidaCpu+ cura
                        print(f"Inimigo se cura!!! Ganhou {cura} pontos de vida.")

        if vidaJogador > 0:
            print(f"\nParabéns {nomeJogador}!, você ganhou!\n")
        else:
            print(f"\nVocê perdeu!\n")