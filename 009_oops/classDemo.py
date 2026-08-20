class Pen:
    price=100
    color = "red"
    company = "Cello"
    
    def to_write(self):
        print(self.price, self.color, self.company)
    
p = Pen()
p.price=800
p.to_write()

p1 = Pen()
p1.to_write()