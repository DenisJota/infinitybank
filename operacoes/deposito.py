from banco import obterConta

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['Saldo'] += valor
        print("Deposito realizado com sucesso!")
    else:
        print("Cliente não encontrado")

