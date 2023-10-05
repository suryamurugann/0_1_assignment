class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = Account("surya", 10000)
print("Account Title:", account1.title)
print("Account Balance:", account1.balance)

account2 = SavingsAccount("surya", 10000, 6)
print("Savings Account Title:", account2.title)
print("Savings Account Balance:", account2.balance)
print("Savings Account Interest Rate:", account2.interestRate)