from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount

    @abstractmethod
    def calculate_extra(self):

        pass


class SavingsAccount(Account):
    def calculate_extra(self):
        interest = self._balance * 0.05
        self._balance += interest
        return interest


class CurrentAccount(Account):
    def calculate_extra(self):
        fee = 10.0
        self._balance -= fee
        return -fee


accounts: list[Account] = [
    SavingsAccount("Ali", 1000),
    CurrentAccount("Sara", 500)
]

for acc in accounts:
    acc.deposit(200)
    acc.calculate_extra()
    print(f"{acc.owner}: ${acc._balance}")