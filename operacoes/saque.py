from banco import obterConta

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['Saldo'] >= valor:
            cliente['Saldo'] -= valor
            print("Saque realizado com sucesso!")
        else:
            print('Saldo Insuficiente! ')
    else:
        print("Cliente não encontrado")

