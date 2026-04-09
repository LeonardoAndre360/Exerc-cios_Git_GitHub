# --- AS NOSSAS CLASSES DE MOLDES (Atores) ---
class Personagem:
    def __init__(self, nome, energia_amaldicoada):
        self.nome = nome
        self.energia_amaldicoada = energia_amaldicoada

    def usar_poder(self):
        return "Concentrando energia amaldiçoada padrão..."
    
class Feiticeiro(Personagem):
    def usar_poder(self):
        return f"{self.nome} ativou sua Técnica Amaldiçoada!"

class Maldicao(Personagem):
    def usar_poder(self):
        return f"A maldição {self.nome} atacou com pura intenção assassina!"


# --- A NOSSA CLASSE GERENCIADORA (O Palco) ---
class CampoDeBatalha:
    def __init__(self):
        # O campo nasce vazio, apenas com uma lista pronta para receber dados
        self.lista_de_lutadores = []

    def adicionar_lutador(self, personagem):
        # O .append pega o objeto que passamos e joga dentro da lista
        self.lista_de_lutadores.append(personagem)

    def iniciar_batalha(self):
        print("--- A BATALHA EM SHIBUYA COMEÇOU! ---")
        
        # O laço 'for' percorre a lista. 
        # A cada volta, a variável temporária 'lutador' assume a identidade de um objeto da lista.
        for lutador in self.lista_de_lutadores:
            
            # Como o Python sabe que 'lutador' é um objeto (Feiticeiro ou Maldicao),
            # ele consegue acionar o método usar_poder() e ler o atributo energia_amaldicoada!
            mensagem_do_poder = lutador.usar_poder()
            print(f"{mensagem_do_poder} (Nível de Energia: {lutador.energia_amaldicoada})")


# --- O PROGRAMA PRINCIPAL (A Execução) ---

# 1. Criamos os nossos objetos soltos
gojo = Feiticeiro("Gojo", 10000)
jogo = Maldicao("Jogo", 1000)

# 2. Criamos o nosso objeto Gerenciador (O Campo de Batalha)
shibuya = CampoDeBatalha()

# 3. Colocamos os objetos dentro do Gerenciador usando o método que criamos
shibuya.adicionar_lutador(gojo)
shibuya.adicionar_lutador(jogo)

# 4. Damos o comando final. O Gerenciador vai cuidar do resto!
shibuya.iniciar_batalha()