# Exemplo de "if", "else" e "elif"
idade = int(input("Quantos anos você tem? ")) # Entrada de dados com "input"
print("Exemplo do comando if")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação." if idade >= 18 else "você não pode tirar a carteira de habilitação."
print(mensagem)