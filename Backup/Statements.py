# condional statement
#if - else / match-case

a = 100
b = 20
c = 300

# if a>b :
#     if a>c:
#         print("A is greater")
#     else:
#         print("B is greater")
# else:
#     if b>c:
#         print("B is greater")  
#     else:
#         print("C is greater") 
    
    
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
else:
    # print("Something went wrong")
    pass
    

# choice  = 21

# match(choice):
#     case 1 : print("Gujarati")
#     case 2 : print("Hindi")
#     case 3 : print("English")
#     case _ : print("Invalid input")


# a = int(input("enter number : "))
# b = int(input("Enter number : "))
# choice = input("""
#                Enter Choice :
#                +,-,*,/
#                """)

# match(choice):
#     case '+':
#         print(a+b)
#     case '-':
#         print(a-b)
#     case '*':
#         print(a*b)
#     case '/':
#         print(a/b)
#     case _ : 
#         print("Invalid input")


# looping statement
# for, while

# for i in range(10):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(1,10,2):
#     print(i)
    
# for i in range(10,1,-1):
#     print(i)


# i = 10

# while i<20:
#     print(i)
#     i+=1

# control statement : break, continue, pass

# for i in range(10):
#     if i==5:
#         # break
#         # continue
#         pass
#     print(i)
