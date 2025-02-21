import textwrap

class Menu:
    @staticmethod
    def display_menu():
        menu = """\n
        ==================== MENU =========================
        Escolha um número de 1-8 para realizar uma operação:
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Saldo
        [5] Novo Usuário
        [6] Nova Conta
        [7] Listar Contas
        [8] Sair
        => """
        return input(textwrap.dedent(menu))