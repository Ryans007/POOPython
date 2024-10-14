"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from Bank import Bank
from Person import Person, Client
from Account import Account, CurrentAccount, SavingsAccount
import os 


# Bank1 = Bank()

# c1 = Client('Luiz', 30)
# c1_account = CurrentAccount(111, 222, 0, 0)
# c1._account = c1_account
# print(c1)
# print(c1._account)
    
# c2 = Client('Ryan', 20)
# c2_account = SavingsAccount(123, 234, 1232)
# c2._account = c2_account
# print(c2)
# print(c2._account)

# c3 = Client('Marta', 23)
# c3_account = SavingsAccount(245, 12323, 14244)
# c3._account = c3_account
# print(c3)
# print(c3._account)
    
# c4 = Client('Hugo', 45)
# c4_account = SavingsAccount(123, 2421, 3223)
# c4._account = c4_account
# print(c4)
# print(c4._account)
    
# c5 = Client('Ryan', 20)
# c5_account = SavingsAccount(123, 234, 1232)
# c5._account = c5_account
# print(c5)
# print(c5._account)
# Bank1.account_insert(c1_account)
# Bank1.client_insert(c1)
# Bank1.account_insert(c2_account)
# Bank1.client_insert(c2)
# Bank1.show_clients()
# c2._account._message()

# print(Bank1.authenticator(c2,c2_account))
# print(Bank1.authenticator(c3,c3_account))
# print(Bank1.authenticator(c4,c4_account))
# print(Bank1.authenticator(c5,c5_account))

# if Bank1.authenticator(c2,c2_account):
#     c2_account.withdraw(10)

# if Bank1.authenticator(c4,c4_account):
#     c4_account.withdraw(10)

# print(Bank1)


