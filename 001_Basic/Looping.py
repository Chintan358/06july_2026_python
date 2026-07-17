#Loping : for, while

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


# flag = 'y'
# while flag=='y':
#     choice  = int(input("enter choice : "))

#     match(choice):
#         case 1 : print("Gujarati")
#         case 2 : print("Hindi")
#         case 3 : print("english")
#         case _ : print("Invalid choice")
    
#     flag = input("Do you want to continue ? press y or n :")
#     if flag=='n':
#         print("you are exit !!!")

balance = 0
choice=0
while choice !=4:
    
    choice = int(input("""
                    1.Deposite
                    2.Withdrow
                    3.Balance
                    4.exit
                    """))
    if choice==1:
        print("*****deposite*****")
        amount = int(input("enter amount : "))
        balance+=amount
        print("done")
    elif choice==2:
        print("*****Withdrow*****")
        amount = int(input("enter amount : "))
        if amount>balance:
            print("Insufficent amount")
        else:
            balance-=amount
            print("done")
        
    elif choice==3:
        print("*****chocek balance*****")
        print("Current balance is : ",balance)
    elif choice==4:
        print("You are exit")
    else:
        print("Invalid choice")