class Personagem:
    def __init__(self, nome, energia_amaldicoada):
        self.nome = nome
        self.energia_amaldicoada = energia_amaldicoada

    def usar_poder(self):
        return "Concentrando energia amaldiçoada padrão..."
    
class Feiticeiro(Personagem):
    def usar_poder(self):
        return f"{self.nome} ativou sua Técnica Amaldiçoada"

class Maldicao(Personagem):
    def usar_poder(self):
        return f"A maldição {self.nome} atacou com pura intenção assassina!"

class CampoDeBatalha():
    def __init__(self):
        self.lista_de_lutadores = []

    def adicionar_lutador(self, personagem):
        self.lista_de_lutadores.append(personagem)

    def iniciar_batalha(self):
        print("--- A BATALHA EM SHIBUYA COMEÇOU ---")
        for lutador in self.lista_de_lutadores:

            mensagem_do_poder = lutador.usar_poder()
            print(f"{mensagem_do_poder} (Nivel de Energia: {lutador.energia_amaldicoada})")

gojo = Feiticeiro("Gojo", 10000)
jogo = Maldicao("Jogo", 1000)

shibuya = CampoDeBatalha()

shibuya.adicionar_lutador(gojo)
shibuya.adicionar_lutador(jogo)

shibuya.iniciar_batalha()

