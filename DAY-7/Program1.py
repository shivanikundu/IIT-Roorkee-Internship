#Create a bank Account class with deposit , withdraw , balance methods
class Bankaccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Creating an account
acc1 = Bankaccount("Shivani", 10000)

# Operations
acc1.check_balance()

acc1.deposit(2000)
acc1.check_balance()

acc1.withdraw(1500)
acc1.check_balance()

acc1.withdraw(10000)  # Insufficient balance