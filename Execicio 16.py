palavras = []

while True:
    elemento = input("Digite os nomes de alunos para adicionar à lista (ou 'fim' para terminar): ")
    if elemento == 'fim':
        break
    palavras += [elemento]

print("Lista de alunos:", palavras)

letra = input("Digite uma letra para filtrar as palavras: ").lower()

for palavra in palavras:
    if palavra.startswith(letra):
        print(palavra)