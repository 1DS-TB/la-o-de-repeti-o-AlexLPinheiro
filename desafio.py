import random

jogadores = []
critico = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1]

hp = random.randint(200, 1000)
<<<<<<< HEAD
=======


>>>>>>> b53ecd9eb47ca650a135aab31f40733ff37a0efb

while True:
    escolha = int(input("\nBLASPHEMOUS 3\n\nDIGITE 1 PARA INICIAR\nDIGITE 2 PARA SAIR\n"))
    if escolha == 2:
        exit()
    else:
        modo = int(input("DIGITE 1 PARA MULTIJOGADOR\nDIGITE 2 PARA JOGAR CONTRA A CPU\n"))
        while True:
            vida = hp
            dano = random.randint(1, 50)
            defesa = random.randint(1, 50)
            dano_oponente = random.randint(1, 50)
            if defesa <= dano_oponente:
                jogadores.append({
                    "nome": input("Digite o nome do Jogador 1: "),
                    "hp_total": hp,
                    "hp_atual": vida,
                    "dano": dano,
                    "defesa": defesa
                })
                break
        while True:
            vida = hp
            dano = dano_oponente
            defesa = random.randint(1, 50)
            if defesa <= jogadores[0]["dano"]:
                if modo == 2:
                    nome = "CPU"
                else:
                    nome = input("Digite o nome do Jogador 2: ")
                jogadores.append({
                    "nome": nome,
                    "hp_total": hp,
                    "hp_atual": vida,
                    "dano": dano,
                    "defesa": defesa
                })
                break
        break

for j in range(len(jogadores)):
    print(
        f"\n{jogadores[j]['nome']}:\nHP: {jogadores[j]['hp_total']} | Dano: {jogadores[j]['dano']} | Defesa: {jogadores[j]['defesa']}")

rodada = 0
listaPocoes1 = ["1 - Super Força\n\n", "2 - Super cura\n\n", "3 - Super vida\n\n", "4 - Pula Pula"]
listaPocoes2 = ["1 - Super Força\n\n", "2 - Super cura\n\n", "3 - Super vida\n\n", "4 - Pula Pula"]

pular_proximo_turno = -1

while jogadores[0]["hp_atual"] > 0 and jogadores[1]["hp_atual"] > 0:
    multPocaoPula = 1
    if multPocaoPula == 1:
        rodada += 1
        print(f"\n=== RODADA {rodada} ===")
        for j in range(len(jogadores)):
            if jogadores[j]["hp_atual"] <= 0:
                continue
            multPocaoDano = 1
            multPocaoCura = 1
            multPocaoVida = 0
            pocaoUsada = 0

<<<<<<< HEAD
    for j in range(len(jogadores)):
        if jogadores[j]["hp_atual"] <= 0:
            continue
        if j == pular_proximo_turno:
            print(f"\n{jogadores[j]['nome']} está com problemas no sistema e perderá uma rodada!")
            pular_proximo_turno = -1
            continue

        multPocaoDano = 1
        multPocaoCura = 1
        multPocaoVida = 0
        pocaoUsada = 0

        while True:
            print(f"\nTurno de {jogadores[j]['nome']}")
            print(f"Seu HP: {jogadores[j]['hp_atual']} || HP do inimigo: {jogadores[1 - j]['hp_atual']}")
            jogadores[j]["hp_atual"] += multPocaoVida
            texto = ""
            if jogadores[j]["nome"] != "CPU":
                acao = int(input("\n1 - Atacar | 2 - Curar | 3 - Inventário: "))

                if acao == 1:
                    danoCritico = random.randint(0, 9)
                    dano = ((jogadores[j]["dano"] - jogadores[1 - j]["defesa"]) * critico[danoCritico]) * multPocaoDano
                    dano = max(dano, 0)
                    jogadores[1 - j]["hp_atual"] -= dano
                    print(f"\n{jogadores[j]['nome']} ataca! {jogadores[1 - j]['nome']} perdeu {dano} de HP!")
                    break

                elif acao == 2:
                    if jogadores[j]["hp_atual"] < jogadores[j]["hp_total"] - (20 * multPocaoCura):
                        jogadores[j]["hp_atual"] += (20 * multPocaoCura)
                        print("Você se curou +20 HP!")
                    else:
                        cura = jogadores[j]["hp_total"] - jogadores[j]["hp_atual"]
                        jogadores[j]["hp_atual"] += cura
                        print(f"Você se curou +{cura} HP!")
                    break

                else:
                    listaPocoes = listaPocoes1 if j == 0 else listaPocoes2
                    if pocaoUsada == 1:
                        print("Você já usou uma poção nessa rodada!\n\n")
                    else:
                        for i in listaPocoes:
                            texto += i
                        pocao = int(input(f"\nInventário:\n\n{texto}\n\n5- Sair"))
                        if pocao == 1 and "1 - Super Força\n\n" in listaPocoes:
                            multPocaoDano = 2
                            pocaoUsada += 1
                            listaPocoes.remove("1 - Super Força\n\n")
                        if pocao == 2 and "2 - Super cura\n\n" in listaPocoes:
                            multPocaoCura = 2
                            pocaoUsada += 1
                            listaPocoes.remove("2 - Super cura\n\n")
                        if pocao == 3 and "3 - Super vida\n\n" in listaPocoes:
                            multPocaoVida = 50
                            pocaoUsada += 1
                            listaPocoes.remove("3 - Super vida\n\n")
                        if pocao == 4 and "4 - Pula Pula" in listaPocoes:
                            pular_proximo_turno = 1 - j 
                            pocaoUsada += 1
                            listaPocoes.remove("4 - Pula Pula")
            else:
                acaoCpu = random.randint(1, 2)
                if acaoCpu == 1:
                    danoCritico = random.randint(0, 9)
                    dano = (jogadores[j]["dano"] - jogadores[1 - j]["defesa"]) * critico[danoCritico]
                    dano = max(dano, 0)
                    jogadores[1 - j]["hp_atual"] -= dano
                    print(f"{jogadores[j]['nome']} ataca! {jogadores[1 - j]['nome']} perdeu {dano} de HP!")
                else:
                    if jogadores[j]["hp_atual"] < jogadores[j]["hp_total"] - 20:
                        jogadores[j]["hp_atual"] += 20
                        print(f"{jogadores[j]['nome']} se curou +20 HP!")
                    else:
                        cura = jogadores[j]["hp_total"] - jogadores[j]["hp_atual"]
                        jogadores[j]["hp_atual"] += cura
                        print(f"{jogadores[j]['nome']} se curou +{cura} HP!")
                break
=======



            while True:


                    print(f"\nTurno de {jogadores[j]['nome']}")
                    print(f"Seu HP: {jogadores[j]['hp_atual']} || HP do inimigo: {jogadores[1 - j]['hp_atual']}")
                    jogadores[j]["hp_atual"] += multPocaoVida
                    texto = ""
                    if jogadores[j]["nome"] != "CPU":
                        acao = int(input("\n1 - Atacar | 2 - Curar | 3 - Inventário: "))

                        if acao == 1:
                            danoCritico = random.randint(0, 9)
                            dano = ((jogadores[j]["dano"] - jogadores[1-j]["defesa"]) * critico[danoCritico])*multPocaoDano
                            dano = max(dano, 0)
                            jogadores[1-j]["hp_atual"] -= dano
                            print(f"\n{jogadores[j]['nome']} ataca! {jogadores[1-j]['nome']} perdeu {dano} de HP!")
                            break

                        elif acao == 2:
                            if jogadores[j]["hp_atual"] < jogadores[j]["hp_total"] - (20 * multPocaoCura):
                                jogadores[j]["hp_atual"] += (20 * multPocaoCura)
                                print("Você se curou +20 HP!")
                            else:
                                cura = jogadores[j]["hp_total"] - jogadores[j]["hp_atual"]
                                jogadores[j]["hp_atual"] += cura
                                print(f"Você se curou +{cura} HP!")
                            break

                        else:
                            listaPocoes = listaPocoes1 if j == 0 else listaPocoes2
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
                    else:
                        if multPocaoPula == 1:
                            acaoCpu = random.randint(1, 2)
                            if acaoCpu == 1:
                                danoCritico = random.randint(0, 9)
                                dano = (jogadores[j]["dano"] - jogadores[1-j]["defesa"]) * critico[danoCritico]
                                dano = max(dano, 0)
                                jogadores[1-j]["hp_atual"] -= dano
                                print(f"{jogadores[j]['nome']} ataca! {jogadores[1-j]['nome']} perdeu {dano} de HP!")
                            else:
                                if jogadores[j]["hp_atual"] < jogadores[j]["hp_total"] - 20:
                                    jogadores[j]["hp_atual"] += 20
                                    print(f"{jogadores[j]['nome']} se curou +20 HP!")
                                else:
                                    cura = jogadores[j]["hp_total"] - jogadores[j]["hp_atual"]
                                    jogadores[j]["hp_atual"] += cura
                                    print(f"{jogadores[j]['nome']} se curou +{cura} HP!")
                            break


>>>>>>> b53ecd9eb47ca650a135aab31f40733ff37a0efb

if jogadores[0]["hp_atual"] > 0:
    print(f"\nParabéns {jogadores[0]['nome']}! Você venceu!")
else:
    print(f"\nParabéns {jogadores[1]['nome']}! Você venceu!")
