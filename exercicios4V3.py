def exibir_menu():
    taxas = ["Dinheiro(10% de desconto)", "Cartão de Débito(Preço normal)", "Cartão de Crédito á vista(5% de acréscimo)", "Cartão de Crédito Parcelado (15% de acréscimo)", "Cancelar e Sair"]
    lista_numerada = [f"{taxa} - {metodos}" for taxa, metodos in enumerate(taxas, start=1)]
    print("\n".join(lista_numerada))

def main():
    dinheiro = lambda v: v * 0.90
    debito = lambda v: v
    credito_a_vista = lambda v: v * 1.05
    credito_parcelado = lambda v: v * 1.15

    while True:
        exibir_menu()
        escolha = input("Qual será a forma de pagamento:\n")
        if escolha == "5":
            print("Até a proxima compra")
            break
        if escolha not in ["1", "2", "3", "4"]:
            print("Escolha invalida, escolha uma das 5 opções.")
            continue

        try:
            conversor = float(input("Qual o valor do pagamento?\n"))
        except ValueError:
            print("Letra não é um valor, digite um número")
            continue
        while conversor <= 0:
            conversor = float(input("Erro, não existe valor devedor, digite um valor positivo:\n"))

        if escolha == "1":
            print(f"O valor com desconto fica em R${dinheiro(conversor):.2f}")
        
        elif escolha == "2":
            print(f"Como o valor foi no débito o valor continua o mesmo: R${debito(conversor):.2f}")
        
        elif escolha == "3":
            print(f"O acrescimo no valor faz ficar em R${credito_a_vista(conversor):.2f}")
        
        elif escolha == "4":
            parcelar = int(input("Em quantas parcelas gostaria, parcelamos em até 12 vezes?\n"))
            while parcelar < 2 or parcelar > 12:
                parcelar = int(input("Quantidade inválida! Escolha entre 2 e 12 parcelas:\n"))
            total_com_juros = credito_parcelado(conversor)
            valor_da_parcela = total_com_juros / parcelar
            print(f"O total com juros é R${total_com_juros:.2f}")
            print(f"Sua compra foi dividida em {parcelar}x de R${valor_da_parcela:.2f} por mês")

        while True:
            resposta = input("Gostaria de fazer outra compra? (S/N)\n")
            if resposta in ["Sim", "sim", "s", "S"]:
                print("Voltando para o menu...")
                break
            elif resposta in ["Não", "nao", "não", "n", "N"]:
                print("Então até a proxima")
                return
            else:
                print("Resposta inválida! Por favor, digite apenas Sim ou Não.")

main()

