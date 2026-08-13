def test():
    try :
        k = int(input("enter number : "))
        return k
    except Exception as e:
        return e
    finally:
        print("always execute")
        
print(test())