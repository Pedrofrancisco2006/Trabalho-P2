
lista = []

while True:
    alunos = input("Digite os nomes de alunos para adicionar à lista (ou 'fim' para terminar): ")
    if alunos == 'fim':
        break
    lista += [alunos]

print("Lista de alunos:", lista)

