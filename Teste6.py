radar_titan = {}

def Detectar_titan(titan):
    titan = titan.strip().title()
    if titan in radar_titan:
        return("Aviso: Este Titã já está sendo monitorado!")
    else:
        radar_titan[titan] = False
        return f"Titã {titan} detectado no radar!"
    
def listar_titan(lista):
   if not lista:
    return("O radar está limpo. Nenhuma ameaça.")
   else:
    resultado = []
    for nome_titan, concluida in sorted(lista.items(), key=lambda x: (x[1], x[0])):
        status = "💀 Abatido" if concluida else "⚠️ Vivo"
        resultado.append(f"{status} - {nome_titan}")
    return "\n".join(resultado)
   
def perder_sinal(perca):
    perda = perda.strip().title()
    if perda in radar_titan:
       del radar_titan[perda]
       return f"Perdemos o sinal do Titã '{perca}'."
    else:
       return f"Erro: Titã não encontrado."
    
def abater_titan(abate):
   abate = abate.strip().title()
   if abate in radar_titan:
      radar_titan[abate] = True
      return f"Alvo '{abate}' foi abatido com sucesso!"
   else:
      return f"O titã não listado"
   
def exibir_menu():
    return (
    "\n-- LISTA DE DECISÕES --"
    "\n1-  Detectar Titan"
    "\n2 - Relatorio"
    "\n3 - Perder Sinal"
    "\n4 - Abater Titã"
    "\n5 - Retornar a Muralha:"
    )

def main():
   while True:
      print(exibir_menu())
      escolha = input("Escolha uma opção:\n")

      if escolha == "1":
        nome = input("Qual titã você adicionar?\n").strip().title()
        nome = nome.replace("Titã","").replace("Tita","")
        print(Detectar_titan(nome))

      elif escolha == "2":
        print(listar_titan(radar_titan))

      elif escolha == "3":
        nome = input("Qual titã você perdeu de vista?\n").strip().title()
        nome = nome.replace("Titã","").replace("Tita","")
        print(perder_sinal(nome))

      elif escolha == "4":
        nome = input(("Qual titã você abateu?\n")).strip().title()
        nome = nome.replace("Titã","").replace("Tita","")
        print(abater_titan(nome))

      elif escolha == "5":
         print("Retornando até as Muralhas")
         break
      else:
         print("Opção invalida, escolha uma das cinco opções")

if __name__ == "__main__":
    main()