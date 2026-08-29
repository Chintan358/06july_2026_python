class Salary:
    
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def annual_salary(self):
        return self.salary*12+self.bonus
    
class Employee : 
    
    def __init__(self,name,age,salary,bonus):
        self.age = age
        self.name = name
        self.salary = salary
        self.bonus = bonus
        
    def total_sal(self):
        s = Salary(self.salary, self.bonus)
        print(f"{self.name} : anunal salary is : {s.annual_salary()}")
    
    


e1 = Employee("Tech",55,5000,2000)
e1.total_sal()