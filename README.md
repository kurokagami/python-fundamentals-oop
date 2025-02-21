# Sistema de Banco OOP - Fundamentos de Python

Este projeto foi desenvolvido como parte do curso de Python da Suzano DIO, com o objetivo de otimizar um sistema bancário já existente (<a href="https://github.com/kurokagami/python-optimize-fundamentals">Acessar</a>), aplicando os conceitos de programação orientada a objetos em sua estrutura.


## Funcionalidades Requisitadas

- **OOP**: O Sistema agora deve utilizar o conceito de programação orientada a objetos.
- **Conta**: A Classe Conta deve conter os métodos de saldo(), nova_conta(), sacar(), depositar() e uma classe filha ContaCorrente.
- **Historico**: A Classe Historico deve conter o método adicionar_transacao() que recebe o tipo Transacao.
- **Transação**: Classe Saque e Deposito que extende a Interface Transacao contendo o método registrar().
- **Cliente**: A Classe Cliente deve conter os métodos realizar_transacao() e adicionar_conta().
- **Pessoa**: Extensão da Classe Cliente, deve conter nome, data_nascimento, cpf e endereco.



## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/python-000?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![Pip](https://img.shields.io/badge/Pip-000?style=for-the-badge&logo=python&logoColor=677ff6)](https://pip.pypa.io/en/stable/)

## Minhas Implementações Pessoais

- **Estrutura**:  As classes estão organizadas em arquivos separados, facilitando a manutenção.
- **Setup**: O setup está configurado para permitir o envio do pacote para o PyPI, caso necessário.
- **Tratamento de Erros**: Adição de Blocos `try` para evitar que o programa quebre em casos de valor inserido não seja convertido corretamente.
- **Validações**: Implementação de validações para CPF, data de nascimento e nome.
- **Aninhamento**: O endereço dos clientes é armazenado em um dicionário dentro da lista de clientes.
- **Utils**: Funções auxiliares e validações estão organizadas em módulos separados para facilitar a reutilização do código.
- **Exibição de Saldo**: O cliente pode consultar o saldo atual da conta.
- **Data e Hora**: A biblioteca TzLocal é utilizada para armazenar a data e hora local, que serão exibidas no extrato bancário.


## Testes Realizados

- **Caracteres Inválidos**: O sistema impede a inserção de caracteres não numéricos durante as operações.
- **Depósito Negativo ou Zero**: Depósitos com valores negativos ou iguais a zero são rejeitados.
- **Saque Negativo ou Zero**: Saques de valores negativos ou iguais a zero não são permitidos.
- **Exceções Conta Corrente**:  O sistema garante que não é possível sacar um valor superior ao saldo, ao limite permitido ou ao limite diário de saques.
- **Usuário Repetido**: O cadastro de clientes com o mesmo CPF é impedido.
- **Conta sem Usuário**: Apenas clientes cadastrados podem criar uma conta.
- **Validações**: CPF (11 Caracter Numérico), Data de Nascimento (dd-mm-aaaa) e Nome (Somente Letras).
- **Operações**: Para realizar qualquer operação, o cliente deve ser válido e possuir pelo menos uma conta.

<br>
<br>

<details align="left">
  <summary></summary> 
 
  - Time Is <a href="https://time.is/">time.is</a>
  - Package Manager <a href="https://pip.pypa.io/en/stable/">Pip Package Manager</a>
  - Time Zone Lib <a href="https://docs.python.org/3/library/datetime.html">Time Zone Lib</a>
  - Tzlocal <a href="https://pypi.org/project/tzlocal/">Tzlocal Lib</a>
  - ABC <a href="https://docs.python.org/3/library/abc.html">ABC Lib</a>
 
  <div align="right">Made by <a href="https://github.com/kurokagami/">Kuro Kagami</a>.</div>

</details>
