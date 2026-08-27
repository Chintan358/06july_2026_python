class Pen:
    
    def __init__(self,price, color, company):
        self.price  = price
        self.color = color
        self.company = company
        
    def display(self):
        print(self.price,self.color,self.company)
    
    
class Pencil:
    
    def __init__(self,length):
        self.length = length 
        
class NoteBook(Pencil,Pen):
    def __init__(self, price, color, company,pages):
        self.pages=  pages
        super().__init__(price, color, company)
    
    def display(self):
        print(self.price,self.color,self.company,self.pages)
    
    
p = Pen(50,"Red","Cello")
p.display()


n = NoteBook(30,"White","Classmate",200)
n.display()