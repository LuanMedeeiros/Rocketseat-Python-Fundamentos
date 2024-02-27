lista = [1, 2, 3, 4, 5]
for elemento1 in lista:
    print(elemento1)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento2 in tupla:
    print(elemento2)

pessoa = {"nome": "João", "idade": 20, "cidade": "São paulo"}
print("\nFor utilizando dicionario - chave")
for chaves in pessoa.keys():
    print(chaves)

print("\nFor utilizando dicionario - valor")
for valores in pessoa.values():
    print(valores)

print("\nFor utilizando dicionario - chave/valor")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("\nUtilizando a função range()")
# range(): intervalo numérico
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in range(5):
    print("Numero:", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

print("\n")
# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")