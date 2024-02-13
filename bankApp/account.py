class Account:

    def __init__(self, name: str, balance: int, pin: str, number: str):
        self._name = name
        self._balance = balance
        self._pin = pin
        self._number = number

    def deposit(self, amount: int):
        if amount > 0:
            self._balance += amount

    def check_balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int):
        if amount > 0 & self._balance > amount:
            self._balance -= amount
