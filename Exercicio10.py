numero = int(input("Digite um número para verificar se é perfeito: "))


divisores = []
for i in range(1, numero):
    if numero % i == 0:
        divisores.append(i)


soma_divisores = sum(divisores)


if soma_divisores == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")