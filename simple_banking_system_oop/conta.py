from historico import Historico
from transacao import Saque, Deposito
from utils import Validator

# <-- Conta Padrão --> #
class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod    
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        
        if valor > 0:
            if not Validator.exceptions_saldo(valor, saldo):
                return False
            
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Deposito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! valor informado é invalido @@@")
            return False
        
        return True
    
# <-- Conta Corrente --> #
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > 0:
            if not Validator.exceptions(valor, self.saldo, self.limite, numero_saques, self.limite_saques):
                return False
        
        return super().sacar(valor)
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """