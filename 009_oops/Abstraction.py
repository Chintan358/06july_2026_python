from abc import ABC,abstractmethod

class Account(ABC):
    balance = 0
    
    def get_balance(self):
        print(f"current balance is {self.balance}")
      
    @abstractmethod  
    def deposite(self,amount):
        pass
    
    @abstractmethod
    def withdrow(self,amount):
        pass
    
class Saving(Account):
    def deposite(self, amount):
        self.balance+=amount
        
    def withdrow(self, amount):
        if amount>self.balance:
            print("insufficeint amount")
        else:
            self.balance-=amount

class Loan(Account):
    
    def withdrow(self, amount):
        self.balance+=amount
        
    def deposite(self, amount):
        if amount > self.balance:
            k = amount-self.balance
            print(f"loan cleard - return amount is : {k}")
            self.balance=0
        else:
            self.balance-=amount


# s = Saving()
# s.get_balance()
# s.deposite(5000)
# s.deposite(3000)
# s.get_balance()
# s.withdrow(1000)
# s.get_balance()


# l = Loan()
# l.get_balance()
# l.withdrow(5000)
# l.get_balance()
# l.deposite(1000)
# l.get_balance()


