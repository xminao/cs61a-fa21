class Account:
    interest = 0.02
    holder = 'xminao'

    def __init__(self, account_holder):
        #self.holder = account_holder
        self.balance = 0

a = Account('opps')
print(a.holder)
print(type(a.holder))