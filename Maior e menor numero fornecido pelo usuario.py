numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()  


numeros = [int(num) for num in numeros]


maior = max(numeros)
menor = min(numeros)


print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")