def before(org_func):
    def excute():
       print("hello") 
       org_func()
    return excute

@before
def test():
    print("test calling")
    
@before
def display():
    print("display calling")
    
test()
display()