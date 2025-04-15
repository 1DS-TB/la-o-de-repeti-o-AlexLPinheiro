import random
jogadores = []
critico = [1,1,1,1,1,1,1,1,2,1]
while True:
    hp = random.randint(200, 1000)
    dano = random.randint(1, 50)
    defesa = random.randint(1, 50)
    dano_oponente = random.randint(1, 50)
    if defesa <= dano_oponente:
        jogadores.append({
            "nome": input("Digite o nome do Jogador 1: "),
            "hp_total": hp,
            "hp_atual": hp,
            "dano": dano,
            "defesa": defesa
        })
        break


while True:
    escolha = int(input("BLASPHEMOUS 3\n\nDIGITE 1 PARA INICIAR\nDIGITE 2 PARA SAIR\n"))
    if escolha == 2:
        break
    else:
        modo = int(input("DIGITE 1 PARA MULTIJOGADOR\nDIGITE 2 PARA JOGAR CONTRA A CPU\n"))
        while True:
            hp = random.randint(200, 1000)
            dano = dano_oponente
            defesa = random.randint(1, 50)
            if defesa <= jogadores[0]["dano"]:
                if modo ==2:
                    nome = "CPU"
                else:
                    nome = input("Digite o nome do Jogador 2: ")
                jogadores.append({
                    "nome": nome,
                    "hp_total": hp,
                    "hp_atual": hp,
                    "dano": dano,
                    "defesa": defesa
                })
                break


            for j in range(len(jogadores)):
                print(f"\n{jogadores[j]["nome"]}:\nHP: {hp}\nDano: {jogadores[j]["dano"]}||Defesa: {jogadores[j]["defesa"]}")
            '''rodada = 0
            listaPocoes = ["1 - Super Força\n\n", "2 - Super cura\n\n", "3 - Super vida\n\n", "4 - Pula Pula"]
            while jogadores[0]["hp_atual"] > 0 and jogadores[1]["hp_atual"] > 0:
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
'''
            '''if vidaJogador > 0:
                print(f"\nParabéns {nomeJogador}!, você ganhou!\n")
            else:
                print(f"\nVocê perdeu!\n")
'''