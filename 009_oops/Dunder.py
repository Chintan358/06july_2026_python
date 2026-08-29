# class Demo:
    
#     def __init__(self):
#         print("init calling")
        
#     def __str__(self):
#         return "Hello"

# d = Demo()
# print(d)


# class Sample:
    
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b
        
# s = Sample(10,20)
# s1 = Sample(10,20)
# print(s==s1)


class Test : 
    
    def __init__(self,a):
        self.a = a
        
    def __len__(self):
        return len(self.a)
    
    def __getitem__(self, key):
        return self.a[key]
    
    def __setitem__(self, key, value):
        self.a[key] = value
        
t = Test([10,20,30,40,50])
# print(len(t))
# print(t[1])
t[1] = 5000
print(t.a)
