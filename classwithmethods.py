class BankAccount:
    def __init__(self, Holder_name, Balance=0):
        self.Holder_name = Holder_name
        self.Balance = Balance

    def deposit(self, amount):
        self.Balance += amount
        return f"Deposited {amount}. New Balance: {self.Balance}"

    def withdraw(self, amount):
        if amount > self.Balance:
            return "Insufficient Balance!"
        else:
            self.Balance -= amount
            return f"Withdrew {amount}. New Balance: {self.Balance}"

    def check_balance(self):
        return f"Available Balance: {self.Balance}"
obj=BankAccount("Akhila",4000)
print(obj.deposit(1000))
print(obj.withdraw(1500))
print(obj.check_balance())

