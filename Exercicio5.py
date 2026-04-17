def exibir_menu():
        menu = ["Adicionar Livros", "Listar Livros", "Remover Livros", "Atualizar quantidade", "Registrar emprestimo", "Exibir histórico", "Sair"]
        listagem = [f"{menu} - {metodos}" for menu, metodos in enumerate(menu, start= 1)]
        print("-- Biblioteca --")
        print("\n".join(listagem))

def main():
        acervo_biblioteca = {}
        historico_emprestismo = []

        while True:
            exibir_menu()
            escolha = input("Qual Opção da biblioteca você gostaria de acessar?\n")
            if escolha == "7":
                   print("Até a próxima!")
                   break
            elif escolha not in ["1", "2", "3", "4", "5", "6"]:
                   print("Escolha invalida, escolha uma das 7 opções, atráves dos números")
                   continue
            
            elif escolha == "1":
                   print("Você escolheu Adicionar livro.")
                   livro = input("Qual livro você gostaria de adicionar ?\n").upper().strip()
                   variavel_do_autor = input("Qual o nome do autor ?\n").upper().strip()
                   variavel_de_quantidade = int(input("Qual a quantidade ?\n"))
                   acervo_biblioteca[livro] = {
                          "autor": variavel_do_autor,
                          "quantidade": variavel_de_quantidade
                   }
            
            elif escolha == "2":
                   if len(acervo_biblioteca) == 0:
                         print("Não a nenhum livro na biblioteca")
                   else:
                     print("-- Lista de Livros --")
                     titulos_em_ordem = sorted(acervo_biblioteca.keys())
                     for titulo in titulos_em_ordem:
                            nome_autor =  acervo_biblioteca[titulo]["autor"]
                            qtd_disponivel = acervo_biblioteca[titulo]["quantidade"]
                            print(f"{titulo} - Autor {nome_autor} - quantidade: {qtd_disponivel}")

            elif escolha == "3":
                   titulo_digitado = input("Qual titulo você você gostaria de remover?\n").upper().strip()
                   if titulo_digitado in acervo_biblioteca:
                          del acervo_biblioteca[titulo_digitado]
                   else:
                          print("O livro não está listado em nossa biblioteca")

            elif escolha == "4":
                   titulo_solicitado = input("Qual seria o livro que gostaria de atualizar?\n").upper().strip()
                   qtd_atualizada = int(input("Qual vai ser a nova quantidade"))
                   if titulo_solicitado in acervo_biblioteca:
                     acervo_biblioteca[titulo_solicitado]["quantidade"] = qtd_atualizada
                   else:
                          print("Livro não encontrado")

            elif escolha == "5":
                   livro_emprestado = input("Qual livro você gostaria de levar ?\n").upper().strip()
                   qtd_a_menos = int(input("Qual será a quantidade ?\n"))
                   if livro_emprestado in acervo_biblioteca:
                     if qtd_a_menos <= acervo_biblioteca[livro_emprestado]["quantidade"]:
                           acervo_biblioteca[livro_emprestado]["quantidade"] -= qtd_a_menos
                           historico_emprestismo.append(f"{livro_emprestado} - {qtd_a_menos} exemplares")
                           print("Emprestimo realizado com sucesso!")
                     else:
                           print("Erro: Não há exemplares suficientes disponíveis")
                   else:
                         print("Livro não encontrado")
            elif escolha == "6":
                  if len(historico_emprestismo) == 0:
                        print("Não há nenhum emprestimo")
                  else:
                        print("\n-- Histórico de Empréstimo --")
                        for item in historico_emprestismo:
                              print(item)

main()
              
                   