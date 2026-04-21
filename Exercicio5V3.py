def obter_pontos_validos(valor):
    try:
        pontos = int(valor)
        if pontos < 0:
            return 0
        return pontos
    except ValueError:
        return "Erro: Insira um número válido para os pontos."
    
def validar_feiticeiro_existe(barreira, nome):
    if nome in barreira:
        return True
    return f"Erro: O feiticeiro {nome} não está registrado na barreira."

def adicionar_feiticeiro(barreira, nome, grau, pontos):
    if validar_feiticeiro_existe(barreira, nome) == True:
        return f"Erro: {nome} já está na barreira."
    barreira[nome] = {"grau": grau, "pontos": pontos}
    return f"Jogador: {nome} adicionado com sucesso."

def listar_jogadores(barreira):
    if not barreira:
        return "Não há nenhum jogador nesta barreira."
    jogadores = []
    for nome, dados in sorted(barreira.items()):
        jogadores.append(f"Nome: {nome} | Grau: {dados['grau']} | Pontos: {dados['pontos']}")
    return "\n".join(jogadores)

def remover_feiticeiro(barreira, nome):
    if validar_feiticeiro_existe(barreira, nome) == True:
        del barreira[nome]
        return "Feiticeiro eliminado da barreira!"
    else:
        return validar_feiticeiro_existe(barreira, nome)
    
def atualizar_pontos(barreira, nome, novos_pontos):
    if validar_feiticeiro_existe(barreira, nome) == True:
        dados_jogadores = barreira.get(nome, {})
        dados_jogadores["pontos"] = novos_pontos
        return f"Quantidade de pontos do {nome} atualizada para {novos_pontos}"
    else:
        return validar_feiticeiro_existe(barreira, nome)
    
def registrar_duelo(barreira, historico, vencedor, perdedor, pontos_apostados):
    if validar_feiticeiro_existe(barreira, vencedor) == True and validar_feiticeiro_existe(barreira, perdedor) == True:
        barreira[vencedor]["pontos"] += pontos_apostados
        barreira[perdedor]["pontos"] -= pontos_apostados
        historico.append(f"{vencedor} derrotou {perdedor} e absorveu {pontos_apostados} pontos")
        return "Duelo registrado com sucesso!"
    else:
        return "Erro: Um dos feiticeiros não foi encontrado na barreira."
    
def exibir_historico(historico):
    if not historico:
        return "Não teve lutas na barreira"
    else:
        return "\n".join(historico)
    
def exibir_menu():
    opcoes = ["Adicionar Jogador", "Listar Jogadores", "Remover Jogador(Morto)", "Atualizar Pontos", "Duelo", "Exibir o Historico de feiticeiros", "Sair" ]
    listagem = [f"{indice} - {opcao}" for indice, opcao in enumerate(opcoes, start= 1)]
    print("=== Jogo do Abate ===")
    print("\n".join(listagem))
    print("==========================")

def menu():
    barreira = {}
    historico = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            jogador = input("Digite o nome do jogador: ").upper().strip()
            grau = input("Qual é seu grau de Feiticeiro: ")
            pontos = obter_pontos_validos(input("Digite a quantidade pontos que ele possui: "))
            print(adicionar_feiticeiro(barreira, jogador, grau, pontos))
        
        elif opcao == "2":
            print(listar_jogadores(barreira))

        elif opcao == "3":
            jogador = input("Digite o jogador que foi eliminado: ").upper().strip()
            print(remover_feiticeiro(barreira, jogador))

        elif opcao == "4":
            jogador = input("Digite o nome do jogador: ").upper().strip()
            pontos = obter_pontos_validos(input("Digite seus novos pontos: "))
            print(atualizar_pontos(barreira, jogador, pontos))

        elif opcao == "5":
            vencedor = input("Digite o nome do Vencedor: ").upper().strip()
            perdedor = input("Digite o nome do Perdedor: ").upper().strip()
            pontos_apostados = obter_pontos_validos(input("Quantos pontos foram apostados? "))
            print(registrar_duelo(barreira, historico, vencedor, perdedor, pontos_apostados))

        elif opcao == "6":
            print(exibir_historico(historico))

        elif opcao == "7":
            print("Encerrando barreira...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
