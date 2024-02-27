# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando uma nova chave
pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

# Alterando uma chave
pessoa["idade"] = 31
print("Idade após alteração da chave:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário após remover o par chave-valor 'sobrenome':", pessoa)

# Método keys
chaves = list(pessoa.keys()) # Para acessar cada elemento individualmente é preciso transformar em uma lista
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Método values
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Método items
itens = list(pessoa.items())
print("Pares cahve-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))