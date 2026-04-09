class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return("O Animal emitiu um som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        return ("O cachorro latiu!")
    
class Gato(Animal):
    def emitir_som(self):
        return ("O Gato Miou!")
    
cachorro = Cachorro("Sif",5)
gato = Gato("Felix", 3)

print(f"{cachorro.emitir_som()} Seu nome é {cachorro.nome}, e ele tem {cachorro.idade} anos")
print(f"{gato.emitir_som()} Seu nome é {gato.nome}, ele tem {gato.idade} anos")

