maior_numero = None
menor_numero = None
numeros = []

entrada = input("Digite um número (ou 'fim' para encerrar): ")

while entrada.lower() != 'fim':
    if entrada.replace('.', '', 1).lstrip('-').isdigit():
        numero = float(entrada)
        if maior_numero is None or numero > maior_numero:
            maior_numero = numero
        if menor_numero is None or numero < menor_numero:
            menor_numero = numero
        numeros.append(numero)
        entrada = input("Digite outro número (ou 'fim' para encerrar): ")
    else:
        print("Entrada inválida. Digite um número válido ou 'fim' para encerrar.")
        entrada = input("Digite outro número (ou 'fim' para encerrar): ")

if numeros:
    print(f"O maior número é: {maior_numero}")
    print(f"O menor número é: {menor_numero}")
else:
    print("Nenhum número válido foi inserido.")
