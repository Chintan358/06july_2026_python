class Product:
    
    def add_product(self):
        print("product added")
        
class Payment:
    
    def make_payment(self):
        print("payment done")

class Order(Product,Payment):
    
    def place_order(self):
        print("order placed")
        
o = Order()
o.add_product()
o.make_payment()
o.place_order()