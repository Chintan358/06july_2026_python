class Salary:
    
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def annual_salary(self):
        return self.salary*12+self.bonus
    
class Employee : 
    
    def __init__(self,name,age,s):
        self.age = age
        self.name = name
        self.s =s
        
    def total_sal(self):
        print(f"{self.name} : anunal salary is : {s.annual_salary()}")
    
    
s = Salary(5000,2000)
e = Employee("tops",25,s)
e1 = Employee("Tech",55,s)
e.total_sal()
e1.total_sal()