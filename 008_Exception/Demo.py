print("program started")

try :
    a = 10
    b = a/2
    print(b)
except Exception as e:
    print(e)
else:
    print("success")
    
finally:
    print("always executable")
    
    
print("program ended")