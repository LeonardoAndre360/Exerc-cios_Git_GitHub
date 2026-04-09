# Variável global de tarefas
Dicionario= {}

def adicionar_tarefa(nome):
    nome = nome.strip().title()
    if nome in Dicionario:
        return "Erro esta Tarefa já existe"
    else:
        Dicionario[nome] = "Pendente"
        return "adicionada com sucesso"

def listar_tarefas(Dicionario):
    if not Dicionario:
        return "Nenhuma tarefa adicionada"
    else:
        resultado = ["\n --- Suas Tarefas ---"]
        for tarefa, status in sorted(Dicionario.items(), key=lambda x: x[0]):
            status = marca = "[X]" if status == "Concluido" else "[]"
            resultado.append(f"{marca} {tarefa}")
        return "\n".join(resultado)

def remover_tarefa(nome):
    nome= nome.strip().title()
    if nome in Dicionario:
        del Dicionario[nome]
        return "Tarefa removida"
    else:
        return "Erro, Tarefa que não existe"

def marcar_concluida(nome):
    nome = nome.strip().title()
    if nome in Dicionario:
        Dicionario[nome] = "Concluido"
        return "Sua tarefa esta concluida"
    else:
        return "Erro! Tarefa que não existe"

def exibir_menu():
    return (
        "\n -- Menu de Tarefas -- \n"
        "1 - Adicionar tarefa\n"
        "2 - Listar Tarefas\n"
        "3 - Remover Tarefas\n" 
        "4 - Marcar tarefa como concluida\n"
        "5 - Sair\n"  
    )

def main():
    while True:
        print(exibir_menu())
        nome = input("Escolha uma opção:\n")

        if nome == "1":
            nome = input("Qual tarefa voce irá adicionar?\n")
            print(adicionar_tarefa(nome))
        elif nome == "2":
            print(listar_tarefas(Dicionario))
        elif nome == "3":
            nome = input("Qual tarefa iremos remover:")
            print(remover_tarefa(nome))
        elif nome == "4":
            nome = input("Qual tarefa está concluida?\n")
            print(marcar_concluida(nome))
        elif nome == "5":
            print("Adeus! Até logo")
            break
        else:
            print("Opção invalida, escolha outra")

if __name__ == "__main__":
    main()