# parent - super - base
class A:
    
    id = 20
    def test(self):
        print("test calling")
        
# child - sub - derived   
class B(A):
    
    def sample(self):
        print(self.id)
        print("sample calling")
        
#multilevel     
# class C(B):
#     pass

# class C(A):
#     pass

# class C(A,B):
#     pass

# class D(C):
#     pass
        
b  =B()
b.sample()
b.test()