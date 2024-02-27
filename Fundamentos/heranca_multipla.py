class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."

# Herança multipla:
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcego emite sons ultassônicos."

morcego = Morcego("Batman")

# Acessando métodos da classe base 'Animal'
print(f"\nNome do morcego: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

# Acessando métodos das classes 'Mamiferos' e 'Ave'
print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")

print("\nFim.")