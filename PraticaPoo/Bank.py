from Person import Person, Client
from Account import Account, CurrentAccount, SavingsAccount

class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__accounts = []
        self.__clients = []
    
    def account_insert(self, *accounts: Account) -> None:
        self.__accounts.extend(accounts)

    def client_insert(self, *clients: Client) -> None:
        self.__clients.extend(clients) 
     
    def authenticator(self, client: Person, account: Account) -> bool:
        authenticator = False
        def agency_check() -> bool:
            for acc in self.__accounts:
                if acc.agency == account.agency:
                    return True
            print('The Agency is not from that bank')
            return False
        def client_check() -> bool:
            for cli in self.__clients:
                if (client.name == cli.name) and (client.age == cli.age):
                    return True
            print('The Client is not from that bank')
            return False 
        def account_check() -> bool:
            for acc in self.__accounts:
                if (acc.agency == account.agency) and (acc.account_number == account.account_number):
                    return True
            print('The Account is not from that bank')
            return False
        if agency_check() and client_check() and account_check():
           authenticator = True
        return authenticator
        
    def __repr__(self) -> str:
        return f'{type(self).__name__}()'
           
    def show_clients(self):
        for client in self.__clients:
            print(f'Client: {client.name} | Account Number: '\
                  f'{client._account.account_number}')
        print()
               
    

if __name__ == '__main__':
    Bank1 = Bank('Brandesco')

    c1 = Client('Pablo', 30)
    c1_account = CurrentAccount(111, 222, 0, 0)
    c1._account = c1_account
    print(c1)
    print(c1._account)
    
    c2 = Client('Ryan', 20)
    c2_account = SavingsAccount(123, 234, 1232)
    c2._account = c2_account
    print(c2)
    print(c2._account)

    c3 = Client('Marta', 23)
    c3_account = SavingsAccount(245, 12323, 14244)
    c3._account = c3_account
    print(c3)
    print(c3._account)
    
    c4 = Client('Hugo', 45)
    c4_account = SavingsAccount(123, 2421, 3223)
    c4._account = c4_account
    print(c4)
    print(c4._account)
    
    c5 = Client('Ryan', 20)
    c5_account = SavingsAccount(123, 234, 1232)
    c5._account = c5_account
    print(c5)
    print(c5._account)
    Bank1.account_insert(c1_account)
    Bank1.client_insert(c1)
    Bank1.account_insert(c2_account)
    Bank1.client_insert(c2)
    Bank1.show_clients()
    c2._account._message()

    print(Bank1.authenticator(c1,c1_account))
    print(Bank1.authenticator(c2,c2_account))
    print(Bank1.authenticator(c3,c3_account))
    print(Bank1.authenticator(c4,c4_account))
    print(Bank1.authenticator(c5,c5_account))

    print(Bank1)
    
