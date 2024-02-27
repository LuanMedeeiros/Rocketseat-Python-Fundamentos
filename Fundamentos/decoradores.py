from typing import Any

# Exemplo de decorador:
def meu_decorador(func):
    def wrapper():
        print("\nAntes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

# Exemplo de decorador (Usando classe)
class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> Any:
        print("\nAntes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")
        
@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada")

segunda_funcao()