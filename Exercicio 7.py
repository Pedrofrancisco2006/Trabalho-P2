lista = []

while True:
    elemento = input("Digite um elemento para adicionar à lista (ou 'parar' para terminar): ")
    if elemento == 'parar':
        break
    lista += [elemento]

print("Lista completa:", lista)
