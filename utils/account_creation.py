
# importing library for Abstract Base Class
# from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

"""Initiating Bank account class"""
class BankAccount(): # Parent class
    def __init__(self, account_holder, initial_balance, age):
        self.age = age # Public
        self._name = account_holder # Restricted
        self.__balance = initial_balance # Private
        self._transactions = []

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self._name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._transactions.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

    @abstractmethod
    def add_interest(self):
        return "This account type does not support interest."

    def generate_statement(self):
        statement = "Generic Account Statement\n"
        statement += f"Account Holder: {self.get_name()}\n"
        statement += f"Balance: ${self.get_balance()}\n"
        statement += "Transactions:\n"
        for transaction in self._transactions:
            statement += f"  - {transaction}\n"
        return statement



"""Inheritance. Allows a class to inherit attributes and methods from another class"""
class SavingsAccount(BankAccount): # Child class
    # adding new atribute
    interest_rate = 0.05

    def __init__(self, account_holder, initial_balance, age):
        # calling the parent constructor __init__
        super().__init__(account_holder, initial_balance, age)

    # overwriting add_interest function
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return f"Added interest: ${interest}. New balance: ${self.get_balance()}"

    def generate_statement(self):
        # calling the parent class's generate_statement method and extend its functionality
        statement = super().generate_statement()
        statement += f"\nInterest Rate: {self.interest_rate * 100}%"
        return statement
