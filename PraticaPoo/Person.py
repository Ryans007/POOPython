from Account import Account, SavingsAccount, CurrentAccount

class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name 
        self._age = age
    
    @property
    def name(self) -> str:
        return self._name 
    
    @property
    def age(self) -> int:
        return self._age
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @age.setter
    def age(self, age: int) -> None:
        self._age = age
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.name!r}, {self.age!r})'

class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self._account: Account | None
    



if __name__ == '__main__':
    c1 = Client('Luiz', 30)
    c1._account = CurrentAccount(111, 222, 0, 0)
    print(c1)
    print(c1._account)
    c2 = Client('Ryan', 20)
    c2._account = SavingsAccount(123, 234, 1232)
    print(c2)
    print(c2._account)
    

