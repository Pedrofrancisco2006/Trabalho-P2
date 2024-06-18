print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


operacao = input("Digite sua escolha (1/2/3/4): ")


if operacao == '1':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("Resultado: ", resultado)
elif operacao == '2':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("Resultado: ", resultado)
elif operacao == '3':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("Resultado: ", resultado)
elif operacao == '4':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado: ", resultado)
    else:
        print("Erro: divisão por zero!")
else:
    print("Opção inválida!")