fila = []


def adicionar_cliente(cliente):
    fila.append(cliente)
    print(f"Cliente {cliente} adicionado à fila.")


def atender_cliente():
    if fila:
        cliente_atendido = fila.pop(0)
        print(f"Cliente {cliente_atendido} atendido.")
    else:
        print("Não há clientes na fila para atender.")


adicionar_cliente("João")
adicionar_cliente("Maria")
adicionar_cliente("Pedro")
adicionar_cliente("Romulo")
adicionar_cliente("Mario")

atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()