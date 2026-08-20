class Student:
    
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
    
    def display(self):
        print(self.id, self.name, self.email)
        
# s = Student(10,"Purva","purva@gmail.com")
# s.display()

# s1 = Student(11,"Hasib","hasib@gmail.com")
# s1.display()

# id  = input("enter id : ")
# name = input("enter name : ")
# email = input("enter email : ")
# s = Student(id,name,email)
# s.display()


