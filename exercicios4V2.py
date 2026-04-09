def exibir_menu():
    tipos_conversores = ["Celsius para Fahrenheit", "Quilômetros para Milhas", "Quilogramas para Libras", "Horas para Segundos", "Sair do programa"]
    lista_formatada = [f"{conversor} - {nomes}" for conversor, nomes in enumerate(tipos_conversores, start=1)]
    print("\n".join(lista_formatada))  

def main():
    
    fahrenheit = lambda c: (c * 9/5) + 32
    milhas = lambda km: km * 0.621371
    libras = lambda kg: kg * 2.20462
    segundos = lambda h: h * 3600
    
    while True:
        exibir_menu()
        escolha = input("Digite a opção desejada:\n")
        if escolha == "5":
            print("Até a proxima")
            break
        if escolha not in ["1", "2", "3", "4"]:
            print("Opção invalida, escolha uma das 5 opções")
            continue

        try:
           conversor = float(input("Digite o primeiro valor que deseja converter:\n"))
        except ValueError:
            print("Letra não é um valor, Digite um número")
            continue
        if escolha == "1":
            print(f"A conversão de Celsius para Fahrenheit é: {fahrenheit(conversor)}ºF")
        elif escolha == "2":
            while conversor < 0:
                conversor = float(input("Não existe quilômetros negativos, digite valores positivos:\n"))
            else:
                print(f"O valor de Quilômetros para Milhas é: {milhas(conversor)}mi")
        elif escolha == "3":
            while conversor < 0:
                conversor = float(input("Não existe Kilos negativos, digite valores positivos:\n"))
            else:
                print(f"O valor de Quilogramas para Libras é: {libras(conversor)} Libras")
        elif escolha == "4":
            while conversor < 0:
                conversor = float(input(("Não existe horas negativas, digite valores positivos:\n")))
            else:
                print(f"O valor de Horas para Segundos é: {segundos(conversor)} segundos")
        
        while True:
                resposta = input("Você quer fazer outra conversão ?(Sim / Não):\n")
                if resposta in ["Sim", "sim", "s", "S"]:
                    print("Voltando para o menu...")
                    break
                elif resposta in ["Não", "nao", "não", "n", "N"]:
                    print("Então até a proxima")
                    return
                else:
                    print("Resposta inválida! Por favor, digite apenas Sim ou Não.")

main()
