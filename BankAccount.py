"""This program can be used to create and manipulate a personal bank account:
Accepting deposits
Allowing withdrawals
Showing the balance
Showing the details of the account"""

class BankAccount(object):
    balance  = 0
    #name of account owner
    def __init__(self, name):
        self.name = name

    #returns name and balance
    def __repr__(self):
        return "This account belongs to %s. Balance: $ %.2f" % (self.name, self.balance)

    #prints balance
    def show_balance(self):
        print "Balance: $ %.2f" % (self.balance)

    #makes deposit
    def deposit(self, amount):
        if amount <= 0:
            print "Invalid amount."
            return
        else:
            print "$ %.2f had been deposited." % (amount)
            self.balance += amount
            self.show_balance()

    #withdraw
    def withdraw(self, amount):
        if amount > self.balance:
            print "Invalid amount."
            return
        else:
            print "$ %.2f is being withdrawn." % (amount)
            self.balance -= amount
            self.show_balance()
            return

my_account = BankAccount("Mili")
print my_account.name
print my_account
print my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account

