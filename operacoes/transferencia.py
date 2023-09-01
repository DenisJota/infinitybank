from banco import obterConta, banco

def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    clienteOri = obterConta(contaOri)
    clienteDes = obterConta(contaDes)
    if clienteOri and clienteDes:
        if clienteOri['Saldo'] >= valor:
            clienteOri['Saldo'] -= valor
            clienteDes['Saldo'] += valor
            print("Transferência realizada com sucesso!")
        else:
            print('Saldo Insuficiente! ')
    else:
        print("Uma ou mais contas não encontradas! ")
