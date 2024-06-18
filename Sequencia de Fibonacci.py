def fibonacci_ate(numero):
    fib = [0, 1]  
    
   
    while fib[-1] <= numero:
        fib.append(fib[-1] + fib[-2])
    
    
    if fib[-1] > numero:
        fib.pop()

    return fib


while True:
    try:
        num = int(input("Digite um número inteiro positivo para exibir a sequência de Fibonacci (ou '0' para sair): "))
        if num == 0:
            print("Programa encerrado.")
            break
        if num < 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        
       
        fib_sequence = fibonacci_ate(num)
        
       
        print(f"A sequência de Fibonacci até {num} é: {fib_sequence}")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")