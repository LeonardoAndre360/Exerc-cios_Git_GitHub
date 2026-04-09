def exibir_menu():
        operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Sair do programa"]
        lista_formatada = [f"{numeros} - {nomes}" for numeros, nomes in enumerate(operacoes, start=1)]
        print("\n".join(lista_formatada))
def main():
    soma = lambda a, b: a + b
    subtracao = lambda a, b: a - b
    multiplicacao = lambda a, b: a * b
    divisao = lambda a, b: a / b
    while True:
        exibir_menu()
        escolha = input("Escolha uma das opções:\n")
        if escolha == "5":
             print("Até a proxima")
             break
        if escolha not in ["1", "2", "3", "4"]:
             print("Opção invalida, escolha uma das 5 opções")
             continue
        

        try:
            numero1 = float(input("Digite o primeiro número:\n"))
            numero2 = float(input("Digite o segundo número:\n"))
        except ValueError:
            print("Opção invalida, escolha outro número")
            continue
        if escolha == "1":
            print(f"O resultado é: {soma(numero1, numero2)}")
        elif escolha == "2":
            print(f"O resultado é: {subtracao(numero1, numero2)}")
        elif escolha == "3":
            print(f"O resultado é: {multiplicacao(numero1, numero2)}")
        elif escolha == "4":
            
            while numero2 == 0:
                numero2 = float(input("Não existe disvisão por zero, digite outro numero:\n"))
            else :
                print(f"O resultado é: {divisao(numero1, numero2)}")
        while True:
                resposta = input("Você quer jogar de novo? (Sim / Não):\n")
                if resposta in ["Sim", "sim", "s", "S"]:
                    print("Voltando para o menu...")
                    break
                elif resposta in ["Não", "nao", "não", "n", "N"]:
                    print("Então até a proxima")
                    return
                else:
                    print("Resposta inválida! Por favor, digite apenas Sim ou Não.")
            
        


main()       


