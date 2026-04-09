print ("Escolha uma opção")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Divisão")
print ("4 - Multiplicação")

opcao = input("Digite a operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("O resultado é ", num1 + num2)
elif opcao == "2":
    print("O resultado é ", num1 - num2)
elif opcao == "3":
    if num2 == 0:
        print("Erro, não existe multiplicação por 0")
    else:
        print("O resultado é ",num1 / num2)
elif opcao == "4":
    print("O resultado é ", num1 * num2)

