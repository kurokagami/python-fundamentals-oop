from utils import TimeConfig

# <-- Historico --> #
class Historico():
    def __init__(self):
        self._transacoes = []
        self._time_config = TimeConfig()
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
 
        data_atual = self._time_config.get_local_datetime()
        print(f"Data da transação: {data_atual}")
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": data_atual,
            }
        )  
    