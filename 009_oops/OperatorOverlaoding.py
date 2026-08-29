class calc :
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return self.a+other.a,self.b+other.b
    
 
        
c = calc(10,20)
c1 = calc(30,40)

r = c+c1
print(r)