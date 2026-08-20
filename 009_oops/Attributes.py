class User : 
    
    collage = "abc"
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    def run(self):
        print(self.name,self.email,self.collage)
    
    @classmethod 
    def display(cls):
        print(cls.collage)
        
    @staticmethod
    def sample(a):
        print("static method")
   
User.collage="xyz"  
  
u = User("test","test@gmail.com")
u.run()

      
u1 = User("test1","test@gmail1.com")
u1.run()

User.display()
User.sample(10)
           