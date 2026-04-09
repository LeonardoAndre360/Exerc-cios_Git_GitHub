estoque = {}

def adicionar_produto(nome, valor, quantidade):
    if nome in estoque:
        return f"Aviso este {nome} já está no estoque"
    else:
        estoque[nome] = {"quantidade": quantidade, "valor": valor}
        return f"Item adicionado com sucesso"

def lista_estoque(lista):
    if not lista:
        return("Ainda não tem nenhum produto no estoque")
    else:
        resultado = []
        for nome_produto, detalhes in sorted(lista.items(), key=lambda x: x[0]):
            qtd = detalhes["quantidade"]
            valor = detalhes["valor"]
            frase = f"{nome_produto}: {qtd} disponiveis - R$ {valor:.2f}"
            resultado.append(frase)
        return "\n".join(resultado)
        
def remover_itens(remover):
    remover = remover.strip().title()
    if remover in estoque:
        del estoque[remover]
        return(f"O item {remover} foi tirado do estoque")
    else:
        return("O item solicitado não esta no estoque")
    
def atualizar_quantidade(atz, nova_qtd):
    atz = atz.strip().title()
    if atz in estoque:
        estoque[atz]["quantidade"] = nova_qtd
        return f"Sucesso! A quantidade de '{atz}' foi atualizada para {nova_qtd}."
    else:
        return f"O produto não está no estoque"

def exibir_menu():
    return(
        "\n -- Lista do Estoque --"
        "\n1 - Adicionar produto"
        "\n2 - Listar produtos"
        "\n3 - Remover produto"
        "\n4 - Atualizar quantidade de produto"
        "\n5 - Sair"
    )
def main():
    while True:
        print(exibir_menu())
        escolha = input("Qual opção irá escolher?\n")
        
        if escolha == "1":
            nome = input("Qual é o nome do produto ?\n").strip().title()
            quantidade = int(input (f"Qual será a quantidade do {nome} ?\n"))
            valor = float(input(f"Qual será o valor do {nome} ?\n").replace(",", "."))
            print(adicionar_produto(nome, valor, quantidade))
        
        elif escolha == "2":
            print(lista_estoque(estoque))
        
        elif escolha == "3":
            perda_produto = input("Qual item voce gostaria de retirar?\n").strip().title()
            print(remover_itens(perda_produto))
        elif escolha == "4":
            atualizar = input("Qual item voce quer atualizar?\n").strip().title()
            nova_qtd = int(input(f"Qual será a nova quantidade {atualizar}?\n"))
            print(atualizar_quantidade(atualizar, nova_qtd))
        
        elif escolha == "5":
            print("Até a próxima!")
            break
        else:
            print("Opção invalida escolha uma das 5 opções")

if __name__ == "__main__":
    main()

