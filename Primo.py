def eh_primo(numero):
    # Verifica se o número é maior que 1
    if numero <= 1:
        return False
    
    # Verifica se o número é divisível por algum número além de 1 e ele mesmo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    # Se não encontrou nenhum divisor além de 1 e ele mesmo, então é primo
    return True

# Função para entrada do usuário e verificação de número primo
def main():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo (ou '0' para sair): "))
            if num == 0:
                print("Programa encerrado.")
                break
            if num < 0:
                print("Por favor, digite um número inteiro positivo.")
                continue
            
            if eh_primo(num):
                print(f"{num} é um número primo.")
            else:
                print(f"{num} não é um número primo.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
if __name__ == "__main__":
    main()            