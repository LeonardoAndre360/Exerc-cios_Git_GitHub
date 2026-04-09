titas_no_radar = {}
expedicao_ativa = True
while expedicao_ativa:
    print("Relatar um novo titã no radar(Adicionar Tarefa)")
    print("Ver mapa dos titas(Listar titas)")
    print("Titã abatido(Concluir tarefa)")
    print("Recuar para a muralha(Retirada)")

    acao = input("Oque iremos fazer: ").upper()

    if acao == ("ADICIONAR TAREFA"):
        nome_do_titan = input("Qual titã você viu? ").title().strip()
        nome_do_titan = nome_do_titan.replace("Titã","").replace("Tita","")
        titas_no_radar[nome_do_titan] = "Vivo"
        print(nome_do_titan, "Adicionado")
    elif acao == ("LISTAR TITAS"):
        if len(titas_no_radar) == 0:
            print("Não tem nenhum titã registrado")
        else:
            print("A quantidade de titãs é: ", titas_no_radar)
    elif acao == ("CONCLUIR TAREFA"):
        nome_do_titan = input("Qual titã você derrotou").title().strip().replace("Titã", "").replace("Tita", "")
        if nome_do_titan in titas_no_radar:
            titas_no_radar[nome_do_titan] = "Morto"
            print("O Titã", nome_do_titan, "foi Abatido")
        else:
            print("Aviso: Este titã não estava no nosso radar!")
    elif acao == ("RETIRADA"):
        print("Recuamos para as mulharas")
        expedicao_ativa = False
    else:
        print("Opção invalida")

