# Classe exemplo:
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos exemplo:
print("\nExemplos de Objetos:")
pessoa1 = Pessoa("Luan", 20)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Rodrigo", 32)
mensagem = pessoa2.saudacao()
print(mensagem)