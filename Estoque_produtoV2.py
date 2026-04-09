def adicionar_produto(estoque, nome, quantidade, preco):
    nome = nome.title()
    if nome in estoque:
        return "Erro: Produto já cadastrado."
    else:
        estoque[nome] = {"quantidade": quantidade, "preço": preco}
        return "Produto adicionado com sucesso!"

def listar_produtos(estoque):
    if not estoque:
        return "O estoque está vazio."
    else:
        resultado = []
        # O lambda olha para o nome do produto (posição 0)
        for nome, detalhes in sorted(estoque.items(), key=lambda x: x[0]):
            resultado.append(f"{nome}: {detalhes['quantidade']} disponíveis - R$ {detalhes['preço']:.2f}")
        return "\n".join(resultado)

def remover_produto(estoque, nome):
    nome = nome.title()
    if nome in estoque:
        del estoque[nome]
        return f"Produto '{nome}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."

def atualizar_quantidade(estoque, nome, nova_qtd):
    nome = nome.title()
    if nome in estoque:
        estoque[nome]["quantidade"] = nova_qtd
        return "Quantidade atualizada com sucesso!"
    else:
        return "Erro: Produto não encontrado."

def exibir_menu():
    return (
        "\n1 - Adicionar produto"
        "\n2 - Listar produtos"
        "\n3 - Remover produto"
        "\n4 - Atualizar quantidade"
        "\n5 - Sair"
    )

def main():
    # O Dicionário agora nasce aqui dentro! Ele é Local.
    estoque = {} 
    
    while True:
        print(exibir_menu())
        opcao = input("Escolha a opção: ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            # O main entrega o "estoque" junto com os outros ingredientes!
            print(adicionar_produto(estoque, nome, quantidade, preco))
            
        elif opcao == "2":
            print(listar_produtos(estoque))
            
        elif opcao == "3":
            nome = input("Nome do produto: ")
            print(remover_produto(estoque, nome))
            
        elif opcao == "4":
            nome = input("Nome do produto: ")
            nova_qtd = int(input("Nova quantidade: "))
            print(atualizar_quantidade(estoque, nome, nova_qtd))
            
        elif opcao == "5":
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida.")

# A chave de ignição
if __name__ == "__main__":
    main()