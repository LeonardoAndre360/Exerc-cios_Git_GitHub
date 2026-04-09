shikigami = {}

def adicionar_shikigami(adicionar):
    adicionar = adicionar.strip().title()
    if adicionar in shikigami:
        return("Este shikigami já foi encontrado")
    else:
        shikigami[adicionar] = False
        return f"O '{adicionar}' foi encontrado"

def listar_shikigami(listagem):
    if not listagem:
        return("Nenhum, shikigami na lista")
    else:
        resultado = []
        for nome_shikigami, concluida in sorted(listagem.items(), key=lambda x: (x[1], x[0])):
            status = "🐺 Domado" if concluida else "🩸 Selvagem"
            resultado.append(f"{status} - {nome_shikigami}")
        return "\n".join(resultado)

def perder_shikigami(perda):
    perda = perda.strip().title()
    if perda in shikigami:
        del shikigami[perda]
        return f"O '{perda}' foi destruido para sempre!"
    else:
        return f"Shikigami não está na lista"

def dominar_shikigami(domar):
    domar = domar.strip().title()
    if domar in shikigami:
        shikigami[domar] = True
        return f"O '{domar}' foi dominado!"
    else:
        return f"Erro: Shikigami não encontrado no ritual."

def exibir_menu():
    return (
        "\n -- Menu do Usuário das 10 Sombras --"
        "\n 1 - Adicionar shikigami"
        "\n 2 - Listar Shikigami"
        "\n 3 - Perca do Shikigami"
        "\n 4 - Domar shikigami"
        "\n 5 - Ir para casa"
    )

def main():
    while True:
        print(exibir_menu())
        escolha = input("Escolha uma Opção\n")

        if escolha == "1":
            nome = input("Qual shikigami voce vai adicionar?\n").strip().title()
            print(adicionar_shikigami(nome))
        elif escolha == "2":
            print(listar_shikigami(shikigami))
        elif escolha == "3":
            nome = input("Qual shikigami foi destruido?\n").strip().title()
            print(perder_shikigami(nome))
        elif escolha == "4":
            nome = input("Qual shikigami você dominou?\n").strip().title()
            print(dominar_shikigami(nome))
        elif escolha == "5":
            print("Até o proximo dia")
            break
        else:
            print("Opção invalida, escolha de 1 a 5 das opções")

if __name__ == "__main__":
    main()