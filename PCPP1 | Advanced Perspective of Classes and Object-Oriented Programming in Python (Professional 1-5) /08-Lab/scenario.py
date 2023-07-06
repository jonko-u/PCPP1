# Level of difficulty
#
# Medium
# Objectives
#
#     improving the student's skills in operating with the getter, setter, and deleter methods;
#     improving the student's skills in creating their own exceptions.
#
# Scenario
#
#     Implement a class representing an account exception,
#     Implement a class representing a single bank account,
#     This class should control access to the account number and account balance attributes by implementing the properties:
#         it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
#         it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
#         when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
#         it should not be possible to delete an account as long as the balance is not zero;
#     test your class behavior by:
#         setting the balance to 1000;
#         trying to set the balance to -200;
#         trying to set a new value for the account number;
#         trying to deposit 1.000.000;
#         trying to delete the account attribute containing a non-zero balance.

class AccountException(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException("Cannot set a negative balance")
        self._balance = value

    @account_number.setter
    def account_number(self, value):
        raise AccountException("Cannot change the account number")

    def deposit(self, amount):
        if amount > 100000:
            print("Large deposit detected: ", amount)
        self.balance += amount

    def withdraw(self, amount):
        if amount > 100000:
            print("Large withdrawal detected: ", amount)
        self.balance -= amount

    def __del__(self):
        if self.balance != 0:
            raise AccountException("Cannot delete account with a non-zero balance")

# Create a bank account with a balance of 1000
account = BankAccount("123456", 1000)

# Try to set a negative balance
try:
    account.balance = -200
except AccountException as e:
    print("Error:", e)

# Try to set a new value for the account number
try:
    account.account_number = "654321"
except AccountException as e:
    print("Error:", e)

# Deposit 1,000,000
account.deposit(1000000)

# Try to delete the account with a non-zero balance
try:
    del account
except AccountException as e:
    print("Error:", e)