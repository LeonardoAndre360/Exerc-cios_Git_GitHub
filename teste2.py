while True:
    print ("Digite qual metodo você quer calcular ")
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Encerrar o programa")

    opcao = input("Qual operação irá fazer: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número"))
        print ("O resultado é:", num1 + num2)
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número"))
        print("O resultado é ", num1 - num2)
    elif opcao == "3":
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número"))
        print("O resultado é ", num1 * num2)
    elif opcao == "4":
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número"))
        if num2 == 0:
            print("Erro, não existe divisão por 0")
        else:
            print("O resultado é ", num1 / num2)
            
    elif opcao == "5":
        print("Encerrando a calculadora, até mais!")
        break
    else:
        print("Opção invalida, por favor tente novamente")


