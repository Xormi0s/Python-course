class Crypto:
    def __init__(self, name):
        self.name = name
        self.price = 0
        
    def __str__(self) -> str:
        return f"This is {self.name} a cryptocurrency"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Crypto):
            return self.name == value.name
        return False
    
    def __add__(self, value: object):
        if isinstance(value, Crypto):
            combo = self.name + " " + value.name
            return Crypto(combo)
        else:
            raise ValueError("Can not perform addition between them!")
        
    def set_price(self, price):
        self.price += price
        
    def get_price(self):
        if hasattr(self, "price"):
            return self.price 
        else:
            print("Price not yet set!")
    
    def calc_value(self, quantity):
        if hasattr(self, "price"):
            return self.price * quantity
        else:
            print("Price not yet set!")
            
class Bitcoin(Crypto):
    def __init__(self):
        super().__init__("Bitcoin")
        
    def __str__(self) -> str:
        return "Bitcoin is decentralized!"
    
    def mine(self):
        return "Mining the next Block..."

class Ethereum(Crypto):
    def __init__(self):
        super().__init__("Ethereum")
        
    def __str__(self) -> str:
        return "Ethereum uses smart contracts!"
    
    def mine(self):
        return "Mining the next token..."
    
    
crypto1 = Crypto("Sky")
crypto2 = Crypto("Sam")
crypto3 = Crypto("Bitcoin")

bitcoin = Bitcoin()
ether = Ethereum()

print(crypto1)

print(bitcoin == crypto3)
print(bitcoin == ether)

print(ether + crypto2)
ether.set_price(1500)
print(ether.get_price())


portfolio = [
    {"crypto":bitcoin, "quantity": 5},
    {"crypto":ether, "quantity": 32},
    {"crypto":crypto1, "quantity": 25}
]

for asset in portfolio:
    crypto = asset["crypto"]
    quantity = asset["quantity"]
    
    total = crypto.calc_value(quantity)
    print(f'The total value of {crypto.name} with your amount of {quantity} is {total}')