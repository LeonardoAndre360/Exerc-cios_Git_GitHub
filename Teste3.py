energia_amaldicoada = 1000
nome = input("Qual é seu nome ")
if nome == "Sukuna" or nome == "sukuna":
        energia_amaldicoada = (energia_amaldicoada * 10)
vivo = True
while vivo:
    print("Qual será sua decisão na batalha:")
    print("1 - Ver a sua quantidade de Energia")
    print("2 - Usar a sua tecnica")
    print("3 - Recuperar a sua energia")
    print("4 - Fugir")
    opcao = input("Qual será sua decisão ")

    if opcao == "1":
        print ("Sua energia amaldiçoada é:", energia_amaldicoada) 
    elif opcao == "2":
        while True:
            print("A - Cães Divinos(Custo 100 de energia)")
            print("B - Nue(Custo 150 de energia)")
            print("C - Cobra Orochi(Custo 180 de energia)")
            print("D - Elefante Maximo(Custo 200 de energia)")
            print("E - Toca do coelho(Custo 50 de energia)")
            print("F - Sapo(Custo 70 de energia)")
            print("G - Cervo Circular(Custo 350 de energia)")
            print("H - Touro Perfurante(Custo 500 de energia)")
            print("I - Tigre Fúnebre(Custo 700 de energia)")
            print("J - Mahoraga(Custo a vida se não for o Sukuna(1000 pontos))")
            print("V - Voltar as opções anteriores")
            
            invocacao = input("Escolha sua invocação ")

            if invocacao == "A" or invocacao == "a":
                if energia_amaldicoada < 200:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 200
                    print("Você invocou os Caes divinos")
                    break
            elif invocacao == "B" or invocacao == "b":
                if energia_amaldicoada < 150:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 150
                    print("Você invocou o Nue")
                    break
            elif invocacao == "C" or invocacao == "c":
                if energia_amaldicoada < 180:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 180
                    print("Você invocou a Cobra Orochi")
                    break
            elif invocacao == "D" or invocacao == "d":
                if energia_amaldicoada < 200:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 200
                    print("Você invocou o Elefante Máximo")
                    break
            elif invocacao == "E" or invocacao == "e":
                if energia_amaldicoada < 50:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 50
                    print("Você invocou a Toca do Coelho")
                    break
            elif invocacao == "F" or invocacao == "f":
                if energia_amaldicoada < 70:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 70
                    print("Você invocou o Sapo")
                    break
            elif invocacao == "G" or invocacao == "g":
                if energia_amaldicoada < 350:
                    print("Energia insuficiente")
                    
                else:
                    energia_amaldicoada = energia_amaldicoada - 350
                    print("Você invocou o Cervo Circular")
                    break
            elif invocacao == "H" or invocacao == "h":
                if energia_amaldicoada < 500:
                    print("Energia insuficiente")
                    
                else:
                    energia_amaldicoada = energia_amaldicoada - 500
                    print("Você invocou o Touro Perfurante")
                    break
            elif invocacao == "I":
                if energia_amaldicoada < 700:
                    print("Energia insuficiente")
                else:
                    energia_amaldicoada = energia_amaldicoada - 700
            elif invocacao == "J" or invocacao == "j":
                if nome == "Sukuna" or nome == "sukuna":
                    if energia_amaldicoada < 1000:
                        print("Energia insuficiente")
                    else:
                        energia_amaldicoada = energia_amaldicoada - 1000
                        print("Furube Yura Yura: General Divino Mahoraga foi invocado na batalha")
                        break
                else:
                    print("Furube Yura Yura: General divino Mahoraga")
                    print("Voce morreu no ritual")
                    vivo = False
                    break
            elif invocacao == "V" or invocacao == "v":
                print("Voltando...")
                break
            else:
                print("Opção invalida, escolha um dos shikigamis")
        
    elif opcao == "3":
        num1 = float(input("Quanto você recupera de energia? "))
        energia_amaldicoada = (energia_amaldicoada + num1)
        print("Sua energia atual é: ", energia_amaldicoada)
    elif opcao == "4":
        print("Parabens! Você é um coverde e fugiu de uma batalha, parabéns Haruta")
        break
    else:
        print("Opção invalidade, rápido! Escolha uma opção antes que morra ")