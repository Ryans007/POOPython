from abc import ABCMeta, abstractmethod
from AccountException import AccountException

class Account(metaclass= ABCMeta):
    def __init__(self, agency: int, account_number: int, balance: float=0) -> None:
        self.agency = agency
        self.account_number = account_number
        self._balance = balance
    
    @abstractmethod
    def withdraw(self, value: float) -> float: pass
    
    def deposit(self, value: float) -> float:
         self._balance += value
         self._message(f'DEPOSIT: {value}')
         return self._balance 
    
    def _message(self, msg: str = '') -> None:
        print(f'Your balance: {self._balance:.2f} ({msg})')

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.agency!r}, '\
               f'{self.account_number!r}, {self._balance!r})'
    
class CurrentAccount(Account):
    def __init__(self, agency: int, account_number: int, balance: float=0, extra_limit: float=0) -> None :
        super().__init__(agency, account_number, balance)
        self._extra_limit = extra_limit
    
    def withdraw(self, value: float) -> float:
        try:
            if value > self._balance + self._extra_limit:
                raise AccountException('value above limit')
            self._balance -= value
            self._message(f'WITHDRAW: {value}')
        except AccountException:
            print('withdrawal denied')
        finally:
            return self._balance
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.agency!r}, {self.account_number!r}, {self._balance!r},'\
               f' {self._extra_limit!r})'
        

class SavingsAccount(Account):
    def __init__(self, agency: int, account_number: int, balance: float=0) -> None:
        super().__init__(agency, account_number, balance)
    
    def withdraw(self, value: float) -> float:
        try:
            if value > self._balance:
                raise AccountException('value above limit')
            self._balance -= value
            self._message(f'WITHDRAW: {value}')
        except AccountException:
            print('withdrawal denied')
        finally:
            return self._balance

if __name__ == '__main__':
    cp1 = SavingsAccount(111,222)
    cp1.withdraw(1)
    cp1.deposit(1)
    cp1.withdraw(1)
    cp1.withdraw(1)
    print('##')
    cc1 = CurrentAccount(111,222,0,100)
    cc1.withdraw(1)
    cc1.deposit(1)
    cc1.withdraw(1)
    cc1.withdraw(1)
    cc1.withdraw(1)
    cc1.withdraw(1)
    print('##')



