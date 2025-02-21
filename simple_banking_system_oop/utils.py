from datetime import datetime
from tzlocal import get_localzone

# <--- Validações e Exceções ---> #
class Validator():
    @staticmethod
    def name_validade():
        nome = input("Informe o nome completo: ")
        if not all(c.isalpha() or c.isspace() for c in nome):
            print("\n@@@ Nome Inválido, Utilize apenas Letras e Espaços em Brancos! @@@")
            return
        return nome

    @staticmethod
    def date_validade():
        try:
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            data_convertida = datetime.strptime(data_nascimento, "%d-%m-%Y")
            ano = data_convertida.year
            if ano < 1900 or ano > 2025:
                print("\n@@@ Ano fora do intervalo permitido. O ano deve estar entre 1900 e 2007. @@@")
                return
            return data_convertida
        except ValueError:
            print("\n@@@ Data inválida, Utilize o Formato Correto: (dd-mm-aaaa) @@@")

    @staticmethod
    def postal_validade():
        endereco_input = input("Informe o endereço (logradouro-numero-bairro-cidade-estado): ")
        split = endereco_input.split("-") 
        chaves = ["logradouro", "nro", "bairro", "cidade", "estado"]
        endereco = {chaves[i]: split[i] for i in range(len(split))}
        return endereco

    @staticmethod
    def filter_clients(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    @staticmethod
    def recovery_client_account(cliente):
        if not cliente.contas:
            print("\n@@@ Cliente não possui conta! @@@")
            return
    
        # FIXME: não permite cliente escolher a conta
        return cliente.contas[0]  

    @staticmethod
    def exceptions(valor, saldo, limite, numero_saques, LIMITE_SAQUES):
        valor = float(valor)
        limite = float(limite)
        
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if not Validator.exceptions_saldo(valor, saldo):
            return False
        elif excedeu_limite:
            print(f"Operação falhou! Valor do saque excede o limite (limite de R$ {limite})")
            return False
        elif excedeu_saques:
            print(f"Operação falhou! Número máximo (3) de saques excedido\nSaques realizados hoje: {numero_saques}")
            return False
        else:
            return True

    @staticmethod
    def exceptions_saldo(valor, saldo):
        if valor > saldo:
            print(f"Operação falhou! Saldo Insuficiente\nSaldo Atual: R$ {saldo}")
            return False
        return True
      
# <--- CONFIG  ---> #   
class TimeConfig():
    local_timezone = get_localzone()
    
    @classmethod
    def get_local_datetime(cls):
        local_date = datetime.now(cls.local_timezone).strftime("%d-%m-%Y %H:%M:%S")
        return local_date