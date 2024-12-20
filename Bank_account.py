'''
create a bank account class that has two attributes:

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"
        
    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        print("Deposit Accepted")

    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        
        if self.balance >= self.withdraw_amount:
            self.balance = self.balance - self.withdraw_amount
            print("Withdrawal Accepted")

        else:
            print("Funds Unavailable!")

acct1 = Account('Jose',100)

print(acct1)   

'''
Account owner:   Jose
Account balance: $100
'''

acct1.owner   # 'Jose'

acct1.balance   # 100

acct1.deposit(50)  #  Deposit Accepted

acct1.withdraw(75)  # Withdrawal Accepted

acct1.withdraw(500)   # Funds Unavailable! 
