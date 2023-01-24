class Account:
    interest = 0.08
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

a = Account('xminao')
a.interest = 0.09
print("Account Interest: " + str(Account.interest))
print(a.holder + " Interest: " + str(a.interest))
