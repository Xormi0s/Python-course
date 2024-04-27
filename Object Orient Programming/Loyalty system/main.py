class Customer():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        

class LoyaltyPoints():
    def __init__(self):
        self.points = 0
        
    def earn_points(self, amount):
        self.points += amount
        
    def redeem_points(self, amount):
        if self.points >= amount:
            self.points -= amount
        else:
            print("Not enoug points!")
            
    def show_balance(self):
        return self.points
    
    
class VIPCustomer(Customer, LoyaltyPoints):
    def __init__(self, id, name):
        Customer.__init__(self, id, name)
        LoyaltyPoints.__init__(self)


class Transaction():
    def __init__(self, id, customer, amount):
        self.trans_id = id
        self.customer = customer
        self.amount = amount
        
class TransactionHistory():
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction.trans_id, transaction.customer.name, transaction.amount)
            
            

vip = VIPCustomer("VIP007", "Jonas")
vip.earn_points(500)
vip.redeem_points(100)

transaction1 = Transaction("T015", vip, "+500")
transaction2 = Transaction("T016", vip, "-100")

transaction_history = TransactionHistory()
transaction_history.add_transaction(transaction1)
transaction_history.add_transaction(transaction2)

transaction_history.show_transactions()

balance = vip.show_balance()

print()
print(f"Customer ID: {vip.id}")
print(f"Customer Name: {vip.name}")
print(f"Loyalty Point Balance: {balance}")