def obter_dados_livro(titulo, autor, quantidade):
    return f"{titulo} {autor} {quantidade}"

def obter_quantidade_livro(valor):
    try:
        quantidade = int(valor)
        if quantidade < 0:
            return 0
        return quantidade
    except ValueError:
        return "Por favor, insira um número válido para a quantidade."

def validar_livro_existe(biblioteca, titulo):
    if titulo in biblioteca:
        return True
    return f"Erro: O livro '{titulo}' não foi encontrado."

def adicionar_livro(biblioteca, titulo, autor, quantidade):
    if validar_livro_existe(biblioteca, titulo) == True:
        return f"Erro: O livro '{titulo}' já está cadastrado."
    biblioteca[titulo] = {"autor": autor, "quantidade": quantidade}
    return f"Livro '{titulo}' adicionado com sucesso"

def listar_livros(biblioteca):
    if not biblioteca:
        return "Não há livros cadastrados."
    linhas = []
    for titulo, dados in sorted(biblioteca.items()):
        linhas.append(f"Título: {titulo} | Autor: {dados['autor']} | Quantidade: {dados['quantidade']}")
    return "\n".join(linhas)

def remover_livro(biblioteca, titulo):
    if validar_livro_existe(biblioteca, titulo) == True:
        del biblioteca[titulo]
        return f"Livro '{titulo}' removido com sucesso!"
    else:
        return validar_livro_existe(biblioteca, titulo)

def atualizar_quantidade(biblioteca, titulo, nova_quantidade):
    if validar_livro_existe(biblioteca, titulo) == True:
        dados_livro = biblioteca.get(titulo, {})
        dados_livro["quantidade"] = nova_quantidade
        return f"Quantidade de exemplares do livro '{titulo}' atualizada para {nova_quantidade}"
    else:
        return validar_livro_existe(biblioteca, titulo)

def registrar_emprestimo(biblioteca, historico, titulo, quantidade):
    if validar_livro_existe(biblioteca, titulo) == True:
        if biblioteca[titulo].get("quantidade", 0) >= quantidade:
            biblioteca[titulo]["quantidade"] -= quantidade
            historico.append((titulo, quantidade))
            return f"{quantidade} exemplares de '{titulo}' emprestados com sucesso!"
        else:
            return f"Erro: Quantidade insuficiente no estoque para o livro '{titulo}'."
    else:
        return validar_livro_existe(biblioteca, titulo)

def obter_quantidade_livro_para_emprestimo(biblioteca, titulo, valor):
    try:
        quantidade = int(valor)
        if quantidade <= 0:
            return "Erro: Quantidade deve ser maior que zero."
        elif quantidade > biblioteca.get(titulo, {}).get("quantidade", 0):
            return f"Erro: Quantidade indisponível para o livro '{titulo}'."
        else:
            return quantidade
    except ValueError:
        return "Erro: Insira um número válido."

def exibir_historico_emprestimos(historico):
    if not historico:
        return "Não há histórico de empréstimos."
    return "\n".join([f"Livro: {titulo} | Qtd emprestada: {qtd}" for titulo, qtd in historico])

def exibir_menu():
    return """
=== Menu da Biblioteca ===
1. Adicionar Livro
2. Listar Livros
3. Remover Livro
4. Atualizar Quantidade
5. Registrar Empréstimo
6. Exibir Histórico
0. Sair
==========================
"""

def menu():
    biblioteca = {}
    historico = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            quantidade = obter_quantidade_livro(input("Digite a quantidade: "))
            print(adicionar_livro(biblioteca, titulo, autor, quantidade))
            
        elif opcao == "2":
            print(listar_livros(biblioteca))
            
        elif opcao == "3":
            titulo = input("Digite o título do livro a ser removido: ")
            print(remover_livro(biblioteca, titulo))
            
        elif opcao == "4":
            titulo = input("Digite o título do livro: ")
            quantidade = obter_quantidade_livro(input("Digite a nova quantidade: "))
            print(atualizar_quantidade(biblioteca, titulo, quantidade))
            
        elif opcao == "5":
            titulo = input("Digite o título do livro para empréstimo: ")
            quantidade_emprestada = input("Digite a quantidade desejada: ")
            quantidade_valida = obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade_emprestada)
            
            if isinstance(quantidade_valida, int):
                print(registrar_emprestimo(biblioteca, historico, titulo, quantidade_valida))
            else:
                print(quantidade_valida)
                
        elif opcao == "6":
            print(exibir_historico_emprestimos(historico))
            
        elif opcao == "0":
            print("Encerrando o sistema da biblioteca...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()