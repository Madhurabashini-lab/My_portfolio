class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def check_balance(self):
        print(f"Balance: ${self.balance}")
        return self.balance
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance}")
        return interest

AliceAccount = BankAccount("1234", "Alice", 5000, 0.05)
BobAccount = BankAccount("5678", "Bob", 1000, 0.1)

AliceAccount.check_balance()
BobAccount.check_balance()

AliceAccount.apply_interest()
BobAccount.apply_interest()

AliceAccount.deposit(250)
BobAccount.deposit(50)