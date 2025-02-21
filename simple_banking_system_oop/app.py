from menu import Menu
from operacoes import Operacoes

class App:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.operacoes = Operacoes(self.clientes, self.contas)

    def start(self):
        while True:
            opcao = Menu.display_menu()
            if opcao == "1":
                self.operacoes.make_deposit()
            elif opcao == "2":
                self.operacoes.make_withdrawal()
            elif opcao == "3":
                self.operacoes.view_statement()
            elif opcao == "4":
                self.operacoes.view_balance()
            elif opcao == "5":
                self.operacoes.create_client()
            elif opcao == "6":
                numero_conta = len(self.contas) + 1
                self.operacoes.create_account(numero_conta)
            elif opcao == "7":
                self.operacoes.list_accounts()
            elif opcao == "8":
                print("Finalizando Operação. Até Logo!")
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")