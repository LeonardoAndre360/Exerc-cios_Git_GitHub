saldo = 1000
while True:
    print ("Qual opção ira usar: ")
    print ("1 - Ver saldo")
    print ("2 - Depositar")
    print ("3 - Sacar")
    print ("4 - Sair")

    opcao = input ("digite o número da sua opção ")

    if opcao == "1":
        print(saldo)
    elif opcao == "2":
        num1 = float(input("Quanto gostaria de depositar: "))
        saldo = saldo + num1
        print("Saldo atual é: ", saldo)
    elif opcao == "3":
        num1 = float(input("Quanto gostaria de sacar: "))
        if num1 > saldo:
            print("saldo insuficiente")
        else:
            saldo = saldo - num1
            print("seu saldo atual é:", saldo)
    elif opcao == "4":
        print("Até a proxima, obrigado por usar nossos serviços")
        break
    else:
        print("Opção invalidade, escolha uma entre as 4 opções")