class Account:
    interest = 0.02

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0