from banco import obterConta


def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Seu saldo: {cliente['Saldo']}")
    else:
        print('Cliente não encontrado!')
