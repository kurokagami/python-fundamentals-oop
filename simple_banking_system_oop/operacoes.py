import textwrap
from utils import Validator
from transacao import Saque, Deposito
from conta import ContaCorrente
from cliente import PessoaFisica

# <-- Operações Bancárias --> #
class Operacoes:
    def __init__(self, clientes, contas):
        self.clientes = clientes
        self.contas = contas

    def make_deposit(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = Validator.filter_clients(cpf, self.clientes)
        
        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return
        
        valor = float(input("Informe o valor do Depósito: "))
        transacao = Deposito(valor)
        
        conta = Validator.recovery_client_account(cliente)
        if not conta:
            return
        
        cliente.realizar_transacao(conta, transacao)

    def make_withdrawal(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = Validator.filter_clients(cpf, self.clientes)
        
        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return
        
        valor = float(input("Informe o valor do Saque: "))
        transacao = Saque(valor)
        
        conta = Validator.recovery_client_account(cliente)
        if not conta:
            return
        
        cliente.realizar_transacao(conta, transacao)

    def view_statement(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = Validator.filter_clients(cpf, self.clientes)
        
        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return
        
        conta = Validator.recovery_client_account(cliente)
        if not conta:
            return
        
        print("==================EXTRATOS======================")
        transacoes = conta.historico.transacoes
        
        extrato = ""
        if not transacoes:
            extrato = "Não foram realizadas movimentações"
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}\tR${transacao['data']}:"
        
        print(extrato)
        print(f"\nSaldo Atual:\tR$ {conta.saldo:.2f}")
        print("================================================")

    def view_balance(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = Validator.filter_clients(cpf, self.clientes)
        
        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return
        
        conta = Validator.recovery_client_account(cliente)
        if not conta:
            return
        
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    
    def create_client(self):
        try:
            cpf = input("Informe o CPF (Somente Números): ")
            if cpf != cpf.isdigit() and len(cpf) != 11:
                print("CPF Inválido. Deve conter 11 Dígitos. Utilize Apenas Números. Tente Novamente!")
                return 
            
            cliente = Validator.filter_clients(cpf, self.clientes)
            
            if cliente:
                print("\n@@@ Já existe um usuário com esse CPF! @@@")
                return

            nome = Validator.name_validade()
            data_nascimento = Validator.date_validade()
            endereco = Validator.postal_validade()
            
            cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
            
            self.clientes.append(cliente)
            
            print("=== Usuário Criado com Sucesso!!! ===")
        except ValueError:
            print("\n@@@ Erro interno durante a criação de usuário. Tente Novamente! @@@")
    
    def create_account(self, numero_conta):
        cpf = input("Informe o CPF (Somente Números): ")
        cliente = Validator.filter_clients(cpf, self.clientes)
        
        if not cliente:
            print("\n@@@ Cliente não encontrado! operação encerrada! @@@")
            return
        
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        self.contas.append(conta)
        cliente.contas.append(conta)
        
        print("\n=== Conta criada com sucesso! ===")

    def list_accounts(self):
        for conta in self.contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))
