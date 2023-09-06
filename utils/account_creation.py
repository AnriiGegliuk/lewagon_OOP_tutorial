
"""Initiating Bank account class"""

class BankAccount:
    def __init__(self, account_holder, initial_balance, age):
        self.age = age
        self.__name = account_holder  # Private attribute
        self.__balance = initial_balance  # Private attribute, denoted by the double underscores

    # Public method to get balance
    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount"

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"




"""Inheritance. Allows a class to inherit attributes and methods from another class"""
class SavingsAccount(BankAccount):
    # adding new atribute
    interest_rate = 0.05

    def __init__(self, account_holder, initial_balance):
        # Call the parent constructor __init__
        super().__init__(account_holder, initial_balance)

    # adding new function
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return f"Added interest: ${interest}. New balance: ${self.get_balance()}"
