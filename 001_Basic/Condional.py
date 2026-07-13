# if-else, match-case

# age = 19
# if age>18:
#     print("Elegeble for voting")
# else:
#     print("Not Elegeble")

a = 200
b = 200
c = 200

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greate")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")


# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")
# else:
#     print("something went wrong...")


# marks = 25
# 91 - 100 : A
# 71 - 90 :b
#51 - 70 : C
#35 - 50 :D
# 0 - 34 : F

# marks = int(input("Enter marks : "))
# if marks>=91 and marks<=100:
#     print("Grade A")
# elif marks>=71 and marks<=90:
#     print("Grade B")
# elif marks>=51 and marks<=70:
#     print("grade C")
# elif marks>=35 and marks<=50:
#     print("grade D")
# elif marks>=0 and marks<=34:
#     print("grade F")
# else:
#     print("Invalid marks")


choice  = int(input("enter choice : "))

match(choice):
    case 1 : print("Gujarati")
    case 2 : print("Hindi")
    case 3 : print("english")
    case _ : print("Invalid choice")