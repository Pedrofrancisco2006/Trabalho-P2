fila = []

while True:
    elemento = input("Digite um elemento para adicionar à lista (ou 'parar' para terminar): ")
    if elemento == 'pare':
        break
    fila += [elemento]

print("Lista completa:", fila)

def adicionar_cliente(cliente):
    fila.append(cliente)
    print(f"Cliente {cliente} adicionado à fila.")


def atender_cliente():
    if fila:
        cliente_atendido = fila.pop(0)
        print(f"Cliente {cliente_atendido} atendido.")
    else:
        print("Não há clientes na fila para atender.")

atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()
