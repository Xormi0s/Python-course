class Account():
    def __init__(self, acc_num, balance):
        self.account = acc_num
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough money!!")
    
    def get_balance(self):
        return self.balance
    
class IntrestAccount(Account):
    def __init__(self, acc_num, balance, interest_rate):
        super().__init__(acc_num, balance)
        self.rate = interest_rate
        
    def calc_interest(self):
        return self.balance * self.rate
    

class Transactions():
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def history(self):
        for transaction in self.transactions:
            print(transaction)
            
class SavingsAccount(IntrestAccount, Transactions):
    def __init__(self, acc_num, balance, interest_rate):
        IntrestAccount.__init__(self, acc_num, balance, interest_rate)
        Transactions.__init__(self)
         
        
        
savings = SavingsAccount("SA154", 5000, 0.45)
savings.deposit(2500)
savings.withdrawl(650)

savings.add_transaction("Deposit: 2500")
savings.add_transaction("Withdrawl: 650")

savings.history()
print("Balance:",savings.get_balance())
print("Interest:", savings.calc_interest())