from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.deposito import depositar
from operacoes.transferencia import transferir
from banco import *
from time import sleep


def menu():
    while True:
        print('''
--------------- MENU --------------
        1 - Adicionar conta
        2 - Editar nome
        3 - Consultar nome
        4 - Excluir conta
        5 - Listar todos
        6 - Realizar Saque
        7 - Realizar Depósito
        8 - Realizar Transferência
        9 - Consultar Saldo
        10- Sair
------------------------------------''')
        opcao = int(input("Qual a sua opção: "))
        if opcao == 1:
            nome = input("Digite o nome do Cliente: ")
            saldo = float(input('Digite o Saldo: '))
            adicionarConta(nome, saldo)
            sleep(1)
        elif opcao == 2:
            conta = int(input("Digite o número da conta: "))
            nome = input("Digite o novo nome do Cliente: ")
            editarNome(conta, nome)
            sleep(1)
        elif opcao == 3:
            conta = int(input("Digite o número da conta: "))
            buscarCliente(conta)
            sleep(1)
        elif opcao == 4:
            conta = int(input("Digite o número da conta: "))
            removerConta(conta)
            sleep(1)
        elif opcao == 5:
            listarTodos()
            sleep(5)
        elif opcao == 6:
            conta = int(input("Digite o número da conta: "))
            valor = float(input('Digite o Valor do Saque: '))
            sacar(conta, valor)
            sleep(1)
        elif opcao == 7:
            conta = int(input("Digite o número da conta: "))
            valor = float(input('Digite o Valor do depósito: '))
            depositar(conta, valor)
            sleep(1)
        elif opcao == 8:
            contaOrigem = int(input("Digite o número da sua conta: "))
            contaDestino = int(input("Digite o número da conta que quer transferir: "))
            valor = float(input('Digite o Valor da Transferência: '))
            transferir(contaOrigem, contaDestino, valor)
            sleep(1)
        elif opcao == 9:
            conta = int(input("Digite o número da conta: "))
            consultarSaldo(conta)
            sleep(1)
        elif opcao == 10:
            print('Finalizando...')
            sleep(1)
            break
        else:
            print('Opção inválida! Tente de novo: ')
            sleep(1)


menu()